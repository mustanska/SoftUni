function solve() {
    let number = Number(document.getElementById('input').value);

    let option = Array.from(document.querySelectorAll('#selectMenuTo option'))
        .filter(option => option.selected)[0]
    
    let resultNumber = '';
    
    switch (option.value) {
        case 'binary':
            resultNumber = toBinary(number);
            break;
        case 'hexadecimal':
            resultNumber = toHexadecimal(number);
            break;
    }

    document.getElementById('result').value = resultNumber;

    function toBinary(number) {
        return number.toString(2);
    }

    function toHexadecimal(number) {
        return number.toString(16).toUpperCase();
    }
}