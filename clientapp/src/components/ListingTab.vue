<template>
  <div>
    <b-tabs content-class="mt-3" pills>
      <hr>
      <b-tab active>
        <template slot="title">
          <strong> Posty</strong>
          <b-badge variant="primary" size="sm" to="/post/new" v-if="isLogged">new</b-badge>
        </template>
        <b-row class="mt-2" align-h="start">
          <b-col cols=1>
          </b-col>
        </b-row>
        <b-row class="mt-2">
          <b-col cols=12>
            <post-preview :key="post_preview"
                          v-for="post_preview in post_previews"
                          v-bind:postPreview="post_preview">
            </post-preview>
          </b-col>
        </b-row>
      </b-tab>
      <b-tab>
        <template slot="title">
          <strong> Oferty pracy</strong>
          <b-badge variant="primary" size="sm" to="" v-if="isLogged">new</b-badge>
        </template>
        <b-row class="mt-2" align-h="start">
          <b-col cols=1>
          </b-col>
        </b-row>
        <b-row class="mt-2">
          <b-col cols=12>
            <job-preview>xd
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
      }
    },

    created() {
      this.$store.dispatch('getAllPostPreviews').then(() => {
        console.log("Created")
      });
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
