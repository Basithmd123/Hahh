from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def greet():
    name = ""
    if request.method == "POST":
        name = request.form.get("name", "")
    return render_template("greet.html", name=name)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
