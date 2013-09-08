from bottle import route, run, template, get, post, request, redirect, error, static_file, SimpleTemplate
import pymongo
from pymongo import MongoClient
from subprocess import call
######## CONTENT BEING TESTED #################

#the error message
@error(404)
def error(error):
	return "Sorry, the page you requested was not found (404 Error)!"

#get the CSS file
@route('/static/<filename>')
def send_static(filename):
	print "I'm being called!"
	print call(["pwd"]);
	return static_file(filename, root='./static/')

#the home page 
@route('/')
def home():
	return template('views/home.tpl');

@route('/base')
def base():
	return template('views/base.tpl');



###### EXAMPLES FOR LATER ####################

@get('/login') # or @route('/login')
def login():
    return '''
        <form action="/login" method="post">
            Title: <input name="title" type="text" />
            Date <input name="date" type="text" />
            Body <input name="body" type="text" />
            <input value="Save" type="submit" />
        </form>
    '''

@post('/login') # or @route('/login', method='POST')
def do_login():
    title = request.forms.get('title')
    date = request.forms.get('date')
    body = request.forms.get('body')

    client = MongoClient()
    db = client.hello

    doc = {}
    doc["title"] = title
    doc["date"] = date
    doc["body"] = body

    db.posts.save(doc)

    redirect('/blog')

@route('/hello/save/<name>')
def index(name = 'World'):
	client = MongoClient()
	db = client.hello

	#make a doc for this name
	doc = {}
	doc["name"] = name

	#put this into the database
	db.names.save(doc)

	return "Your document was successfully saved!"



@route('/blog')
def index(name='World'):
	client = MongoClient()
	db = client.hello
	cursor = db.posts.find()

	blog = ""
	for doc in cursor:
		blog += doc["title"]
		blog += "<br/>"
		blog += doc["date"]
		blog += "<br/>"
		blog += doc["body"]
		blog += "<br/>"

	return blog

@route('/hello/names')
def index(name='World'):
	#get all documents in the 'names' collection
	#print them out on the screen
	client = MongoClient()
	db = client.hello
	cursor = db.names.find()

	names = ""
	for doc in cursor:
		names += doc["name"]
		names += "<br/>"

	return names


@route('/hello/<name>')
def index(name='World'):
    return template('<b>Hello {{name}}</b>!', name=name)


##### TO RUN THE APP #############
run(host='localhost', port=3000, debug=True)