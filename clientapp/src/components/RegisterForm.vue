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
export default {
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
      console.log(this.form)

      if(this.form.first_name === "" 
         || this.form.last_name === ""
         || this.form.email === ""
         || this.form.username === "") {
           alert("Nie wprowadzono wszystkich danych")
           return;
         }

      if(this.form.password !== this.passwordRepeat
         || this.form.password === ""
         || this.passwordRepeat === "") {
        alert("Hasla sie roznia!")
        return;
      }

      this.$store.dispatch('createUser', this.form).then(message => {
        alert(message)
        
        if(message === 'Użytkownik zostal zarejestrowany') {
          this.$router.push('/login')
      });
    }
  }
}
</script>

<style scoped>

</style>
