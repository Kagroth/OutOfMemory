<template>
    <div>
        <!-- Brak CV, mozliwosc jego utworzenia -->
        <div v-if="!hasCV && !isCreating">
            <b-row>
                <b-col class="text-center">
                    Nie masz jeszcze CV
                </b-col>
            </b-row>
            <b-row class="mt-2" align-h="center">
                <b-col cols=4 class="text-center">
                    <b-button variant="success" size="sm" @click="showCreatorHandler">Nowe CV</b-button>
                </b-col>
            </b-row>
        </div>
        <!-- Jest CV, wyświetlenie go i umożliwienie edycji -->
        <div v-else>
            <h3>Twoje CV</h3>
            <b-row v-for="experience in experienceCV" :key="experience">
                <b-col> {{ experience.startDate }} </b-col>
                <b-col> {{ experience.endDate }} </b-col>
                <b-col> {{ experience.company }} </b-col>
                <b-col> {{ experience.description }} </b-col>                
            </b-row>
            <b-row v-for="skill in skillsCV" :key="skill">
                <b-col> {{ skill.name }} </b-col>
                <b-col> {{ skill.level }} </b-col>
            </b-row>
        </div>
        <!-- CV kreator -->
        <div v-if="showCreator">
            <b-row>
                <b-col cols=12>
                    <b-form>
                        <b-form-group label="Twoje doświadczenie">                        
                            <div v-for="(exp, index) in experiences" :key="(exp, index)" class="mt-2">
                                <b-row>
                                    <b-col cols=11>
                                        <span>Wpis nr: {{ index + 1}}</span>
                                    </b-col>
                                    <b-col cols=1>
                                        <b-button variant="danger" size="sm" @click="removeExperience(index)">Usuń</b-button>
                                    </b-col>
                                </b-row>                            
                                <b-form-input v-model="exp.startDate" :type="date" placeholder="MM-RRRR"></b-form-input>
                                <b-form-input v-model="exp.endDate" :type="date" placeholder="MM-RRRR"></b-form-input>                                
                                <b-form-input v-model="exp.company" :type="text" placeholder="Nazwa firmy"></b-form-input>
                                <b-form-textarea v-model="exp.description" placeholder="Opisz czym się zajmowałeś"></b-form-textarea>                            
                            </div>
                            <b-button variant="primary" size="sm" @click="addNewExperience" class="mt-2">Dodaj nowy wpis</b-button>
                        </b-form-group>
                        <hr>
                        <b-form-group label="Twoje umiejętności:">
                            <div v-for="(skill, index) in skills" :key="(skill, index)" class="mt-2">
                                <b-row>
                                    <b-col cols=11>
                                        <span>Wpis nr: {{ index + 1}}</span>
                                    </b-col>
                                    <b-col cols=1>
                                        <b-button variant="danger" size="sm" @click="removeSkill(index)">Usuń</b-button>
                                    </b-col>                           
                                </b-row>
                                <b-form-input v-model="skill.name" :type="text"></b-form-input>                        
                                <b-form-select v-model="skill.level" :options="levels"></b-form-select>
                            </div>
                            <b-button variant="primary" size="sm" @click="addNewSkill" class="mt-2">Dodaj nową umiejętność</b-button>
                        </b-form-group>
                    </b-form>
                </b-col>
            </b-row>  
            <b-row>
                <b-col>
                    <hr>
                    <b-button variant="success" size="sm" @click="saveCV">Zapisz</b-button>
                </b-col>
            </b-row>
        </div>       
    </div>    
</template>

<script>
export default {
    data() {
        return {
            hasCV: "",
            showCreator: false,
            isCreating: false,
            isEditing: false,
            skills: [],
            experiences: [],
            levels: [
                'Junior',
                'Regular',
                'Advanced',
                'Master'
            ]
        }
    },

    created(){
        /*
            Inicjalizacja parametrow: hasCV, showCreator, isCreating, isEditing
        */
        console.log(this.$store.state.currentUser.user.cv)
        this.hasCV = this.$store.state.currentUser.user.cv !== undefined // jesli pole cv jest undefined, wtedy hasCV = false
        console.log(this.hasCV)
        this.isCreating = false
        this.showCreator = false
        this.isEditing = false;
    },

    methods: {
        showCreatorHandler() {
            this.showCreator = true;
            this.isCreating = true;
        },

        addNewExperience() {
            this.experiences.push({
                startDate: "",
                endDate: "",
                company: "",
                description: ""
            })
        },

        addNewSkill() {
            this.skills.push({
                name: "",
                level: ""
            })
        },

        removeExperience(index) {
            this.experiences.splice(index, 1)
        },

        removeSkill(index) {
            this.skills.splice(index, 1)
        },

        saveCV() {
            /*
                Zapis CV do bazy
            */
           // z kazdego elementu tablicy this.skills, utworz String postaci 'name level' i ze wszytkich tych stringow utworz 1 string
           // ktorego elementy oddzielone sa przecinkami
           let skills = this.skills.map(skill => skill.name + " " + skill.level).join(",")
           
           // z kazdego elementu tablicy this.experiences utworz String postaci 'startDate endDate company description'
           // i ze wszytkich tych stringow utworz 1 string ktorego elementy oddzielone sa przecinkami
           let experiences = this.experiences.map(experience => {
               let expString = "";
               for(let property of ['startDate', 'endDate', 'company', 'description']) {
                   expString += experience[property] + " "
               }
               return expString
           }).join(",")
           
           console.log(skills)
           console.log(experiences)
           
           this.$store.dispatch('createCV', {
               skills: skills,
               experiences: experiences
           }).then(() => {
               console.log("CV zostalo utworzone")
           })
        }
    },

    computed: {
        // wyswietlenie wpisow cv wymaga jego konwersji stringa na tablice
        experienceCV() {
            if(this.hasCV) {
                // mapowanie stringa na tablice obiektow reprezentujacych wpis w cv
                let experiencesArray = this.$store.state.currentUser.user.cv.experience.trim().split(',')

                experiencesArray = experiencesArray.map(experience => {
                    let exp = experience.split(" ")
                    
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
