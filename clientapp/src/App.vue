<template>
  <div id="app">
    <main-nav></main-nav>
  </div>
</template>

<script>
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap-vue/dist/bootstrap-vue.css";
import MainNav from './components/MainNav.vue';

export default {
  name: 'app',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  },
  components: {
    'main-nav': MainNav
  }
}
</script>

<style scoped>

</style>
