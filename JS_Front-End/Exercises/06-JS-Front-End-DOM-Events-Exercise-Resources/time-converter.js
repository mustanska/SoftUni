document.addEventListener('DOMContentLoaded', solve);

function solve() {
    const convertButtons = document.querySelectorAll('input[type=submit]');
    const inputFields = document.querySelectorAll('input[type=number]');

    convertButtons.forEach(button => {
        button.addEventListener('click', HandleConvertButton);
    })

    function HandleConvertButton(e) {
        e.preventDefault();

        const currentForm = e.currentTarget.parentElement;
        const inputData = currentForm.querySelector('input[type=number]');

        let timeUnit = inputData.value;
        const timeType = currentForm.id;

        const convertedTimes = getConvertedTimes(timeUnit, timeType);

        inputFields.forEach(field => {
            const id = field.parentElement.id;
            field.value = convertedTimes[id];
        })
        
        
    }
    
    function getConvertedTimes(time, type) {
        let seconds = convertTimeToSeconds(time, type);

        return {
            days: seconds / 86400,
            hours: seconds / 3600,
            minutes: seconds / 60,
            seconds: seconds
        }
    }

    function convertTimeToSeconds(time, type) {
        let seconds = 0;

        switch (type) {
            case 'days':
                seconds = time * 86400;
                break;
            case 'hours':
                seconds = time * 3600;
                break;
            case 'minutes':
                seconds = time * 60;
                break;
            case 'seconds':
                seconds = time;
                break;
        }

        return seconds;
    }
}