import {
    FaLeaf,
    FaHeartbeat,
    FaSeedling
} from "react-icons/fa";

function CropCard({ crop }) {

    const health =
        crop.health >= 80 ? "Excellent" :
        crop.health >= 60 ? "Healthy" :
        crop.health >= 40 ? "Warning" :
        "Critical";

    return (

        <div className="card crop-card">

            <div className="card-header">

                <div className="card-title">

                    <FaLeaf className="card-icon"/>

                    <span>Crop Status</span>

                </div>

                <span className="status-badge">

                    {health}

                </span>

            </div>

            <div className="crop-health">

                <FaHeartbeat className="health-icon"/>

                <div>

                    <small>Crop Health</small>

                    <h2>{crop.health}%</h2>

                </div>

            </div>

            <div className="crop-details">

                <div className="detail">

                    <FaSeedling/>

                    <div>

                        <small>Growth Stage</small>

                        <strong>{crop.stage}</strong>

                    </div>

                </div>

                <div className="detail">

                    🌾

                    <div>

                        <small>Yield</small>

                        <strong>{crop.yield_prediction}</strong>

                    </div>

                </div>

            </div>

        </div>

    );

}

export default CropCard;