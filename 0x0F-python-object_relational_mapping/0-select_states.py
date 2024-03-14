#!/usr/bin/python3
"""lists all states from the database hbtn_0e_0_usa"""
import MySQLdb


conn = MySQLdb.connect(host="localhost", port=3306, user="root",  passwd="root", db="hbtn_0e_0_usa")
cur = conn.cursor()
cur.execute(SELECT * FROM states ORDERBY ASC states.id)
query_rows = cur.fetchall()
for row in query_rows:
    print("{}, {}".format(states.id, states))

cur.close()
conn.close()
