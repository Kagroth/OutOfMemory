<template>
    <div class="mb-3">
        <div class="shadow-sm">            
            <b-row class="pl-2">
                <b-col cols=12 class="lead" @click="showDetails"> {{ postPreview.title }}</b-col>
            </b-row>            
            <b-row>
                <b-col cols=8>
                    <b-img
                        :key="tag"
                        v-for="tag in postPreview.tags"
                        :src="getImage(tag.tagName)"
                        @click="getPostsByTag(tag.tagName)"
                        :title="tag.tagName">
                    </b-img>
                </b-col>
                <b-col cols=4>
                    <b-row class="pr-3">
                        <b-col class="text-right">
                            Wyświetleń: {{ postPreview.viewsCount }}                   
                        </b-col>
                    </b-row>
                    <b-row class="pr-3">
                        <b-col class="text-right">
                            Odpowiedzi: {{ postPreview.commentsCount }}
                        </b-col>
                    </b-row>
                </b-col>
            </b-row>
            <b-row class="pl-2">
                <b-col><small>Autor: {{ postPreview.author }}</small></b-col>
            </b-row>
            <b-row class="pl-2">
                <b-col><small>{{ postPreview.createdAt.substring(0, 10) }}</small></b-col>
            </b-row>          
        </div>
    </div>    
</template>

<script>
export default {
    props: ['postPreview'],

    data(){
        return {
        }
    },

    created() {
    },

    methods: {
        mapTagName(tagName) {
            switch(tagName) {
                case "Java":
                    return "Java"
                case "CSS":
                    return "CSS3"
                case "JavaScript":
                    return "JavaScript"
                case "HTML":
                    return "HTML5"
                case "Spring":
                    return "Spring"
                case "Cpp":
                    return "Cpp"
                case "CSharp":
                    return "CSharp"
                case "MATLAB":
                    return "MATLAB"
                case "Perl":
                    return "Perl"
                case "Python":
                    return "Python"
                case "R":
                    return "R"
                case "Ruby":
                    return "Ruby"
                case "SQL":
                    return "SQL"
                case "JSON":
                    return "JSON"
                case "XML":
                    return "XML"
                case "Swift":
                    return "Swift"
                case "C":
                    return "C"
                case "Angular":
                    return "Angular"
                case "Cloud":
                    return "Cloud"
                case "NodeJS":
                    return "NodeJS"
                case "ReactJS":
                    return "ReactJS"
                case "VueJS":
                    return "VueJS"
                default: 
                    return ""
            }    
        },

        /*
        dynamiczne ladowanie image*/
        getImage(tagName) {
            let mappedTag = this.mapTagName(tagName)

            if(mappedTag === "")
                return null
            
            return require("../assets/" + mappedTag + ".png")
        },
        
        showDetails (event) {
            event.preventDefault();
            let pk = this.postPreview.pk;
            console.log("Zmieniam na details!");
            this.$router.push({name: 'PostDetails', params: { pk }});
        },

        getPostsByTag(tagName) {
            event.preventDefault();
            console.log(tagName);
            this.$store.dispatch('getPostsByTag', {
                tagName: tagName
            })
        }
    },
}
</script>

<style scoped>
.cardBadges, .cardAuthor
{
    float: left;
}
</style>
