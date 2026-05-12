from flask import Flask, render_template, request, send_file
from scrapper import search_incruit, search_saramin
from file import save_to_csv




app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    saramin_jobs = search_saramin(keyword,1)
    incruit_jobs = search_incruit(keyword,1)
    all_jobs = saramin_jobs + incruit_jobs
    return render_template("search.html", jobs=enumerate(all_jobs), keyword=keyword)


@app.route("/file")
def file():
    keyword = request.args.get("keyword")
    all_jobs = search_incruit(keyword,1) + search_saramin(keyword,1)
    save_to_csv(all_jobs)
    return send_file("downloads.csv", as_attachment=True)




if __name__ == '__main__':
    app.run(debug=True)