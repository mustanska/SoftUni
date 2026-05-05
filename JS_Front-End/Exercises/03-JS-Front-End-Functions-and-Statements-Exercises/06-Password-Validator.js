function passwordValidator(password){
    let isValid = true;

    if(!checkPasswordLength(password)){
        console.log("Password must be between 6 and 10 characters");
        isValid = false;
    }

    if(!checkPasswordCharacters(password)){
        console.log("Password must consist only of letters and digits");
        isValid = false;
    }

    if(!checkPasswordDigits(password)){
        console.log("Password must have at least 2 digits");
        isValid = false;
    }

    if(isValid){
        console.log("Password is valid");
        
    }

    function checkPasswordLength(password){
        if(password.length < 6 || password.length > 10){
            return false;
        }

        return true;
    }

    function checkPasswordCharacters(password){
        const pattern = /^[A-Za-z0-9]+$/g;
        return pattern.test(password);
    }

    function checkPasswordDigits(password){
        const pattern = /[0-9][0-9]+/g;
        return pattern.test(password);
    }
}

passwordValidator('logIn');
passwordValidator('MyPass123');
passwordValidator('Pa$s$s');