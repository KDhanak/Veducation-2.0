import axios, { InternalAxiosRequestConfig, AxiosResponse, AxiosInstance } from "axios";
import Cookies from "js-cookie";
import isTokenExpired from "./tokens";

const apiClient: AxiosInstance = axios.create({
    baseURL: `${import.meta.env.VITE_BACKEND_BASE_URL}/core`,
    withCredentials: true,
    headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
    },
    timeout: 10000,
});


apiClient.interceptors.request.use(
    (config: InternalAxiosRequestConfig): InternalAxiosRequestConfig => {
        const csrfToken = Cookies.get('csrftoken');
        if (csrfToken) {
            config.headers['X-CSRFToken'] = csrfToken;
        }

        const accessToken = Cookies.get("access_token");
        if (accessToken && !isTokenExpired(accessToken)) {
            config.headers['Authorization'] = `Bearer ${accessToken}`;
        }
        return config;
    },
    (error): Promise<any> => {
        return Promise.reject(error);
    }
);

export const refreshAccessToken = async () => {
    try {
        const refreshToken = Cookies.get("refresh_token");

        if (!refreshToken) {
            throw new Error("No refresh token available");
        }
        const response = await axios.post(
            `${import.meta.env.VITE_BACKEND_BASE_URL}/api/token/refresh`,
            { refresh: refreshToken },
            { withCredentials: true }
        );

        const { access } = response.data;

        Cookies.set("access_token", access, { expires: 7, secure: true });

        return { access };
    } catch (error) {
        console.error("Failed to refresh access token", error);
        throw error;
    }
}

apiClient.interceptors.response.use(
    (response: AxiosResponse): AxiosResponse => {
        return response;
    },
    async (error): Promise<any> => {
        const originalRequest = error.config;
        if (error.response.status === 401 && !originalRequest._retry) {
            const refreshToken = Cookies.get("refresh_token");

            if (refreshToken) {
                originalRequest._retry = true;

                try {
                    const newTokens = await refreshAccessToken();

                    Cookies.set("access_token", newTokens.access);
                    originalRequest.headers['Authorization'] = `Bearer ${newTokens.access}`;

                    return axios(originalRequest);
                } catch (refreshError) {
                    console.error("Token refresh failed", refreshError);
                    return Promise.reject(refreshError);
                }

            }
        }
        return Promise.reject(error);
    }
);

export default apiClient;
