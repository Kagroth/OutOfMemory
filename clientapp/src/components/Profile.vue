<template>
  <div>
    <b-row align-v="center">
      <b-col>
          <avatar :image="'http://localhost:8000' + profile.avatar" size=200 v-if="profile.avatar != null"></avatar>
          <avatar :fullname="profile.user.username" size='200' v-else></avatar>
      </b-col>
      <b-col>
        <h2> {{ profile.user.username }} </h2>
      </b-col>
    </b-row>
    <hr>
    <b-row>
      <b-col cols=5 class="">
        Liczba postów: {{ profile.user.posts.length }} <br>
        Liczba komentarzy: {{ profile.user.comments.length }}
      </b-col>
    </b-row>
    <b-row class=" mt-1">
      <b-col>
        <hr>
      </b-col>
    </b-row>
    <b-row>
      <b-col class="mt-2">
        {{profile.description}}
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
          <b-tab title="Oferty pracy" v-if="profile.user.jobOffers.length > 0">
            <job-offer :key="index" v-for="(offer, index) in profile.user.jobOffers" v-bind:jobOffer="offer"></job-offer>
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
  import axios from 'axios'
  import JobPreview from "./JobPreview";

  export default {
    components: {
      "post-preview": PostPreview,
      "comment": Comment,
      "job-offer": JobPreview,
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
        editButtonText: "Edytuj",
        selectedImage: null,
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
      },
      onAvatarChange(event){
        console.log(event)
        this.selectedImage = event.target.files[0]
      },
      onUpload(){
        const fd = new FormData();
        fd.append('image',this.selectedImage, this.selectedImage.name)
        this.$store.dispatch('onAvatarUpload', {
          avatar: this.selectedImage,
        })
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
