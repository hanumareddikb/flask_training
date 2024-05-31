from flask import Flask
from endpoints.people_endpoints import people_blueprint

app = Flask(__name__)
app.register_blueprint(people_blueprint)

if __name__ == '__main__':
    app.run(debug=True)