/*
    Plik zawiera obiekt zawierajacy URL do API
*/
export default {
    baseURL: "http://localhost:8000/",
    endpoints: {
        login: "token/",
        register: "user/",
        post_previews: "post_preview/",
        searchPost: "post/search/",
        createPost: "post/new/"
    },

    getLoginEndpoint() {
        return this.baseURL + this.endpoints.login;
    },

    getRegisterEndpoint() {
        return this.baseURL + this.endpoints.register;
    },

    getPostPreviewsEndpoint() {
        return this.baseURL + this.endpoints.post_previews;
    },

    getSearchPostEndpoint() {
        return this.baseURL + this.endpoints.searchPost;
    },

    getCreatePostEndpoint() {
        return this.baseURL + this.endpoints.createPost;
    }
}