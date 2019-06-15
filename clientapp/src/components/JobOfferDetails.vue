<template>
    <div>
        {{ jobOffer }}
    </div>    
</template>

<script>

export default {
    data () {
        return {
        }
    },

    created() {
    },

    computed: {
        jobOffer () {
            return this.$store.state.jobOffers.find(job => {
                return job.pk === this.$route.params.pk
            })
        },

        isLogged () {
            return this.$store.state.isLogged;
        }
    },

    methods: {
    }
}
</script>

<style scoped>
</style>
