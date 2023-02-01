from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_users():
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
    return jsonify(users)


app.run(debug=True)
