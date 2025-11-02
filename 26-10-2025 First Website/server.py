from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")   # Home route
def hello_world():
    return "Hello, Dhruba and Moumita Kumar Dolai!"

# @app.route("/<username>")   # Dynamic route for username
# def greet_user(username):
#     return f"Hello, {username}!"

@app.route("/<username>")   # Dynamic route for username
def greet_user(username):
    return render_template('index.html', username=username) # Render index.html for dynamic username route from templates folder.

@app.route("/<username>/<int:post_id>")   # Dynamic route for username and post_id
def user_blog_post(username, post_id):
    return render_template('index.html', username=username, post_id=post_id) # Render index.html for dynamic username and post_id route from templates folder.


@app.route("/admin")   # Admin route
def admin():
    return render_template('index.html') # Render index.html for admin route from templates folder. Template folder should be in the same directory as this server.py file.

@app.route("/about.html")
def about():
    return render_template('about.html') # Render about.html for about route from templates folder.

@app.route("/blog")
def blog():
    return "Welcome to the blog!"

@app.route("/blog/Dogs")
def blog_dogs():
    return "Welcome to the Dogs blog!"