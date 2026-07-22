import {
    FaTemperatureHigh,
    FaTint,
    FaLeaf,
    FaCalendarAlt
} from "react-icons/fa";

function KPI({ title, value, type }) {

    const icons = {
        temperature: <FaTemperatureHigh />,
        moisture: <FaTint />,
        crop: <FaLeaf />,
        day: <FaCalendarAlt />
    };

    const colors = {
        temperature: "#EF4444",
        moisture: "#2563EB",
        crop: "#16A34A",
        day: "#F59E0B"
    };

    return (

        <div className="card kpi-card">

            <div
                className="kpi-icon"
                style={{
                    background: colors[type]
                }}
            >

                {icons[type]}

            </div>

            <div className="kpi-content">

                <p>{title}</p>

                <h2>{value}</h2>

            </div>

        </div>

    );

}

export default KPI;