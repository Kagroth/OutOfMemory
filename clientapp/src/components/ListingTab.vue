<template>
  <div>
    <b-tabs>
      <b-tab title="Posty">
        <post-preview 
            v-for="post_preview in post_previews"
            v-bind:author="post_preview.author"
            v-bind:creationDate="post_preview.creationDate"    
            v-bind:viewsCount="post_preview.viewsCount"
            v-bind:answersCount="post_preview.answersCount"
            v-bind:title="post_preview.title"
            v-bind:tags="post_preview.tags"
        ></post-preview>
      </b-tab>
      <b-tab title="Oferty pracy">Two</b-tab>
    </b-tabs>
  </div>
</template>
<script>
//custom components
import PostPreview from "./PostPreview.vue";

// Tab components
import BTabs from "bootstrap-vue/es/components/tabs/tabs";
import BTab from "bootstrap-vue/es/components/tabs/tab";

export default {
  components: {
    "post-preview": PostPreview,
    "b-tabs": BTabs,
    "b-tab": BTab
  },

  props: ['post_previews'],
  
  data() {
    return {
    };
  }
};
</script>
<style scoped>
</style>
