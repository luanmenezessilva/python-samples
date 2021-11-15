from flask import Flask, jsonify, request, make_response
import jwt
import datetime
from functools import wraps

app = Flask(__name__)

app.config['SECRET_KEY'] = 'thisisthesecretkey'

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token') # http://127.0.0.1/5000/router?token=asdfasfasdf

        if not token:
            return jsonify({'message': 'Token is missing'}), 403

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
        except:
            return jsonify({'message': 'Token is invalid'}), 403
        
        return f(*args, **kwargs)
    return decorated


# Route para qualquer um acessar
@app.route('/unprotected')
def unprotected():
    return jsonify({'message': 'Anyone can view this'}), 200

# Route para apenas autorizados acessar
@app.route('/protected')
@token_required
def protected():
    return jsonify({'message': 'This is only for people with valid tokens'}), 200

# Route para conseguir autorizaÃ§Ã£o
@app.route('/login')
def login():
    auth = request.authorization

    if auth and auth.password == '1':
        token = jwt.encode({'user': auth.username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
        return jsonify({'token': token.decode('UTF-8')})

    return make_response ('Could verify!', 401, {'WWW-Authenticate' : 'Basic realm="Login Required"'})


if __name__ == '__main__':
    app.run(host='127.0.0.1',port=8084, debug=True)
    # app.run(debug=True)