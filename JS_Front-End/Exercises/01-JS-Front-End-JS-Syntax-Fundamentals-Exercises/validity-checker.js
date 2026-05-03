function validityChecker(x1, y1, x2, y2) {

    checkPoint(0, 0, x1, y1);
    checkPoint(0, 0, x2, y2);
    checkPoint(x1, y1, x2, y2);

    function checkPoint(x1, y1, x2, y2) {
        let distance = findDistance(x1, y1, x2, y2);

        if (x1 == 0 && y1 == 0) {
            if (Number.isInteger(distance)) {
                return console.log(`{${x2}, ${y2}} to {${x1}, ${y1}} is valid`);
                ;
            }

            return console.log(`{${x2}, ${y2}} to {${x1}, ${y1}} is invalid`);
        }

        if (Number.isInteger(distance)) {
            return console.log(`{${x1}, ${y1}} to {${x2}, ${y2}} is valid`);
            ;
        }

        return console.log(`{${x1}, ${y1}} to {${x2}, ${y2}} is invalid`);

    }
    function findDistance(x1, y1, x2, y2) {
        let distance = Math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2);

        return distance;
    }
}

validityChecker(3, 0, 0, 4);
validityChecker(2, 1, 1, 1);