function solve(inputArray) {
    const garages = {};

    inputArray.map(garageInfo => createGarage(garageInfo, garages));
    Object.entries(garages).forEach(printGarageInfo);
    

    function createGarage(garageInfo, garages) {
        let [garageNumber, carInfo] = garageInfo.split(' - ');

        if(!garages[garageNumber]) {
            garages[garageNumber] = [];
        }

        garages[garageNumber].push(getCarInfo(carInfo));
    }

    function getCarInfo(carInfo) {
        let entries = carInfo
            .split(', ')
            .map((pair) => pair.split(': '));
        
        return Object.fromEntries(entries);
    }

    function printGarageInfo(garage) {
        let [garageNumber, cars] = garage;

        console.log(`Garage № ${garageNumber}`);
        cars.forEach(printCarInfo);
    }

    function printCarInfo(car) {
        const entries = Object.entries(car);
        let result = '--- ';

        entries.forEach(([key, value], index) => {
            result += `${key} - ${value}`;

            if(index < entries.length - 1){
                result += ', ';
            }
    });
        
        console.log(result); 
    }
}

solve(
    [
        '1 - color: blue, fuel type: diesel',
        '1 - color: red, manufacture: Audi',
        '2 - fuel type: petrol',
        '4 - color: dark blue, fuel type: diesel, manufacture: Fiat'
    ]
);
solve(
    [
        '1 - color: green, fuel type: petrol',
        '1 - color: dark red, manufacture: WV',
        '2 - fuel type: diesel',
        '3 - color: dark blue, fuel type: petrol'
    ]
);