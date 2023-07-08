from flask import Flask,render_template,request
import reward_list

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def main_page():
    if request.method == 'GET':
        text = "ここに結果が出力されます"
        return render_template("page.html",text=text)
    elif request.method == 'POST':
        name = request.form["name"]
        text = "こんにちは" + name + "さん"
        return render_template("page.html",text=text)

@app.route("/reward", methods=["POST"])
def rewardlist():
    rewardlist= reward_list.main()
    return render_template("reward.html",list = rewardlist)
## 実行
if __name__ == "__main__":
    app.run(debug=True)