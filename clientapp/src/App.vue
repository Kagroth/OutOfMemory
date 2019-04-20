<template>
  <div id="app">
    <main-nav></main-nav>
    <b-container fluid class="content">
      <b-row>
        <b-col cols="auto">
          <listing-tab></listing-tab>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap-vue/dist/bootstrap-vue.css";

// Layout components
import BContainer from 'bootstrap-vue/es/components/layout/container';
import BRow from 'bootstrap-vue/es/components/layout/row';
import BCol from 'bootstrap-vue/es/components/layout/container';

// custom components
import MainNav from './components/MainNav.vue';
import ListingTab from './components/ListingTab.vue';

export default {
  name: 'app',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  },
  components: {
    'b-container': BContainer,
    'b-row': BRow,
    'b-col': BCol,
    'main-nav': MainNav,
    'listing-tab': ListingTab
  }
}
</script>

<style scoped>
.content {

  position: absolute;
    top: 10%;
  
  background-color: lightblue;
}
</style>
