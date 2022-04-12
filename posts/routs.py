from flask import Blueprint

posts = Blueprint('posts',__name__, url_prefix='/posts')

@posts.route('/getposts')
def getdata():
    return {'key':'value'}