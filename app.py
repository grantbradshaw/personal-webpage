from flask import Flask, render_template
from sassutils.wsgi import SassMiddleware
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.wsgi_app = SassMiddleware(app.wsgi_app, {
    'app': ('static/sass', 'static/css', '/static/css')
})
app.config.from_object(os.environ['APP_SETTINGS'])


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()