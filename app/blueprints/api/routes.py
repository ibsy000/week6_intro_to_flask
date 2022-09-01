from . import api
from flask import jsonify, request # request is a variable that is representing the latest request
from app.models import Post, User

@api.route('/')
def index():
    names = ['Brian', 'Tatyana', 'Nate', 'Sam']
    return jsonify(names)


@api.route('/posts', methods=["GET"]) # get request
def get_posts():
    posts = Post.query.all()
    return jsonify([p.to_dict() for p in posts])


@api.route('/posts/<post_id>')
def get_post(post_id):
    post = Post.query.get_or_404(post_id)
    return jsonify(post.to_dict())



@api.route('/posts', methods=["POST"]) # post request
def create_post():
    if not request.is_json:
        return jsonify({'error': 'Your request content-type must be application/json'}), 400
    # get the data from the request body
    data = request.json
    print(data, type(data))
    for field in ['title', 'body', 'user_id']:
        if field not in data:
            # if field not in request body, respond with a 400 error
            return jsonify({'error': f'{field} must be in request body'}), 400
            # error is the response and 400 is the server error
    
    # Get fields from data dict
    title = data.get('title')
    body = data.get('body')
    user_id = data.get('user_id')

    # Create new instance of post with data
    new_post = Post(title=title, body=body, user_id=user_id)
    return jsonify(new_post.to_dict()), 201


# Create route to grab specified user's data ('email', 'id', 'password', 'username', 'date_created', 'id')
@api.route('/users/<id>', methods=["GET"])
def get_user(id):
    user = User.query.get_or_404(id)
    return jsonify(user.to_dict())


# Create route to create a new user and send POST request to add to our data
@ api.route('/users/', methods=["POST"])
def create_user():
    if not request.is_json:
        return jsonify({'error': 'Your request content-type must be application/json'}), 400

    data = request.json
    for field in ['email', 'username', 'password']:
        if field not in data:
            return jsonify({'error': f'{field} must be in request body'}), 400
    
    # Get fields from data dictionary
    email = data.get('email')
    username = data.get('username')
    password = data.get('password')

    # Create a new instance of a created user with the data
    new_user = User(email=email, username=username, password=password)
    return jsonify(new_user.to_dict()), 201