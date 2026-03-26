document.addEventListener('DOMContentLoaded', solve);

function solve() {
    const convertBtn = document.getElementById('convert');
    convertBtn.addEventListener('click', convertDistanceHandler);

    function convertDistanceHandler(e) {
        const distance = document.getElementById('inputDistance').value;
        const inputOption = Array.from(document.getElementById('inputUnits'))
            .filter(option => option.selected)
            .map(option => option.value)[0];
        const outputOption = Array.from(document.getElementById('outputUnits'))
            .filter(option => option.selected)    
            .map(option => option = option.value)[0];
        
        const meters = convertDistanceToMeter(distance, inputOption);
        const result = convertMetersToSelectedOption(meters, outputOption);

        const convertedDistanceField = document.getElementById('outputDistance');
        convertedDistanceField.value = result;
        
        
    }

    function convertDistanceToMeter(distance, selectedOption) {
        let meters = 0;

        switch (selectedOption) {
            case 'km':
                meters = distance * 1000;
                break;
            case 'm':
                meters = distance;
                break;
            case 'cm':
                meters = distance * 0.01;
                break;
            case 'mm':
                meters = distance * 0.001;
                break;
            case 'mi':
                meters = distance * 1609.34;
                break;
            case 'yrd':
                meters = distance * 0.9144;
                break;
            case 'ft':
                meters = distance * 0.3048;
                break;
            case 'in':
                meters = distance * 0.0254;
                break;
        }

        return meters;
    }

    function convertMetersToSelectedOption(meters, selectedOption) {
        let distance = 0;

        switch (selectedOption) {
            case 'km':
                distance = meters / 1000;
                break;
            case 'm':
                distance = meters;
                break;
            case 'cm':
                distance = meters / 0.01;
                break;
            case 'mm':
                distance = meters / 0.001;
                break;
            case 'mi':
                distance = meters / 1609.34;
                break;
            case 'yrd':
                distance = meters / 0.9144;
                break;
            case 'ft':
                distance = meters / 0.3048;
                break;
            case 'in':
                distance = meters / 0.0254;
                break;
        }

        return distance;
    }
}