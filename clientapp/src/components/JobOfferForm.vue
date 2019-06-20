<template>
  <div>
    <b-form>
      <b-form-group
        id="input-group-1"
        label="Nazwa stanowiska:"
        label-for="input-1"
      >
        <b-form-input
          id="input-1"
          v-model="jobOffer.title"
          required
          placeholder="np. DevOps"
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-2" label="Pensja minimalna:" label-for="input-2">
        <b-form-input
          id="input-2"
          v-model="jobOffer.salaryMin"
          required
          placeholder="np. 1800"
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-3" label="Pensja maksymalna:" label-for="input-3">
        <b-form-input
          id="input-3"
          v-model="jobOffer.salaryMax"
          required
          placeholder="np. 16000"
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-4" label="Opis stanowiska:" label-for="input-4">
        <b-form-textarea
          id="input-4"
          v-model="jobOffer.description"
          required
          placeholder="np. Firma zajnumje się..."
        ></b-form-textarea>
      </b-form-group>

      <b-form-group id="input-group-5" label="Wymagania na stanowisku:" label-for="input-5">
        <b-form-textarea
          id="input-5"
          v-model="jobOffer.requirements"
          required
          placeholder="np. Angielski biznesowy, Java, PSM1"
        ></b-form-textarea>
      </b-form-group>

      <b-form-group id="input-group-6" label="Nazwa firmy:" label-for="input-6">
        <b-form-input
          id="input-6"
          v-model="jobOffer.companyName"
          required
          placeholder="Tu wpisz nazwę firmy"
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-7" label="Adres firmy:" label-for="input-7">
        <b-form-input
          id="input-7"
          v-model="jobOffer.companyLocation"
          required
          placeholder="Tu wpisz adres twojej firmy"
        ></b-form-input>
      </b-form-group>

      <b-button @click="createJobOffer" variant="primary">Stwórz ofertę</b-button>
    </b-form>
    <b-card class="mt-3" header="Form Data Result">
      <pre class="m-0">{{ jobOffer }}</pre>
    </b-card>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        jobOffer: {
          title: "",
          salaryMin: "",
          salaryMax: "",
          description: "",
          requirements: "",
          companyName: "",
          companyLocation: "",
        }
      }
    },
    name: "JobOfferForm",
    methods: {
      createJobOffer() {
        console.log(this.jobOffer);

        if (this.jobOffer.title === ""
          || this.jobOffer.salaryMin === ""
          || this.jobOffer.salaryMax === ""
          || this.jobOffer.description === ""
          || this.jobOffer.requirements === ""
          || this.jobOffer.companyName === ""
          || this.jobOffer.companyLocation === "") {
          alert("Nie wypelniono wszystkich danych");
          return;
        }

        this.$store.dispatch('createJobOffer', this.jobOffer).then(response => {
          alert("Utworzono ofertę pracy")
          this.$router.push("/")
        });
      }
    }
  }
</script>

<style scoped>

</style>
