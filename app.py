from flask import Flask,render_template,request
import reward_list

app = Flask(__name__)

point = 100

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
    
    return render_template('home.html',events=events,exchange_description=exchange_description)

@app.route("/exchange")
def rewardlist():
    rewardlist= reward_list.main()
    return render_template("reward.html",list = rewardlist,point=point)

@app.route("/recieve_reward")
def recievereward():
    global point
    id = request.form.get('id')
    print(id)
    usepoint,rewardlist = reward_list.point_change(id)
    point -= usepoint
    return render_template("complete_recieve.html",list = rewardlist,point=point)

## 実行
if __name__ == "__main__":
    app.run(debug=True)