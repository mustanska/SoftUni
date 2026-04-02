const mainSectionElement = document.getElementById('main');

async function solution() {
    const response = await fetch('http://localhost:3030/jsonstore/advanced/articles/list');
    const data = await response.json();
    const elements = Object.values(data)
        .map(createElement);

    mainSectionElement.append(...elements);

    const moreBtnElements = document.querySelectorAll('.button');

    moreBtnElements.forEach(button => button.addEventListener('click', showContentHandler));

}

async function showContentHandler(e) {
    const currentMoreBtn = e.currentTarget;
    const btnId = currentMoreBtn.id;
    const currentAccordionElement = currentMoreBtn.closest('.accordion');
    const contentDivElement = currentAccordionElement.querySelector('.extra');

    if (currentMoreBtn.textContent === 'LESS') {
        contentDivElement.style.display = 'none';
        currentMoreBtn.textContent = 'MORE';

        return;
    }

    const response = await fetch(`http://localhost:3030/jsonstore/advanced/articles/details/${btnId}`);
    const data = await response.json();

    contentDivElement.style.display = 'block';
    const contentPElement = contentDivElement.querySelector('p');
    contentPElement.textContent = data.content;

    currentMoreBtn.textContent = 'LESS';
}

function createElement(elementInfo) {
    const accordionDivElement = createElementStructure();

    const headerElement = accordionDivElement.querySelector('.head span');
    headerElement.textContent = elementInfo.title;

    const moreBtnElement = accordionDivElement.querySelector('.head button');
    moreBtnElement.id = elementInfo._id;

    return accordionDivElement;
}

function createElementStructure() {
    const accordionDivElement = document.createElement('div');
    accordionDivElement.classList.add('accordion');

    accordionDivElement.innerHTML = `
        <div class="head">
            <span></span>
            <button class="button" >More</button>
        </div>
        <div class="extra">
            <p></p>
        </div>
    `;

    return accordionDivElement;
}

solution();