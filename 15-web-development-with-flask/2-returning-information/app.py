from flask import Flask

app = Flask(__name__)


posts = {
    0: {
        'title': 'Hello, world',
        'content': 'This is my first blog post!'
    }
}


@app.route('/')
def home():
    return 'Hello World!'

@app.route('/post_form/<int:post_id>')
def post_form(post_id):
    """
    This function runs when a user visits route such as:
    - /post/0
    - /post/2
    - /post/99
    But not:
    - /post/a
    - /post/something/else
    - /posts/1
    Then we get the 0 as a number (not a string!) as argument, so we can use it.
    """

    # Retrieve the post from our global posts dictionary by the ID passed in as argument.
    post = posts.get(post_id)

    # Return the title and content formatted a bit nicer.
    return (f"title: {post['title']}, content:\n\n{post['content']}")


if __name__ == '__main__':
    app.run(debug=True)