from flask import Flask, render_template, request
from flask_cors import CORS
from models import create_post, get_posts

# note - Flask always looks for a 'template' folder for templates.

# initiate server
app = Flask(__name__)

CORS(app)

# see homepage with posts, create post
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        pass

    if request.method == 'POST':
        # grab incoming content
        name = request.form.get('name')
        post = request.form.get('post')

        create_post(name, post)

    posts = get_posts()

    # render_template for displaying desired html on screen
    return render_template('index.html', posts=posts)


if __name__ == "__main__":
    app.run(debug=True)