import { createStore } from 'vuex'
import type { UserRoleType } from '../types/UserRoleType'
import type { GenderType } from '../types/GenderType'
import type { LoginInfoType } from './../types/LoginInfoType'
import type { UserAccountType } from '@/types/UserAccountType'
import axios from 'axios'

const loginInfoStore = createStore<{ loginInfo?: LoginInfoType}>({
    state: {
        loginInfo: undefined
    } as { loginInfo?: LoginInfoType},
    mutations: {
        setLoginInfo(state: { loginInfo?: LoginInfoType}, loginInfo: LoginInfoType) {
            state.loginInfo = loginInfo
        },
        async logOut(state: { loginInfo?: LoginInfoType}) {
            await axios.post('auth/logout')
            state.loginInfo = undefined
        }
    },
    actions: {},
    getters: {
        isLoggedIn(state: { loginInfo?: LoginInfoType}) : boolean {
            return !!state.loginInfo
        },
        userId(state: { loginInfo?: LoginInfoType}) : number | undefined {
            return state.loginInfo?.userId
        },
        firstName(state: { loginInfo?: LoginInfoType}) : string | undefined {
            return state.loginInfo?.firstName
        },
        lastName(state: { loginInfo?: LoginInfoType}) : string | undefined {
            return state.loginInfo?.lastName
        },
        email(state: { loginInfo?: LoginInfoType}) : string | undefined {
            return state.loginInfo?.email
        },
        gender(state: { loginInfo?: LoginInfoType}) : GenderType | undefined {
            return state.loginInfo?.gender
        },
        role(state: { loginInfo?: LoginInfoType}) : UserRoleType | undefined {
            return state.loginInfo?.role
        },
        accountType(state: { loginInfo?: LoginInfoType}) : UserAccountType | undefined {
            return state.loginInfo?.accountType
        }
    },
})

export default loginInfoStore