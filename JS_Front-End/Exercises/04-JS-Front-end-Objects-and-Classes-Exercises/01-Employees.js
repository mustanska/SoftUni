function solve(inputArray) {
    const employees = inputArray.map(name => {
        const employee = getEmployee(name);

        return employee;
    })

    employees.forEach(employee => {printEmployee(employee)});

    function getEmployee(name) {
        const employee = {
            name,
            personalNumber: name.length
        }

        return employee;
    }

    function printEmployee(employee) {
        console.log(`Name: ${employee.name} -- Personal Number: ${employee.personalNumber}`);
    }
}

solve([
'Silas Butler',
'Adnaan Buckley',
'Juan Peterson',
'Brendan Villarreal'
]);
solve([
'Samuel Jackson',
'Will Smith',
'Bruce Willis',
'Tom Holland'
]);