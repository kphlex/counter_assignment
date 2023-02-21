from flask import Flask, render_template, redirect, session, request

app = Flask(__name__)
app.secret_key = 'key1'


@app.route('/')
def capture():
    if 'visit' and 'count' not in session:
        session['visit'] = 0
        session['count'] = 0
        session['increment'] = 2
    else:
        session['visit'] += 1
    return render_template('layout.html')


@app.route('/add')
def add():
    session['count'] += session['increment']
    return redirect('/')


@app.route('/increment', methods=['POST'])
def change_increment():
    session['count'] += int(request.form['increment'])
    session['increment'] = int(request.form['increment'])
    return redirect('/')

@app.route('/reset')
def reset_count():
    session.clear()
    return redirect('/')

@app.errorhandler(404)
def invalid_request(e):
    return ("Under construction")



if __name__ == '__main__':
    app.run(debug=True)