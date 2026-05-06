function solve(inputArray) {
    movies = []

    for (const row of inputArray) {
        if (row.includes('addMovie')) {
            addMovie(row, movies);
        } else if (row.includes('directedBy')) {
            addDirector(row, movies);
        } else if (row.includes('onDate')) {
            addDate(row, movies);
        }
    }

    printFullInfo(movies);
    

    function addMovie(row, movies) {
        let movieName = row.replace('addMovie ', '');

        const movieObj = {
            name: movieName
        }

        movies.push(movieObj);
    }

    function addDirector(row, movies) {
        let [movieName, director] = row.split(' directedBy ');
        movies.map(movie => {
            if(movie.name === movieName) {
                movie.director = director;
            }
        })

    }

    function addDate(row, movies) {
        let [movieName, date] = row.split(' onDate ');
        movies.map(movie => {
            if (movie.name === movieName) {
                movie.date = date;
            }
        })
    }

    function printFullInfo(movies) {
        movies
            .filter(movie => movie.director && movie.date)
            .forEach(movie => console.log(JSON.stringify(movie)));
    }
}

solve([
    'addMovie Fast and Furious',
    'addMovie Godfather',
    'Inception directedBy Christopher Nolan',
    'Godfather directedBy Francis Ford Coppola',
    'Godfather onDate 29.07.2018',
    'Fast and Furious onDate 30.07.2018',
    'Batman onDate 01.08.2018',
    'Fast and Furious directedBy Rob Cohen'
]);
solve([
    'addMovie The Avengers',
    'addMovie Superman',
    'The Avengers directedBy Anthony Russo',
    'The Avengers onDate 30.07.2010',
    'Captain America onDate 30.07.2010',
    'Captain America directedBy Joe Russo'
]);