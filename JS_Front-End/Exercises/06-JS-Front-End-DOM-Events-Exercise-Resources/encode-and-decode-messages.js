document.addEventListener('DOMContentLoaded', solve);

function solve() {
    const encodeForm = document.getElementById('encode');
    const decodeForm = document.getElementById('decode');

    const textToEncodeField = encodeForm.querySelector('textarea');
    const textToDecodeField = decodeForm.querySelector('textarea');


    const encodeBtn = encodeForm.querySelector('button');
    encodeBtn.addEventListener('click', encodeMesageHandler);

    function encodeMesageHandler(e) {
        e.preventDefault();

        const textArr = textToEncodeField.value.split('');
        const encodeTextArr = textArr.map(character => {
            charCode = character.charCodeAt(0) + 1;
            character = String.fromCharCode(charCode);
            
            return character;
        })
        
        textToDecodeField.value = encodeTextArr.join('');
        
        textToEncodeField.value = '';
    }

    const decodeBtn = decodeForm.querySelector('button');
    decodeBtn.addEventListener('click', decodeMessageHandler);

    function decodeMessageHandler(e) {
         e.preventDefault();

        const textArr = textToDecodeField.value.split('');
        const decodeTextArr = textArr.map(character => {
            charCode = character.charCodeAt(0) - 1;
            character = String.fromCharCode(charCode);
            
            return character;
        })
        
        textToDecodeField.value = decodeTextArr.join('');
    }
}