<template>
    <div class="mb-3">
        <div class="shadow-lg">
            <b-row class="pl-2">
                <b-col cols=12 class="lead" @click="showDetails"> {{ postPreview.title }}</b-col>
            </b-row>            
            <b-row class="pl-1">
                <b-col cols=8>
                    <b-img
                        width="25"
                        height="25"
                        :key="index"
                        v-for="(tag, index) in postPreview.tags"
                        :src="getImage(tag.tagName)"
                        @click="getPostsByTag(tag.tagName)"
                        :title="tag.tagName">
                    </b-img>
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
                <b-col @click="showProfile"><small>Autor: {{ postPreview.author }}</small></b-col>
            </b-row>
            <b-row class="pl-2">
                <b-col><small>{{ postPreview.createdAt.substring(0, 10) }}</small></b-col>
            </b-row>          
        </div>
    </div>    
</template>

<script>
export default {
    props: ['postPreview'],

    data(){
        return {
        }
    },

    created() {
    },

   methods: {
        mapTagName(tagName) {
            return tagName
        },

        /*
        dynamiczne ladowanie image*/
        getImage(tagName) {
            let mappedTag = this.mapTagName(tagName)

            if(mappedTag === "")
                return null
            
            return require("../assets/" + mappedTag + ".png")
        },
        
        showDetails (event) {
            event.preventDefault();
            let pk = this.postPreview.pk;
            console.log("Zmieniam na details!");
            this.$router.push({name: 'PostDetails', params: { pk }});
        },

        getPostsByTag(tagName) {
            event.preventDefault();
            console.log(tagName);
            this.$store.dispatch('getPostsByTag', {
                tagName: tagName
            })
        },

        showProfile() {
            let username = this.postPreview.author

            if(username === this.$store.state.currentUser.user.username) {
                this.$router.push("/profile")
                return
            }

            this.$router.push({name: 'UserProfile', params: { username }})
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
