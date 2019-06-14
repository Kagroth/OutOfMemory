/*
    Plik zawiera obiekt zawierajacy URL do API
*/
export default {
    baseURL: "http://localhost:8000/",
    endpoints: {
        login: "token/",
        register: "profile/",
        profile: "profile/",
        cv: 'profile/cv/',
        post_previews: "post_preview/",
        searchPost: "post/search/",
        postByTag: "post/tag/",
        createPost: "post/new/",
        postDetails: "post/details/",
        addComment: 'post/comment/new/',
        rateComment: 'post/comment/',
        tags: 'tag/',
        jobs: 'job/',   
    },

    getLoginEndpoint() {
        return this.baseURL + this.endpoints.login;
    },

    getRegisterEndpoint() {
        return this.baseURL + this.endpoints.register;
    },

    getProfileEndpoint() {
        return this.baseURL + this.endpoints.profile;
    },

    getCVEndpoint() {
        return this.baseURL + this.endpoints.cv;
    },

    getPostPreviewsEndpoint() {
        return this.baseURL + this.endpoints.post_previews;
    },

    getSearchPostEndpoint() {
        return this.baseURL + this.endpoints.searchPost;
    },

    getPostByTagEndpoint() {
        return this.baseURL + this.endpoints.postByTag;
    },

    getCreatePostEndpoint() {
        return this.baseURL + this.endpoints.createPost;
    },

    getPostDetailsEndpoint() {
        return this.baseURL + this.endpoints.postDetails;
    },

    getAddCommentEndpoint() {
        return this.baseURL + this.endpoints.addComment;
    },

    getRateCommentEndpoint() {
        return this.baseURL + this.endpoints.rateComment;
    },

    getTagsEndpoint() {
        return this.baseURL + this.endpoints.tags;
    },

    getJobsEndpoint() {
        return this.baseURL + this.endpoints.jobs;
    }
}
