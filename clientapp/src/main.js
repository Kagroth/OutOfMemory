import Vue from 'vue'
import App from './App.vue'
import BootstrapVue from 'bootstrap-vue'
import VueRouter from 'vue-router'
import Vuex from 'vuex'
import VueResource from 'vue-resource'
import Routes from './routes'

Vue.use(BootstrapVue);
Vue.use(VueRouter);
Vue.use(Vuex);
Vue.use(VueResource);


const store = new Vuex.Store({
  state: {
    username: null,    
    isLoggedUser: (localStorage.getItem('token') === null),

    posts: [

    ],

    posts_previews: [

    ],

  },

  mutations: {

  },

  actions: {
    
  }
});

const router = new VueRouter({
  routes: Routes,
  mode: 'history'
});

new Vue({
  el: '#app',
  render: h => h(App),
  router: router
})