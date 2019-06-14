<template>
  <div class="mb-3">
    <div class="shadow-sm">
      <b-row class="pl-2">
        <b-col cols=8 class="lead"> {{ jobOffer.title }}</b-col>
        <b-col cols=4 class="text-right"> Wynagrodzenie od <b>{{ jobOffer.salaryMin }} PLN</b> - <b>{{jobOffer.salaryMax}} PLN</b></b-col>
      </b-row>
      <b-row class="pl-2">
        <b-col cols=12>
          <!--
          <div>
            {{jobOffer.requirements}}
          </div>
          -->
        </b-col>
      </b-row>
      <b-row>
        <b-col cols=12>
          <!--
          <b-img
            :key="tag"
            v-for="tag in job.tags"
            :src="getImage(tag.tagName)">
          </b-img>
          -->
        </b-col>
      </b-row>
      <b-row class="pl-2">
        <b-col cols=12>
          <small>Autor: {{jobOffer.author}}</small>
        </b-col>
      </b-row>
      <b-row class="pl-2">
        <b-col cols=12>
          <small>{{jobOffer.createDate}}</small>
        </b-col>
      </b-row>
    </div>
  </div>
</template>

<script>
  export default {
    props: ['jobOffer'],

    data() {
      return {        
      }
    },

    methods: {
      mapTagName(tagName) {
        switch (tagName) {
          case "Java":
            return "icons8-java-48"
          case "CSS":
            return "icons8-css3-48"
          case "Javascript":
            return "icons8-javascript-48"
          case "HTML":
            return "icons8-html-5-48"
          case "Spring":
            return "icons8-spring-logo-48"
          default:
            return ""
        }
      },

      /*
      dynamiczne ladowanie image*/
      getImage(tagName) {
        let mappedTag = this.mapTagName(tagName)

        if (mappedTag === "")
          return null

        return require("../assets/" + mappedTag + ".png")
      },
    }
  }
</script>

<style scoped>

</style>
