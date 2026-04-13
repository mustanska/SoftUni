window.addEventListener("load", solve);

function solve() {
    const taskTitleInputElement = document.getElementById('task-title');
    const taskCategoryInputElement = document.getElementById('task-category');
    const taskContentInputElement = document.getElementById('task-content');

    const reviewUlListElement = document.getElementById('review-list');
    const publishedUlListElement = document.getElementById('published-list');

    const publishBtnElement = document.getElementById('publish-btn');
    publishBtnElement.addEventListener('click', addTaskReviewHandler);

    function addTaskReviewHandler(e) {
        e.preventDefault();

        const title = taskTitleInputElement.value;
        const category = taskCategoryInputElement.value;
        const content = taskContentInputElement.value;

        if(!title || !category || !content) {
            return;
        }

        const liElement = createTaskElement(title, category, content);
        reviewUlListElement.appendChild(liElement);

        clearInputValues();
    }

    function createTaskElement(title, category, content){
        const liElement = document.createElement('li');
        liElement.classList.add('rpost');

        const articleElement = document.createElement('article');

        const titleHeaderElement = document.createElement('h4');
        titleHeaderElement.textContent = title;
        articleElement.appendChild(titleHeaderElement);

        const pCategoryElement = document.createElement('p');
        pCategoryElement.textContent = `Category: ${category}`;
        articleElement.appendChild(pCategoryElement);

        const pContentElement = document.createElement('p');
        pContentElement.textContent = `Content: ${content}`;
        articleElement.appendChild(pContentElement);

        liElement.appendChild(articleElement);

        const editBtnElement = document.createElement('button');
        editBtnElement.classList.add('action-btn', 'edit');
        editBtnElement.textContent = 'Edit';
        editBtnElement.addEventListener('click', () => {
            liElement.remove();

            taskTitleInputElement.value = title;
            taskCategoryInputElement.value = category;
            taskContentInputElement.value = content;
        })
        liElement.appendChild(editBtnElement);

        const postBtnElement = document.createElement('button');
        postBtnElement.classList.add('action-btn', 'post');
        postBtnElement.textContent = 'Post';
        postBtnElement.addEventListener('click', () => {
            editBtnElement.remove();
            postBtnElement.remove();
            
            publishedUlListElement.appendChild(liElement);
        })
        liElement.appendChild(postBtnElement);

        return liElement;
    }

    function clearInputValues() {
        taskTitleInputElement.value = '';
        taskCategoryInputElement.value = '';
        taskContentInputElement.value = '';
    }
}