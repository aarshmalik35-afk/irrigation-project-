import {
    FaSun,
    FaCloud,
    FaCloudRain,
    FaBolt,
    FaTint,
    FaWind,
    FaTemperatureHigh,
    FaTachometerAlt
} from "react-icons/fa";

function WeatherCard({ weather }) {

    const getWeatherIcon = () => {
        switch (weather.condition?.toLowerCase()) {
            case "sunny":
                return <FaSun className="weather-icon sunny" />;

            case "cloudy":
                return <FaCloud className="weather-icon cloudy" />;

            case "rain":
                return <FaCloudRain className="weather-icon rain" />;

            case "storm":
                return <FaBolt className="weather-icon storm" />;

            default:
                return <FaSun className="weather-icon sunny" />;
        }
    };

    const getStatusClass = () => {
        if (weather.temperature >= 38) return "danger";
        if (weather.rainfall > 10) return "warning";
        return "success";
    };

    const getStatus = () => {
        if (weather.temperature >= 38)
            return "High Heat";

        if (weather.rainfall > 10)
            return "Rain Expected";

        return "Ideal Conditions";
    };

    return (
        <div className="card weather-card">

            <div className="weather-top">

                <div>
                    <h3>Weather</h3>
                    <span className="weather-condition">
                        {weather.condition}
                    </span>
                </div>

                {getWeatherIcon()}

            </div>

            <div className="temperature">

                {weather.temperature}°

            </div>

            <div className="feels-like">

                Feels like {weather.temperature + 2}°C

            </div>

            <div className="weather-divider"></div>

            <div className="weather-stats">

                <div className="stat">

                    <FaTint />

                    <div>

                        <span>Humidity</span>

                        <strong>{weather.humidity}%</strong>

                    </div>

                </div>

                <div className="stat">

                    <FaCloudRain />

                    <div>

                        <span>Rainfall</span>

                        <strong>{weather.rainfall} mm</strong>

                    </div>

                </div>

                <div className="stat">

                    <FaWind />

                    <div>

                        <span>Wind</span>

                        <strong>{weather.wind_speed ?? 12} km/h</strong>

                    </div>

                </div>

                <div className="stat">

                    <FaTachometerAlt />

                    <div>

                        <span>Pressure</span>

                        <strong>{weather.pressure ?? 1008} hPa</strong>

                    </div>

                </div>

            </div>

            <div className={`weather-alert ${getStatusClass()}`}>

                <FaTemperatureHigh />

                <span>{getStatus()}</span>

            </div>

        </div>
    );
}

export default WeatherCard;