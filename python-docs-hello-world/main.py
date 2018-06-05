from flask import Flask, render_template, request
import sqlite3 as sql
app = Flask(__name__)

import sqlite3
import csv 
import sys

# firstline = True; 
# f = open("People.csv", 'rb')
# reader = csv.reader(f)
# for row in reader:
#    if firstline:
#       firstline = False;
#       continue;
#    try:
#       name = row[0]
#       grade = row[1]
#       room = row[2]
#       telnum = row[3]
#       keywords = row[5]
#       picture = row[4]
      
#       with sql.connect("database.db") as con:
#          cur = con.cursor()
         
#          cur.execute("INSERT INTO people (name,grade,room,temnum,picture,keywords) VALUES (?,?,?,?,?,?)",(name,grade,room,telnum,picture,keywords))
         
#          con.commit()
#          msg = "Record successfully added"
#          # print("Record su");
#    except:
#       # con.rollback()
#       msg = "error in insert operation"
#       # print("error")
 
# f.close()
conn = sqlite3.connect('database.db')
#print("Opened database successfully")

#conn.execute('CREATE TABLE people (name TEXT, grade INTEGER, room TEXT, temnum TEXT, picture TEXT, keywords TEXT)')
#print("Table created successfully")
#conn.close()




@app.route('/')
def home():
   return render_template('home.html')

@app.route('/enternew')
def new_student():
   return render_template('student.html')

# @app.route('/search_by_name')
# def new_student():
      

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   if request.method == 'POST':
      try:
         name = request.form['name']
         grade = request.form['grade']
         room = request.form['room']
         telnum = request.form['telnum']
         keywords = request.form['keywords']
         picture = request.form['picture']
         
         with sql.connect("database.db") as con:
            cur = con.cursor()
            
            cur.execute("INSERT INTO people (name,grade,room,temnum,picture,keywords) VALUES (?,?,?,?,?,?)",(name,grade,room,telnum,picture,keywords))
            
            con.commit()
            msg = "Record successfully added"
            print("Record su");
      except:
         con.rollback()
         msg = "error in insert operation"
         print("error")
      
      finally:
         return render_template("result.html",msg = msg)
         con.close()

@app.route('/list')
def list():
   con = sql.connect("database.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from people")
   
   rows = cur.fetchall();
   print(rows);
   #this is a comment
   return render_template("list.html",rows = rows)

if __name__ == '__main__':
   app.run(debug = True,use_reloader=False)