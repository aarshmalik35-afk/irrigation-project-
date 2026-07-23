import axios from "axios";

const api = axios.create({
    baseURL: "http://irrigation.eba-whnpsfmm.us-east-1.elasticbeanstalk.com",
});

export default api;
