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
                <b-badge variant="primary" class="mr-1" :key="tagName" v-for="tagName in tags">{{ tagName.tagName }}</b-badge>
            </b-card-text>            <!-- tymczasowe rozwiazanie -->
            <div slot="footer"><small>{{ creationDate.slice(0, 10) }}</small></div>
        </b-card>
    </div>    
</template>

<script>
export default {
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
