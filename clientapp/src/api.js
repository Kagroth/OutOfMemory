/*
    Plik zawiera obiekt zawierajacy URL do API
*/
export default {
    baseURL: "http://localhost:8000/",
    endpoints: {
        login: "login/",
        register: "user/",
        posts: "post/"
    },

    getLoginEndpoint() {
        return this.baseURL + this.endpoints.login;
    },

    getRegisterEndpoint() {
        return this.baseURL + this.endpoints.register;
    },

    getPostEndpoint() {
        return this.baseURL + this.endpoints.posts;
    }
}