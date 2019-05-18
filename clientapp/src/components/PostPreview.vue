<template>
    <div @click="showDetails" class="mb-1">
        <b-card v-bind:title="postPreview.title">            
            <b-card-text>
                <div class="cardAuthor w-75">
                    <span>Autor: {{ postPreview.author }} </span>
                </div>
                <div class="cardBadges w-25">
                    <span class="mr-5">Wyswietlen: {{ postPreview.viewsCount}} </span><br>
                    <span class="mr-5">Odpowiedzi: {{ postPreview.commentsCount }} </span>
                </div>
            </b-card-text>
            <b-card-text>
                <b-badge variant="primary" class="mr-1" :key="tag" v-for="tag in postPreview.tags">{{ tag.tagName }}</b-badge>
            </b-card-text>            <!-- tymczasowe rozwiazanie -->
            <div slot="footer"><small>{{ postPreview.createdAt.substring(0, 10) }}</small></div>
        </b-card>
    </div>    
</template>

<script>
export default {
    props: ['postPreview'],

    data(){
        return {
        }
    },

    methods: {
        showDetails () {
            let pk = this.postPreview.pk;
            console.log("Zmieniam na details!");
            this.$router.push({name: 'PostDetails', params: { pk }});
        }
    },
}
</script>

<style scoped>
.cardBadges, .cardAuthor
{
    float: left;
}
</style>
