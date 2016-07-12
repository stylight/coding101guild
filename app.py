from flask import Flask, render_template
import os
static_folder_root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static")

app = Flask(__name__)
app._static_folder = static_folder_root


@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/sessions/<session_number>')
def sessions(session_number):
    folder = 'sessions/'
    template = 'session_{session_number}.html'.format(
        session_number=session_number)
    return render_template(folder + template)


if __name__ == "__main__":
    app.run(debug=True)
