<template>
  <div>
    <b-row>
      <b-col cols="4" offset="4">
        <b-form>
          <b-form-group label="Nazwa uzytkownika:" label-for="usernameInput">
            <b-form-input
              id="usernameInput"
              v-model="form.username"
              type="text"
              :state="emailState"
              placeholder="Twoja nazwa uzytkownika"
            ></b-form-input>
          </b-form-group>
          <b-form-group label="Haslo:" label-for="passwordInput">
            <b-form-input
              id="passwordInput"
              v-model="form.password"
              type="password"
              placeholder="Haslo"
            ></b-form-input>
          </b-form-group>
          <b-button variant="primary" @click="sendLoginForm">Zaloguj</b-button>
        </b-form>
      </b-col>
    </b-row>
    <b-row>
        <b-col cols=4 offset=4 class="mt-3">
            <p class="small">
                Nie masz konta?
                <router-link to="/register">Zarejestruj się</router-link>
            </p>
        </b-col>
    </b-row>
  </div>
</template>

<script>
import api from "../api.js";

export default {
  data() {
    return {
      form: {
        username: "",
        password: ""
      }
    };
  },

  methods: {
    sendLoginForm(event) {
      event.preventDefault();
      console.log(this.form);
      this.$store.dispatch('loginUser', this.form);
      /*
      this.$http.post(api.getLoginEndpoint(), this.form).then(
        (response) => { 
          console.log(response.data.access);
          if(response.status === 200) {
            localStorage.setItem("token", response.data.access);
            localStorage.setItem("refreshToken", response.data.refresh);
            console.log("Emituje zdarzenie");
            this.$emit('loginEvent');
            alert("zalogowano")
          }
          else {
            alert("bledne dane")
          }

        }, // on success
        (response) => { console.log(response.data); alert("bledne dane") ;} // on fail
      );*/
    }
  },

  /*
  created() {
    localStorage.setItem('token', "");
  },*/

  computed: {
    emailState() {
      /*Walidacja maila */
    },

    passwordState() {
      /*Walidacja hasla
              niekoniecznie potrzebne
            */
    }
  }
};
</script>

<style scoped>
</style>
