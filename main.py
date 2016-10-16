from datetime import datetime
from flask import Flask, render_template
from jinja2 import Template

app = Flask(__name__)


@app.route('/')
def hello_world():
    time = 'Maybe at {0}'.format(datetime.now().strftime('%H:%M'))
    hello = "When will she come?"

    return render_template('where-she.html', title=hello, heading=hello, content=time)

def test():
    pass


if __name__ == '__main__':
    app.run()
