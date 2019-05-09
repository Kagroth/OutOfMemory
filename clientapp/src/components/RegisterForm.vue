<template>
  <div>
      <b-row>
          <b-col cols=4 offset=4>
              <b-form>
                  <b-form-group label="Imię:" label-for="firstNameInput">
                      <b-form-input
                        id="firstNameInput"
                        type="text"
                        placeholder="Jan"
                        v-model="form.first_name"
                      >                          
                      </b-form-input>
                  </b-form-group>
                  <b-form-group label="Nazwisko:" label-for="lastNameInput">
                      <b-form-input
                        id="lastNameInput"
                        type="text"
                        placeholder="Kowalski"
                        v-model="form.last_name"
                      >                          
                      </b-form-input>
                  </b-form-group>
                  <b-form-group label="Email:" label-for="emailInput">
                      <b-form-input
                        id="emailInput"
                        type="email"
                        placeholder="jankowalski@domena.pl"
                        v-model="form.email"
                      >                          
                      </b-form-input>
                  </b-form-group>
                  <b-form-group label="Username:" label-for="usernameInput">
                      <b-form-input
                        id="usernameInput"
                        type="text"
                        placeholder="Twoja nazwa uzytwkonika"
                        v-model="form.username"
                      >                          
                      </b-form-input>
                  </b-form-group>
                  <b-form-group label="Hasło:" label-for="passwordInput">
                      <b-form-input
                        id="passwordInput"
                        type="password"
                        placeholder=""
                        v-model="form.password"
                      >                          
                      </b-form-input>
                  </b-form-group>
                  <b-form-group label="Powtórz hasło:" label-for="passwordRepeatInput">
                      <b-form-input
                        id="passwordRepeatInput"
                        type="password"
                        placeholder=""
                        v-model="passwordRepeat"
                      >                          
                      </b-form-input>
                  </b-form-group>
                  <b-button variant="primary" @click="sendRegisterForm"> Załóż konto</b-button>
              </b-form>
          </b-col>
      </b-row>
  </div>  
</template>

<script>
import api from "../api.js";

// Form components
import BForm from "bootstrap-vue/es/components/form/form";
import BFormGroup from "bootstrap-vue/es/components/form-group/form-group";
import BFormInput from "bootstrap-vue/es/components/form-input/form-input";
import BFormCheckbox from "bootstrap-vue/es/components/form-checkbox/form-checkbox";
import BButton from "bootstrap-vue/es/components/button/button";

// Layout components
import BRow from "bootstrap-vue/es/components/layout/row";
import BCol from "bootstrap-vue/es/components/layout/col";

export default {
    components: {
    "b-form": BForm,
    "b-form-group": BFormGroup,
    "b-form-input": BFormInput,
    "b-form-checkbox": BFormCheckbox,
    "b-button": BButton,
    "b-row": BRow,
    "b-col": BCol
  },

  data() {
      return {
        form: {
          first_name: "",
          last_name: "",
          email: "",
          username: "",
          password: ""          
        },
        passwordRepeat: ""
      }
  },

  methods: {
    sendRegisterForm(event) {
      this.$http.post(api.getRegisterEndpoint(), this.form).then(
        (response) => { console.log(response.data); alert("Zarejestrowano") }, // on success
        (response) => { console.log(response.data); alert("Nie udalo sie zarejestrowac") } // on fail
      );
    }
  }
}
</script>

<style scoped>

</style>
