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
    release = datetime.datetime(2016, 7, 27, 17, 35, 0)
    # release = datetime.datetime(2016, 7, 26, 11, 45, 0)
    if time_now > release:
        return False
    else:
        return True

Hint = namedtuple("Hint", ["src", "caption"])
Solution = namedtuple("Solution", ["title", "id_", "repl_src"])

class Challenge(object):

    def __init__(
        self, title='', id_='', hints=None, description=None, repl_src='',
        repl_solution='', graphic=None):
        self.title = title
        self.id_ = id_
        self.hints = hints
        if description is None:
            self.description = 'Modify the follow code according to the specification.'
        else:
            self.description = description
        self.repl_src = repl_src
        self.graphic = graphic
        self.repl_solution = repl_solution


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
                repl_src="//repl.it/embed/CeZU/2.js",
                repl_solution='//repl.it/embed/CeZe/0.js'
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
                repl_src="//repl.it/embed/CgBf/2.js",
                repl_solution="//repl.it/embed/CgBm/1.js"
            ),
            Challenge(
                title='Integers',
                id_='integers',
                description='Modify the follow code so that the type of the variable <i>my_int</i> is an integer.',
                repl_src="//repl.it/embed/CgBx/0.js",
                repl_solution='//repl.it/embed/CgCA/0.js'
            ),
            Challenge(
                title='Booleans',
                id_='booleans',
                description='Modify the follow code so that the type of the variable <i>my_bool</i> is a boolean.',
                repl_src="//repl.it/embed/CgCS/0.js",
                repl_solution='//repl.it/embed/CgEq/0.js'
            ),
            Challenge(
                title='Lists',
                id_='lists',
                repl_src="//repl.it/embed/CgFH/1.js",
                repl_solution='//repl.it/embed/CgFJ/0.js'
            ),
            Challenge(
                title='List Append',
                id_='list_append',
                repl_src="//repl.it/embed/CgFm/0.js",
                repl_solution='//repl.it/embed/CgFp/0.js'
            ),
            Challenge(
                title='List Indices',
                id_='list_indices',
                repl_src='//repl.it/embed/Ce0B/3.js',
                repl_solution='//repl.it/embed/CgN2/0.js'
            ),
            Challenge(
                title='Personalized Greeting',
                id_='personalzied_greeting',
                repl_src="//repl.it/embed/CeZl/2.js",
                repl_solution='//repl.it/embed/CgMZ/0.js'
            ),
            Challenge(
                title='Conditional Greeting',
                id_='conditional_greeting',
                repl_src="//repl.it/embed/CeZt/1.js",
                repl_solution='//repl.it/embed/CeZv/0.js'
            ),
            Challenge(
                title='Counter',
                id_='counter',
                repl_src='//repl.it/embed/CeZw/3.js',
                repl_solution='//repl.it/embed/CeZx/1.js'
            ),
            Challenge(
                title='Print Even Numbers',
                id_='even_nums',
                repl_src='//repl.it/embed/CgXv/0.js',
                repl_solution='//repl.it/embed/CgXw/0.js'
            ),
            Challenge(
                title='Friends',
                id_='friends',
                repl_src='//repl.it/embed/CeZn/12.js',
                repl_solution='//repl.it/embed/CeZn/13.js'
            ),
            Challenge(
                title='Beer Song',
                id_='beer_song',
                repl_src='//repl.it/embed/Ce0F/1.js',
                repl_solution='//repl.it/embed/Ce0G/1.js'
            ),
            # Challenge(
            #     title='',
            #     id_='',
            #     repl_src='',
            #     repl_solution=''
            # ),
        ]

    return challenges


@app.route('/sessions/<session_number>')
def sessions(session_number):
    folder = 'sessions/'
    template = 'session_{session_number}.html'.format(
        session_number=session_number)

    challenges = session_challenges(session_number)

    return render_template(
        folder + template,
        challenges=challenges,
        disable_solutions=disable_solutions,
        enumerate=enumerate
    )


if __name__ == "__main__":
    app.run(debug=True)
