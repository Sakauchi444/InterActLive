from flask import Flask,render_template,request
import reward_list

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
        }
    ]
    
    # 商品交換の説明
    exchange_description = "商品交換の説明文です。"
    
    return render_template('./home.html', events=events, exchange_description=exchange_description)

@app.route("/exchange")
def rewardlist():
    rewardlist= reward_list.main()
    return render_template("reward.html",list = rewardlist)

@app.route("/recieve_reward")
def recievereward():
    # ポイント消費処理
    return render_template("reward.html",list = rewardlist)

## 実行
if __name__ == "__main__":
    app.run(debug=True)