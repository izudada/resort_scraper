from app import app

@app.route("/admin/dashboard")
def admin_dashboard():
    return "Welcome To Admin Dashboard"


@app.route("/admin/profile")
def admin_profile():
    return "<h1 style='color:pink'> Change Admin Details!! </h1>"