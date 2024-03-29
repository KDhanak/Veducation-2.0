import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  server: {
    host: true, // For docker to to access frontend.
    port: 3000 // To host the frontend on port 3000 instead of default.
  }
})
