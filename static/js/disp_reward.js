for (var i=0; i<list_data.length; i++){
    document.write('<div class="box75">')
    document.write('<div class="box-title">'+list_data[i].title+'</div>');
    document.write('<a class="item-price">必要ポイント：'+list_data[i].price+'</a><br>');
    document.write(list_data[i].detail+'<br>');
    // document.write('<form method="post" action="/recieve_reward"><input type="submit" class="btn btn--purple btn--radius btn--cubic" value="購入"></form>');
    document.write('<a href="/recieve_reward"><button type="submit" name="id" value="'+i+'">購入</button></a>')
    document.write('</div>');
}
