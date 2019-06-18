<template>
    <div>        
        <!-- Jest CV, wyświetlenie go i umożliwienie edycji -->
        <div>
            <div>
                <b-row>
                    <b-col><h3>CV użytkownika {{ cv.user }}</h3></b-col>
                </b-row>
                <b-row>
                    <b-col>
                        Kontakt: {{ cv.email }}
                    </b-col>
                </b-row>
                <hr>
                <div>
                    <b-row>
                        <b-col cols=8>
                            <h4>Doświadczenie: </h4>
                            <b-row>
                                <b-col cols=2><h5>Od</h5></b-col>
                                <b-col cols=2><h5>Do</h5></b-col>
                                <b-col cols=8><h5>Firma i opis</h5></b-col>
                            </b-row>
                            <b-row v-for="(experience, index) in this.cv.experience" :key="index" class="mt-3">
                                <b-col cols=2> {{ experience.startDate }} </b-col>
                                <b-col cols=2> {{ experience.endDate }} </b-col>
                                <b-col cols=8> <span class="font-weight-bold">{{ experience.company }} </span><br> {{ experience.description }} </b-col>           
                            </b-row>
                        </b-col>

                        <b-col cols=4 class="border-left">
                            <h4>Umiejętności: </h4>
                            <b-row>
                                <b-col cols=6 class="text-center"><h5>Umiejętność</h5></b-col>
                                <b-col cols=6 class="text-center"><h5>Poziom</h5></b-col>
                            </b-row>
                            <b-row v-for="(skill, index) in this.cv.skills" :key="index">
                                <b-col cols=6 class="text-center"> {{ skill.name }} </b-col>
                                <b-col cols=6 class="text-center"> {{ skill.level }} </b-col>
                            </b-row>
                        </b-col>
                    </b-row>                   
                </div>  
            </div>                 
        </div>      
    </div>    
</template>

<script>
export default {
    data() {
        return {
            cv: {}
        }
    },

    created(){
        this.$store.dispatch('getUserCV', {username: this.$route.params.username}).then(data => {
            console.log(data)
            this.cv = data
            this.cv.experience = this.deserializeExperienceCV()
            this.cv.skills = this.deserializeSkillsCV()
            console.log(this.cv)
        })
    },

    methods: {
        deserializeExperienceCV() {
            if(this.cv.experience !== "") {
                let experiencesArray = this.cv.experience.trim().split(';')

                experiencesArray = experiencesArray.map(experience => {
                    let exp = experience.split(",")
                    
                    return {
                        startDate: exp[0],
                        endDate: exp[1],
                        company: exp[2],
                        description: exp[3],                        
                    }
                })

                return experiencesArray
            }
            else 
                return ""
        },

        deserializeSkillsCV() {
            if(this.cv.skills !== "") {
                let skillsArray = this.cv.skills.trim().split(',')

                skillsArray = skillsArray.map(skill => {
                    let sk = skill.split(" ")
                    
                    return {
                        name: sk[0],
                        level: sk[1]                      
                    }
                })

                return skillsArray
            }
            else
                return ""
        }
    },

    computed: {
        // wyswietlenie wpisow cv wymaga jego konwersji stringa na tablice
        experienceCV() {
            if(this.hasCV) {
                // mapowanie stringa na tablice obiektow reprezentujacych wpis w cv
                let experiencesArray = this.$store.state.currentUser.user.cv.experience.trim().split(';')

                experiencesArray = experiencesArray.map(experience => {
                    let exp = experience.split(",")
                    
                    return {
                        startDate: exp[0],
                        endDate: exp[1],
                        company: exp[2],
                        description: exp[3],                        
                    }
                })

                return experiencesArray
            }
            
            return ""
        },

        // wyswietlenie umiejetnosci w cv wymaga jego konwersji stringa na tablice
        skillsCV() {
            if(this.hasCV) {
                let skillsArray = this.$store.state.currentUser.user.cv.skills.trim().split(',')

                skillsArray = skillsArray.map(skill => {
                    let sk = skill.split(" ")
                    
                    return {
                        name: sk[0],
                        level: sk[1]                      
                    }
                })

                return skillsArray
            }
            
            return ""
        }
    }
}
</script>

<style scoped>

</style>
