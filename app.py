from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
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
