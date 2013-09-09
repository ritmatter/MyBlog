from bottle import route, run, template, get, post, request, redirect, error, static_file, SimpleTemplate
import pymongo
from pymongo import MongoClient
from subprocess import call

######## CONTENT BEING TESTED #################

#the error message
@error(404)
def error(error):
	return template("views/error.tpl")

#get the CSS file
@route('/static/<filename>')
def send_static(filename):
	print "I'm being called!"
	print call(["pwd"]);
	return static_file(filename, root='./static/')

#the home page 
@route('/')
def home():
	client = MongoClient()
	db = client.blog
	posts = db.posts.find()
	return template('views/home.tpl', posts=posts)

#the posts page
@route('/posts')
def posts():
	client = MongoClient()
	db = client.blog
	posts = db.posts.find()
	return template('views/posts.tpl', posts=posts)

#the about page
@route('/about')
def about():
	return template('views/about.tpl')

#the contact page
@route('/contact')
def contact():
	return template('views/contact.tpl')

#the base page
@route('/base')
def base():
	return template('views/base.tpl')

#the login page, carefully disguised to avoid hacking
@get('/rit')
def login():
	return template('views/rit.tpl')

#the posting page, after I have verified that I'm myself
@route('/rit', method="post")
def validate():
	username = request.forms.get('username')
	password = request.forms.get('password')
	
	client = MongoClient()
	db = client.blog
	cursor = db.login.find()

	for doc in cursor:
		if (doc["username"] == username and doc["password"] == password):
			return template('views/input.tpl', name=username)

	return "<p>Psych!  That's the wrong password!</p>"

#the just-posted page, to confirm content was received
@route('/posted', method="post")
def posted():
	title = request.forms.get('title')
	print "The title is " + title
	date = request.forms.get('date')
	print "The date is " + date
	content = request.forms.get('content')
	print "The content is " + content

	client = MongoClient()
	db = client.blog

	doc = {}
	doc["title"] = title
	doc["date"] = date
	doc["content"] = content

	db.posts.save(doc)
	return template('views/posted.tpl')


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