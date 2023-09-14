from flask import Flask, render_template, request, redirect, url_for
import datetime

app = Flask(__name__)

# 各クラスのデータベース
database = {
    "北館1階":{
        "マルチパーパスホール":["MPH　手帳甲子園", "混雑していない", ":".join(map(str, [datetime.datetime.now().hour, datetime.datetime.now().minute]))],
        "ELC":["ELC　英語部　ポスターの掲示・動画制作/フォーチュンクッキー", "混雑していない", ":".join(map(str, [datetime.datetime.now().hour, datetime.datetime.now().minute]))],
    },
    "北館2階":{
         "3G":["3-G　歴史部　伊勢屋　団子/東京湾要塞", "混雑していない", ":".join(map(str, [datetime.datetime.now().hour, datetime.datetime.now().minute]))],
         "3H":["3-H　美術部　作品展示・作品販売", "混雑していない", ":".join(map(str, [datetime.datetime.now().hour, datetime.datetime.now().minute]))],
    },
    "北館3階":{
        "1S":["1-S　オーストラリア研究　英語Ver", "混雑していない", ":".join(map(str, [datetime.datetime.now().hour, datetime.datetime.now().minute]))],
        "1T":["1-T　オーストラリア研究　英語Ver", "混雑していない", ":".join(map(str, [datetime.datetime.now().hour, datetime.datetime.now().minute]))],
        "2S":["2-S　研究発表", "混雑していない", ":".join(map(str, [datetime.datetime.now().hour, datetime.datetime.now().minute]))],
        "2T":["2-T　King of shotting", "混雑していない", ":".join(map(str, [datetime.datetime.now().hour, datetime.datetime.now().minute]))],
    },
    "北館4階":{
        "3M":["3M PTA/渉外部", "混雑していない", ":".join(map(str, [datetime.datetime.now().hour, datetime.datetime.now().minute]))],
    },
    "南館2階":{
        "J1A":["J1-A　グローバル探求", "混雑していない", ":".join(map(str, [datetime.datetime.now().hour, datetime.datetime.now().minute]))],
        "J1B":["J1-B　グローバル探求", "混雑していない", ":".join(map(str, [datetime.datetime.now().hour, datetime.datetime.now().minute]))],
        "J2A":["J2-A　英語落語", "混雑していない", ":".join(map(str, [datetime.datetime.now().hour, datetime.datetime.now().minute]))],
        "J2B":["J2-B　英語落語", "混雑していない", ":".join(map(str, [datetime.datetime.now().hour, datetime.datetime.now().minute]))],
        "J3A":["J3-A　オーストラリア研究", "混雑していない", ":".join(map(str, [datetime.datetime.now().hour, datetime.datetime.now().minute]))],
        "J3B":["J3-B　オーストラリア研究", "混雑していない", ":".join(map(str, [datetime.datetime.now().hour, datetime.datetime.now().minute]))],
        "技術室":["中学校技術室　英語落語", "混雑していない", ":".join(map(str, [datetime.datetime.now().hour, datetime.datetime.now().minute]))],
        "通路":["J2-A/B前　中学国際文化部　生け花展示", "混雑していない", ":".join(map(str, [datetime.datetime.now().hour, datetime.datetime.now().minute]))],
        "3A":["3-A　文芸部　駄菓子・市販のパン・ジュース", "混雑していない", ":".join(map(str, [datetime.datetime.now().hour, datetime.datetime.now().minute]))],
        "3B":["3-B　茶道部　お茶と和菓子（まんじゅう）", "混雑していない", ":".join(map(str, [datetime.datetime.now().hour, datetime.datetime.now().minute]))],
        "3C":["3-C　囲碁将棋部　詰将棋・囲碁", "混雑していない", ":".join(map(str, [datetime.datetime.now().hour, datetime.datetime.now().minute]))],
    },
    "南館3階":{
        "2A":["2-A　2-K　シューティングゲーム", "混雑していない", ":".join(map(str, [datetime.datetime.now().hour, datetime.datetime.now().minute]))],
        "2B":["2-B　縁日", "混雑していない", ":".join(map(str, [datetime.datetime.now().hour, datetime.datetime.now().minute]))],
        "2C":["2-C　ゴーストゲームセンター", "混雑していない", ":".join(map(str, [datetime.datetime.now().hour, datetime.datetime.now().minute]))],
        "2D":["2-D　大型展示物", "混雑していない", ":".join(map(str, [datetime.datetime.now().hour, datetime.datetime.now().minute]))],
        "2E":["2-E　魔法学園", "混雑していない", ":".join(map(str, [datetime.datetime.now().hour, datetime.datetime.now().minute]))],
        "2F":["2-F　VS豪", "混雑していない", ":".join(map(str, [datetime.datetime.now().hour, datetime.datetime.now().minute]))],
        "2G":["2-G　2-H　脱出ゲーム", "混雑していない", ":".join(map(str, [datetime.datetime.now().hour, datetime.datetime.now().minute]))],
        "2H":["写真部　写真展示", "混雑していない", ":".join(map(str, [datetime.datetime.now().hour, datetime.datetime.now().minute]))],
        "2I":["2-I　ユニバーサルスタジオトーヨー（UST)", "混雑していない", ":".join(map(str, [datetime.datetime.now().hour, datetime.datetime.now().minute]))],
        "2J":["2-J　謎解きゲーム", "混雑していない", ":".join(map(str, [datetime.datetime.now().hour, datetime.datetime.now().minute]))],
        "地歴公民科室":["地歴公民科室　弓道の歴史の研究", "混雑していない", ":".join(map(str, [datetime.datetime.now().hour, datetime.datetime.now().minute]))],
        "小演習室２":["小演習室②　生け花展示・アメリカンフラワー販売", "混雑していない", ":".join(map(str, [datetime.datetime.now().hour, datetime.datetime.now().minute]))],
        "小演習室３":["小演習室③　1ST　アナと雪の女王（劇）", "混雑していない", ":".join(map(str, [datetime.datetime.now().hour, datetime.datetime.now().minute]))],
    },
    "南館4階":{
        "1A":["1-A　STEAM教育で学んだプレゼン結果", "混雑していない", ":".join(map(str, [datetime.datetime.now().hour, datetime.datetime.now().minute]))],
        "1B":["1-B　STEAM教育で学んだプレゼン結果", "混雑していない", ":".join(map(str, [datetime.datetime.now().hour, datetime.datetime.now().minute]))],
        "1C":["1-C　STEAM教育で学んだプレゼン結果", "混雑していない", ":".join(map(str, [datetime.datetime.now().hour, datetime.datetime.now().minute]))],
        "1D":["1-D　STEAM教育で学んだプレゼン結果", "混雑していない", ":".join(map(str, [datetime.datetime.now().hour, datetime.datetime.now().minute]))],
        "1E":["1-E　STEAM教育で学んだプレゼン結果", "混雑していない", ":".join(map(str, [datetime.datetime.now().hour, datetime.datetime.now().minute]))],
        "1F":["1-F　STEAM教育で学んだプレゼン結果", "混雑していない", ":".join(map(str, [datetime.datetime.now().hour, datetime.datetime.now().minute]))],
        "1G":["1-G　STEAM教育で学んだプレゼン結果", "混雑していない", ":".join(map(str, [datetime.datetime.now().hour, datetime.datetime.now().minute]))],
        "1H":["1-H　STEAM教育で学んだプレゼン結果", "混雑していない", ":".join(map(str, [datetime.datetime.now().hour, datetime.datetime.now().minute]))],
        "1I":["1-I　STEAM教育で学んだプレゼン結果", "混雑していない", ":".join(map(str, [datetime.datetime.now().hour, datetime.datetime.now().minute]))],
        "1J":["1-J　STEAM教育で学んだプレゼン結果", "混雑していない", ":".join(map(str, [datetime.datetime.now().hour, datetime.datetime.now().minute]))],
        "1O":["1-O　オリジナル研究発表", "混雑していない", ":".join(map(str, [datetime.datetime.now().hour, datetime.datetime.now().minute]))],
        "大演習室1":["南館4階大演習室　1-L/M STEAM教育で学んだプレゼン結果", "混雑していない", ":".join(map(str, [datetime.datetime.now().hour, datetime.datetime.now().minute]))],
        "大演習室2":["南館4階大演習室　数理研同好会　ポスター展示", "混雑していない", ":".join(map(str, [datetime.datetime.now().hour, datetime.datetime.now().minute]))],
    },
    "三号館1階":{
        "昇降口":["昇降口　担任の先生似顔絵コンテスト", "混雑していない", ":".join(map(str, [datetime.datetime.now().hour, datetime.datetime.now().minute]))],
        "昇降口":["Tシャツコンテスト　", "混雑していない", ":".join(map(str, [datetime.datetime.now().hour, datetime.datetime.now().minute]))],
        "化学室1":["化学室　科学同好会　実験実演", "混雑していない", ":".join(map(str, [datetime.datetime.now().hour, datetime.datetime.now().minute]))],
        "化学室2":["化学室　科学部　科学手品・研究出展", "混雑していない", ":".join(map(str, [datetime.datetime.now().hour, datetime.datetime.now().minute]))],
        "グリーンホール":["グリーンホール　1K　探究活動TEDスピーチ", "混雑していない", ":".join(map(str, [datetime.datetime.now().hour, datetime.datetime.now().minute]))],
        "図書室":["図書室　図書委員会　図書館の本の魅力をもっと知ってもらおう/古本市/パンの店ひつじ雲パン", "混雑していない", ":".join(map(str, [datetime.datetime.now().hour, datetime.datetime.now().minute]))],
        "PC教室1・2":["PC教室　ICT Lab　VRバトルロワイヤル", "混雑していない", ":".join(map(str, [datetime.datetime.now().hour, datetime.datetime.now().minute]))],
    },
    "三号館2階":{
        "AEZ":["AEZ　2-LM　お化け屋敷", "混雑していない", ":".join(map(str, [datetime.datetime.now().hour, datetime.datetime.now().minute]))],
        "レクチャールーム":["レクチャールーム　建築模型コンテスト", "混雑していない", ":".join(map(str, [datetime.datetime.now().hour, datetime.datetime.now().minute]))],
    },
    "三号館3階":{
        "1K":["1-K　軽音楽研究部　ライブ（演奏発表会）", "混雑していない", ":".join(map(str, [datetime.datetime.now().hour, datetime.datetime.now().minute]))],
        "2K":["2-K　軽音楽研究部　ライブ（演奏発表会）", "混雑していない", ":".join(map(str, [datetime.datetime.now().hour, datetime.datetime.now().minute]))],
        "講堂1":["三号館3階大ホール　演劇部　演劇発表", "混雑していない", ":".join(map(str, [datetime.datetime.now().hour, datetime.datetime.now().minute]))],
        "講堂2":["三号館3階大ホール　落語研究同好会　落語研究発表", "混雑していない", ":".join(map(str, [datetime.datetime.now().hour, datetime.datetime.now().minute]))],
        "講堂3":["三号館3階大ホール前フロア　国語科　短歌展示", "混雑していない", ":".join(map(str, [datetime.datetime.now().hour, datetime.datetime.now().minute]))],
        "演習室A":["演習室A　書道同好会　書道の研究結果", "混雑していない", ":".join(map(str, [datetime.datetime.now().hour, datetime.datetime.now().minute]))],
    },
    "三号館4階":{
        "演習室C":["演習室C　2-G　お化け屋敷", "混雑していない", ":".join(map(str, [datetime.datetime.now().hour, datetime.datetime.now().minute]))],
        "AL②1":["AL②　2-A　お化け屋敷", "混雑していない", ":".join(map(str, [datetime.datetime.now().hour, datetime.datetime.now().minute]))],
        "AL②2":["AL②　3-F　お化け屋敷", "混雑していない", ":".join(map(str, [datetime.datetime.now().hour, datetime.datetime.now().minute]))],
    }

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
    # ここはローカルと外部で書き換える
    return redirect("http://ict-lab.toyo-ushiku.jp/北館1階")

# 実働時にはdebugはオフに
# 今回は実験がてら、flaskのテストサーバーではなく、wsgiのサーバーを使って実装したい
if __name__ == "__main__":
    app.run(port=8000, host="0.0.0.0", debug=True)