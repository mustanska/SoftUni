function solve(inputArray) {
    let arrayOfArrays = [];
    let arrayOfUniqueArrays = [];

    for (const jsonArrayString of inputArray) {
        let sortedArray = JSON.parse(jsonArrayString).sort((a, b) => b - a);
        arrayOfArrays.push(sortedArray);
    }

    arrayOfArrays = arrayOfArrays.sort((a, b) => a.length - b.length);
    
    for (const array of arrayOfArrays) {
        let currentArray = array;
        let isEqual = false;

        for (const uniqueArray of arrayOfUniqueArrays) {
            if(isEqualArrays(currentArray, uniqueArray)){
                isEqual = true;
                break;
            }
        }

        if(!isEqual) {
            arrayOfUniqueArrays.push(currentArray);
        }
    }

    for (const uniqueArray of arrayOfUniqueArrays) {
        console.log(`[${uniqueArray.join(', ')}]`);
    }
    
    
    function isEqualArrays(firstArray, secondArray) {
        if (firstArray.length !== secondArray.length) {
            return false;
        }

        for (let i = 0; i < firstArray.length; i++) {
            if(firstArray[i] !== secondArray[i]) {
                return false;
            }
        }

        return true;
    }
}

solve(
    ["[-3, -2, -1, 0, 1, 2, 3, 4]",
        "[10, 1, -17, 0, 2, 13]",
        "[4, -3, 3, -2, 2, -1, 1, 0]"
    ]
);
solve(
    ["[7.14, 7.180, 7.339, 80.099]",
        "[7.339, 80.0990, 7.140000, 7.18]",
        "[7.339, 7.180, 7.14, 80.099]"]
);