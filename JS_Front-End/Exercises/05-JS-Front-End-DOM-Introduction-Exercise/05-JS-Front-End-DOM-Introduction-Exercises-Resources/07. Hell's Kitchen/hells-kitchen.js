function solve() {
    let restaurantsInput = JSON.parse(document.querySelector('#inputs textarea').value);
    let restaurants = getAllRestaurants(restaurantsInput);
    let bestRestaurant = getBestRestaurant(restaurants);
    document.querySelector('#bestRestaurant p').textContent = printBestRestaurant(bestRestaurant);
    document.querySelector('#workers p').textContent = printBestRestaurantWorkers(bestRestaurant.workers);

    function getAllRestaurants(restaurantsInput) {
        let restaurants = {};

        for (const restaurant of restaurantsInput) {
            let [restaurantName, workersString] = restaurant.split(' - ');
            let workers = workersString.split(', ');
            let workersObj = {};

            for (const worker of workers) {
                let [workerName, salary] = worker.split(' ');
                salary = Number(salary);

                workersObj[workerName] = salary;
            }

            if (restaurants.hasOwnProperty(restaurantName)) {
                Object.assign(restaurants[restaurantName], workersObj);
            } else {
                restaurants[restaurantName] = workersObj;
            }

        }
        return restaurants;
    }

    function getBestRestaurant(restaurants) {
        let bestAverageSalary = Number.MIN_SAFE_INTEGER;
        let bestSalary = Number.MIN_SAFE_INTEGER;
        let bestRestaurantName = '';

        for (const restaurant in restaurants) {
            const salaries = Object.values(restaurants[restaurant]);
            let averageSalary = getAvarageSalary(salaries);

            if (averageSalary > bestAverageSalary) {
                bestAverageSalary = averageSalary;
                bestSalary = getBestSalary(salaries);
                bestRestaurantName = restaurant;
            }
        }

        const workers = getSortedWorkers(restaurants[bestRestaurantName]);

        const bestRestaurant = {
            name: bestRestaurantName,
            averageSalary: bestAverageSalary,
            bestSalary,
            workers
        }

        return bestRestaurant;
        
    }

    function getAvarageSalary(salaries) {
        let sumSalaries = salaries.reduce((acc, salary) => acc + salary, 0);
        
        return sumSalaries / salaries.length;
    }

    function getBestSalary(salaries) {
        return Math.max(...salaries);
    }

    function getSortedWorkers(workersObj) {
        const entries = Object.entries(workersObj).sort((a, b) => b[1] - a[1]);
        
        return Object.fromEntries(entries);
    }

    function printBestRestaurant(bestRestaurant) {
        return `Name: ${bestRestaurant.name} Average Salary: ${bestRestaurant.averageSalary.toFixed(2)} Best Salary: ${bestRestaurant.bestSalary.toFixed(2)}`;
    }

    function printBestRestaurantWorkers(workers) {
        let result = []

        Object.entries(workers).forEach(worker => {result.push(`Name: ${worker[0]} With Salary: ${worker[1]}`)})

        return result.join(' ');
    }
}