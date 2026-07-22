import { useEffect, useState } from "react";
import AIActivityLog from "../components/AIActivityLog";
import Topbar from "../components/Topbar";
import KPI from "../components/KPI";

import api from "../services/api";

import WeatherCard from "../components/Weathercard";
import SoilCard from "../components/SoilCard";
import CropCard from "../components/CropCard";
import AnalyticsCard from "../components/AnalyticsCard";
import RecommendationCard from "../components/RecommendationCard";
import ControlPanel from "../components/ControlPanel";

import "../styles/Dashboard.css";

function Dashboard() {

    const [farm, setFarm] = useState(null);
    const [recommendations, setRecommendations] = useState([]);

    const loadRecommendations = () => {
        api
            .get("/recommendations")
            .then((response) => {
                setRecommendations(response.data);
            })
            .catch((error) => {
                console.error("Recommendation Error:", error);
            });
    };

    const loadFarm = () => {
        api
            .get("/farm")
            .then((response) => {
                setFarm(response.data);
                loadRecommendations();
            })
            .catch((error) => {
                console.error("Farm Error:", error);
            });
    };

    const nextDay = () => {
        api
            .post("/next-day")
            .then(() => {
                loadFarm();
            })
            .catch((error) => {
                console.error(error);
            });
    };

    const irrigate = (litres) => {
        api
            .post(`/irrigate/${litres}`)
            .then(() => {
                loadFarm();
            })
            .catch((error) => {
                console.error(error);
            });
    };

    const fertilize = (fertilizer, amount) => {

        api
            .post("/fertilize", {
                fertilizer: fertilizer,
                amount: Number(amount),
            })
            .then(() => {
                loadFarm();
            })
            .catch((error) => {
                console.error(error);
            });
    };

    useEffect(() => {
        loadFarm();
    }, []);

    if (!farm) {
        return <p>Loading...</p>;
    }

    return (
    <div className="dashboard">

<div className="kpi-grid">

    <KPI
        title="Temperature"
        value={`${farm.weather.temperature}°C`}
        type="temperature"
    />

    <KPI
        title="Soil Moisture"
        value={`${farm.soil.moisture}%`}
        type="moisture"
    />

    <KPI
        title="Crop Health"
        value={`${farm.crop.health}%`}
        type="crop"
    />

    <KPI
        title="Simulation Day"
        value={farm.day}
        type="day"
    />

</div>

        <div className="dashboard-grid">

            <WeatherCard weather={farm.weather} />

            <SoilCard soil={farm.soil} />

            <CropCard crop={farm.crop} />

            <AnalyticsCard analytics={farm.analytics} />

            <RecommendationCard
                recommendations={recommendations}
            />

            <AIActivityLog
                logs={farm.ai_logs}
            />

            <div className="full-width">

                <ControlPanel
                    nextDay={nextDay}
                    irrigate={irrigate}
                    fertilize={fertilize}
                />

            </div>

        </div>

    </div>
    );
}

export default Dashboard;