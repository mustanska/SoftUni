function solve(inputArray) {
    const towns = inputArray.map(row => {
        const town = getTown(row);

        return town;
    })

    towns.forEach(town => console.log(town));

    function getTown(row) {
        let [town, latitude, longitude] = row.split(' | ');
        const townObj = {
            town,
            latitude: Number(latitude).toFixed(2),
            longitude: Number(longitude).toFixed(2)
        }

        return townObj;
    }
}

solve(['Sofia | 42.696552 | 23.32601',
'Beijing | 39.913818 | 116.363625']);

(solve(['Plovdiv | 136.45 | 812.575']));