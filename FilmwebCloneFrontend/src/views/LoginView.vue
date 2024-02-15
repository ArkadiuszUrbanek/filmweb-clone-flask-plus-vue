<template>
    <div class="flex justify-center items-center h-screen bg-gradient-to-b from-yellow-500 via-red-500 to-pink-500">
        <div class="w-screen max-w-[400px] shadow-lg p-5 rounded bg-white">
            <p class="font-bold text-2xl text-center mt-3 mb-8">Login</p>
            <form class="mb-3" v-on:submit.prevent="onSubmit">
                <label for="email" class="block">Email</label>
                <input
                    type="text"
                    id="email"
                    v-model="v$.email.$model"
                    v-on:blur="v$.email.$touch()"
                    v-bind:class="{ 'border-red-500': v$.email.$error }"
                    placeholder="Type your email"
                    class="border-b-2 pt-3 pb-3 mb-3 w-full focus:outline-none"
                />
                <template v-for="(error, index) in v$.email.$errors" :key="index">
                    <span class="block text-sm font-semibold text-red-500"> {{ error.$message }}</span>
                </template>
                <label for="password" class="block">Password</label>
                <input
                    type="password"
                    id="password"
                    v-model="v$.password.$model"
                    v-on:blur="v$.password.$touch()"
                    v-bind:class="{ 'border-red-500': v$.password.$error }"
                    placeholder="Type your password"
                    class="border-b-2 pt-3 pb-3 mb-3 w-full focus:outline-none"
                />
                <template v-for="(error, index) in v$.password.$errors" :key="index">
                    <span class="block text-sm font-semibold text-red-500"> {{ error.$message }}</span>
                </template>
                <button
                    type="submit"
                    v-bind:disabled="v$.$invalid"
                    v-bind:class="{ 'cursor-not-allowed': v$.$invalid }"
                    class="block bg-gradient-to-r from-yellow-500 via-red-500 to-pink-500 text-white pt-3 pb-3 pl-6 pr-6 rounded w-full mt-5"
                >
                    Login
                </button>
            </form>
            <div class="mt-6 mb-3 text-center text-sm block w-fit m-auto">
                Don't have an account?
                <router-link to="/signup" class="font-medium">
                    Sign up
                </router-link>
            </div>
            <div class="text-center w-[100%] flex items-center mb-2">
                <hr class="float-left ml-auto mr-auto w-[40%]">Or<hr class="float-right ml-auto mr-auto w-[40%]">
            </div>
            <button v-on:click="loginWithGoogle" class="flex items-center border rounded-[20px] m-auto w-[240px] mb-2">
                <svg class="float-left flex-shrink-0" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" width="40px" height="40px">
                    <path fill="#fbc02d" d="M43.611,20.083H42V20H24v8h11.303c-1.649,4.657-6.08,8-11.303,8c-6.627,0-12-5.373-12-12	s5.373-12,12-12c3.059,0,5.842,1.154,7.961,3.039l5.657-5.657C34.046,6.053,29.268,4,24,4C12.955,4,4,12.955,4,24s8.955,20,20,20	s20-8.955,20-20C44,22.659,43.862,21.35,43.611,20.083z"/>
                    <path fill="#e53935" d="M6.306,14.691l6.571,4.819C14.655,15.108,18.961,12,24,12c3.059,0,5.842,1.154,7.961,3.039	l5.657-5.657C34.046,6.053,29.268,4,24,4C16.318,4,9.656,8.337,6.306,14.691z"/>
                    <path fill="#4caf50" d="M24,44c5.166,0,9.86-1.977,13.409-5.192l-6.19-5.238C29.211,35.091,26.715,36,24,36	c-5.202,0-9.619-3.317-11.283-7.946l-6.522,5.025C9.505,39.556,16.227,44,24,44z"/>
                    <path fill="#1565c0" d="M43.611,20.083L43.595,20L42,20H24v8h11.303c-0.792,2.237-2.231,4.166-4.087,5.571	c0.001-0.001,0.002-0.001,0.003-0.002l6.19,5.238C36.971,39.205,44,34,44,24C44,22.659,43.862,21.35,43.611,20.083z"/>
                </svg>
                <p class="text-md inline-block w-full font-medium pr-[10px]">Log in with Google</p>
            </button>
            <button v-on:click="loginWithFacebook" class="flex items-center border rounded-[20px] m-auto w-[240px] align-middle">
                <svg class="float-left flex-shrink-0" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" width="40px" height="40px">
                    <linearGradient id="Ld6sqrtcxMyckEl6xeDdMa" x1="9.993" x2="40.615" y1="9.993" y2="40.615" gradientUnits="userSpaceOnUse">
                        <stop offset="0" stop-color="#2aa4f4"/>
                        <stop offset="1" stop-color="#007ad9"/>
                    </linearGradient>
                    <path fill="url(#Ld6sqrtcxMyckEl6xeDdMa)" d="M24,4C12.954,4,4,12.954,4,24s8.954,20,20,20s20-8.954,20-20S35.046,4,24,4z"/>
                    <path fill="#fff" d="M26.707,29.301h5.176l0.813-5.258h-5.989v-2.874c0-2.184,0.714-4.121,2.757-4.121h3.283V12.46 c-0.577-0.078-1.797-0.248-4.102-0.248c-4.814,0-7.636,2.542-7.636,8.334v3.498H16.06v5.258h4.948v14.452 C21.988,43.9,22.981,44,24,44c0.921,0,1.82-0.084,2.707-0.204V29.301z"/>
                </svg>
                <p class="text-md inline-block w-full font-medium pr-[10px]">Log in with Facebook</p>
            </button>
        </div>
    </div>
</template>

<script lang="ts">
    import useVuelidate from '@vuelidate/core'
    import { required, email, minLength } from '@vuelidate/validators'
    import axios from 'axios'

    export default {
        setup: () => ({ v$: useVuelidate() }),
        created () {
            this.lastPath = (this.$router.options.history.state.back as string | undefined)?.split('?')[0]
        },
        data() {
            return {
                nonReturnablePaths: ['/confirm-email', '/signup', '/login'] as string[],
                lastPath: undefined as string | undefined,
                email: '',
                password: ''
            }
        },
        validations() {
            return {
                email: { required, email },
                password: { required, minLength: minLength(6) }
            }
        },
        methods: {
            onSubmit() {
                this.v$.$validate()
                .then(() => {
                    axios.post('auth/login', {
                        email: this.email,
                        password: this.password
                    })
                    .then((response) => {
                        this.$toast.open({
                            message: 'You are now logged in.',
                            type: 'success'
                        })

                        this.$store.commit('setLoginInfo', response.data)
                        if (!this.lastPath || this.nonReturnablePaths.includes(this.lastPath)) this.$router.push({ path: '/' })
                        else this.$router.push({ path: this.lastPath })
                    })
                    .catch((error) => {
                        this.$toast.open({
                            message: 'Failed to log the user in.',
                            type: 'error'
                        })
                    })
                })
                .catch(() => {
                    this.$toast.open({
                        message: 'Login form is not valid.',
                        type: 'error'
                    })
                })
            },
            loginWithGoogle() {
                window.location.href = 'http://127.0.0.1:5000/auth/login/google'
                /*try {async 
                    const response = await axios.get('auth/login/google', { params: { next: '/' }})
                    console.log(JSON.stringify(response))

                } catch(error) {
                    this.$toast.open({
                        message: 'Failed to log the user in using Google account.',
                        type: 'error'
                    })
                }*/
            },
            loginWithFacebook() {
                window.location.href = 'http://127.0.0.1:5000/auth/login/facebook'
            }
        }
    }
</script>
