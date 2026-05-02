async function getInfo() {
    const stopId = document.getElementById('stopId').value.trim();
    const stopNameElement = document.getElementById('stopName');
    const ulBusesElement = document.getElementById('buses');

    ulBusesElement.innerHTML = '';

    try {
        const res = await fetch(`http://localhost:3030/jsonstore/bus/businfo/${stopId}`);
        const data = await res.json();

        const busesEntries = Object.entries(data.buses);

        stopNameElement.textContent = data.name;

        for (const [busId, time] of busesEntries) {
            const liElement = document.createElement('li');
            liElement.textContent = `Bus ${busId} arrives in ${time} minutes`;

            ulBusesElement.appendChild(liElement);
        }
    } catch (err) {
        stopNameElement.textContent = 'Error';
    }
}