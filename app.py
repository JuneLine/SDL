from flask import *

@app.route('/home')
def Home():
    return render_template('heroku-testing.html', title='Home')

if __name__ ==  '__main__':
    app.run(port='80')