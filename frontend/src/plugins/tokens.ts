import { jwtDecode, JwtPayload } from "jwt-decode";

export const isTokenExpired = (token: string) => {
    if (!token) return true; // Return true if there is no token (expired)
    
    const decoded: JwtPayload = jwtDecode<JwtPayload>(token);
    return decoded.exp ? decoded.exp * 1000 < Date.now() : true; // Check expiration
};

export default isTokenExpired
