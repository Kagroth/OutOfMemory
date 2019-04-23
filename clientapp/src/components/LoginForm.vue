<template>
  <div>
    <b-row>
      <b-col cols="4" offset="4">
        <b-form>
          <b-form-group label="Email:" label-for="emailInput">
            <b-form-input
              id="emailInput"
              v-model="form.email"
              type="email"
              :state="emailState"
              placeholder="jankowalski@domena.pl"
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
          <b-button variant="primary">Zaloguj</b-button>
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
        email: "",
        password: ""
      }
    };
  },

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
