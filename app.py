from flask import Flask, render_template, request, redirect, url_for
import datetime
import json

app = Flask(__name__)

with open("database.json", "r") as f:
    database = json.load(f)

# メインページ 館ごとに混雑状況を確認できる
@app.route("/<tabname>")
def main(tabname):
    return render_template("index.html", tabname=tabname, data=database[tabname])

# 混雑状況の更新ページ
@app.route("/update/<tabname>", methods=["GET"])
def update(tabname):
    _class = request.args.get("class")
    congestion = request.args.get("congestion")
    print(_class, congestion)
    if _class != None and congestion != None:
        database[tabname][_class][2] = congestion
        database[tabname][_class][3] = ":".join(map(str, [datetime.datetime.now().hour, datetime.datetime.now().minute]))
        print(database)
        with open("database.json", "w") as f:
            json.dump(database, f, indent=2)

    return render_template("update.html",tabname=tabname, data=database[tabname])

# /に来たら北館ページに遷移
@app.route("/")
def redi():
    # ここはローカルと外部で書き換える
    return redirect("http://ict-lab.toyo-ushiku.jp/北館1階")

@app.route("/update")
def redirect_update():
    return redirect("http://ict-lab.toyo-ushiku.jp/update/北館1階")

# 実働時にはdebugはオフに
# 今回は実験がてら、flaskのテストサーバーではなく、wsgiのサーバーを使って実装したい
if __name__ == "__main__":
    app.run(port=8000, host="0.0.0.0", debug=True)