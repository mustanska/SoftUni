document.addEventListener('DOMContentLoaded', solve);

function solve() {
    const tableElement = document.querySelector('table');
    const resultElement = document.getElementById('check');

    const submitBtn = document.querySelector('input[type=submit]');
    submitBtn.addEventListener('click', checkRowsAndColumnsHandler);

    const clearBtn = document.querySelector('input[type=reset]');
    clearBtn.addEventListener('click', resetTableHandler);

    function checkRowsAndColumnsHandler(e) {
        e.preventDefault();

        const sodomuTable = Array.from(tableElement.querySelectorAll('tbody tr'))
            .map(tr => {
                const inputNumbers = tr.querySelectorAll('td input[type=number]');
                return Array.from(inputNumbers).map(number => number.value);
            });

        let result = '';

        if (checkRowsNumbers(sodomuTable) && checkColumnsNumbers(sodomuTable)) {
            tableElement.style.border = '2px solid green';
            result = 'Success!';
        } else {
            tableElement.style.border = '2px solid red';
            result = 'Keep trying...'
        }

        resultElement.textContent = result;
    }

    function resetTableHandler(e) {
        e.preventDefault();
        const inputNumbers = document.querySelectorAll('td input[type=number]');
        inputNumbers.forEach(input => input.value = '');
        tableElement.style.border = 'none';
        resultElement.textContent = '';

    }

    function checkRowsNumbers(table) {
        return table
            .map(row => {
                const uniqueRowNumbers = Array.from(new Set(row));

                if (uniqueRowNumbers.length === row.length) {
                    return true;
                }

                return false;
            })
            .every(el => el === true);
    }

    function checkColumnsNumbers(table) {
        const columnsCount = table[0].length;

        for (i = 0; i < columnsCount; i++) {
            const column = table.map(row => row[i]);
            const uniqueColumnNumbers = Array.from(new Set(column));

            if (uniqueColumnNumbers.length !== column.length) {
                return false;
            }
        }

        return true;
    }
}