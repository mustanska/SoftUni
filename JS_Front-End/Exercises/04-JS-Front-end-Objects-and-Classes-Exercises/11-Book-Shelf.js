function solve(inputArray) {
    const shelves = [];

    for (const row of inputArray) {
        if (row.includes('->')) {
            createShelf(row, shelves);
        } else if (row.includes(':')) {
            addBook(row, shelves);
        }
    }

    const sortedShelves = sortShelves(shelves);

    printInfo(sortedShelves);


    function createShelf(row, shelves) {
        let [id, genre] = row.split(' -> ');

        const shelfObj = {
            id,
            shelfGenre: genre,
            books: []
        }

        let shelfId = shelves.filter(shelf => shelf.id === id);

        if (shelfId.length === 0) {
            shelves.push(shelfObj);
        }

    }

    function addBook(row, shelves) {
        let [bookInfo, genre] = row.split(', ');
        let [title, author] = bookInfo.split(': ');

        let book = {
            title,
            author
        }

        for (const shelf of shelves) {
            if (shelf.shelfGenre === genre) {
                shelf.books.push(book);
            }
        }
    }

    function sortShelves(shelves) {
        for (i = 0; i < shelves.length; i++) {
            let shelfEntries = Object.entries(shelves[i]);
            shelves.splice(i, 1, shelfEntries);
        }
        
        shelves.sort((a, b) => b[2][1].length - a[2][1].length);

        for (i = 0; i < shelves.length; i++) {
            let shelf = Object.fromEntries(shelves[i]);
            shelves.splice(i, 1, shelf);
        }

        shelves.map(shelf => sortBooks(shelf.books));

        return shelves;
    }

    function sortBooks(books) {
        for (i = 0; i < books.length; i++) {
            let bookEntries = Object.entries(books[i]);
            books.splice(i, 1, bookEntries);
        }

        books.sort((a, b) => a[0][1].localeCompare(b[0][1]));

        for (i = 0; i < books.length; i++) {
            let book = Object.fromEntries(books[i]);
            books.splice(i, 1, book);
        }
    }

    function printInfo(shelves) {
        for (const shelf of shelves) {
            console.log(`${shelf.id} ${shelf.shelfGenre}: ${shelf.books.length}`);
            
            for (const book of shelf.books) {
                console.log(`--> ${book.title}: ${book.author}`);
            }
        }
    }
}

solve([
    '1 -> history',
    '1 -> action',
    'Death in Time: Criss Bell, mystery',
    '2 -> mystery',
    '3 -> sci-fi',
    'Child of Silver: Bruce Rich, mystery',
    'Hurting Secrets: Dustin Bolt, action',
    'Future of Dawn: Aiden Rose, sci-fi',
    'Lions and Rats: Gabe Roads, history',
    '2 -> romance',
    'Effect of the Void: Shay B, romance',
    'Losing Dreams: Gail Starr, sci-fi',
    'Name of Earth: Jo Bell, sci-fi',
    'Pilots of Stone: Brook Jay, history'
]);
solve([
    '1 -> mystery',
    '2 -> sci-fi',
    'Child of Silver: Bruce Rich, mystery',
    'Lions and Rats: Gabe Roads, history',
    'Effect of the Void: Shay B, romance',
    'Losing Dreams: Gail Starr, sci-fi',
    'Name of Earth: Jo Bell, sci-fi'
]);