#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

con = lite.connect('test.db')

with con:

    cur = con.cursor()
    cur.execute("CREATE TABLE address(Id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, Name TEXT, Add1 TEXT, Add2 TEXT, City TEXT, Postcode TEXT)")
    cur.execute("INSERT INTO Address VALUES(1,'Mickey Mouse','1 Fantasia Avenue', 'Disney World ', 'Florida', 'AA1 2BB')")
