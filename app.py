#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask,render_template,request
import reward_list
import os
import openai
import re
openai.api_type = "azure"
openai.api_base = "https://sample-ken-uk.openai.azure.com/"
openai.api_version = "2023-03-15-preview"
openai.api_key = "24959fc582944f77ac07cb77da6b8c0f"

app = Flask(__name__)

@app.route('/')
def home():
    # 現在のイベントの写真リスト（ダミーデータ）
    events = [
        {
            'id': '1',
            'image': '/static/event1.png'
        },
        {
            'id': '2',
            'image': '/static/event2.png'
        },
        {
            'id': '3',
            'image': '/static/event3.png'
        },
    ]
    
    # 商品交換の説明
    exchange_description = '''
                            スポーツ観戦の新たな興奮が待っています！<br/>
                            参加してポイントを貯め、素晴らしい商品と交換しましょう！
                            応援グッズやオフィシャルアイテムなど、あなたのスポーツ愛をさらに深めるチャンスです。
                            ホームページで詳細をチェック！」
                            '''
    
    return render_template('home.html', events=events, exchange_description=exchange_description)

@app.route("/exchange")
def rewardlist():
    rewardlist= reward_list.main()
    return render_template("reward.html",list = rewardlist)

@app.route("/recieve_reward")
def recievereward():
    # ポイント消費処理
    return render_template("reward.html",list = rewardlist)

@app.route("/login", methods=["GET"])
def login():
    return render_template("login.html")

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
