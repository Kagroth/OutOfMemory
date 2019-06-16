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
        <b-row>
          <b-col cols=11 offset=1>
            <hr>
          </b-col>
            <b-col cols=10 offset=1>
                Liczba wyswietlen: {{ jobOffer.viewsCount }}
            </b-col>
            <b-col cols=10 offset=1>
                Liczba aplikacji: {{ jobOffer.numberOfApplications }}
            </b-col>
        </b-row>
      </b-col>

      <!-- prawy panel z przyciskiem Aplikuj -->
      <b-col cols="4" class="border-left">
        <b-row class="mt-1">
          <b-col>Firma</b-col>
        </b-row>
        <b-row class="mt-1">
          <b-col>{{ jobOffer.companyName }}</b-col>
        </b-row>
        <b-row class="mt-1">
          <b-col>Miejscowosc</b-col>
        </b-row>
        <b-row class="mt-1">
          <b-col>{{ jobOffer.companyLocation }}</b-col>
        </b-row>
        <b-row class="mt-1">
          <b-col>Data</b-col>
        </b-row>
        <b-row class="mt-1">
          <b-col>{{ jobOffer.dateofpost }}</b-col>
        </b-row>
        <b-row class="mt-2">
          <b-col v-if="isLogged" cols="12" class="text-center">
            <div v-if="hasCV">
                <b-button squared variant="warning" class="w-100">Aplikuj</b-button>
            </div>
            <div v-else class="shadow-sm border p-2">
                Aby aplikować, musisz posiadać CV. <br>
                Możesz je utworzyć w panelu zarządzania profilem
            </div>            
          </b-col>
          <b-col v-else cols=12>
              <div class="text-center shadow-sm border p-1">
                  Aby aplikować, musisz się zalogować
              </div>              
          </b-col>
        </b-row>
      </b-col>
    </b-row>
  </div>
</template>

<script>
export default {
  data() {
    return {
        hasCV: ""
    };
  },

  created() {
       this.hasCV = !(this.$store.state.currentUser.user.cv === undefined || // jesli pole cv jest undefined lub null, wtedy hasCV = false
                       this.$store.state.currentUser.user.cv === null) 
     
        console.log(this.hasCV)
        this.$store.dispatch('getJobOfferDetails', this.$route.params.pk)
  },

  computed: {
    jobOffer() {
      return this.$store.state.jobOfferDetails

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
