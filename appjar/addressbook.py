#!/usr/bin/env python
 
from appJar import gui

import sqlite3 as lite

import sys
import os

os.chdir('/home/steve/scripts/appjar/') # Provide the path here

sql_db="test.db"
table_name="address"

con = lite.connect(sql_db)
cursor = con.cursor()

global row_num
row_num=0

def press(btn):
    if btn == "Save":
       tFname=app.getEntry("myname")
       tAdd1=app.getEntry("Add1")
       tAdd2=app.getEntry("Add2")
       tCity=app.getEntry("City")
       tPostcode=app.getEntry("Postcode")

       print(app.getEntry("myname"))
       print("values :", tFname, tAdd1, tAdd2, tCity, tPostcode)
       cursor.execute('''INSERT INTO address(Name, Add1, Add2, City, Postcode)
                     VALUES(?,?,?,?,?)''', (tFname, tAdd1, tAdd2, tCity, tPostcode))

       con.commit()
       app.clearAllEntries()
       app.setFocus("myname")

    if btn == "List":
       with con:

        con.row_factory = lite.Row

        cur = con.cursor()
        cur.execute("SELECT * FROM address")

        rows = cur.fetchall()

        for row in rows:
            print("%s %s %s %s %s %s" % (row["Id"], row["Name"], row["Add1"], row["Add2"], row["City"], row["Postcode"]))

    if btn == "Quit":
       con.commit()
       con.close()
       app.stop()
       
    if btn == ">":
       global row_num
       row_num=row_num+1       
       with con:    
        con.row_factory = lite.Row
        cur = con.cursor()
        cur.execute('''SELECT * FROM address WHERE Id=?''', (row_num,))

        rows = cur.fetchall()
        
        for row in rows:
            app.setEntry("myname",row["Name"])
            app.setEntry("Add1",row["Add1"])
            app.setEntry("Add2",row["Add2"])
            app.setEntry("City",row["City"])
            app.setEntry("Postcode",row["Postcode"])
      
    if btn == "<":
       row_num=row_num-1       
       with con:    
        con.row_factory = lite.Row
        cur = con.cursor()
        cur.execute('''SELECT * FROM address WHERE Id=?''', (row_num,))

        rows = cur.fetchall()
        
        for row in rows:
            app.setEntry("myname",row["Name"])
            app.setEntry("Add1",row["Add1"])
            app.setEntry("Add2",row["Add2"])
            app.setEntry("City",row["City"])
            app.setEntry("Postcode",row["Postcode"])

       

app=gui()
app.setBg("slateblue")
app.setPadding([20,5])
app.setInPadding([20,5])
app.setSticky("w")

app.addLabel("l0", " ",0,0)

app.addLabel("l1", "Name     :",1,0)
app.addEntry("myname",1,1)
app.setEntryBg("myname", "Lightblue")

app.addLabel("l2", "Address 1:",2,0)
app.addEntry("Add1",2,1)
app.setEntryBg("Add1", "Lightblue")

app.addLabel("l3", "Address 2:",3,0)
app.addEntry("Add2",3,1)
app.setEntryBg("Add2", "Lightblue")

app.addLabel("l4", "City     :",4,0)
app.addEntry("City",4,1)
app.setEntryBg("City", "Lightblue")

app.addLabel("l5", "Postcode :",5,0)
app.addEntry("Postcode",5,1)
app.setEntryBg("Postcode", "Lightblue")

app.setAllEntryWidths(35 )

app.addButtons(["Save", "List", "Quit", "Edit", "<", ">"], press, )


app.setButtonBg("Save","LightBlue")
app.setButtonBg("List","LightBlue")
app.setButtonBg("Quit","LightBlue")
app.setButtonBg("Edit","LightBlue")
app.setButtonBg("<","LightBlue")
app.setButtonBg(">","LightBlue")

app.setButtonFg("Save","Black")
app.setButtonFg("List","Black")
app.setButtonFg("Quit","Black")
app.setButtonFg("Edit","Black")
app.setButtonFg("<","Black")
app.setButtonFg(">","Black")


app.setFocus("myname")

app.go()
