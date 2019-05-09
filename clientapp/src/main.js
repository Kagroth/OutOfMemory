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
    //isLoggedUser: (localStorage.getItem('token') === null),

    posts: [

    ],

    posts_previews: [
      {
        author: "pjoterN",
        creationDate: "20.04.2019",
        viewsCount: 5,
        answersCount: 1,
        title: "Mam problem z NullPointerException",
        tags: ["Java", "MySQL"]
      },

      {
        author: "saszka",
        creationDate: "20.04.2019",
        viewsCount: 3,
        answersCount: 0,
        title: "Jak wysrodkowac diva w CSS",
        tags: ["HTML", "CSS"]
      },

      {
        author: "mariusz",
        creationDate: "19.04.2019",
        viewsCount: 23,
        answersCount: 7,
        title: "Nie dzialaja mi props w Vue.js",
        tags: ["Javascript", "Vue", "Frontend"]
      },

      {
        author: "mariusz",
        creationDate: "16.04.2019",
        viewsCount: 17,
        answersCount: 3,
        title: "Jak zrobic czary mary w Springu",
        tags: ["Java", "Spring"]
      }
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
  router: router,
  store: store,
})