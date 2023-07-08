for (var i=0; i<list_data.length; i++){
    document.write('Title：'+list_data[i].title+'<br>');
    document.write('price：'+list_data[i].price+'<br>');
    document.write('detail：'+list_data[i].detail+'<br>');
    document.write('<form method="post" action="/recieve_reward"><input type="submit" class="nes-btn is-success" value="購入"></form>');
    document.write('<br>');
}

const createItem = (item = null) => {
    const e = document.createElement('div')
    e.className = 'item-box'
    if (item) {
        const title = document.createElement('a')
        title.className = 'item-title'
        title.innerHTML = item.title
        e.appendChild(title)

        const price = document.createElement('a')
        price.className = 'item-price'
        price.innerHTML = '¥' + Number(item.price).toLocaleString()
        e.appendChild(price)

        const desc = document.createElement('a')
        desc.className = 'item-desc'
        desc.innerHTML = '補足：'+item.detail
        e.appendChild(desc)

        const botton = document.createElement('button')
        botton.innerHTML = '購入'
        e.appendChild(botton)
    }
}

const parent = document.getElementById('table-wrapper')

list_data.forEach(item => {
    parent.appendChild(createItem(item))
})