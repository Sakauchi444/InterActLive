#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask,render_template,request
import reward_list
import os
import re
import requests
import json

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
    events = [
        [
            '日本 vs ブラジル',
            '/static/event1.png'
        ],
        [
            'スペイン vs ブラジル',
            '/static/event2.png'
        ],
        [
            'スペイン vs 日本',
            '/static/event3.png'
        ]
    ]

    return render_template("event.html", eventdetail=events[id-1][0], image=events[id-1][1], event_id=id)

@app.route("/question", methods=["GET"])
def question():
    # 各種情報を設定
    YOUR_RESOURCE_NAME = "sample-ken-UK"
    YOUR_DEPLOYMENT_NAME = "sample-ken-deploy"
    YOUR_API_KEY = "24959fc582944f77ac07cb77da6b8c0f"
    YOUR_RESOURCE_URL = "https://sample-ken-uk.openai.azure.com"
    YOUR_AZURE_COGNITIVE_SEARCH_ENDPOINT = "https://cogsearch-uk.search.windows.net/"
    YOUR_AZURE_COGNITIVE_SEARCH_KEY = "XOVwE9qDvD0UznBSYTfG84I2BTH3PO77lLVJcbjSUcAzSeBSRg4f"
    YOUR_AZURE_COGNITIVE_SEARCH_INDEX_NAME = "index"

    # URLを設定
    url = f"{YOUR_RESOURCE_URL}/openai/deployments/{YOUR_DEPLOYMENT_NAME}/extensions/chat/completions?api-version=2023-06-01-preview"

    chatgpt_url = f"{YOUR_RESOURCE_URL}/openai/deployments/{YOUR_DEPLOYMENT_NAME}/chat/completions?api-version=2023-06-01-preview"

    # ヘッダーを設定
    headers = {
        "Content-Type": "application/json",
        "api-key": YOUR_API_KEY,
        "chatgpt_url": chatgpt_url,
        "chatgpt_key": YOUR_API_KEY,
    }

    # データを設定
    data = {
        "dataSources": [
            {
                "type": "AzureCognitiveSearch",
                "parameters": {
                    "endpoint": YOUR_AZURE_COGNITIVE_SEARCH_ENDPOINT,
                    "key": YOUR_AZURE_COGNITIVE_SEARCH_KEY,
                    "indexName": YOUR_AZURE_COGNITIVE_SEARCH_INDEX_NAME,
                },
            },
        ],
        "messages": [
            {
                "role": "user",
                "content": "#命令書\nあなたはクイズの出題者です。Data Sourceの情報に基づいてワールドカップにまつわるクイズを4題出題してください\n#制約条件\n– データセットを参照して回答してください。\n– 異なる4択の選択肢とその答えを作成してください。\n– 日本語で問題を作成してください。\n#出題例\n\n問題文:FIFAワールドカップの優勝回数が最も多い国はどこですか?\na) ブラジル\nb) イタリア\nc) アルゼンチン\nd) ドイツ\n答え: a) ブラジル",
            },
        ],
    }

    # リクエストを送信し、レスポンスを取得
    response = requests.post(url, headers=headers, data=json.dumps(data))
    resp_json = response.json()
    ques_response = resp_json['choices'][0]['messages'][1]['content']

    # レスポンスを表示
    print(ques_response)

    # 整形
    ques_split = re.split('問題|\?|？|答え:|答え：', ques_response)
    print(ques_split)
    ques_list = []
    for i in range(len(ques_split)):
        temp = ques_split[i].replace('\n', '  ')
        if i % 3 == 1:
            m = re.findall('.*:(.*)', temp)
            print(m)
            ques_list.append(m[0])
        elif i % 3 == 2:
            ques_list.append(temp)
        else:
            ques_list.append(temp.replace('[doc1]', ''))

    # ques_list = ["q1", "a", "q2", "b", "q3", "c", "q4", "d"]
    print(ques_list)

    return render_template("question.html", ques_list=ques_list)

## 実行
if __name__ == "__main__":
    app.run(debug=True)
