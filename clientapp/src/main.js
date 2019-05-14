import Vue from 'vue'
import App from './App.vue'
import BootstrapVue from 'bootstrap-vue'
import VueRouter from 'vue-router'
import Vuex from 'vuex'
import Routes from './routes'
import store from './store/index'

Vue.use(BootstrapVue);
Vue.use(VueRouter);
Vue.use(Vuex);

const router = new VueRouter({
  routes: Routes,
  mode: 'history'
});

new Vue({
  el: '#app',
  render: h => h(App),
  router: router,
  store: store,

  created () {
    this.$store.commit('init');
  }
})