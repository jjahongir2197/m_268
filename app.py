from flask import Flask, render_template, request, redirect

app = Flask(__name__)

posts = []

@app.route("/", methods=["GET", "POST"])
def blog():
    if request.method == "POST":
        title = request.form["title"]
        posts.append(title)
        return redirect("/")

    return render_template("blog.html", posts=posts)

if __name__ == "__main__":
    app.run(debug=True)
