function radioCrystals(numbersArray) {
    let targetThickness = numbersArray[0];
    let chunksThickness = numbersArray.slice(1, numbersArray.length);

    let cutOperation = chunk => chunk / 4;
    let lapOperation = chunk => chunk * 0.8;
    let grindOperation = chunk => chunk - 20;
    let etchOperation = chunk => chunk - 2;
    let xRayOperation = chunk => chunk + 1;

    let operationsType = ['Cut', 'Lap', 'Grind', 'Etch'];
    let operations = [cutOperation, lapOperation, grindOperation, etchOperation];

    for (let i = 0; i < chunksThickness.length; i++) {
        console.log(`Processing chunk ${chunksThickness[i]} microns`);
        chunksThickness.splice(i, 1, operationThickness(chunksThickness[i], targetThickness, operations, operationsType));
        console.log(`Finished crystal ${targetThickness} microns`);
    }

    function operationThickness(chunk, target, operations, types) {
        for (let i = 0; i < operations.length; i++) {
            chunk = singleOperation(chunk, target, operations[i], types[i]);

            if (chunk === target) {
                return chunk;
            }
        }
    }

    function singleOperation(chunk, target, operation, type) {
        let executionCount = 0;
        let checkChunk = chunk;

        while (checkChunk > target - 1) {
            checkChunk = operation(checkChunk);

            if (checkChunk >= target - 1) {
                executionCount += 1;
                chunk = checkChunk;
            }
        }

        if (executionCount) {
            console.log(`${type} x${executionCount}`);
            console.log('Transporting and washing');
            chunk = Math.floor(chunk);
        }

        if (chunk === target - 1) {
            chunk = xRayOperation(chunk);
            console.log('X-ray x1');
        }
        return chunk;
    }
}

radioCrystals([1375, 50000]);
radioCrystals([1000, 4000, 8100]);
radioCrystals([100, 99]);