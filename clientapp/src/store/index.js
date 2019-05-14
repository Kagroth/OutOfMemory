import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import api from '../api'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
      token: "",
      isLogged: "",
  
      post_previews: [],
      posts: []
    },
  
    mutations: {
      init (state) {
        state.token = localStorage.getItem('token'),
        state.isLogged = (localStorage.getItem('token') !== "null"
                          && localStorage.getItem('token') !== undefined)
      },
  
      setToken (state, payload) {
        localStorage.setItem('token', payload.token);
        state.token = localStorage.getItem('token');
        state.isLogged = (localStorage.getItem('token') != null)
      },
  
      setUsers (state, payload) {
        state.users = payload
      },
  
      setPostPreviews (state, payload) {
        console.log(payload)
        state.post_previews = payload;
      },
  
      logout (state) {
        localStorage.setItem('token', null);
        state.token = null;
        state.isLogged = false;
      }
    },
  
    actions: {
      createUser ({commit}, payload) {
        console.log("Wysylam request rejestracji")
  
        axios.post(api.getRegisterEndpoint(), payload)
             .then(response => console.log("Sukces" + response))
             .catch(error => console.log(error.response))
      },
  
      loginUser ({commit}, payload) {
        console.log("Wysylam request logowania");
  
        return new Promise((resolve, reject) => {
          axios.post(api.getLoginEndpoint(), payload)
             .then(response => {
               console.log(response.data.access);
               commit('setToken', {
                 token: response.data.access
               });
               
               resolve()
             })
             .catch(error => {            
               console.log(error.response);
               reject()
             })
        })      
      },
  
      getAllUsers({commit}, payload) {
        console.log("Wysylam zadanie pobrania userow!");
  
        return new Promise((resolve, reject) => {
          axios.get('http://localhost:8000/users/')
               .then((response) => {
                 commit('setUsers', response.data)
                 resolve();
               })
               .catch(() => {
                 console.log("Blad pobierania userow");
                 reject();
               })
        })
      },
  
      getAllPostPreviews ({commit}, payload) {
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
  
      createPost ({commit}, payload) {
        console.log("Wysylam request z utworzeniem posta")

        return new Promise((resolve, reject) => {
          let authHeader = "Bearer " + this.state.token;

          axios.post(api.getCreatePostEndpoint(), {
            params: payload },
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
      }
    }
  })