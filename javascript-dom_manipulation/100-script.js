document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('add_item').addEventListener('click', function() {
        const ul = document.querySelector('.my_list');
        const li = document.createElement('li');
        li.appendChild(document.createTextNode('Item'));
        ul.appendChild(li);
    });

    document.getElementById('remove_item').addEventListener('click', function() {
        const list = document.querySelector('.my_list');
        if (list.lastElementChild) {
            list.removeChild(list.lastElementChild);
        }
    });

    document.getElementById('clear_list').addEventListener('click', function() {
        document.querySelector('.my_list').innerHTML = '';
    });
});