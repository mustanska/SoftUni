function solve(arrayWithArrays) {
    class Flight {
        constructor(flightNumber, flightDestination) {
            this.number = flightNumber;
            this.destination = flightDestination;
            this.status = 'Ready to fly';
        }
    }

    let [flights, changedStatusOfFlights, searchedFlightStatus] = arrayWithArrays;
    let flightObjectsArray = getFlightsInArray(flights);

    changeStatusOfFlights(flightObjectsArray, changedStatusOfFlights);
    printSearchedFlights(flightObjectsArray, searchedFlightStatus);
    
    

    function getFlightsInArray(flights) {
        let flightObjectsArray = []

        for (const flight of flights) {
            let [flightNumber, flightDestination] = flight.split(/\s(.+)/g);
            let flightObject = new Flight(flightNumber, flightDestination);

            flightObjectsArray.push(flightObject);
        }

        return flightObjectsArray;
    }

    function changeStatusOfFlights(flightObjectsArray, changedStatusOfFlights) {
        for (const flight of flightObjectsArray) {
            for (const changedFlight of changedStatusOfFlights) {
                let [flightNumber, flightStatus] = changedFlight.split(' ');

                if(flight.number === flightNumber){
                    flight.status = flightStatus;
                }
            }
        }
    }

    function printSearchedFlights(flightObjectsArray, searchedFlightStatus) {
        let searchedStatus = searchedFlightStatus[0];

        for (const flight of flightObjectsArray) {
            if(flight.status === searchedStatus) {
                console.log(`{ Destination: '${flight.destination}', Status: '${flight.status}' }`);
            }
        }
    }
}

solve([['WN269 Delaware',
    'FL2269 Oregon',
    'WN498 Las Vegas',
    'WN3145 Ohio',
    'WN612 Alabama',
    'WN4010 New York',
    'WN1173 California',
    'DL2120 Texas',
    'KL5744 Illinois',
    'WN678 Pennsylvania'],
['DL2120 Cancelled',
    'WN612 Cancelled',
    'WN1173 Cancelled',
    'SK430 Cancelled'],
['Cancelled']
]);
solve([['WN269 Delaware',
    'FL2269 Oregon',
    'WN498 Las Vegas',
    'WN3145 Ohio',
    'WN612 Alabama',
    'WN4010 New York',
    'WN1173 California',
    'DL2120 Texas',
    'KL5744 Illinois',
    'WN678 Pennsylvania'],
['DL2120 Cancelled',
    'WN612 Cancelled',
    'WN1173 Cancelled',
    'SK330 Cancelled'],
['Ready to fly']
]);