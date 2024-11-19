fetch('https://swapi-api.hbtn.io/api/films/?format=json')
    .then(response => response.json())
    .then(data => {
        for (const list of data.results) {
            const ul = document.createElement('li');
            ul.textContent = list.title;
            document.querySelector('#list_movies').appendChild(ul);
        }
    });
