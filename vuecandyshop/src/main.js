import { createApp } from 'vue';
import App from './App.vue';
import axios from 'axios';
import router from './router';

// Konfiguracja Axios z wykorzystaniem zmiennej środowiskowej
axios.defaults.baseURL = process.env.VUE_APP_API_URL;
axios.defaults.withCredentials = false; // Ustawienie withCredentials globalnie


// Tworzenie aplikacji Vue
const app = createApp(App);

// Dodanie routera do aplikacji
app.use(router);

// Dodanie Axios do globalnych właściwości aplikacji
app.config.globalProperties.$axios = axios;

// Montowanie aplikacji
app.mount('#app');
