function solve(stockProducts, orderedProducts) {
    const stock = {}

    for (i = 0; i < stockProducts.length; i += 2) {
        stock[stockProducts[i]] = Number(stockProducts[i + 1]);
    }

    for (i = 0; i < orderedProducts.length; i += 2) {
        productName = orderedProducts[i];
        productQuantity = Number(orderedProducts[i + 1]);

        addProduct(productName, productQuantity, stock);
    }

    printProducts(stock);

    function addProduct(productName, productQuantity, stock) {
        if (stock[productName]) {
            stock[productName] += productQuantity;
        } else {
            stock[productName] = Number(productQuantity);
        }
    }

    function printProducts(stock) {
        Object.entries(stock).forEach(product => console.log(`${product[0]} -> ${product[1]}`));
    }
}

solve([
    'Chips', '5',
    'CocaCola', '9',
    'Bananas', '14',
    'Pasta', '4',
    'Beer', '2'
],
    [
        'Flour', '44',
        'Oil', '12',
        'Pasta', '7',
        'Tomatoes', '70',
        'Bananas', '30'
    ]);
solve([
    'Salt', '2',
    'Fanta', '4',
    'Apple', '14',
    'Water', '4',
    'Juice', '5'
],
[
    'Sugar', '44',
    'Oil', '12',
    'Apple', '7',
    'Tomatoes', '7',
    'Bananas', '30'
])