<template>
  <div>
    <b-navbar type="dark" variant="dark" fixed="top">
      <b-navbar-brand href="#">
        <router-link to="/">OutOfMemory</router-link>
      </b-navbar-brand>
      <b-navbar-nav>
        <b-nav-form class="ml-5">
          <b-form-input v-model="searchParam" size="sm" placeholder="Wprowadz szukana fraze"></b-form-input>
          <b-button variant="success" size="sm" class="orangeBg ml-1" @click="search">Szukaj</b-button>
        </b-nav-form>
      </b-navbar-nav>
      <b-navbar-nav class="ml-auto" v-if="!isLogged">
        <b-nav-item to="/login" href="#" class="menuLink">Logowanie</b-nav-item>
        <b-nav-item to="/register" href="#" class="menuLink">Rejestracja</b-nav-item>
      </b-navbar-nav>
      <b-navbar-nav class="ml-auto" v-else>
        <b-nav-item-dropdown to="" href="#" id="menuDropdownLink" :text="username" right>
          <b-dropdown-item to="/profile" class="blackText">Profil</b-dropdown-item>
          <b-dropdown-item :to="{name: 'ProfileSettings'}" class="blackText">Ustawienia</b-dropdown-item>
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

    search () {
      if(this.searchParam === "") {
        Promise.all([
          this.$store.dispatch('getAllPostPreviews'),
          this.$store.dispatch('getAllJobOffers')]
        )     

        return
      }

      let activeTab = document.querySelector('ul.nav > li > a.active')
      let action = ""

      if(activeTab.querySelector('strong').innerText === "Posty") {
        action = "searchPosts"
      }
      else {
        action = "searchJobOffers"
      }

      this.$store.dispatch(action, this.searchParam);
    }
  }
};
</script>

<style scoped>
.orangeBg {
  background-color: #ff9b04;
}

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
