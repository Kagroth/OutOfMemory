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
              v-for="post_preview in posts_previews"
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
import api from "../api.js";
import PostPreview from "./PostPreview.vue";

export default {
  components: {
    'post-preview': PostPreview
  },

  data() {
    return {

    }
  },

  computed: {
    posts_previews() {
      return this.$store.state.posts_previews;
    }
  },

  created() {
    console.log(); 
    console.log(this.$store);

    this.$http.get(api.getPostEndpoint(), {headers: {Authorization: "Bearer " + localStorage.getItem('token')}}).then(
      // on success
      (response) => {
        console.log(response.data);
        this.posts_prevs = response.data;
      },
      
      // on fail
      (response) => {
        console.log(response.data);
      }
    );
  },

  methods: {

  }

};
</script>
<style scoped>
</style>
