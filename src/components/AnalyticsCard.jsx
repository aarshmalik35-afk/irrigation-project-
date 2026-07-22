import {
    FaChartLine,
    FaTint,
    FaLeaf,
    FaWater,
    FaFlask,
    FaSeedling
} from "react-icons/fa";

function AnalyticsCard({ analytics }) {

    return (

        <div className="card analytics-card">

            <div className="card-header">

                <div className="card-title">

                    <FaChartLine className="card-icon" />

                    <span>Farm Analytics</span>

                </div>

                <span className="status-badge">

                    UPDATED

                </span>

            </div>

            <div className="analytics-grid">

                <div className="metric">
                    <FaWater />
                    <div>
                        <small>Water Used</small>
                        <strong>{analytics.water_used} L</strong>
                    </div>
                </div>

                <div className="metric">
                    <FaTint />
                    <div>
                        <small>Irrigations</small>
                        <strong>{analytics.irrigations}</strong>
                    </div>
                </div>

                <div className="metric">
                    <FaChartLine />
                    <div>
                        <small>Efficiency</small>
                        <strong>{analytics.efficiency}%</strong>
                    </div>
                </div>

                <div className="metric">
                    <FaFlask />
                    <div>
                        <small>Nitrogen Used</small>
                        <strong>{analytics.nitrogen}</strong>
                    </div>
                </div>

                <div className="metric">
                    <FaSeedling />
                    <div>
                        <small>Phosphorus Used</small>
                        <strong>{analytics.phosphorus}</strong>
                    </div>
                </div>

                <div className="metric">
                    <FaLeaf />
                    <div>
                        <small>Potassium Used</small>
                        <strong>{analytics.potassium}</strong>
                    </div>
                </div>

                <div className="metric">
                    <FaChartLine />
                    <div>
                        <small>Simulation Day</small>
                        <strong>Day {analytics.days}</strong>
                    </div>
                </div>

            </div>

        </div>

    );

}

export default AnalyticsCard;