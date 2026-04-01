function attachEvents() {
    const sendBtnElement = document.getElementById('submit');
    const refreshBtnElement = document.getElementById('refresh');
    const textAreaElement = document.getElementById('messages');

    refreshBtnElement.addEventListener('click', async () => {
        const response = await fetch('http://localhost:3030/jsonstore/messenger');
        const data = await response.json();
        const messages = Object.values(data)
            .map(message => `${message.author}: ${message.content}`);
        
        textAreaElement.value = messages.join('\n');
    })

    sendBtnElement.addEventListener('click', async () => {
        const author = document.querySelector('input[name=author]').value;
        const content = document.querySelector('input[name=content]').value;

        const messageObj = {author, content}

        const response = await fetch('http://localhost:3030/jsonstore/messenger', {
            method: 'POST',
            headers: {
                'content-type': 'application/json'
            },
            body: JSON.stringify(messageObj)
        })
    })
}

attachEvents();