<template>
    <div class="mb-1">
        <b-card v-bind:title="title">            
            <b-card-text>
                <div class="cardAuthor w-75">
                    <span>Autor: {{ author }} </span>
                </div>
                <div class="cardBadges w-25">
                    <span class="mr-5">Wyswietlen: {{ viewsCount}} </span><br>
                    <span class="mr-5">Odpowiedzi: {{ answersCount }} </span>
                </div>
            </b-card-text>
            <b-card-text>
                <b-badge variant="primary" class="mr-1" :key="tagName" v-for="tagName in tags">{{ tagName }}</b-badge>
            </b-card-text>            <!-- tymczasowe rozwiazanie -->
            <div slot="footer"><small>{{ creationDate.slice(0, 10) }}</small></div>
        </b-card>
    </div>    
</template>

<script>
// Cards components
import BCard from 'bootstrap-vue/es/components/card/card';
import BCardHeader from 'bootstrap-vue/es/components/card/card-header';
import BCardFooter from 'bootstrap-vue/es/components/card/card-footer';
import BCardBody from 'bootstrap-vue/es/components/card/card-body';
import BCardTitle from 'bootstrap-vue/es/components/card/card-title';
import BCardText from 'bootstrap-vue/es/components/card/card-text';

// Badge components
import BBadge from 'bootstrap-vue/es/components/badge/badge';

export default {
    components: {
        'b-card': BCard,
        'b-card-header': BCardHeader,
        'b-card-footer': BCardFooter,
        'b-card-body': BCardBody,
        'b-card-title': BCardTitle,
        'b-card-text': BCardText,
        'b-badge': BBadge
    },

    props: ['author', 'creationDate',
            'viewsCount', 'answersCount',
            'title', 'tags'],

    data(){
        return {
        }
    }
}
</script>

<style scoped>
.cardBadges, .cardAuthor
{
    float: left;
}
</style>
