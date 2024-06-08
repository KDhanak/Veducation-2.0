import axios from "axios";

const apiClient = axios.create({
    baseURL: `${import.meta.env.VITE_BACKEND_BASE_URL}/core`,
    withCredentials: false,
    headers: {
        Accept: "application/json",
        "Content-Type": "application",
    },
    timout: 10000,
});

apiClient.interceptors.request.use(
    (config) => {
        return config;
    },

    (error) => {
        return Promise.reject(error);
    }
);

apiClient.interceptors.response.use(
    (response) => {
        return response;
    },

    (error) => {
        return Promise.reject(error);
    }
);

export default apiClient;
