import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import api from '../api'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    token: "",
    isLogged: "",
    username: "",
    currentUser: "",
    post_previews: [],
    posts: [],
    postDetails: "",
    tags: [],
    jobOffers: [],
    jobOfferDetails: ""
  },

  mutations: {
    init(state) {
      state.token = localStorage.getItem('token'),
        state.isLogged = (localStorage.getItem('token') !== "null"
          && localStorage.getItem('token') !== undefined)
      state.username = localStorage.getItem('username') || ""

    },

    setToken(state, payload) {
      localStorage.setItem('token', payload.token);
      localStorage.setItem('username', payload.username);
      state.token = localStorage.getItem('token');
      state.isLogged = (localStorage.getItem('token') != null);
      state.username = payload.username;
    },

    setUsers(state, payload) {
      state.users = payload
    },

    setCurrentProfile(state, payload) {
      state.currentUser = payload;
      console.log(state.currentUser);
    },

    setPostPreviews(state, payload) {
      console.log(payload)
      state.post_previews = payload;
    },

    setPostDetails(state, payload) {
      state.postDetails = payload;
    },

    setJobOfferDetails(state, payload) {
      state.jobOfferDetails = payload
    },

    updateCommentOfPostDetails(state, payload) {
      const item = state.postDetails.comments.find(comment => comment.pk === payload.pk)
      Object.assign(item, payload)  // podmienienie komentarza na ten z nową oceną
    },

    setTags(state, payload) {
      state.tags = payload
    },

    setJobOffers(state, payload) {
      state.jobOffers = payload
    },

    logout(state) {
      localStorage.setItem('token', null);
      state.token = null;
      state.isLogged = false;
    }
  },

  actions: {
    createUser({ commit }, payload) {
      console.log("Wysylam request rejestracji")

      return new Promise((resolve, reject) => {
        axios.post(api.getRegisterEndpoint(), payload)
          .then(response => {
            console.log("Sukces" + response)
            resolve(response.data.message)
          })
          .catch(error => console.log(error.response))
      })
    },

    loginUser({ commit, dispatch }, payload) {
      console.log("Wysylam request logowania");

      return new Promise((resolve, reject) => {
        axios.post(api.getLoginEndpoint(), payload)
          .then(response => {
            console.log(response.data.access);
            commit('setToken', {
              token: response.data.access,
              username: payload.username
            });

            dispatch('getLoggedUserProfile')
            resolve()
          })
          .catch(error => {
            console.log(error.response);
            reject()
          })
      })
    },

    getLoggedUserProfile({ commit }) {
      let authHeader = "Bearer " + this.state.token;

      return new Promise((resolve, reject) => {
        axios.get(api.getProfileEndpoint(), {
          headers: {
            "Authorization": authHeader
          }
        }).then(response => {
          console.log(response.data);
          commit('setCurrentProfile', response.data);
          resolve()
        }).catch(() => {
          reject()
        })
      })
    },

    getAllPostPreviews({ commit }, payload) {
      console.log("Wysylam zadanie wyswietlenia post previews!")

      return new Promise((resolve, reject) => {
        let authHeader = "Bearer " + this.state.token;
        axios.get(api.getPostPreviewsEndpoint())
          .then((response) => {
            commit('setPostPreviews', response.data)
            resolve()
          })
          .catch(() => {
            alert("Blad pobierania postow")
            reject()
          })
      })
    },

    searchPosts({ commit }, payload) {
      console.log(payload);

      let urlToFilteredPosts = api.getSearchPostEndpoint() + "?param=" + payload;
      console.log(urlToFilteredPosts);

      return new Promise((resolve, reject) => {
        axios.get(urlToFilteredPosts)
          .then((response) => {
            commit('setPostPreviews', response.data)
            resolve()
          })
          .catch(() => {
            alert("Blad wyszukiwania postow")
            reject()
          })
      })
    },

    getPostsByTag({ commit }, payload) {
      let urlToFilterPostsByTag = api.getPostByTagEndpoint() + payload.tagName;

      return new Promise((resolve, reject) => {
        axios.get(urlToFilterPostsByTag)
          .then((response) => {
            commit('setPostPreviews', response.data)
            resolve()
          })
          .catch(() => {
            alert("Blad wyszukiwania postow")
            reject()
          })
      })
    },

    getAllTags({ commit }) {
      return new Promise((resolve, reject) => {
        let authHeader = "Bearer " + this.state.token;
        axios.get(api.getTagsEndpoint())
          .then((response) => {
            console.log(response.data)
            commit('setTags', response.data)
            resolve()
          })
          .catch(() => {
            alert("Blad pobierania tagow")
            reject()
          })
      })
    },

    createPost({ commit }, payload) {
      console.log("Wysylam request z utworzeniem posta")

      return new Promise((resolve, reject) => {
        let authHeader = "Bearer " + this.state.token;

        axios.post(api.getCreatePostEndpoint(), {
          params: payload
        },
          {
            headers: {
              'Authorization': authHeader
            }
          })
          .then(response => {
            console.log(response.data)
            resolve()
          })
          .catch(() => {
            alert("Nie udalo sie utworzyc posta")
            reject()
          })
      })
    },

    createJobOffer({ commit }, payload) {
      console.log("Wysylam request z utworzeniem oferty pracy")

      return new Promise((resolve, reject) => {
        let authHeader = "Bearer " + this.state.token;

        axios.post(api.getCreateJobOfferEndpoint(), {
          params: payload
        },
          {
            headers: {
              'Authorization': authHeader
            }
          })
          .then(response => {
            console.log(response.data)
            resolve()
          })
          .catch(() => {
            alert("Nie udalo sie utworzyc oferty pracy")
            reject()
          })
      })
    },

    getPostDetails({ commit }, payload) {
      return new Promise((resolve, reject) => {
        axios.get(api.getPostDetailsEndpoint() + payload)
          .then((response) => {
            commit('setPostDetails', response.data)
            resolve(response.data)
          })
          .catch(() => {
            alert("Blad pobierania posta")
            reject()
          })
      })
    },

    getJobOfferDetails({ commit }, payload) {
      return new Promise((resolve, reject) => {
        axios.get(api.getJobOfferDetailsEndpoint() + payload)
          .then((response) => {
            commit('setJobOfferDetails', response.data)
            resolve(response.data)
          })
          .catch(() => {
            alert("Blad pobierania posta")
            reject()
          })
      })
    },

    addComment({ commit, dispatch }, payload) {
      let authHeader = "Bearer " + this.state.token;

      return new Promise((resolve, reject) => {
        axios.post(api.getAddCommentEndpoint(), {
          params: payload
        },
          {
            headers: {
              'Authorization': authHeader
            }
          })
          .then(response => {
            console.log(response)
            console.log(payload.postPk)
            dispatch('getPostDetails', payload.postPk)
              .then(() => {
                console.log("Udalo sie")
              })
              .catch((error) => {
                console.log(error)
              });
            resolve()
          })
          .catch(() => {
            console.log("nie udalo sie dodac komentarza")
            reject()
          })
      })
    },

    rateComment({ commit }, payload) {
      let authHeader = "Bearer " + this.state.token;

      return new Promise((resolve, reject) => {
        axios.post(api.getRateCommentEndpoint() + payload.commentPk, {
          rate: payload.rate
        },
          {
            headers: {
              'Authorization': authHeader
            }
          })
          .then(response => {
            console.log(response)
            commit('updateCommentOfPostDetails', response.data)
            resolve()
          })
          .catch(() => {
            reject()
          })
      })
    },

    getAllJobOffers({ commit }) {
      return new Promise((resolve, reject) => {
        axios.get(api.getJobsEndpoint())
          .then((response) => {
            console.log(response.data)
            commit('setJobOffers', response.data)
            resolve()
          })
          .catch(() => {
            alert("Blad pobierania tagow")
            reject()
          })
      })
    },

    updateUserDescription({ commit, dispatch }, payload) {
      let authHeader = "Bearer " + this.state.token;

      return new Promise((resolve, reject) => {
        axios.put(api.getProfileEndpoint(), {
          userPk: payload.userPk,
          newDescription: payload.description
        },
          {
            headers: {
              'Authorization': authHeader
            }
          })
          .then(response => {
            console.log(response)
            dispatch('getLoggedUserProfile')
            resolve()
          })
          .catch((error) => {
            reject(error)
          })
      })
    },

    //edycja ofert pracy
    updateJobOffer({ commit }, payload) {
      let authHeader = "Bearer " + this.state.token;

      return new Promise((resolve, reject) => {
        axios.put(api.getJobOfferEditEndpoint(), {
          params: payload
        },
          {
            headers: {
              'Authorization': authHeader
            }
          })
          .then(response => {
            console.log(response)
          })
          .catch((error) => {
            reject(error)
          })
      })
    },

    applyForOffer({ commit }, payload) {
      let authHeader = "Bearer " + this.state.token;

      return new Promise((resolve, reject) => {
        axios.post(api.getApplyForOfferEndpoint(payload.offerPk),{}, {
          headers: {
            'Authorization': authHeader
          }
        }).then( response => {
          console.log(response)
          console.log(response.data.message)
          resolve(response.data.message)
        }).catch(error => {
          console.log(error)
          reject()
        })
      })
    },

    createCV({ dispatch }, payload) {
      let authHeader = "Bearer " + this.state.token;

      return new Promise((resolve, reject) => {
        axios.post(api.getCVEndpoint(), {
          skills: payload.skills,
          experience: payload.experiences
        },
          {
            headers: {
              'Authorization': authHeader
            }
          })
          .then(response => {
            console.log(response)
            dispatch('getLoggedUserProfile')
            resolve()
          })
          .catch((error) => {
            reject(error)
          })
      })
    },

    deleteCV({ dispatch }) {
      let authHeader = "Bearer " + this.state.token;
      return new Promise((resolve, reject) => {
        axios.delete(api.getCVEndpoint(),
          {
            headers: {
              'Authorization': authHeader
            }
          })
          .then(response => {
            console.log(response)
            dispatch('getLoggedUserProfile')
            resolve()
          })
          .catch((error) => {
            reject(error)
          })
      })
    },

    onAvatarUpload({ commit, dispatch }, payload) {
      let authHeader = "Bearer " + this.state.token;

      return new Promise((resolve, reject) => {
        axios.put(api.getUploadAvatarEndpoint() + this.state.username + "Avatar.jpg",
          payload.avatar,
          {
            headers: {
              'Authorization': authHeader
            }
          }
        ).then(res => {
          console.log(res)
          dispatch('getLoggedUserProfile')
          resolve()
        }).catch((error) => {
          reject(error)
        })
      })
    },
  }
})
