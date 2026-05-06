function solve(inputArray) {
    let products = getObjectOfProducts(inputArray);
    let sortedProductsArray = sortProducts(products);
    let catalog = createCatalog(sortedProductsArray);

    printCatalog(catalog);

    function getObjectOfProducts(inputArray) {
        let products = {}

        for (const product of inputArray) {
            let [key, value] = product.split(' : ');

            products[key] = Number(value);
        }

        return products;
    }

    function sortProducts(products){
       return Object.entries(products).sort((a, b) => a[0].toLowerCase().localeCompare(b[0].toLowerCase()));
    }

    function createCatalog(productsArray){
        let catalog = {};

        for(const product of productsArray){
            let firstLetter = product[0][0];
            if(firstLetter in catalog){
               catalog[firstLetter].push(product); 
            } else {
                catalog[firstLetter] = [product];
            }
        }
        
        return catalog;
    }

    function printCatalog(catalog){
        const catalogEntries = Object.entries(catalog);

        for (const [group, products] of catalogEntries) {
            console.log(group);
            
            for (const [name, price] of products) {
                console.log(`  ${name}: ${price}`);
            }
        }
    }
}

solve([
    'Appricot : 20.4',
    'Fridge : 1500',
    'TV : 1499',
    'Deodorant : 10',
    'Boiler : 300',
    'Apple : 1.25',
    'Anti-Bug Spray : 15',
    'T-Shirt : 10'
]);

solve([
    'Omlet : 5.4',
    'Shirt : 15',
    'Cake : 59'
]);