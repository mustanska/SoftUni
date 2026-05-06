function solve(inputArray) {
    const leaders = {}

    for (const row of inputArray) {
        if (row.includes('arrives')) {
            addLeader(row, leaders);
        } else if (row.includes(':')) {
            addArmy(row, leaders);
        } else if (row.includes('+')) {
            addCount(row, leaders);
        } else if (row.includes('defeated')) {
            deleteLeader(row, leaders);
        }
    }

    const sortedLeaders = sortLeaders(leaders);

    printInfo(sortedLeaders);


    function addLeader(row, leaders) {
        let leaderName = row.replace(' arrives', '');
        leaders[leaderName] = {
            totalCount: 0,
            armies: {}
        };
    }
    function addArmy(row, leaders) {
        let [leaderName, armyInfo] = row.split(': ');
        let [armyName, armyCount] = armyInfo.split(', ');
        armyCount = Number(armyCount);

        if (leaders[leaderName]) {
            leaders[leaderName].armies[armyName] = armyCount;
            leaders[leaderName].totalCount += armyCount;
        }
    }

    function addCount(row, leaders) {
        let [armyNameInput, countInput] = row.split(' + ');
        countInput = Number(countInput);

        for (const leaderName in leaders) {
            for (const armyName in leaders[leaderName].armies) {     
                if(armyName === armyNameInput) {
                    leaders[leaderName].armies[armyName] += countInput;
                    leaders[leaderName].totalCount += countInput;
                }
            }
        }
    }

    function deleteLeader(row, leaders) {
        let leaderName = row.replace(' defeated', '');

        if(leaders[leaderName]){
            delete leaders[leaderName];
        }
    }

    function sortLeaders(leaders) {
        let entries = Object.entries(leaders);
        let sortedLeaders = Object.fromEntries(entries.sort((a,b) => b[1].totalCount - a[1].totalCount));
        
        for (const leaderName in sortedLeaders) {
            sortedLeaders[leaderName].armies = sortArmies(leaderName, sortedLeaders);
        }

        return sortedLeaders;
    }

    function sortArmies(leaderName, leaders) {
        let entries = Object.entries(leaders[leaderName].armies);
        let sortedEntries = entries.sort((a, b) => b[1] - a[1]);

        return Object.fromEntries(sortedEntries);
    }

    function printInfo(leaders) {
        for (const leaderName in leaders) {
            console.log(`${leaderName}: ${leaders[leaderName].totalCount}`);

            for (const armyName in leaders[leaderName].armies) {
                console.log(`>>> ${armyName} - ${leaders[leaderName].armies[armyName]}`);
            }
        }
    }
}

solve([
    'Rick Burr arrives',
    'Fergus: Wexamp, 30245',
    'Rick Burr: Juard, 50000',
    'Findlay arrives',
    'Findlay: Britox, 34540',
    'Wexamp + 6000',
    'Juard + 1350',
    'Britox + 4500',
    'Porter arrives',
    'Porter: Legion, 55000',
    'Legion + 302',
    'Rick Burr defeated',
    'Porter: Retix, 3205'
]);

solve([
    'Rick Burr arrives',
    'Findlay arrives',
    'Rick Burr: Juard, 1500',
    'Wexamp arrives',
    'Findlay: Wexamp, 34540',
    'Wexamp + 340',
    'Wexamp: Britox, 1155',
    'Wexamp: Juard, 43423'
]);