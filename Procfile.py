web: gunicorn flask101:app

@app.route('/')
def Home():
    return render_template('heroku-testing.html', title='Home')

if __name__ =  '__main__':
    app.run(port='80')