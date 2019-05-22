<template>
    <div>
        <b-row>
            <b-col class="username">
                <h3>
                    {{ profile.user.username }}
                </h3>
            </b-col>
        </b-row>
        <b-row>
            <b-col cols=5 class="stats">
                Liczba postów: {{ profile.user.posts.length }} <br>
                Liczba komentarzy: {{ profile.user.comments.length }}
            </b-col>
            <b-col cols=5></b-col>
            <b-col cols=2 class=" cvButton text-right" align-self="center">
                <b-button size="sm" variant="info">Moje CV</b-button>
            </b-col>
        </b-row>
        <b-row class=" mt-1">
            <b-col cols=12>
                <hr>
               Opis:
            </b-col>
            <b-col>
                {{ profile.description }}
                <hr>
            </b-col>
        </b-row>
        <b-row>
            <b-col class="mt-5">
                <b-tabs>
                    <b-tab title="Posty">
                        <post-preview v-for="post_prev in profile.user.posts"
                                      v-bind:postPreview="post_prev"></post-preview>
                    </b-tab>
                    <b-tab title="Komentarze">
                        <comment v-for="comment in profile.user.comments"
                                 v-bind:comment="comment"></comment>
                    </b-tab>
                </b-tabs>
            </b-col>
        </b-row>
    </div>
</template>

<script>
import PostPreview from './PostPreview'
import Comment from './Comment'

export default {
    components: {
        "post-preview": PostPreview,
        "comment": Comment
    },

    created() {
        this.$store.dispatch('getLoggedUserProfile')
                    .then(() => {
                        console.log("dupa")
                    });
    },

    computed: {
        profile() {
            return this.$store.state.currentUser;
        }
    },
}
</script>

<style scoped>
.username {
    background-color: lightgreen;
}

.stats {
    background-color: yellow;
}

.cvButton {
    background-color: silver;
}

.descriptionRow {
    border-top: solid 1px;
}
</style>
