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
            <!--
            <post-preview :key="post_preview"
              v-for="post_preview in post_previews"
              v-bind:author="post_preview.author"
              v-bind:creationDate="post_preview.creationDate"    
              v-bind:viewsCount="post_preview.viewsCount"
              v-bind:answersCount="post_preview.answersCount"
              v-bind:title="post_preview.title"
              v-bind:tags="post_preview.tags"
          ></post-preview>
          -->
          <post-preview :key="post_preview"
            v-for="post_preview in posts_prevs"
            v-bind:author="post_preview.author"
            v-bind:creationDate="post_preview.createdAt"
            v-bind:viewsCount="post_preview.viewsCount"
            v-bind:answersCount="post_preview.comments.length"
            v-bind:title="post_preview.title"
            v-bind:tags="post_preview.tags">
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

// Tab components
import BTabs from "bootstrap-vue/es/components/tabs/tabs";
import BTab from "bootstrap-vue/es/components/tabs/tab";

// Layout components
import BRow from 'bootstrap-vue/es/components/layout/row';
import BCol from 'bootstrap-vue/es/components/layout/col';

// Button component
import BButton from 'bootstrap-vue/es/components/button/button';

export default {
  components: {
    "post-preview": PostPreview,
    "b-tabs": BTabs,
    "b-tab": BTab,
    'b-row': BRow,
    'b-col': BCol,
    'b-button': BButton
  },

  props: ['post_previews'],
  
  data() {
    return {
      posts_prevs: []
    };
  },

  created() {
    console.log(); 

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
