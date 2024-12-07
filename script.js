window.addEventListener('load', function() {
    fetch('/movies')
        .then(response => response.json())
        .then(data => {
            const moviesDiv = document.getElementById('movies');
            data.forEach(movie => {
                const movieElement = document.createElement('div');
                movieElement.innerHTML = <h2>${movie.title}</h2>
                                          <p>Genre: ${movie.genre}</p>
                                          <p>Release Year: ${movie.release_year}</p>;
                moviesDiv.appendChild(movieElement);
            });
      });
});
