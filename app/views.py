from app import app

@app.route("/")
def index():
    return "Hello User"


@app.route("/about")
def about():
    return "<h1 style='color:red'> About!! </h1>"