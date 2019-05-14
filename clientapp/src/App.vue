<template>
  <div id="app">
    <main-nav></main-nav>
    <b-container fluid class="content">
      <b-row>
        <b-col cols=8 offset=2>
          <router-view></router-view>
          <!--<listing-tab v-bind:post_previews="post_previews"></listing-tab>-->
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap-vue/dist/bootstrap-vue.css";

// custom components
import MainNav from './components/MainNav.vue';
import ListingTab from './components/ListingTab.vue';

export default {
  name: 'app',

  components: {
    'main-nav': MainNav,
    'listing-tab': ListingTab
  },

  data() {
    return {
    }
  },

  methods: {
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
