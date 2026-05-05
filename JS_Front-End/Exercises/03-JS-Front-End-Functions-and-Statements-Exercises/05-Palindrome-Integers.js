function palindromeIntegers(numbers){
    for (const number of numbers) {
        console.log(checkIsPalindrome(number.toString()));
        
    }

    function checkIsPalindrome(characters){
        isPalindrome = false;
        for(let i = 0; i < characters.length; i++){
            if(characters[i] === characters[characters.length - 1 -i]){
                isPalindrome = true;
            }else{
                isPalindrome = false;
            }
        }

        return isPalindrome;
    }
}

palindromeIntegers([123,323,421,121]);
palindromeIntegers([32,2,232,1010]);