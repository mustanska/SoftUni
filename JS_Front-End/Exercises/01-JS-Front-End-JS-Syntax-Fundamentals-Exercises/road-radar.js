function roadRadar(speed, area){
    let speedLimit = findSpeedLimit(area);
    let difference = 0;
    let status = '';

    if(speed > speedLimit){
        difference = speed - speedLimit;
        status = findStatus(difference);
        return console.log(`The speed is ${difference} km/h faster than the allowed speed of ${speedLimit} - ${status}`);
    }

    return console.log( `Driving ${speed} km/h in a ${speedLimit} zone`);
    

    function findSpeedLimit(area){
        if(area == 'motorway'){
            return 130;
        }
        if(area == 'interstate'){
            return 90;
        }if(area == 'city'){
            return 50;
        }if(area == 'residential'){
            return 20;
        }

    }
    function findStatus(difference){
        if(difference <= 20){
            return 'speeding';
        }

        if(difference <= 40){
            return 'excessive speeding';
        }

        return 'reckless driving';
    }
}

roadRadar(40, 'city');
roadRadar(21, 'residential');
roadRadar(120, 'interstate');
roadRadar(200, 'motorway');