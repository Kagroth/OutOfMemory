<template>
  <div>
    <b-tabs>
      <b-tab title="Posty">
        <b-row class="mt-2" align-h="start">
          <b-col cols=1>
            <b-button variant="success" to="/post/new">Dodaj</b-button>
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
      <b-tab title="Oferty pracy">Two</b-tab>
    </b-tabs>
  </div>
</template>

<script>
//custom components
import PostPreview from "./PostPreview.vue";

export default {
  components: {
    'post-preview': PostPreview
  },

  computed: {
    post_previews() {
      return this.$store.state.post_previews;
    }
  },

  created() {
    this.$store.dispatch('getAllPostPreviews');
  }
};
</script>

<style scoped>
</style>
