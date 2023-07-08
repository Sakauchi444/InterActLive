from flask import Flask,render_template,request, session, url_for, redirect
from datetime import timedelta

app = Flask(__name__)

app.secret_key = 'abcdefghijklmn'
app.permanent_session_lifetime = timedelta(minutes=3)

@app.route("/", methods=["GET", "POST"])
def main_page():
    if request.method == 'GET':
        text = "ここに結果が出力されます"
        return render_template("page.html",text=text)
    elif request.method == 'POST':
        session.permanent = True
        session["point"] = 0
        session["ques_num"] = 1

        name = request.form["name"]
        text = "こんにちは" + name + "さん"
        return render_template("page.html",text=text)

@app.route("/event/<int:id>", methods=["GET"])
def event(id):
    session["event_id"] = id

    return render_template("event.html", event_id=id, point=session["point"])

@app.route("/question", methods=["GET", "POST"])
def question():
    if session["ques_num"] >= 5:
        return redirect(url_for('event', id=session["event_id"]))

    if request.method == 'GET':
        ques_txt = "問題サンプル"
        choice_list = ["c1", "c2", "c3", "c4"]
        session["answer"] = "c1"

        return render_template("question.html", point=session["point"], ques_num=session["ques_num"], ques_txt=ques_txt, choice_list=choice_list, event_id=session["event_id"])
    elif request.method == 'POST':
        if request.form.get('q') == session["answer"]:
            session["point"] += 10

        session["ques_num"] += 1
        ques_txt = "問題サンプル" + str(session["ques_num"])
        choice_list = ["c1", "c2", "c3", "c4"]
        session["answer"] = "c1"

        if session["ques_num"] >= 5:
            return redirect(url_for('event', id=session["event_id"]))
        else:
            return render_template("question.html", point=session["point"], ques_num=session["ques_num"], ques_txt=ques_txt, choice_list=choice_list, event_id=session["event_id"])

## 実行
if __name__ == "__main__":
    app.run(debug=True)