#!/usr/bin/env python
 
"""
A simple TKinter GUI to enter data into a given table in a database.

This program will build a small sample table into a given database
and then build a simple TKinter window with label and entry widgets
for each column in the table.
"""
import sqlite3
import tkinter as tk
from tkinter import N, S, E, W
from tkinter import TOP, BOTTOM, LEFT, RIGHT, END, ALL


def main():
    """Main function for demo."""
    # define some variables for demo only.
    # In full app, these will come programmatically.
    db = 'foo.sqlite'
    tbl = 'bar'
    columns = 'ID integer primary key', 'bizz text', 'bam text'
    create_table(db, tbl, *columns)

    root = tk.Tk()
    demo_window = EntryWindow(root, *[db, tbl])
    root.mainloop()


# create a sample table for demo purposes only.
# in full app the database schema would be created elsewhere.
def create_table(database, table, *col_defs):
    """
    Insert a simple table into sqlite3 database.

    Args:
        database (string):
        Name of database function will be creating table in.

        table (string):
        Name of table to be created in given database.

        *col_defs (tuple of strings):
        A tuple of strings containing the SQL column definitions for the
        given table being created in given database.
    """
    stmnt = (('create table {}('+('{},'*len(col_defs))[:-1]+');')
             .format(table, *col_defs))
    with sqlite3.connect(database) as conn:
        c = conn.cursor()
        c.execute('drop table if exists {};'.format(table))
        c.execute(stmnt)
        conn.commit()


class EntryWindow(tk.Frame):

    """
    Provides a simple data entry window for a given table in given database.

    Automatically generates labels and entry fields based on the column
    headers for the given table.  Provides a button to submit the row of data
    into the table and a button to close window.
    """

    def __init__(self, master=None, *args):
        tk.Frame.__init__(self, master)
        self.master = master
        self.database = args[0]
        self.table = args[1]
        self.init_window()

    def init_window(self):
        """Build the entry window."""
        self.master.title('Enter data into {}'.format(self.table.upper()))
        self.grid(column=0, row=0, sticky=(N, W, E, S), padx=10, pady=5)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        def get_col_names(self):
            """Retrieve column names for given table in database."""
            with sqlite3.connect(self.database) as conn:
                c = conn.cursor()
                c.execute("PRAGMA table_info('{}')".format(self.table))
                # Currently only uses one value from returned tuple.
                # TODO: Add logic to utilize type, not null and PK fields.
                self.col_names = [x[1] for x in c.fetchall()]
            return self.col_names

        self.column_names = get_col_names(self)

        # Add a label and entry box for each column in table.
        # TODO: Add functionality to gray out primary key fields where the
        #       database should be assigning the next value.
        # TODO: Add some validation logic.
        self.item_entry = []
        for item in self.column_names:
            num = len(self.item_entry)
            # print(num, ' --> '+item)
            tk.Label(self, text=item).grid(row=num, column=0,
                                           pady=1, sticky=E)
            self.item_entry.append(tk.Entry(self))
            self.item_entry[num].grid(row=num, column=1, pady=1, padx=5)

        def add_item(self):
            """Get entries from input fields and insert into database table."""
            entries = [e.get() for e in self.item_entry]
            # Build the SQL statement
            stmnt = ('insert into {0}({1}) values ({2})'
                     .format(self.table, ','.join(self.column_names),
                             ':'+',:'.join(self.column_names)))
            # print(stmnt, entries)
            with sqlite3.connect(self.database) as conn:
                c = conn.cursor()
                c.execute(stmnt, entries)
                conn.commit()
            clear_fields(self)

        def clear_fields(self):
            """Clear fields of entry windo and return focus to first field."""
            for e in self.item_entry:
                e.delete(0, END)
            self.item_entry[0].focus()

        # Add button to submit user inputs into database.
        submit_button = tk.Button(self, text='Add Item', width=8,
                                  command=lambda: add_item(self))
        submit_button.grid(row=3, column=0, sticky=E, pady=10, padx=1)

        # Add a cancel button which closes window.
        quit_button = tk.Button(self, text='Cancel', width=8,
                                command=self.quit)
        quit_button.grid(row=3, column=1, sticky=W, pady=10, padx=1)

if __name__ == '__main__':
    main()