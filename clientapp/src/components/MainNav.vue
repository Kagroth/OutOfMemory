<template>
  <div>
    <b-navbar variant="primary" fixed="top">
      <b-navbar-brand href="#">
        <router-link to="/">OutOfMemory</router-link>
      </b-navbar-brand>
      <b-navbar-nav>
        <b-nav-form class="ml-5">
          <b-form-input size="sm" placeholder="Wprowadz szukana fraze"></b-form-input>
          <b-button size="sm" class="ml-1">Szukaj</b-button>
        </b-nav-form>
      </b-navbar-nav>
      <b-navbar-nav class="ml-auto">
        <b-nav-item to="/login" href="#" class="menuLink">Logowanie</b-nav-item>
        <b-nav-item to="/register" href="#" class="menuLink">Rejestracja</b-nav-item>
      </b-navbar-nav>
    </b-navbar>
  </div>
</template>

<script>
/* Layout components
import BContainer from "bootstrap-vue/es/components/layout/container";
import BRow from "bootstrap-vue/es/components/layout/row";
import BCol from "bootstrap-vue/es/components/layout/col";
*/

// Nav components
import BNav from "bootstrap-vue/es/components/nav/nav";
import BNavItem from "bootstrap-vue/es/components/nav/nav-item";
import BNavText from "bootstrap-vue/es/components/nav/nav-text";
import BNavForm from "bootstrap-vue/es/components/nav/nav-form";
import BNavItemDropdown from "bootstrap-vue/es/components/nav/nav-item-dropdown";

// Navbar components
import BNavbar from "bootstrap-vue/es/components/navbar/navbar";
import BNavbarNav from "bootstrap-vue/es/components/navbar/navbar-nav";
import BNavbarBrand from "bootstrap-vue/es/components/navbar/navbar-brand";
import BNavbarToggle from "bootstrap-vue/es/components/navbar/navbar-toggle";

//Form components
import BFormInput from "bootstrap-vue/es/components/form-input/form-input";

//Button
import BButton from 'bootstrap-vue/es/components/button/button';

export default {
  components: {
    "b-navbar": BNavbar,
    "b-navbar-brand": BNavbarBrand,
    "b-navbar-nav": BNavbarNav,
    "b-nav-form": BNavForm,
    "b-nav-item": BNavItem,
    "b-form-input": BFormInput,
    'b-button': BButton
  },
  data() {
    return {
      message: "Nawigacja"
    };
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
