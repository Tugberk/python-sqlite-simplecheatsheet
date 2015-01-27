# -*- coding: utf-8 -*-
import sqlite3

#just create this document in whatever way you want to
con = sqlite3.connect('quotes.db')
#c = con.cursor()

#creating a table in a new database

#c.execute("create table quotesTable(id INTEGER PRIMARY KEY AUTOINCREMENT, author TEXT NOT NULL, quote TEXT NOT NULL)")

#inserting data into a database table

'''
c.execute("insert into quotesTable(author, quote) values('Trisha Yearwood','What is meant to be will always find a way.')")
con.commit()
'''


#reading from a database simply take all there is
'''
c.execute("select * from quotesTable")
result = c.fetchall()
print result
'''

#lets use execute many, because it is really useful if you are going to add bunch of data
'''
data_to_be_added = [
	('Anonymous','Although gold dust is precious, it clouds vision.'),	
	('Felon','There is no good or bad but thinking makes it so.'),	
	('Anonymous','No one is lucky, some were patient.'),	
	('Bertrand Russell','The time you enjoy wasting is not wasted time.')
]

c.executemany("insert into quotesTable(author, quote) values(?,?)", data_to_be_added)
con.commit()
'''

#lets see if we can read data in a different way
'''
c.execute("select * from quotesTable")

#here, we see it is useful. we want to get a simple value here. try it.
while True:
	row = c.fetchone()
	
	if row == None:
		break
	
	#print "id:" + str(row[0]) + "  author:" + row[1] + "  quote:" + row[2]
	print row[1] + "--" + row[2]
'''

#another, maybe more useful way alternative to the above - dictionary cursor 
#here, remember to put the line below
con.row_factory = sqlite3.Row
#this c=con.cursor() is normally at the top. but if we want to use the row_factory, we should use it below
c = con.cursor()

c.execute("select * from quotesTable")

rows = c.fetchall()

for row in rows:
	print "%s %s" % (row["author"], row["quote"])
	


