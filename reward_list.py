def main():
    return [
        {
            "id":1,
            "title":"選手とのビデオ通話チケット",
            "price":1000,
            "detail":"参加者がお気に入りの選手と個人的に交流できる貴重な機会。",
            "img":"../static/img/video_chat"
        },
        {
            "id":2,
            "title":"サイン入りの公式ユニフォーム",
            "price":500,
            "detail":"チームの現役選手全員からのサインが入った特別なユニフォーム。"
        },
        {
            "id":3,
            "title":"オフィシャルクラブグッズ",
            "price":300,
            "detail":"チームのマフラーやキャップ、ステッカー、バッジなどのグッズ"
        },
        {
            "id":4,
            "title":"クラブの歴史本",
            "price":50,
            "detail":"チームの歴史や成功を紹介した本やDVD。"
        },
        {
            "id":5,
            "title":"スタジアムツアーチケット",
            "price":300,
            "detail":"スタジアムの内部を案内してもらえるツアーのチケット。"
        },
        {
            "id":6,
            "title":"飲食物一割引券",
            "price":100,
            "detail":"ゲームデーにスタジアムで利用できる飲食物の割引券。"
        },
        {
            "id":7,
            "title":"無料食事券",
            "price":300,
            "detail":"スタジアムのフードコートで使用可能な無料食事クーポン。"
        },
        {
            "id":8,
            "title":"vip席観戦体験",
            "price":500,
            "detail":"最高のロケーションにある席で試合を観戦する権利。"
        },
      ]

def point_change(id):
    reward_list = main()
    for i in reward_list:
        if i['id'] == id:
            return i['price'],i
    return 0,i
