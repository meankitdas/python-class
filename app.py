from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def htmlpage():
    return render_template("template.html")


@app.route('/randi')
def call():
    return "call me"


@app.route('/sec')
def section_b():
    return "section b students are awesome"


if __name__ == "__main__":
    app.run()
