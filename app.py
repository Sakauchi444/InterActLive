import os
import openai
import re
openai.api_type = "azure"
openai.api_base = "https://sample-ken-uk.openai.azure.com/"
openai.api_version = "2023-03-15-preview"
openai.api_key = "24959fc582944f77ac07cb77da6b8c0f"

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
        name = request.form["name"]
        text = "こんにちは" + name + "さん"
        return render_template("page.html",text=text)

@app.route("/event/<int:id>", methods=["GET"])
def event(id):
    return render_template("event.html", event_id=id)

@app.route("/question", methods=["GET"])
def question():

    #質問の設定
    content = "#命令書\nあなたはクイズの出題者です。Data Sourceの情報に基づいてワールドカップにまつわるクイズを4題出題してください\n#制約条件\n– データセットを参照して回答してください。\n– 異なる4択の選択肢とその答えを作成してください。\n– 日本語で問題を作成してください。\n#出題例\n\n問題文:FIFAワールドカップの優勝回数が最も多い国はどこですか?\na) ブラジル\nb) イタリア\nc) アルゼンチン\nd) ドイツ\n答え: a) ブラジル"

    response = openai.ChatCompletion.create(
    engine="sample-ken-deploy",
    messages = [{"role":"system","content":"You are an AI assistant that helps people find information."},{"role":"user","content":content},],
    temperature=0,
    max_tokens=800,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    stop=None)

    ques_response = response['choices'][0]['message']['content']
    print(ques_response)

    ques_split = re.split('\?|？|答え:|答え：|\n\n', ques_response)
    print(ques_split)

    ques_list = []
    for i in range(len(ques_split)):
        temp = ques_split[i].replace('\n', '  ')
        if i % 3 == 0:
            m = re.findall('.*:(.*)', temp)
            print(m)
            ques_list.append(m[0])
        else:
            ques_list.append(temp)

    # ques_list = ["q1", "a", "q2", "b", "q3", "c", "q4", "d"]

    print(ques_list)

    return render_template("question.html", ques_list=ques_list)

## 実行
if __name__ == "__main__":
    app.run(debug=True)
