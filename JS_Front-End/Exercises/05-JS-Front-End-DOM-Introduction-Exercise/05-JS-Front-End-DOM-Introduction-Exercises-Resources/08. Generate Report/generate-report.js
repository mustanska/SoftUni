function solve() {
    let columns = Array.from(document.querySelectorAll('thead tr th input'))
        .reduce((acc, column) => {
            let columnName = column.getAttribute('name');
            let checked = column.checked;

            acc[columnName] = checked;

            return acc;
        }, {})

    let columnEntries = Object.entries(columns);

    let rows = document.querySelectorAll('tbody tr');
    const result = [];

    for (const row of rows) {
        let singleResult = {}

        Array.from(row.children)
            .forEach((element, index) => {
                let [columnName, isChecked] = columnEntries[index];

                if (isChecked) {
                    singleResult[columnName] = element.textContent;
                }
            })
        
        result.push(singleResult);
    }

    document.getElementById('output').value = JSON.stringify(result);
}