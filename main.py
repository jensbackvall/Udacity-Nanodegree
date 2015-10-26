import os
import time
import jinja2
import webapp2

from google.appengine.ext import ndb

from variables import *

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape = True)


#I create a wall to use for the wall key. Taken directly from the wallbook example.
DEFAULT_WALL = 'Public'

#Then construct a datastore key.
def wall_key(wall_name = DEFAULT_WALL):
  return ndb.Key('Wall', wall_name)
  

# Below I define the class CommentContainer to store comments with name, comment and date.
class CommentContainer(ndb.Model):
	name = ndb.StringProperty(indexed=False)
	content = ndb.StringProperty(indexed=False)
	date = ndb.DateTimeProperty(auto_now_add = True)


class Handler(webapp2.RequestHandler):
	def write(self, *a, **kw):
		self.response.out.write(*a, **kw)

	def render_str(self, template, **params):
		t = jinja_env.get_template(template)
		return t.render(params)

	def render(self, template, **kw):
		self.write(self.render_str(template, **kw))


class MainPage(Handler):
    def get(self):
#I call the wall, to make sure I put all comments in the same entity
        wall_name = self.request.get('wall_name', DEFAULT_WALL)
        if wall_name == DEFAULT_WALL.lower(): wall_name = DEFAULT_WALL
#Below is where I start to query the comments and names of people commenting, starting with the most recent date and time
        comments_query = CommentContainer.query(ancestor = wall_key(wall_name)).order(-CommentContainer.date)
#And then I prepare the post I've queried, so that I can put it in my 'previous comments' section
        comments = comments_query.fetch()
#Below I render the page.
        self.render("content.html",comments = comments, lesson1 = lesson1, lesson2 = lesson2, lesson3 = lesson3, lesson4 = lesson4, lesson5 = lesson5,
        	        lesson6 = lesson6, lesson7 = lesson7, lesson8 = lesson8, lesson9 = lesson9, lesson10 = lesson10, lesson11 = lesson11,
        	        lesson12 = lesson12, lesson13 = lesson13, lesson14 = lesson14, lesson15 = lesson15, lesson16 = lesson16, lesson17 = lesson17,
        	        lesson18 = lesson18, lesson19 = lesson19, lesson20 = lesson20, lesson21 = lesson21)


# Below I define the class that posts the previous comments into the bottom of my page.
class Post(Handler):
	def post(self):
#I make sure that the parent key is correct, so that all comments 
#are from the same entity.
		wall_name = self.request.get('wall_name',DEFAULT_WALL)
		comment_container = CommentContainer(parent = wall_key(wall_name))
#This is where I get the content from the 'name' and field in my form.
		comment_container.name = self.request.get('name')
#This is where I get the content from the 'content' and field in my form.
		comment_container.content = self.request.get('content')
#If the comment is empty, I redirect to an error page, without trying to write the empty input to the database.
#And this is about as much validation as I have, since I have opted for a simple solution of name and content, without fancy things
#like email and login, and have Autoescaped :-).
		if comment_container.content == '':
			self.redirect("/error")
		else:
#But if the comment has actual content, I write the content to the database.
			comment_container.put()
#And finally I redirect back to the main page.
			self.redirect('/#comment_section')

#Below, I define a handler that will control my small error page, for empty comments.
class Error_Page(Handler):
	def get(self):
		self.render("error.html")
		


app = webapp2.WSGIApplication([
								("/", MainPage),
								("/comments", Post),
								("/error", Error_Page)
								],
								debug = True)
