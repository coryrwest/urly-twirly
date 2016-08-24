import os
import sys
from flask import Flask
from flask import request
app = Flask(__name__)

sys.path.insert(1, os.path.join(sys.path[0], '.'))

import shorturl.parts
import shorturl.dirstore

@app.route('/')
def hello_world():
    return 'Hello and welcome to urly-twirly. A small and simple url shortener. Please see <a href="help">/help</a> for more info.'

@app.route('/help')
def help():
    return 'This is the help page. Hit /create with the <em>token</em> and a <em>url</em> in the query string to get your url.'
    
@app.route('/create', methods=['GET'])
def create():
    token = request.args.get('token')
    url = request.args.get('url')
    if token == '0891':
        part = shorturl.parts.generate_url_part()
        path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'urls')
        shorturl.dirstore.save_url(path, part, url)
        return 'Your short url is: <a href="' + os.path.join(request.url_root, part) + '"/>' + os.path.join(request.url_root, part) + '</a>'
    else:
        return 'Incorrect token'

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    root = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'urls')
    url = shorturl.dirstore.load_url(root, path)
    if url == None:
        return 'That url does not exist'
    else:
        return 'You want: %s' % url

if __name__ == '__main__':
    port = os.getenv('PORT', 8080)
    ip = os.getenv('IP', '0.0.0.0')
    
    app.run(host=ip, port=port)