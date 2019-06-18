<template>
  <div>
    <b-row align-v="center">
      <b-col cols=1>
        <h3>
          <avatar :image="'http://localhost:8000' + profile.avatar" :size=48 v-if="profile.avatar != null"></avatar>
          <avatar :fullname="profile.user.username" :size=48 v-else></avatar>          
        </h3>
      </b-col>
      <b-col>
        <h4> {{ profile.user.username }} </h4>
      </b-col>
    </b-row>
    <b-row>
        <!--
      <b-col cols=5 class="">
        Liczba postów: {{ profile.user.posts.length }} <br>
        Liczba komentarzy: {{ profile.user.comments.length }}
      </b-col>
      -->
      <b-col cols=5></b-col>
      <b-col cols=2 class=" text-right" align-self="center">
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
      </b-col>
      <b-col class="mt-2">
                <span>
                    {{ profile.description }}
                </span>
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
      this.$store.dispatch('getProfile', {username: this.$route.params.username})
        .then(profile => {
          this.profile = profile 
        });
    },

    data() {
      return {
        profile: {}
      }
    },

    methods: {
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
