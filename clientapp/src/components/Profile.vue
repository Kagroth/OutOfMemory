<template>
    <div>
        <b-row>
            <b-col cols=5 class="username">
                Nazwa uzytkownika <br>
                Data dolaczenia: 01-01-2019
            </b-col>
            <b-col cols=5 class="stats">
                Liczba postów: 50 <br>
                Liczba komentarzy: 134
            </b-col>
            <b-col cols=2 class="cvButton text-center" align-self="center">
                <b-button size="sm">Moje CV</b-button>
            </b-col>
        </b-row>
        <b-row>
            <b-col>
                Opis
            </b-col>
        </b-row>
        <b-row>
            <b-col class="mt-5">
                <b-tabs>
                    <b-tab title="Posty">Posty</b-tab>
                    <b-tab title="Komentarze">Komentarze</b-tab>
                </b-tabs>
            </b-col>
        </b-row>
    </div>
</template>

<script>
export default {
    
}
</script>

<style scoped>
.username {
    background-color: lightgreen;
}

.stats {
    background-color: yellow;
}

.cvButton {
    background-color: silver;
}
</style>
