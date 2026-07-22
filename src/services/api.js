import axios from "axios";

const api = axios.create({
    baseURL: "https://irrigation-project-production.up.railway.app"
});

export default api;
