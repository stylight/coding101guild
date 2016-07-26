import datetime
from collections import namedtuple
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

Hint = namedtuple("Hint", ["src", "caption"])
Solution = namedtuple("Solution", ["title", "id_", "repl_src"])

class Challenge(object):

    def __init__(
        self, title='', id_='', hints=None, description='', repl_src='',
        graphic=None):
        self.title = title
        self.id_ = id_
        self.hints = hints
        self.description = description
        self.repl_src = repl_src
        self.graphic = graphic


def session_challenges(session_num):
    challenges = []

    session_num = int(session_num)
    if session_num == 2:
        challenges = [
            Challenge(
                title='Hello, World!',
                id_='hello',
                hints=[
                    Hint(src="/static/images/session2/hello/scratch.png",
                         caption="Scratch"),
                    Hint(src="/static/images/session2/hello/python.png",
                         caption="Python"),
                ],
                description='Modify the following Python program to say, "Hello, World!".',
                repl_src="//repl.it/embed/CeZU/2.js"
            ),
            Challenge(
                title='Strings',
                id_='strings',
                hints=[
                    Hint(src="/static/images/session2/strings/scratch.png",
                         caption="Scratch"),
                    Hint(src="/static/images/session2/strings/python.png",
                         caption="Python"),
                ],
                description='Modify the follow code so that the type of the variable <i>my_string</i> is a string.',
                repl_src="//repl.it/embed/CgBf/0.js"
            ),
            Challenge(
                title='Integers',
                id_='integers',
                description='Modify the follow code so that the type of the variable <i>my_int</i> is an integer.',
                repl_src="//repl.it/embed/CgBx/0.js"
            ),
            Challenge(
                title='Booleans',
                id_='booleans',
                description='Modify the follow code so that the type of the variable <i>my_bool</i> is a boolean.',
                repl_src="//repl.it/embed/CgCS/0.js"
            ),
            Challenge(
                title='Lists',
                id_='lists',
                description='Modify the follow code according to the specification.',
                repl_src="//repl.it/embed/CgFH/1.js"
            ),
        ]

    return challenges

def session_solutions(session_num):
    solutions = []

    session_num = int(session_num)
    if session_num == 2:
        solutions = [
            Solution(
                title='Hello, World!',
                id_='hello',
                repl_src='//repl.it/embed/CeZe/0.js'
            ),
            Solution(
                title='Strings',
                id_='strings',
                repl_src='//repl.it/embed/CgBm/1.js'
            ),
            Solution(
                title='Integers',
                id_='integers',
                repl_src='//repl.it/embed/CgCA/0.js'
            ),
            Solution(
                title='Booleans',
                id_='booleans',
                repl_src='//repl.it/embed/CgEq/0.js'
            ),
            Solution(
                title='Lists',
                id_='lists',
                repl_src='//repl.it/embed/CgFJ/0.js'
            ),
        ]

    return solutions


@app.route('/sessions/<session_number>')
def sessions(session_number):
    folder = 'sessions/'
    template = 'session_{session_number}.html'.format(
        session_number=session_number)

    challenges = session_challenges(session_number)
    solutions = session_solutions(session_number)

    return render_template(
        folder + template,
        challenges=challenges,
        solutions=solutions,
        disable_solutions=disable_solutions,
        enumerate=enumerate
    )


if __name__ == "__main__":
    app.run(debug=True)
