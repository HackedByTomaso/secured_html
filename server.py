from flask import Flask, request, session, redirect, url_for, render_template

app = Flask(__name__)
app.secret_key = "CHANGE_THIS_SECRET"

PASSWORD = "SPtestik"

@app.route("/")
def index():
    return redirect(url_for("appp"))

@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        if request.form.get("password") == PASSWORD:
            session["logged_in"] = True
            return redirect(url_for("appp"))
        error = "Špatné heslo"
    return render_template("login.html", error=error)

@app.route("/app")
def appp():
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    return render_template("app.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True, port=6767, host="0.0.0.0")
