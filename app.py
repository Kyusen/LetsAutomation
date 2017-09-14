from main.wsgi import app
__author__ = "Leonardo Otacílio Narciso Ramos"

if __name__ == "__main__":
    app.run(port=app.config['PORT'],
            debug=app.config['DEBUG'])