<template>
  <div>
    <b-navbar variant="primary" fixed="top">
      <b-navbar-brand href="#">
        <router-link to="/">OutOfMemory</router-link>
      </b-navbar-brand>
      <b-navbar-nav>
        <b-nav-form class="ml-5">
          <b-form-input v-model="filterParam" size="sm" placeholder="Wprowadz szukana fraze"></b-form-input>
          <b-button size="sm" class="ml-1">Szukaj</b-button>
        </b-nav-form>
      </b-navbar-nav>
      <b-navbar-nav class="ml-auto">
        <b-nav-item to="/login" href="#" class="menuLink">Logowanie</b-nav-item>
        <b-nav-item to="/register" href="#" class="menuLink">Rejestracja</b-nav-item>
      </b-navbar-nav>
      <!--
      <b-navbar-nav class="ml-auto">
        <b-nav-item to="" href="#" class="menuLink">Wyloguj</b-nav-item>
      </b-navbar-nav>    
      -->  
    </b-navbar>
  </div>
</template>

<script>
export default {
  data() {
    return {
      message: "Nawigacja",
      filterParam: ""
    };
  },

  methods: {

  }
};
</script>

<style scoped>
.navbar .navbar-nav .menuLink a {
    color: white;
}

.navbar .navbar-brand a {
    text-decoration: none;
    color: white;
}
</style>
