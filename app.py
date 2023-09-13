from flask import Flask, render_template, request, redirect, url_for
import datetime

app = Flask(__name__)

# 各クラスのデータベース
database = {
    "北館1階":{},
    "北館2階":{},
    "北館3階":{},
    "北館4階":{},
    "南館1階":{
        "1A":["1-A", "混雑していない", ":".join(map(str, [datetime.datetime.now().hour, datetime.datetime.now().minute]))],
        "1B":["1-B", "混雑していない", ":".join(map(str, [datetime.datetime.now().hour, datetime.datetime.now().minute]))],
        "1C":["1-C", "混雑していない", ":".join(map(str, [datetime.datetime.now().hour, datetime.datetime.now().minute]))],
        "1D":["1-D", "混雑していない", ":".join(map(str, [datetime.datetime.now().hour, datetime.datetime.now().minute]))],
        "1E":["1-E", "混雑していない", ":".join(map(str, [datetime.datetime.now().hour, datetime.datetime.now().minute]))],
        "1F":["1-F", "混雑していない", ":".join(map(str, [datetime.datetime.now().hour, datetime.datetime.now().minute]))],
        "1G":["1-G", "混雑していない", ":".join(map(str, [datetime.datetime.now().hour, datetime.datetime.now().minute]))],
        "1H":["1-H", "混雑していない", ":".join(map(str, [datetime.datetime.now().hour, datetime.datetime.now().minute]))],
        "1I":["1-I", "混雑していない", ":".join(map(str, [datetime.datetime.now().hour, datetime.datetime.now().minute]))],
        "1J":["1-J", "混雑していない", ":".join(map(str, [datetime.datetime.now().hour, datetime.datetime.now().minute]))],
        "1K":["1-K", "混雑していない", ":".join(map(str, [datetime.datetime.now().hour, datetime.datetime.now().minute]))],
        "1L":["1-L", "混雑していない", ":".join(map(str, [datetime.datetime.now().hour, datetime.datetime.now().minute]))],
        "1M":["1-M", "混雑していない", ":".join(map(str, [datetime.datetime.now().hour, datetime.datetime.now().minute]))],
        "1O":["1-O", "混雑していない", ":".join(map(str, [datetime.datetime.now().hour, datetime.datetime.now().minute]))],
        "1S":["1-S", "混雑していない", ":".join(map(str, [datetime.datetime.now().hour, datetime.datetime.now().minute]))],
        "1T":["1-T", "混雑していない", ":".join(map(str, [datetime.datetime.now().hour, datetime.datetime.now().minute]))],
    },
    "南館2階":{},
    "南館3階":{},
    "南館4階":{},
    "三号館":{}
}

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
        database[tabname][_class][1] = congestion
        database[tabname][_class][2] = ":".join(map(str, [datetime.datetime.now().hour, datetime.datetime.now().minute]))
        print(database)
    return render_template("update.html",tabname=tabname, data=database[tabname])

# /に来たら北館ページに遷移
@app.route("/")
def redi():
    return redirect("/北館")

# 実働時にはdebugはオフに
# 今回は実験がてら、flaskのテストサーバーではなく、wsgiのサーバーを使って実装したい
if __name__ == "__main__":
    app.run(port=8000, host="0.0.0.0", debug=True)