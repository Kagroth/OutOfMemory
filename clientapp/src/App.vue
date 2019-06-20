<template>
  <div id="app">
    <main-nav></main-nav>
    <b-container fluid class="content">
      <b-row>
        <b-col cols=8 offset=2>
          <transition name="component-slide" mode="out-in">
            <router-view :key="$route.fullPath"></router-view>
          </transition>
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

  font-family: Arial, Helvetica, sans-serif
}

.component-slide-enter-active, .component-slide-leave-active {
  transition: all .3s
}

.component-slide-enter, .component-slide-leave-to {
  opacity: 0
}

</style>
