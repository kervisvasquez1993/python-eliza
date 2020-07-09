from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def hola():
    return render_template('el.html')

@app.route('/about')
def abaout():
    return render_template('about.html')

if __name__ == '__main__':
    app.run('0.0.0.0',5000,debug=True)