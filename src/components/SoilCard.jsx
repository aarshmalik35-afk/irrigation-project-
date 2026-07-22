import {
    FaSeedling,
    FaTint,
    FaFlask
} from "react-icons/fa";

function SoilCard({ soil }) {
    return (
        <div className="card soil-card">

            <div className="card-header">

                <div className="card-title">

                    <FaSeedling className="card-icon" />

                    <span>Soil Health</span>

                </div>

                <span className="status-badge">

                    GOOD

                </span>

            </div>

            <div className="soil-moisture">

                <FaTint className="moisture-icon" />

                <div>

                    <small>Moisture</small>

                    <h2>{soil.moisture}%</h2>

                </div>

            </div>

            <div className="nutrient-grid">

                <div className="nutrient">

                    <FaFlask />

                    <div>

                        <small>Nitrogen</small>

                        <strong>{soil.nitrogen}</strong>

                    </div>

                </div>

                <div className="nutrient">

                    <FaFlask />

                    <div>

                        <small>Phosphorus</small>

                        <strong>{soil.phosphorus}</strong>

                    </div>

                </div>

                <div className="nutrient">

                    <FaFlask />

                    <div>

                        <small>Potassium</small>

                        <strong>{soil.potassium}</strong>

                    </div>

                </div>

            </div>

        </div>
    );
}

export default SoilCard;