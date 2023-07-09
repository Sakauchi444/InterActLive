for (var i=0; i<list_data.length; i++){
    document.write('<div class="box75">')
    document.write('<div class="box-title">'+list_data[i].title+'</div>');
    document.write('<a class="item-price">必要ポイント：'+list_data[i].price+'</a><br>');
    document.write(list_data[i].detail+'<br>');
    document.write('<button type="button" onclick="recieve_reward('+Number(i+1)+')">購入</button>')
    document.write('</div>');
}

function recieve_reward(id){
    console.log(id)
    var point = parseInt(localStorage.getItem('point'));
    point = point - Number(list_data[id-1].price);
    localStorage.setItem('point', point);
    location.href = '/recieve_reward/' + Number(id);
}