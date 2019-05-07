/*
    Plik zawiera obiekt zawierajacy URL do API
*/
export default {
    baseURL: "http://localhost:8000/",
    endpoints: {
        login: "login/",
        register: "user/",

    },

    getLoginEndpoint() {
        return this.baseURL + this.endpoints.login;
    },

    getRegisterEndpoint() {
        return this.baseURL + this.endpoints.register;
    }
}