function listOfNames(array){
    let sortedArray = array.sort((a, b) => a.localeCompare(b));

    sortedArray.forEach((element, index) => {
        console.log(`${index + 1}.${element}`);
    });
}

listOfNames(["John", "Bob", "Christina", "Ema"]);