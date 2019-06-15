<template>
  <div>
    <b-row>
      <b-col class="">
        <h3>

          <avatar :image="'http://localhost:8000' + profile.avatar" size='300' v-if="profile.avatar != null"></avatar>
          <avatar :fullname="profile.user.username" size='300' v-else></avatar>
          {{ profile.user.username }}
        </h3>
      </b-col>
    </b-row>
    <b-row>
      <b-col cols=5 class="">
        Liczba postów: {{ profile.user.posts.length }} <br>
        Liczba komentarzy: {{ profile.user.comments.length }}
      </b-col>
      <b-col cols=5></b-col>
      <b-col cols=2 class=" text-right" align-self="center">
        <router-link to="/profile/cv">
          <b-button size="sm" variant="info">Moje CV</b-button>
        </router-link>
      </b-col>
    </b-row>
    <b-row class=" mt-1">
      <b-col>
        <hr>
      </b-col>
    </b-row>
    <b-row>
      <b-col cols=10>
        Opis:
      </b-col>
      <b-col cols=2 class="text-right">
        <b-button size="sm" @click="toggleDescription">{{ editButtonText }}</b-button>
      </b-col>
      <b-col class="mt-2">
                <span v-if="!isDescriptionEditing">
                    {{ profile.description }}
                </span>
        <div class="textarea-container" v-else>
          <textarea v-model="description" rows=10></textarea>
        </div>
        <hr>
      </b-col>
    </b-row>
    <b-row>
      <b-col class="mt-5">
        <b-tabs>
          <b-tab title="Posty">
            <post-preview :key="index" v-for="(post_prev, index) in profile.user.posts"
                          v-bind:postPreview="post_prev"></post-preview>
          </b-tab>
          <b-tab title="Komentarze">
            <comment :key="index" v-for="(comment, index) in profile.user.comments"
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
  import Avatar from 'vue-avatar-component'

  export default {
    components: {
      "post-preview": PostPreview,
      "comment": Comment,
      Avatar
    },

    created() {
      this.$store.dispatch('getLoggedUserProfile')
        .then(() => {
          this.description = this.$store.state.currentUser.description;
        });
    },

    data() {
      return {
        description: this.$store.state.currentUser.description,
        isDescriptionEditing: false,
        editButtonText: "Edytuj"
      }
    },

    methods: {
      toggleDescription() {
        this.isDescriptionEditing = !this.isDescriptionEditing;
        if (this.editButtonText === "Edytuj")
          this.editButtonText = "Zakończ edycję"
        else {
          console.log("Zapisuje opis");
          console.log(this.description);
          this.$store.dispatch('updateUserDescription', {
            userPk: this.$store.state.currentUser.pk,
            description: this.description
          }).then(() => {
            console.log("Zakonczono polaczenie pomyslnie")
            alert("Zakonczono edycje!");
          }).catch((error) => {
            console.log(error)
            alert("Nie udalo sie edytowac opisu");
          })

          this.editButtonText = "Edytuj"
        }
      }
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

  .textarea-container, .textarea-container textarea {
    width: 100%;
  }


</style>
