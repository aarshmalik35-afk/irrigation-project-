import { FaRobot, FaBell } from "react-icons/fa";

function Topbar({day}){

return(

<div className="topbar">

<div className="title">

<h1>

🌱 Smart Irrigation Digital Twin

</h1>

<p>

Autonomous Farm Monitoring Platform

</p>

</div>

<div className="status">

<div className="ai-chip">

<FaRobot/>

&nbsp;

AI ACTIVE

</div>

<div className="ai-chip">

Day {day}

</div>

<FaBell size={22}/>

</div>

</div>

);

}

export default Topbar;