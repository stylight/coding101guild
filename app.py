import datetime
import os

from flask import Flask, render_template

static_folder_root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static")

app = Flask(__name__)
app._static_folder = static_folder_root


@app.route('/')
def index():
    return render_template('index.html')


def disable_solutions():
    time_now = datetime.datetime.now()
    # release = datetime.datetime(2016, 7, 27, 17, 45, 0)
    release = datetime.datetime(2016, 7, 26, 11, 45, 0)
    if time_now > release:
        return False
    else:
        return True


@app.route('/sessions/<session_number>')
def sessions(session_number):
    folder = 'sessions/'
    template = 'session_{session_number}.html'.format(
        session_number=session_number)
    return render_template(
        folder + template, disable_solutions=disable_solutions)


if __name__ == "__main__":
    app.run(debug=True)
