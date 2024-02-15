import './assets/main.css';
import './assets/tailwind.css';
import 'vue-toast-notification/dist/theme-bootstrap.css';

import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import loginInfoStore from './store';
import VuelidatePlugin from '@vuelidate/core';
import FlagIcon from 'vue-flag-icon';
import axios from 'axios';
import ToastPlugin from 'vue-toast-notification';

axios.defaults.baseURL = import.meta.env.VITE_BACKEND_BASE_URL;

const app = createApp(App);

app.use(router);
app.use(loginInfoStore);
app.use(VuelidatePlugin);
app.use(FlagIcon);
app.use(ToastPlugin, { position: 'top-right' });

app.mount('#app');
