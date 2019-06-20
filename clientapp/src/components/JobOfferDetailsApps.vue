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
          <b-col>Firma:</b-col>
        </b-row>
        <b-row class="mt-1">
          <b-col><b>{{ jobOffer.companyName }}</b></b-col>
        </b-row>
        <b-row class="mt-1">
          <b-col>Miejscowosc:</b-col>
        </b-row>
        <b-row class="mt-1">
          <b-col><b>{{ jobOffer.companyLocation }}</b></b-col>
        </b-row>
        <b-row class="mt-1">
          <b-col>Data:</b-col>
        </b-row>
        <b-row class="mt-1">
          <b-col><b>{{ jobOffer.createdAt.substring(0,10) }}</b></b-col>
        </b-row>        
      </b-col>
    </b-row>
    <b-row>
        <b-col cols=11 offset=1>
            <hr>
        </b-col>
    </b-row>
    <b-row v-for="(app, index) in jobOffer.applications" :key="index" class="mt-1">        
        <b-col cols=2 offset=1>
            {{ app.cv.user }}
        </b-col>
        <b-col cols=9 class="text-right">
            <b-button size="sm" @click="showCV(app.cv.user)">Pokaz CV</b-button>
        </b-col>
        <b-col cols=11 offset=1>
            <hr>
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
      console.log(this.$store.state.currentUser.user.cv)
      this.hasCV = !(this.$store.state.currentUser.user.cv === undefined || // jesli pole cv jest undefined lub null, wtedy hasCV = false
        this.$store.state.currentUser.user.cv === null)

      console.log(this.hasCV)
      this.$store.dispatch('getJobOfferDetailsWithApps', {offerPk: this.$route.params.pk})
    },

    methods: {
      applyForOffer(event) {
        event.preventDefault();
        this.$store.dispatch('applyForOffer', {offerPk: this.$route.params.pk}).then(message => {
          alert(message)
        })
      },

      showCV(username) {
          this.$router.push({name: 'CVDetails', params: {username: username}})
      }
    },

    computed: {
      jobOffer() {
        return this.$store.state.jobOfferDetails
      },

      isLogged() {
        return this.$store.state.isLogged;
      }
    },
  };
</script>

<style scoped>
</style>
