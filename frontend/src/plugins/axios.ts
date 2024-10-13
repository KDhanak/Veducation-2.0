import axios, { InternalAxiosRequestConfig, AxiosResponse, AxiosInstance } from "axios";

const apiClient: AxiosInstance = axios.create({
    baseURL: `${import.meta.env.VITE_BACKEND_BASE_URL}/core`,
    withCredentials: false,
    headers: {
        Accept: "application/json",
        "Content-Type": "application/json", 
    },
    timeout: 10000, 
});

apiClient.interceptors.request.use(
    (config: InternalAxiosRequestConfig): InternalAxiosRequestConfig => {
        return config;
    },
    (error: any): Promise<any> => {
        return Promise.reject(error);
    }
);

apiClient.interceptors.response.use(
    (response: AxiosResponse): AxiosResponse => {
        return response;
    },
    (error: any): Promise<any> => {
        return Promise.reject(error);
    }
);

export default apiClient;
