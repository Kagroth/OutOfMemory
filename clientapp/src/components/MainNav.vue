<template>
    <div>
        {{ message }}
        <b-navbar></b-navbar>
    </div>
</template>

<script>
// Nav components
import BNav from 'bootstrap-vue/es/components/nav/nav';
import BNavItem from 'bootstrap-vue/es/components/nav/nav-item';
import BNavText from 'bootstrap-vue/es/components/nav/nav-text';
import BNavForm from 'bootstrap-vue/es/components/nav/nav-form';
import BNavItemDropdown from 'bootstrap-vue/es/components/nav/nav-item-dropdown';

// Navbar components
import BNavbar from 'bootstrap-vue/es/components/navbar/navbar';
import BNavbarNav from 'bootstrap-vue/es/components/navbar/navbar-nav';
import BNavbarBrand from 'bootstrap-vue/es/components/navbar/navbar-brand';
import BNavbarToggle from 'bootstrap-vue/es/components/navbar/navbar-toggle';

export default {
    components: {
        'b-navbar': BNavbar
    },
    data(){
        return {
            message: 'Nawigacja'
        }
    }
}
</script>

<style scoped>

</style>
