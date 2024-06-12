/** @type {import('tailwindcss').Config} */
export default {
    content: [],
    theme: {
        extend: {
            colors: {
                bgGrey: "#242424",
                bgSaffron: "rgba(255, 153, 51)",
            },
            spacing: {
                128: "32rem",
                156: "39rem",
                172: "45rem",
                85: "355px",
            },
        },
    },
    plugins: [],
    purge: ["./index.html", "./src/**/*.vue", "./src/**/*.js"],
};
