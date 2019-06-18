<template>
  <div>
    <b-row class="mt-1">
      <b-col cols=10><h4>{{ post.title }}</h4></b-col>
      <b-col cols=2 class="text-right">{{ post.author }}<br>{{ post.createdAt.substr(0, 10) }}</b-col>
    </b-row>
    <b-row>
      <b-col>
        <b-img
          width="25"
          height="25"
          :key="index"
          v-for="(tag, index) in post.tags"
          :src="getImage(tag.tagName)"
          @click="getPostsByTag(tag.tagName)"
          :title="tag.tagName">
        </b-img>
      </b-col>
      <!--      <b-col offset=1>-->
      <!--        <b-badge variant="primary" class="mr-1" :key="tag" v-for="tag in post.tags"> {{ tag.tagName }}</b-badge>-->
      <!--      </b-col>-->
    </b-row>
    <b-row class="mt-3">
      <b-col class="text-justify">{{ post.postField }}</b-col>
    </b-row>
    <div class="commentSection mt-5">
      <b-row>
        <b-col>
          <h5>Odpowiedzi:</h5>
        </b-col>
      </b-row>
      <b-row>
        <b-col v-if="isLogged">
          <b-button v-b-toggle.addCommentFormCollapse variant="info" class="mb-3" size="sm"
                    @click="onAddCommentCollapseHandler">{{
            collapseButtonText }}
          </b-button>
          <b-collapse id="addCommentFormCollapse">
            <b-form class="mb-2">
              <b-form-textarea rows="10" v-model="commentField" placeholder="Tresc komentarza"/>
            </b-form>
            <b-button variant="success" size="sm" class="mb-3" @click="addComment">Wyślij</b-button>
          </b-collapse>
        </b-col>
      </b-row>

      <b-row>
        <b-col cols="12">
          <comment :key="index" v-for="(comment, index) in post.comments" v-bind:comment="comment"/>
        </b-col>
      </b-row>

    </div>
  </div>
</template>

<script>
  import Comment from './Comment'

  export default {
    components: {
      'comment': Comment
    },

    data() {
      return {
        collapseButtonText: "Dodaj komentarz",
        commentField: ""
      }
    },

    created() {
      console.log(this.$route);
      this.$store.dispatch('getPostDetails', this.$route.params.pk)
        .then((responseData) => {
          if (responseData.message === "Nie ma takiego posta!") {
            alert("Taki post nie istnieje");
            return;
          }
        })
        .catch(() => {
        });
    },

    computed: {
      post() {
        return this.$store.state.postDetails;
      },

      isLogged() {
        return this.$store.state.isLogged;
      }
    },

    methods: {
      mapTagName(tagName) {
        return tagName
      },

      /*
      dynamiczne ladowanie image*/
      getImage(tagName) {
        let mappedTag = this.mapTagName(tagName)

        if (mappedTag === "")
          return null

        return require("../assets/" + mappedTag + ".png")
      },
      onAddCommentCollapseHandler() {
        if (this.collapseButtonText === "Dodaj komentarz") {
          this.collapseButtonText = "Ukryj"
        } else {
          this.collapseButtonText = "Dodaj komentarz"
        }
      },

      addComment() {
        this.$store.dispatch('addComment', {
          postPk: this.post.pk,
          comment: this.commentField
        }).then(() => {
          alert("Komentarz zostal dodany!")
          this.commentField = "";
        }).catch(() => {
          alert("Nie udalo sie dodac komentarza")
        })
      }
    }
  }
</script>

<style scoped>
</style>
