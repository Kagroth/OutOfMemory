<template>
  <div id="app">
    <main-nav></main-nav>
    <b-container fluid class="content">
      <b-row>
        <b-col cols=8 offset=2>
          <router-view v-bind:post_previews="post_previews"></router-view>
          <!--<listing-tab v-bind:post_previews="post_previews"></listing-tab>-->
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
import BCol from 'bootstrap-vue/es/components/layout/col';

// custom components
import MainNav from './components/MainNav.vue';
import ListingTab from './components/ListingTab.vue';

export default {
  name: 'app',
  data () {
    return {
      post_previews: [
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
      ]
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
