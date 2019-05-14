import Vue from 'vue'
import App from './App.vue'
import BootstrapVue from 'bootstrap-vue'
import VueRouter from 'vue-router'
import Vuex from 'vuex'
import VueResource from 'vue-resource'
import Routes from './routes'
import api from './api'
import axios from 'axios'

Vue.use(BootstrapVue);
Vue.use(VueRouter);
Vue.use(Vuex);

const store = new Vuex.Store({
  state: {
    token: localStorage.getItem('token'),
    isLogged: (localStorage.getItem('token') !== null),

    post_previews: []

  },

  mutations: {
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
        axios.get(api.getPostEndpoint(), {headers: {
          'Authorization': authHeader
        }})
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

    createGroup ({commit}, payload) {
      return new Promise((resolve, reject) => {
        let authHeader = "Bearer " + this.state.token;

        axios.post("http://localhost:8000/groups/", {
          params: payload},
          {headers: {
          'Authorization': authHeader
        }})
          .then((response) => {
            resolve()
          })
          .catch((error) => {
            reject()
          })
      })
    }
  }
})

const router = new VueRouter({
  routes: Routes,
  mode: 'history'
});

new Vue({
  el: '#app',
  render: h => h(App),
  router: router,
  store: store,
})