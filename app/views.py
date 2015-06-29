from flask import render_template, request
from app import app
import pymysql as mdb
from a_Model import ModelIt

db = mdb.connect(user="root",host="localhost", db="testdb", charset='utf8')

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html",
       title = 'Home', user = { 'nickname': 'Miguel' },
       )

# @app.route('/db')
# def cities_page():
#     with db:
#         cur = db.cursor()
#         cur.execute("SELECT Name FROM City LIMIT 15;")
#         query_results = cur.fetchall()
#     cities = ""
#     for result in query_results:
#         cities += result[0]
#         cities += "<br>"
#     return cities
# 
# 
# @app.route("/db_fancy")
# 
# def cities_page_fancy():
#     with db:
#         cur = db.cursor()
#         cur.execute("SELECT Name, CountryCode, Population FROM City ORDER BY Population LIMIT 15;")
# 
#         query_results = cur.fetchall()
#     cities = []
#     for result in query_results:
#         cities.append(dict(name=result[0], country=result[1], population=result[2]))
#     return render_template('cities.html', cities=cities) 

@app.route('/input')

def cities_input():

  return render_template("input.html")
  
@app.route('/about')
def about():
    return render_template("about.html")
  
# @app.route('/about')
# 
#   return render_template("about.html")
#   print 'hi there ABOUT!'

@app.route('/parentdet')
def parentdet():

    reviewtext = request.args.get('EXREV')
    print 'here we are'
    print reviewtext
    
    outputs = []
    outputs.append('a','b','c')
  
    the_result = ''

    return render_template("parentdet.html", outputs = outputs, the_result = the_result)
    

#   
@app.route('/output')
def cities_output():

  category = request.args.get('ID')
  state = request.args.get('STATE')
  
  print category
  print state
  print 'hi there!!!!!!!!'

  with db:

    cur = db.cursor()
    
    cur.execute("SELECT minisample.category, minisample.city, minisample.businessname, parents_ONLY.reviewtext, parents_ONLY.stars from parents_ONLY join (select * from business4 WHERE state='%s' AND Category='%s') minisample          ON parents_ONLY.BUSINESSID=minisample.bid LIMIT 50;"%(state,category))
    
#    cur.execute("SELECT minisample.category, minisample.businessname,minisample.bid, parents_ONLY.reviewtext, parents_ONLY.stars, minisample.city from parents_ONLY join (select * from business4 WHERE state='AZ' AND Category='Doctors') minisample ON parents_ONLY.BUSINESSID=minisample.bid;")
   
  #  cur.execute("select b.category, b.businessname, b.businessid, p.reviewtext, p.stars, b.city from business4 as b join parents_ONLY as p on b.businessid=p.businessid where b.category='Pets' and b.state='PA';")#%(category, state))
   #  limit 5;"
   
   
   # cur.execute("SELECT business4.category, business4.businessname, business4.businessid,\
   # parents_ONLY.reviewtext, parents_ONLY.stars, business4.city FROM BUSINESS4 INNER JOIN \
   ## parents_ONLY ON business4.businessid=parents_ONLY.businessid \
   # WHERE business4.category='%s' AND business4.state='%s';"%(category, state))

    query_results = cur.fetchall()

  outputs = []

  for result in query_results:

    outputs.append(dict(category=result[0], city=result[1], businessname=result[2], reviewtext=result[3], stars=result[4]))
    
  the_result = ''

  return render_template("output.html", outputs = outputs, the_result = the_result)
 # return ok

  #call a function from a_Model package. note we are only pulling one result in the query

#  pop_input = cities[0]['population']

#  the_result = ModelIt(city, pop_input)

#  return render_template("output.html", cities = cities, the_result = the_result)

