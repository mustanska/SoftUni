function solve(inputArr) {
    const elementsCount = Number(inputArr.shift());
    const elements = {};
    const tasksStatusPoints = {
        'ToDo': 0,
        'In Progress': 0,
        'Code Review': 0,
        'Done': 0
    };

    for (let i = 0; i < elementsCount; i++) {
        const [assignee, taskId, title, status, estimatedPointsAsString] = inputArr.shift().split(':');
        const estimatedPoints = Number(estimatedPointsAsString);

        if (!elements[assignee]) {
            elements[assignee] = {};

        }

        elements[assignee][taskId] = {
            title,
            status,
            estimatedPoints
        };
    }

    while (inputArr.length > 0) {
        const [command, assignee, ...args] = inputArr.shift().split(':');

        if (!elements.hasOwnProperty(assignee)) {
            console.log(`Assignee ${assignee} does not exist on the board!`);
            continue;
        }

        switch (command) {
            case 'Add New':
                const [newTaskId, title, status, estimatedPointsAsString] = args;
                const estimatedPoints = Number(estimatedPointsAsString);

                elements[assignee][newTaskId] = {
                    title,
                    status,
                    estimatedPoints
                };

                break;
            case 'Change Status':
                const [taskId, newStatus] = args;

                if (!elements[assignee][taskId]) {
                    console.log(`Task with ID ${taskId} does not exist for ${assignee}!`);
                    break;
                }

                elements[assignee][taskId].status = newStatus;

                break;
            case 'Remove Task':
                const index = Number(args[0]);

                const taskKey = Object.keys(elements[assignee]).filter((_, i) => i === index);

                if (taskKey.length === 0) {
                    console.log('Index is out of range!');
                    break;
                }

                const task = taskKey[0];

                delete elements[assignee][task];

                break;
        }
    }

    const elementsValues = Object.values(elements);

    while (elementsValues.length > 0) {
        const assigneeTasksObj = elementsValues.shift();
        const assigneeTasks = Object.values(assigneeTasksObj);

        while (assigneeTasks.length > 0) {
            const task = assigneeTasks.shift();
            tasksStatusPoints[task.status] += task.estimatedPoints;
        }
    }

   Object.entries(tasksStatusPoints).forEach(task => task[0] === 'Done'? console.log(`Done Points: ${task[1]}pts`) : console.log(`${task[0]}: ${task[1]}pts`));

   if (tasksStatusPoints['Done'] >= sumPoints()) {
    console.log('Sprint was successful!');
   } else {
    console.log('Sprint was unsuccessful...');
   }
   
    function sumPoints() {
        return Object.entries(tasksStatusPoints).reduce((acc, task) => task[0] === 'Done'? acc + 0 : acc + task[1], 0);        
    }
}

solve([
    '5',
    'Kiril:BOP-1209:Fix Minor Bug:ToDo:3',
    'Mariya:BOP-1210:Fix Major Bug:In Progress:3',
    'Peter:BOP-1211:POC:Code Review:5',
    'Georgi:BOP-1212:Investigation Task:Done:2',
    'Mariya:BOP-1213:New Account Page:In Progress:13',
    'Add New:Kiril:BOP-1217:Add Info Page:In Progress:5',
    'Change Status:Peter:BOP-1290:ToDo',
    'Remove Task:Mariya:1',
    'Remove Task:Joro:1',
]);
solve([
    '4',
    'Kiril:BOP-1213:Fix Typo:Done:1',
    'Peter:BOP-1214:New Products Page:In Progress:2',
    'Mariya:BOP-1215:Setup Routing:ToDo:8',
    'Georgi:BOP-1216:Add Business Card:Code Review:3',
    'Add New:Sam:BOP-1237:Testing Home Page:Done:3',
    'Change Status:Georgi:BOP-1216:Done',
    'Change Status:Will:BOP-1212:In Progress',
    'Remove Task:Georgi:3',
    'Change Status:Mariya:BOP-1215:Done',
]);