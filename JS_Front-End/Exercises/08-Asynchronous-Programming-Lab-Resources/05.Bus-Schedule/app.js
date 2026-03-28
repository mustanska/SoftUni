function solve() {
    let nextStop = 'depot';

    const infoELement = document.querySelector('.info');
    const departBtnElement = document.querySelector('#depart');
    const arriveBtnElement = document.querySelector('#arrive');

    async function depart() {
        try {
            const res = await fetch(`http://localhost:3030/jsonstore/bus/schedule/${nextStop}`);
            const data = await res.json();

            infoELement.textContent = `Next stop ${data.name}`;

            departBtnElement.disabled = true;
            arriveBtnElement.disabled = false;
        } catch (err) {
            infoELement.textContent = 'Error';

            departBtnElement.disabled = true;
            arriveBtnElement.disabled = true;
        }
    }

    async function arrive() {
        try {
            const res = await fetch(`http://localhost:3030/jsonstore/bus/schedule/${nextStop}`);
            const data = await res.json();

            infoELement.textContent = `Arriving at ${data.name}`;
            nextStop = data.next;

            departBtnElement.disabled = false;
            arriveBtnElement.disabled = true;
        } catch (err) {
            infoELement.textContent = 'Error';

            departBtnElement.disabled = true;
            arriveBtnElement.disabled = true;
        }
    }

    return {
        depart,
        arrive
    };
}

let result = solve();