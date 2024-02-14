<template>
    <RouterView/>
</template>
    
<script lang="ts">
    import { RouterView } from 'vue-router'
    import axios from 'axios'

    export default {
        methods: {
            async beforeUnloadHandler() {
                await axios.post('auth/logout')
            }
        },
        mounted() {
            window.addEventListener('beforeunload', this.beforeUnloadHandler)
        },
        beforeUnmount() {
            window.removeEventListener('beforeunload', this.beforeUnloadHandler)
        }
    }
</script>