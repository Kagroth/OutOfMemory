<template>
  <div>
    <b-tabs content-class="mt-3" pills>
      <hr>
      <b-tab active>
        <template slot="title">
          <strong>Posty</strong>         
        </template>
        <b-row class="mt-2" align-h="start">
          <b-col cols=1>
            <b-button variant="primary" size="sm" to="/post/new" v-if="isLogged">Dodaj</b-button>
          </b-col>
        </b-row>
        <b-row class="mt-3">
          <b-col cols=12>
            <post-preview :key="index"
                          v-for="(post_preview, index) in post_previews"
                          v-bind:postPreview="post_preview">
            </post-preview>
          </b-col>
        </b-row>
      </b-tab>
      <b-tab>
        <template slot="title">
          <strong> Oferty pracy</strong>
        </template>
        <b-row class="mt-2" align-h="start">
          <b-col cols=1>
            <b-button variant="primary" size="sm" to="/job/new" v-if="isLogged">Dodaj</b-button>
          </b-col>
        </b-row>
        <b-row class="mt-2">
          <b-col cols=12>
            <job-preview :key="index"
                         v-for="(jobOffer, index) in jobOffers"
                         v-bind:jobOffer="jobOffer">
            </job-preview>
          </b-col>
        </b-row>
      </b-tab>
    </b-tabs>
  </div>
</template>

<script>
  //custom components
  import PostPreview from "./PostPreview.vue";
  import JobPreview from "./JobPreview.vue";

  export default {
    components: {
      'post-preview': PostPreview,
      'job-preview': JobPreview
    },

    computed: {
      isLogged() {
        return this.$store.state.isLogged;
      },

      post_previews() {
        return this.$store.state.post_previews;
      },

      jobOffers() {
        return this.$store.state.jobOffers;
      }
    },

    created() {
      this.$store.dispatch('getAllPostPreviews').then(() => {
        console.log("Created")
      });

      this.$store.dispatch('getAllJobOffers')
    }
  };
</script>

<style>
  .nav-pills .nav-link.active, .nav-pills .show > .nav-link {
    background-color: #ff9b04;
  }

  .orangeText {
    color: orange;
  }
</style>
