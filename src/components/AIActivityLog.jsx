import { FaRobot } from "react-icons/fa";

function AIActivityLog({ logs }) {
    return (
        <div className="card activity-card">

            <div className="card-header">

                <div className="card-title">

                    <FaRobot className="card-icon" />

                    <span>AI Activity</span>

                </div>

                <span className="status-badge">
                    LIVE
                </span>

            </div>

            <div className="timeline">

                {logs.map((log, index) => (

                    <div
                        key={index}
                        className="timeline-item"
                    >

                        <div className="timeline-dot"></div>

                        <div className="timeline-content">

                            <p>{log}</p>

                        </div>

                    </div>

                ))}

            </div>

        </div>
    );
}

export default AIActivityLog;