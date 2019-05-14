/*
    Plik zawiera obiekt zawierajacy URL do API
*/
export default {
    baseURL: "http://localhost:8000/",
    endpoints: {
        login: "token/",
        register: "user/",
        posts: "post/",
        createPost: "post/new/"
    },

    getLoginEndpoint() {
        return this.baseURL + this.endpoints.login;
    },

    getRegisterEndpoint() {
        return this.baseURL + this.endpoints.register;
    },

    getPostEndpoint() {
        return this.baseURL + this.endpoints.posts;
    },

    getCreatePostEndpoint() {
        return this.baseURL + this.endpoints.createPost;
    }
}