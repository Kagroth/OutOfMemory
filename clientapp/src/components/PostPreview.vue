<template>
    <div class="mb-3">
        <div class="shadow-sm">            
            <b-row class="pl-2">
                <b-col cols=12 class="lead"> {{ postPreview.title }}</b-col>
            </b-row>            
            <b-row>
                <b-col cols=8>
                    <b-img
                        :src="require('../assets/icons8-html-5-48.png')">
                    </b-img>
                    <b-badge 
                    variant="primary" 
                    class="mr-1" 
                    :key="tag" 
                    v-for="tag in postPreview.tags"
                    @click="getPostsByTag(tag.tagName)">{{ tag.tagName }}</b-badge>
                </b-col>
                <b-col cols=4>
                    <b-row class="pr-3">
                        <b-col class="text-right">
                            Wyświetleń: {{ postPreview.viewsCount }}                   
                        </b-col>
                    </b-row>
                    <b-row class="pr-3">
                        <b-col class="text-right">
                            Odpowiedzi: {{ postPreview.commentsCount }}
                        </b-col>
                    </b-row>
                </b-col>
            </b-row>
            <b-row class="pl-2">
                <b-col><small>Autor: {{ postPreview.author }}</small></b-col>
            </b-row>
            <b-row class="pl-2">
                <b-col><small>{{ postPreview.createdAt.substring(0, 10) }}</small></b-col>
            </b-row>
            <b-row class="pl-2">
                
            </b-row>            
        </div>
        <!--
        <b-card v-bind:title="postPreview.title" @click="showDetails">           
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
                <b-badge 
                    variant="primary" 
                    class="mr-1" 
                    :key="tag" 
                    v-for="tag in postPreview.tags"
                    @click="getPostsByTag(tag.tagName)">{{ tag.tagName }}</b-badge>
            </b-card-text>
            <div slot="footer"><small>{{ postPreview.createdAt.substring(0, 10) }}</small></div>
        </b-card>
        -->
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
        showDetails (event) {
            event.preventDefault();
            let pk = this.postPreview.pk;
            console.log("Zmieniam na details!");
            this.$router.push({name: 'PostDetails', params: { pk }});
        },

        getPostsByTag(tagName) {
            event.preventDefault();
            console.log(tagName);
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
