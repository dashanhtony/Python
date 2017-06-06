from flask import Flask, url_for
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'
@app.route('/')#被覆盖
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello World'
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id
@app.route('/projects/')#接受末尾不带/会重定向为此路径
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

@app.route('/login')
def login():
    return 'login'

@app.route('/user2/<username>')
def profile(username):
    return 'user:username %s' % username


with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))

if __name__ == '__main__':
    app.debug = True
    app.run()#app.run(debug=True)