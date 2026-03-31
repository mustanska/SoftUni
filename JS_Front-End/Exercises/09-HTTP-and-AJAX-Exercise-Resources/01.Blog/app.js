function attachEvents() {
    const selectELement = document.getElementById('posts');
    const loadPostsBtn = document.getElementById('btnLoadPosts');

    loadPostsBtn.addEventListener('click', async () => {
        const response = await fetch('http://localhost:3030/jsonstore/blog/posts');
        const data = await response.json();
        const postObjects = Object.values(data);

        const postElements = postObjects.map(createOption);

        selectELement.innerHTML = '';

        selectELement.append(...postElements);
    });

    const viewPostBtn = document.getElementById('btnViewPost');
    viewPostBtn.addEventListener('click', async () => {
        const postTitleElement = document.getElementById('post-title');
        const postBodyElement = document.getElementById('post-body');
        const ulCommentsElement = document.getElementById('post-comments');

        const currentPostID = selectELement.value;

        const postsResponse = await fetch(`http://localhost:3030/jsonstore/blog/posts/`);
        const postsData = await postsResponse.json();
        const post = Object.values(postsData)
            .filter(post => post.id === currentPostID)
            .map(post => {
                postTitleElement.textContent = post.title;
                postBodyElement.textContent = post.body;
            })

        const commentsResponse = await fetch(`http://localhost:3030/jsonstore/blog/comments`);
        const commentsData = await commentsResponse.json();
        const comments = Object.values(commentsData)
            .filter(comment => comment.postId === currentPostID)
            .map(createCommentListItem);

        ulCommentsElement.innerHTML = '';

        ulCommentsElement.append(...comments);
    });
}

function createOption(post) {
    const optionElement = document.createElement('option');
    optionElement.value = post.id;
    optionElement.textContent = post.title;

    return optionElement;
}

function createCommentListItem(comment) {
    const liElement = document.createElement('li');
    liElement.id = comment.id;
    liElement.textContent = comment.text;

    return liElement;
}

attachEvents();