function solve(inputArr) {
    const farmersCount = Number(inputArr.shift());
    const farmers = {}

    for (let i = 0; i < farmersCount; i++) {
        const [name, workArea, tasksStr] = inputArr.shift().split(' ');
        const tasks = tasksStr.split(',');

        farmers[name] = {
            workArea,
            tasks
        };
    }

    let commandLine = inputArr.shift();
    while (commandLine !== 'End') {
        const [command, farmerName, ...args] = commandLine.split(' / ');

        switch (command) {
            case 'Execute':
                const [workArea, task] = args;

                if (farmers[farmerName].workArea === workArea && farmers[farmerName].tasks.includes(task)) {
                    console.log(`${farmerName} has executed the task: ${task}!`);
                } else {
                    console.log(`${farmerName} cannot execute the task: ${task}.`);
                }

                break;
            case 'Change Area':
                const newWorkArea = args[0];

                farmers[farmerName].workArea = newWorkArea;
                console.log(`${farmerName} has changed their work area to: ${newWorkArea}`);

                break;
            case 'Learn Task':
                const newTask = args[0];

                if (farmers[farmerName].tasks.includes(newTask)) {
                    console.log(`${farmerName} already knows how to perform ${newTask}.`);                    
                } else {
                    farmers[farmerName].tasks.push(newTask);
                    console.log(`${farmerName} has learned a new task: ${newTask}.`);
                }

                break;
        }

        commandLine = inputArr.shift();
    }

    for (const farmerName in farmers) {
        let result = `Farmer: ${farmerName}, `;
        result += `Area: ${farmers[farmerName].workArea}, `;
        result += `Tasks: ${farmers[farmerName].tasks.sort((a, b) => a.localeCompare(b)).join(', ')}`;

        console.log(result);
    }
}

solve([
    "2",
    "John garden watering,weeding",
    "Mary barn feeding,cleaning",
    "Execute / John / garden / watering",
    "Execute / Mary / garden / feeding",
    "Learn Task / John / planting",
    "Execute / John / garden / planting",
    "Change Area / Mary / garden",
    "Execute / Mary / garden / cleaning",
    "End"
]);
solve([
    "3",
    "Alex apiary harvesting,honeycomb",
    "Emma barn milking,cleaning",
    "Chris garden planting,weeding",
    "Execute / Alex / apiary / harvesting",
    "Learn Task / Alex / beeswax",
    "Execute / Alex / apiary / beeswax",
    "Change Area / Emma / apiary",
    "Execute / Emma / apiary / milking",
    "Execute / Chris / garden / watering",
    "Learn Task / Chris / pruning",
    "Execute / Chris / garden / pruning",
    "End"
]);