<template>
  <div class="mb-3">
    <div class="shadow-lg">
      <b-row class="px-2">
        <b-col cols=8 class="lead" @click="showDetails"> {{ jobOffer.title }}</b-col>
        <b-col cols=4 class="text-right">
          <b-row>
            <b-col cols=12 class="text-right">
              Wynagrodzenie od <b>{{ jobOffer.salaryMin }} PLN</b> - <b>{{jobOffer.salaryMax}} PLN</b>
            </b-col>
          </b-row>
          <b-row v-if="jobOffer.user == profile">
            <b-col cols=12 class="text-right">
              <b-button size="sm" @click="editJobOffer">Edytuj</b-button>
            </b-col>
          </b-row>
        </b-col>
      </b-row>
      <b-row class="px-2">
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
      <b-row class="px-2">
        <b-col cols=12>
          <small>Autor: {{jobOffer.user}}</small>
        </b-col>
      </b-row>
      <b-row class="px-2">
        <b-col cols=12>
          <small>{{jobOffer.createdAt.substring(0,10)}}</small>
        </b-col>
      </b-row>
    </div>
  </div>
</template>

<script>
  export default {
    props: ['jobOffer'],

    data() {
      return {}
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

      showDetails(event) {
        console.log(this.jobOffer.pk)
        console.log(this.jobOffer)
        event.preventDefault();
        let pk = this.jobOffer.pk;
        console.log("Zmieniam na Job Offer details");
        this.$router.push({name: 'JobOfferDetails', params: {pk}});
      },

      editJobOffer(event) {
        console.log(this.jobOffer.pk)
        console.log(this.jobOffer)
        event.preventDefault();
        let pk = this.jobOffer.pk;
        console.log("Zmieniam na Job Offer Edit Form");
        this.$router.push({name: 'JobOfferEdit', params: {pk}});
      },
    },
    computed: {
      profile() {
        return this.$store.state.username;
      }
    },
  }
</script>

<style scoped>

</style>
