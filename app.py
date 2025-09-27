import os
import webbrowser
from flask import Flask, render_template, request, redirect, url_for
from login import verify_login
from email_analyzer import analyze_email_content  # Updated function

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def login_page():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        valid, role_or_msg = verify_login(username, password)
        if valid:
            return redirect(url_for("dashboard", username=username))
        return render_template("login.html", error=role_or_msg)
    return render_template("login.html")


@app.route("/dashboard/<username>", methods=["GET", "POST"])
def dashboard(username):
    result = None
    if request.method == "POST":
        email_content = request.form.get("email_content")
        if email_content:
            # Analyze the pasted email content directly
            result = analyze_email_content(email_content)
    return render_template("dashboard.html", username=username, result=result)


if __name__ == "__main__":
    webbrowser.open("http://127.0.0.1:5000")
    app.run(host="127.0.0.1", port=5000, debug=True)
