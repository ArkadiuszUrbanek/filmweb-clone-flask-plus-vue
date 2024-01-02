import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import axios from 'axios'

axios.defaults.baseURL = 'https://127.0.0.1:5000/'
axios.defaults.xsrfCookieName = 'X-CSRFToken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

axios.interceptors.request.use(config => {
    const csrfToken = getCSRFTokenFromCookie()
    
    if (csrfToken) config.headers[axios.defaults.xsrfHeaderName!] = csrfToken
    
    return config
})

createApp(App).mount('#app')
