from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def users():
    if request.method == 'POST':
        user = {
            'id': request.json['id'],
            'name': request.json['name']
        }
        # You can add the new user to a database or store it in memory here
        return jsonify({'user': user}), 201
    else:
        # Return all users
        users = [
            {
                'id': 1,
                'name': 'User 1'
            },
            {
                'id': 2,
                'name': 'User 2'
            }
        ]
        return jsonify({'users': users})


app.run(debug=True)
