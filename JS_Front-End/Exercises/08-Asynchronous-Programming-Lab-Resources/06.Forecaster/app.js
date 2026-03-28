function attachEvents() {
    const weatherSymbols = {
        'Sunny': '☀',
        'Partly sunny': '⛅',
        'Overcast': '☁',
        'Rain': '☂'
    }

    const getWeatherBtnElement = document.getElementById('submit');

    getWeatherBtnElement.addEventListener('click', getWeatherRequestHandler);

    async function getWeatherRequestHandler(e) {
        const locationInput = document.getElementById('location').value.trim();

        const res = await fetch('http://localhost:3030/jsonstore/forecaster/locations');
        const data = await res.json();

        const forecastElement = document.getElementById('forecast');
        forecastElement.style.display = 'block';

        const currentForecastElement = document.getElementById('current');
        const upcomingForecastElement = document.getElementById('upcoming');

        const location = data.find(location => location.name === locationInput);

        if (!location) {
            forecastElement.textContent = 'Error';
            return;
        }

        const resCurrentForecast = await fetch(`http://localhost:3030/jsonstore/forecaster/today/${location.code}`);
        const dataCurrentForecast = await resCurrentForecast.json();

        const forecastsElement = document.createElement('div');
        forecastsElement.classList.add('forecasts');

        const spanSymbolElement = document.createElement('span');
        spanSymbolElement.classList.add('condition');
        spanSymbolElement.classList.add('symbol');
        spanSymbolElement.textContent = weatherSymbols[dataCurrentForecast.forecast.condition];

        const spanConditionElement = document.createElement('span');
        spanConditionElement.classList.add('condition');

        const spanNameElement = document.createElement('span');
        spanNameElement.classList.add('forecast-data');
        spanNameElement.textContent = dataCurrentForecast.name;
        const spanDegreesElement = document.createElement('span');
        spanDegreesElement.classList.add('forecast-data');
        spanDegreesElement.textContent = `${dataCurrentForecast.forecast.low}°/${dataCurrentForecast.forecast.high}°`;
        const spanWeatherElement = document.createElement('span');
        spanWeatherElement.classList.add('forecast-data');
        spanWeatherElement.textContent = dataCurrentForecast.forecast.condition;

        spanConditionElement.append(spanNameElement, spanDegreesElement, spanWeatherElement);
        forecastsElement.append(spanSymbolElement, spanConditionElement);
        currentForecastElement.appendChild(forecastsElement);

        const resUpcomingForecast = await fetch(`http://localhost:3030/jsonstore/forecaster/upcoming/${location.code}`);
        const dataUpcomingForecast = await resUpcomingForecast.json();

        const forecastInfoElement = document.createElement('div');
        forecastInfoElement.classList.add('forecast-info');

        dataUpcomingForecast.forecast.forEach(day => {
            const spanUpcomingElement = document.createElement('span');
            spanUpcomingElement.classList.add('upcoming');

            const spanUpcomingSymbolElement = document.createElement('span');
            spanUpcomingSymbolElement.classList.add('symbol');
            spanUpcomingSymbolElement.textContent = weatherSymbols[day.condition];

            const spanUpcomingDegreesElement = document.createElement('span');
            spanUpcomingDegreesElement.classList.add('forecast-data');
            spanUpcomingDegreesElement.textContent = `${day.low}°/${day.high}°`;

            const spanUpcomingWeatherElement = document.createElement('span');
            spanUpcomingWeatherElement.classList.add('forecast-data');
            spanUpcomingWeatherElement.textContent = day.condition;

            spanUpcomingElement.append(spanUpcomingSymbolElement, spanUpcomingDegreesElement, spanUpcomingWeatherElement);
            forecastInfoElement.appendChild(spanUpcomingElement);
        });

        upcomingForecastElement.appendChild(forecastInfoElement);

    }
}

attachEvents();