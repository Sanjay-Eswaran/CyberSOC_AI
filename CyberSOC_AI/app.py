from flask import Flask, render_template

app = Flask(
    __name__,
    template_folder="dashboard/templates",
    static_folder="dashboard/static"
)

@app.route("/")
def dashboard():
    return render_template("dashboard.html")

if __name__ == "__main__":
    print("🔥 DASHBOARD APP RUNNING 🔥")
    app.run(debug=True)
