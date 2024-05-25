/** @type {import('tailwindcss').Config} */
export default {
    content: [],
    theme: {
        extend: {
            colors: {
                bgGrey: "#242424",
            },
            spacing: {
                128: "32rem",
            },
        },
    },
    plugins: [],
    purge: ["./index.html", "./src/**/*.vue", "./src/**/*.js"],
};
