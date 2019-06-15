<template>
  <div>
    <b-row>
      <!-- lewy panel z opisem oferty -->
      <b-col cols="8" class="text-justify">
        <b-row>
          <b-col cols="10" offset="1">
              <h4>
                  {{ jobOffer.title }}
              </h4>
          </b-col>
        </b-row>
        <b-row>
          <b-col cols="10" offset="1">
            Wynagrodzenie:
            {{ jobOffer.salaryMin }}
            -
            {{ jobOffer.salaryMax}}
            PLN
          </b-col>
        </b-row>
        <b-row>
            <b-col cols=11 offset=1>
                <hr>
            </b-col>
        </b-row>
        <b-row>   
          <b-col cols="10" offset="1">
              <h5>Opis</h5>
          </b-col>
        </b-row>
        <b-row>
          <b-col cols="10" offset="1">{{ jobOffer.description }}</b-col>
        </b-row>
        <b-row>
            <b-col cols=11 offset=1>
                <hr>
            </b-col>
        </b-row>
        <b-row>
          <b-col cols="10" offset="1">
              <h5>Wymagania</h5>
          </b-col>
        </b-row>
        <b-row>
          <b-col cols="10" offset="1">{{ jobOffer.requirements }}</b-col>
        </b-row>
      </b-col>

      <!-- prawy panel z przyciskiem Aplikuj -->
      <b-col cols="4" class="border-left">
        <b-row class="mt-1">
          <b-col>Firma</b-col>
        </b-row>
        <b-row class="mt-1">
          <b-col>{{ jobOffer.title }}</b-col>
        </b-row>
        <b-row class="mt-1">
          <b-col>Miejscowosc</b-col>
        </b-row>
        <b-row class="mt-2">
          <b-col cols="12" class="text-center">
            <b-button squared variant="warning" class="w-100">Aplikuj</b-button>
          </b-col>
        </b-row>
      </b-col>
    </b-row>
  </div>
</template>

<script>
export default {
  data() {
    return {};
  },

  created() {},

  computed: {
    jobOffer() {
      return this.$store.state.jobOffers.find(job => {
        return job.pk === this.$route.params.pk;
      });
    },

    isLogged() {
      return this.$store.state.isLogged;
    }
  },

  methods: {}
};
</script>

<style scoped>
</style>
