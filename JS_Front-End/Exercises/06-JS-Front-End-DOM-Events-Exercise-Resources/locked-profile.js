document.addEventListener('DOMContentLoaded', solve);

function solve() {
    const showInfoBtns = document.querySelectorAll('.profile button');

    showInfoBtns.forEach(button => button.addEventListener('click', showInfoHandler));

    function showInfoHandler(e) {
        const showBtn = e.currentTarget;
        const currentProfile = showBtn.parentElement;
        const hiddenFields = currentProfile.querySelectorAll('.hidden-fields');

        const radioBtns = currentProfile.querySelectorAll('.radio-group input[type=radio');
        const lockBtn = Array.from(radioBtns).find(btn => btn.id.endsWith('Lock'));

        if (lockBtn.checked) {
            return;
        }

        if (showBtn.textContent === 'Show more') {
            hiddenFields.forEach(field => field.style.display = 'block');
            showBtn.textContent = 'Show less';
        } else {
            hiddenFields.forEach(field => field.style.display = 'none');
            showBtn.textContent = 'Show more';
        }
    }
}