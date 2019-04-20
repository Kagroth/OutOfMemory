<template>
    <div>
        <b-tabs>
            <b-tab title="Posty">One</b-tab>
            <b-tab title="Oferty pracy">Two</b-tab>
        </b-tabs>
    </div>
</template>
<script>
// Tab components
import BTabs from 'bootstrap-vue/es/components/tabs/tabs';
import BTab from 'bootstrap-vue/es/components/tabs/tab';

export default {
    components: {
        'b-tabs': BTabs,
        'b-tab': BTab
    }    
}
</script>
<style scoped>

</style>
