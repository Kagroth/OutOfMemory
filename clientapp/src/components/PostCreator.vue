<template>
  <div>
    <!--Tytul
            Tagi
    Tresc (wliczajac osadzenie kodu zrodlwego)-->
    <b-row>
      <b-col cols="6" offset="3">
        <b-form>
          <b-form-row>
            <b-col cols="12">
              <b-form-group label="Tytuł pytania:" label-for="postTitle">
                <b-form-input v-model="post.title" id="postTitle" type="text" placeholder="Np. krótka wersja pytania"></b-form-input>
              </b-form-group>
            </b-col>
          </b-form-row>

          <b-form-row>
            <b-col>
              <b-form-group label="Tagi:" label-for="postTags">
                <b-form-input
                  id="postTags"
                  v-model="post.tags"
                  type="text"
                  placeholder="Wpisz tagi, rozdzielone przecinkami"
                ></b-form-input>
              </b-form-group>
            </b-col>
          </b-form-row>

          <b-form-row>
            <b-col cols="9" label-for="postField">Tresc posta:</b-col>
            <b-col cols="3" class="insertCodeCol">
                <b-button id="insertCodeButton" variant="primary" size="sm" disabled>Osadź kod</b-button>
                <b-tooltip target="insertCodeButton" placement="righttop">
                    Wskaż miejsce w polu tekstowym w którym chcesz dodać kod, następnie kliknij ten przycisk
                </b-tooltip>
            </b-col>
          </b-form-row>

          <b-form-row class="mt-1">
            <b-col>
              <b-form-textarea v-model="post.postField" id="postField" rows="15" placeholder="Tu wpisz swoje pytanie"></b-form-textarea>
            </b-col>
          </b-form-row>
        </b-form>
        <b-button variant="success" class="mt-1" @click="createPost">Dodaj</b-button>
      </b-col>
    </b-row>
  </div>
</template>

<script>
// Form components
import BForm from "bootstrap-vue/es/components/form/form";
import BFormGroup from "bootstrap-vue/es/components/form-group/form-group";
import BFormInput from "bootstrap-vue/es/components/form-input/form-input";
import BFormTextarea from "bootstrap-vue/es/components/form-textarea/form-textarea";
import BFormCheckbox from "bootstrap-vue/es/components/form-checkbox/form-checkbox";
import BFormRow from "bootstrap-vue/es/components/form/form-row";
import BButton from "bootstrap-vue/es/components/button/button";


import api from "../api.js";

// Layout components
import BRow from "bootstrap-vue/es/components/layout/row";
import BCol from "bootstrap-vue/es/components/layout/col";

// Tooltip component
import BTooltip from "bootstrap-vue/es/components/tooltip/tooltip";

export default {
  components: {
    "b-form": BForm,
    "b-form-group": BFormGroup,
    "b-form-input": BFormInput,
    "b-form-textarea": BFormTextarea,
    "b-form-checkbox": BFormCheckbox,
    "b-button": BButton,
    "b-row": BRow,
    "b-col": BCol,
    "b-tooltip": BTooltip
  },

  data() {
    return {
      post: {
        title: "",
        postField: "",
        tags: ""
      }
    }    
  },

  methods: {
    createPost() {
      console.log(this.post);
      
      if(this.post.title === ""
         || this.post.postField === ""
         || this.post.tags === "") {
           alert("Nie wypelniono wszystkich danych");
           return;
         }

      this.$http.post(api.getCreatePostEndpoint(), this.post, {headers: {Authorization: "Bearer " + localStorage.getItem('token')}} ).then(
        (response) => {
          console.log(response.body);
          alert("Pomyslnie dodano post");
        },

        (response) => {
          console.log(response.body);
          alert("Nie udalo sie dodac postu");
        }
      );
    }
  }
};
</script>


<style scoped>
.insertCodeCol{
    text-align: right;
}
</style>
