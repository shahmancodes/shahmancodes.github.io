from flask import Flask, render_template, url_for

app = Flask(__name__, 
    static_folder='static',
    template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/projects')
@app.route('/projects.html')
def projects():
    return render_template('projects.html')

@app.route('/books')
@app.route('/books.html')
def books():
    return render_template('books.html')

# Error handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080) 