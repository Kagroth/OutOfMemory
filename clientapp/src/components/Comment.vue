<template>
    <b-col cols=10 offset=1 class="border">
        <b-row>
            <b-col class="text-justify">{{ comment.commentField }}</b-col>
            <b-col cols=1 class="text-center mt-1">
                <b-button variant="success" size="sm" class="w-100">+</b-button><br>
                <span>15</span><br>
                <b-button variant="danger" size="sm" class="w-100">-</b-button>                
            </b-col>
        </b-row>
        <b-row class="mt-1">
            <b-col>Autor: {{ comment.author }} <br> {{ comment.createdAt.substring(0, 10) }}</b-col>
        </b-row>
    </b-col>
</template>

<script>
export default {
    props: ['comment']
}
</script>

<style scoped>

</style>
