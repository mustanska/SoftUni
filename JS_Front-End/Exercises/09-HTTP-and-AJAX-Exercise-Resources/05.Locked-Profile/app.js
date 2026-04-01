const mainElement = document.getElementById('main');
const profileTemplate = document.querySelector('.profile');
const hiddenInfoDivElement = profileTemplate.querySelector('.user1Username');
hiddenInfoDivElement.style.display = 'none';

async function lockedProfile() {
    const response = await fetch('http://localhost:3030/jsonstore/advanced/profiles');
    const data = await response.json();
    console.log(data);
    
    const profiles = Object.values(data)
        .map((profileInfo, index) => createNewProfile(profileInfo));
    
    profileTemplate.remove();

    mainElement.append(...profiles);
    const showMoreBtnElements = document.querySelectorAll('button');
    showMoreBtnElements.forEach(button => button.addEventListener('click', showInformationHandler));
}

function createNewProfile(profileInfo) {
    const profileElement = profileTemplate.cloneNode(true);

    const username = profileElement.querySelector(`input[name=user1Username]`);
    username.value = profileInfo.username;

    const email = profileElement.querySelector(`input[name=user1Email]`);
    email.value = profileInfo.email;

    const age = profileElement.querySelector(`input[name=user1Age]`);
    age.value = profileInfo.age;

    return profileElement;
}

function showInformationHandler(e) {
    const currentShowMoreBtn = e.currentTarget;
    const currentProfileElement = currentShowMoreBtn.closest('.profile');
    const currentHiddenInfoDivElement = currentProfileElement.querySelector(`.user1Username`);

    const lockRadioBtnElement = currentProfileElement.querySelectorAll('input[type=radio]')[0];
    const unlockRadioBtnElement = currentProfileElement.querySelectorAll('input[type=radio]')[1];

    if (currentShowMoreBtn.textContent === 'Show more') {
        if (lockRadioBtnElement.checked) {
            return;
        } else if (unlockRadioBtnElement.checked) {
            currentHiddenInfoDivElement.style.display = 'block';
            currentShowMoreBtn.textContent = 'Hide it';
        }
    } else {
        if (lockRadioBtnElement.checked) {
            return;
        } else if (unlockRadioBtnElement.checked) {
            currentHiddenInfoDivElement.style.display = 'none';
            currentShowMoreBtn.textContent = 'Show more';
        }
    }
}