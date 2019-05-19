<template>
    <b-col cols=10 offset=1 class="border">
        <b-row>
            <b-col class="text-justify">{{ comment.commentField }}</b-col>
            <b-col cols=1 class="text-center mt-1" v-if="isLogged">
                <b-button variant="success" size="sm" class="w-100" @click="rateComment(1)">+</b-button><br>
                <span> {{ comment.rate }} </span><br>
                <b-button variant="danger" size="sm" class="w-100" @click="rateComment(-1)">-</b-button>                
            </b-col>
            <b-col cols=1 v-else class="text-center mt-1">
                <span> {{ comment.rate }} </span>
            </b-col>
        </b-row>
        <b-row class="mt-1">
            <b-col>Autor: {{ comment.author }} <br> {{ comment.createdAt.substring(0, 10) }}</b-col>
        </b-row>
    </b-col>
</template>

<script>
export default {
    props: ['comment'],

    computed: {
        isLogged () {
            return this.$store.state.isLogged;
        }
    },

    methods: {
        rateComment (param) {             
            console.log(param);
            console.log(this.comment.pk);

            this.$store.dispatch('rateComment', {
                commentPk: this.comment.pk,
                rate: param
            }).then(
                () => {console.log("Dodano ocene!");}
            ).catch(
                () => {console.log("Niedodano oceny");}
            );
        }
    }
}
</script>

<style scoped>

</style>
