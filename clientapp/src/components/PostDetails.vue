<template>
    <div>
        <b-row>
            <b-col offset=1>{{ post.author }}</b-col>
        </b-row>
        <b-row>
            <b-col offset=1>{{ post.createdAt.substr(0, 10) }}</b-col>
        </b-row>
        <b-row>
            <b-col offset=1>{{ post.title }}</b-col>
        </b-row>
        <b-row>
            <b-col offset=1>
                <b-badge variant="primary" class="mr-1" :key="tag" v-for="tag in post.tags"> {{ tag.tagName }} </b-badge>
            </b-col>
        </b-row>        
        <b-row class="mt-3">
            <b-col cols=10 offset=1>{{ post.postField }}</b-col>
        </b-row>
        <div class="commentSection mt-5">
            <h5>Odpowiedzi:</h5>
            <b-row :key="comment" v-for="comment in post.comments">{{ comment }}</b-row>
        </div>
        
    </div>    
</template>

<script>
export default {
    created() {
        console.log(this.$route);
        this.$store.dispatch('getPostDetails', this.$route.params.pk);
    },

    computed: {
        post () {
            return this.$store.state.postDetails;
        }
    }
}
</script>

<style scoped>
div {
    background-color: lightgreen;
}
</style>
