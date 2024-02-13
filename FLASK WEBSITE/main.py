
from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
    #definitely this allows for the flask app to reload when a change is made.

