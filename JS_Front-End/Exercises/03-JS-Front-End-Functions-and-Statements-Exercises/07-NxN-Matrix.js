function createMatrix(number){
    let matrix = [];

    for(let i = 0; i < number; i++){
        matrix.push(createMatrixRow(number));
    }

    printMatrix(matrix);


    function createMatrixRow(number){
        let matrixRow = [];

        for(let i = 0; i < number; i++){
            matrixRow.push(number);
        }

        return matrixRow;
    }

    function printMatrix(matrix){
        for(let i = 0; i < matrix.length; i++){
            console.log(matrix[i].join(' '));
            
        }
    }
}

createMatrix(3);
createMatrix(7);
createMatrix(2);