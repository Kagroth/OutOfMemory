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
      <b-col>
        <b-form>
          <b-form-group id="input-group-1" label="Wgraj własny avatar:" label-for="input-1">
            <b-form-file
              v-model="file"
              :state="Boolean(file)"
              placeholder="Choose a file..."
              drop-placeholder="Drop file here..."
              @change="onAvatarChange"
            ></b-form-file>
          </b-form-group>
          <b-button @click="onUpload" size="sm" >Zatwierdź</b-button>
        </b-form>
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
            <post-preview :key="post_prev" v-for="post_prev in profile.user.posts"
                          v-bind:postPreview="post_prev"></post-preview>
          </b-tab>
          <b-tab title="Komentarze">
            <comment :key="comment" v-for="comment in profile.user.comments"
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
  import axios from 'axios'

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
          avatar: fd,
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
