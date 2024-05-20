/** @type {import('tailwindcss').Config} */
export default {
    content: [],
    theme: {
        extend: {
            colors: {
                bgGrey: "#242424",
            },
        },
    },
    plugins: [],
    purge: ["./index.html", "./src/**/*.vue", "./src/**/*.js"],
};
