<template>
  <div>
    <b-navbar variant="primary" fixed="top">
      <b-navbar-brand href="#">
        <router-link to="/">OutOfMemory</router-link>
      </b-navbar-brand>
      <b-navbar-nav>
        <b-nav-form class="ml-5">
          <b-form-input v-model="filterParam" size="sm" placeholder="Wprowadz szukana fraze"></b-form-input>
          <b-button size="sm" class="ml-1" @click="search">Szukaj</b-button>
        </b-nav-form>
      </b-navbar-nav>
      <b-navbar-nav v-if="!isLogged" class="ml-auto">
        <b-nav-item to="/login" href="#" class="menuLink">Logowanie</b-nav-item>
        <b-nav-item to="/register" href="#" class="menuLink">Rejestracja</b-nav-item>
      </b-navbar-nav>
      <b-navbar-nav v-else class="ml-auto">
        <b-nav-item to="" href="#" class="menuLink" @click="logout">Wyloguj</b-nav-item>
      </b-navbar-nav>      
    </b-navbar>
  </div>
</template>

<script>
export default {
  props: ['isLogged'],

  data() {
    return {
      message: "Nawigacja",
      filterParam: ""
    };
  },

  methods: {
    logout() {
      localStorage.removeItem('token');
      this.$emit('logout');
    },

    search() {
      console.log("Wyszukuje!");
    }
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
