from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def homepage():
    return render_template('homepage.html')

@app.route('/admin', methods=['GET'])
def admin():
    return render_template('admin.html')

if __name__ == '__main__':
    app.run(debug=True)