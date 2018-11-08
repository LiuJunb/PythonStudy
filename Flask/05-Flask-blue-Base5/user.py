from main import app

@app.route('/get_user')
def get_user():
    return 'user page'