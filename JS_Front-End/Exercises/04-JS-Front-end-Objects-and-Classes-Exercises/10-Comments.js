function solve(inputArray) {
    const users = {}
    const articles = {}

    for (const row of inputArray) {
        if (row.includes('user')) {
            addUser(row, users);
        } else if (row.includes('article')) {
            addArticle(row, articles);
        } else {
            saveInfoAboutUser(row, users, articles);
        }
    }

    const sortedArticles = sortArticles(articles);
    const sortedUsers = sortUsers(users);

    printInfo(sortedArticles, sortedUsers);

    function addUser(row, users) {
        let username = row.replace('user ', '');

        users[username] = {
            comments: []
        }
    }

    function addArticle(row, articles) {
        let article = row.replace('article ', '');
        articles[article] = 0;
    }

    function saveInfoAboutUser(row, users, articles) {
        let [username, comment] = row.split(' posts on ');
        let [articleName, commentInfo] = comment.split(': ');
        let [commentTitle, commentContent] = commentInfo.split(', ');

        const commentObj = {
            title: commentTitle,
            content: commentContent,
            article: articleName
        }
        
        if(users.hasOwnProperty(username) && articles.hasOwnProperty(articleName)) {
            users[username].comments.push(commentObj);
            articles[articleName] += 1;
        }
    }

    function sortArticles(articles) {
        const entries = Object.entries(articles).sort((a, b) => b[1] - a[1]);

        return Object.fromEntries(entries);
    }

    function sortUsers(users) {
        const entries = Object.entries(users).sort((a, b) => a[0].localeCompare(b[0]));

        return Object.fromEntries(entries);
    }

    function printInfo(sortedArticles, sortedUsers) {
        for (const article in sortedArticles) {
            console.log(`Comments on ${article}`);
            
            for (const username in sortedUsers) {
                if(sortedUsers[username].comments) {
                    for (const comment of sortedUsers[username].comments) {
                        if (comment.article === article) {
                            console.log(`--- From user ${username}: ${comment.title} - ${comment.content}`);
                        }
                    }
                }
            }
        }
    }
}

solve([
    'user aUser123', 
    'someUser posts on someArticle: NoTitle, stupidComment', 
    'article Books', 
    'article Movies', 
    'article Shopping', 
    'user someUser', 
    'user uSeR4', 
    'user lastUser', 
    'uSeR4 posts on Books: I like books, I do really like them', 
    'uSeR4 posts on Movies: I also like movies, I really do', 
    'someUser posts on Shopping: title, I go shopping every day', 
    'someUser posts on Movies: Like, I also like movies very much'
]);
solve([
    'user Mark', 
    'Mark posts on someArticle: NoTitle, stupidComment', 
    'article Bobby', 
    'article Steven', 
    'user Liam', 
    'user Henry', 
    'Mark posts on Bobby: Is, I do really like them', 
    'Mark posts on Steven: title, Run', 
    'someUser posts on Movies: Like'
]);