/*
    Plik zawiera obiekt zawierajacy URL do API
*/
export default {
    baseURL: "http://localhost:56086/user/",
    endpoints: {
        login: "login/",
        register: "register/",

    },

    getLoginEndpoint() {
        return this.baseURL + this.endpoints.login;
    },

    getRegisterEndpoint() {
        return this.baseURL + this.endpoints.register;
    }
}