<template>
  <div>
    <b-navbar variant="primary" fixed="top">
      <b-navbar-brand href="#">
        <router-link to="/">OutOfMemory</router-link>
      </b-navbar-brand>
      <b-navbar-nav>
        <b-nav-form class="ml-5">
          <b-form-input v-model="searchParam" size="sm" placeholder="Wprowadz szukana fraze"></b-form-input>
          <b-button size="sm" class="ml-1" @click="searchPosts">Szukaj</b-button>
        </b-nav-form>
      </b-navbar-nav>
      <b-navbar-nav class="ml-auto" v-if="!isLogged">
        <b-nav-item to="/login" href="#" class="menuLink">Logowanie</b-nav-item>
        <b-nav-item to="/register" href="#" class="menuLink">Rejestracja</b-nav-item>
      </b-navbar-nav>
      <b-navbar-nav class="ml-auto" v-else>
        <b-nav-item-dropdown to="" href="#" id="menuDropdownLink" :text="username" right>
          <b-dropdown-item to="/profile" class="blackText">Profil</b-dropdown-item>
          <b-dropdown-divider></b-dropdown-divider>
          <b-dropdown-item class="blackText" @click="logout">Wyloguj</b-dropdown-item>
        </b-nav-item-dropdown>
      </b-navbar-nav> 
    </b-navbar>
  </div>
</template>

<script>
export default {
  data() {
    return {
      searchParam: ""
    };
  },

  computed: {
    isLogged () {
      return this.$store.state.isLogged;
    },

    username () {
      return this.$store.state.username;
    }
  },

  methods: {
    logout () {
      let currentPath = this.$route.path;
      this.$store.commit('logout');
      alert("Nastapilo wylogowanie");      
      this.$router.push("/");
    },

    searchPosts () {
      this.$store.dispatch('searchPosts', this.searchParam);
    }
  }
};
</script>

<style scoped>
.navbar .navbar-nav .menuLink a {
    color: white;
}

#menuDropdownLink a {
  text-decoration: none;
  color: white;
}

#menuDropdownLink a span {
  color: white;
}

.navbar .navbar-brand a {
    text-decoration: none;
    color: white;
}

.navbar .navbar-nav #menuDropdownLink .dropdown-menu .blackText {
  color: black;
}
</style>
