import { FaRobot, FaCheckCircle } from "react-icons/fa";

function RecommendationCard({ recommendations }) {

    return (

        <div className="card recommendation-card">

            <div className="card-header">

                <div className="card-title">

                    <FaRobot className="card-icon"/>

                    <span>AI Recommendations</span>

                </div>

                <span className="status-badge">

                    AI

                </span>

            </div>

            <div className="recommendation-list">

                {recommendations.map((item, index) => (

                    <div
                        key={index}
                        className="recommendation-item"
                    >

                        <FaCheckCircle className="recommendation-icon"/>

                        <span>{item}</span>

                    </div>

                ))}

            </div>

        </div>

    );

}

export default RecommendationCard;