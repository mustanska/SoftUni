function login(input){
    const pattern = /[A-Za-z]/g;
    let username = input[0];
    let correctPassword = username.match(pattern).reverse().join("");
    let attemptsCount = 0;

    for(let i = 1; i < input.length; i++){
        if(input[i] === correctPassword){
            return console.log(`User ${username} logged in.`);
        }

        if(attemptsCount >= 3){
            return console.log(`User ${username} blocked!`); 
        }
        
        console.log('Incorrect password. Try again.');
        attemptsCount += 1;
    }
}

login(['Acer','login','go','let me in','recA']);
login(['momo','omom']);
login(['sunny','rainy','cloudy','sunny','not sunny']);