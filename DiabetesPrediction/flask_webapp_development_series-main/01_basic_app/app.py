from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome_to_ai():
    return 'Welcome to the world of AI!'

if __name__ == '__main__':
    app.run(debug=True)
