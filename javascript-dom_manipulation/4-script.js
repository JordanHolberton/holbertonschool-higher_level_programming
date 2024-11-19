document.querySelector('#add_item').addEventListener('click', function () {
    const ul = document.querySelector('.my_list');
    const li = document.createElement('li');
    li.appendChild(document.createTextNode('Item'));
    ul.appendChild(li);
});