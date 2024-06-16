from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

@app.route("/")
def home():
    page_title = "Home"
    return render_template('index.html', page_title=page_title)

@app.route("/about")
def about():
    page_title = "About"
    return render_template('about.html', page_title=page_title)
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)