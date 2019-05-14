<template>
    <div>
        <b-row class="mt-1">
            <b-col offset=1 cols=7><h4>{{ post.title }}</h4></b-col>
            <b-col offset=1 cols=2 class="text-right">{{ post.author }}<br>{{ post.createdAt.substr(0, 10) }}</b-col>
        </b-row>
        <b-row>
            <b-col offset=1>
                <b-badge variant="primary" class="mr-1" :key="tag" v-for="tag in post.tags"> {{ tag.tagName }} </b-badge>
            </b-col>
        </b-row>        
        <b-row class="mt-3">
            <b-col cols=10 offset=1 class="text-justify">{{ post.postField }}</b-col>
        </b-row>
        <div class="commentSection mt-5">
            <b-row>
                <b-col cols=10 offset=1>
                    <h5>Odpowiedzi:</h5>
                </b-col>
            </b-row>
            <b-row>
                <b-col v-if="isLogged" cols=9 offset=1>
                    <b-button v-b-toggle.addCommentFormCollapse variant="info" size="sm" @click="onAddCommentCollapseHandler">{{ collapseButtonText }}</b-button>
                    <b-collapse id="addCommentFormCollapse" class="mt-2">
                        <b-form>
                            <b-form-textarea rows="10" v-model="commentField" placeholder="Tresc komentarza"/>                        
                        </b-form>
                        <b-button variant="success" size="sm" class="mt-1" @click="addComment">Wyślij</b-button>
                    </b-collapse>                    
                </b-col>
            </b-row>
            <b-row :key="comment" v-for="comment in post.comments" class="mt-3">
                <comment v-bind:comment="comment"/>
            </b-row>
        </div>        
    </div>    
</template>

<script>
import Comment from './Comment'

export default {
    components: {
        'comment': Comment
    },

    data () {
        return {
            collapseButtonText: "Dodaj komentarz",
            commentField: ""
        }
    },

    created() {
        console.log(this.$route);
        this.$store.dispatch('getPostDetails', this.$route.params.pk);
    },

    computed: {
        post () {
            return this.$store.state.postDetails;
        },

        isLogged () {
            return this.$store.state.isLogged;
        }
    },

    methods: {
        onAddCommentCollapseHandler () {
            if(this.collapseButtonText === "Dodaj komentarz") {
                this.collapseButtonText = "Ukryj"
            }
            else {
                this.collapseButtonText = "Dodaj komentarz"
            }
        },

        addComment () {
            this.$store.dispatch('addComment', {
                postPk: this.post.pk,
                comment: this.commentField
            })
        }
    }
}
</script>

<style scoped>
</style>
