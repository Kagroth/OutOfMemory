<template>
    <div>        
        <!-- Jest CV, wyświetlenie go i umożliwienie edycji -->
        <div v-if="hasCV">
            <!-- CV edytor -->   
            <div v-if="isEditing">
                <b-row>
                    <b-col cols=10 offset=1>
                        <b-form>
                            <b-form-group label="Twoje doświadczenie">
                                <b-form-row v-for="(exp, index) in experiences" :key="(exp, index)" class="border mt-3 shadow-sm">
                                    <b-col cols=11 class="mt-2">
                                        <span>Wpis nr: {{ index + 1}}</span>
                                    </b-col>
                                    <b-col cols=1 class="mt-2">
                                        <b-button variant="danger" size="sm" @click="removeExperience(index)">Usuń</b-button>
                                    </b-col>
                                    <b-col cols=12>
                                        <b-row class="mt-1">
                                            <b-col cols=3>
                                                <b-form-input v-model="exp.startDate" :type="date" placeholder="MM-RRRR"></b-form-input>
                                            </b-col>    
                                            <b-col cols=3>
                                                <b-form-input v-model="exp.endDate" :type="date" placeholder="MM-RRRR"></b-form-input>
                                            </b-col>
                                            <b-col cols=6>
                                                <b-form-input v-model="exp.company" :type="date" placeholder="Nazwa firmy"></b-form-input>
                                            </b-col>                                          
                                        </b-row>
                                        <b-row class="mt-2">
                                            <b-col cols=12>
                                                <b-form-textarea v-model="exp.description" placeholder="Opisz czym się zajmowałeś" class="mb-3"></b-form-textarea>
                                            </b-col>
                                        </b-row>
                                    </b-col>
                                </b-form-row>
                                <b-button variant="primary" size="sm" @click="addNewExperience" class="mt-2">Dodaj nowy wpis</b-button>
                            </b-form-group>
                            <hr>
                            <b-form-group label="Twoje umiejętności:">
                                <b-form-row v-for="(skill, index) in skills" :key="(skill, index)" class="border mt-3 shadow-sm">
                                    <b-col cols=11 class="mt-2">
                                        <span>Wpis nr: {{ index + 1}}</span>
                                    </b-col>
                                    <b-col cols=1 class="mt-2">
                                        <b-button variant="danger" size="sm" @click="removeSkill(index)">Usuń</b-button>
                                    </b-col>
                                    <b-col cols=12 class="mt-2 mb-3">
                                        <b-row>
                                            <b-col cols=6>
                                                <b-form-input v-model="skill.name" :type="text" placeholder="Nazwa technologii"></b-form-input>
                                            </b-col>
                                            <b-col cols=6>
                                                <b-form-select v-model="skill.level" :options="levels"></b-form-select>
                                            </b-col>
                                        </b-row>
                                    </b-col>
                                </b-form-row>
                                <b-button variant="primary" size="sm" @click="addNewSkill" class="mt-2">Dodaj nową umiejętność</b-button>
                            </b-form-group>
                        </b-form>
                    </b-col>
                </b-row>  
                <b-row>
                    <b-col cols=10 offset=1>
                        <hr>
                        <b-button variant="success" size="sm" @click="saveCV">Zapisz</b-button>
                    </b-col>
                </b-row>
            </div>
            <div v-else>
                <b-row>
                    <b-col><h3>Twoje CV</h3></b-col>
                    <b-col class="text-right">
                        <b-button variant="primary" size="sm" @click="showEditorHandler">Edytuj</b-button>
                        <b-button variant="danger" size="sm" @click="deleteCV">Usuń</b-button>
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
                            <b-row v-for="(experience, index) in experienceCV" :key="index" class="mt-3">
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
                            <b-row v-for="(skill, index) in skillsCV" :key="index">
                                <b-col cols=6 class="text-center"> {{ skill.name }} </b-col>
                                <b-col cols=6 class="text-center"> {{ skill.level }} </b-col>
                            </b-row>
                        </b-col>
                    </b-row>                   
                </div>  
            </div>                 
        </div>
        <!-- Brak CV, mozliwosc jego utworzenia -->
        <div v-else>
            <!-- CV kreator -->
            <div v-if="isCreating">
                <b-row>
                    <b-col cols=10 offset=1>
                        <b-form>
                            <b-form-group label="Twoje doświadczenie">
                                <b-form-row v-for="(exp, index) in experiences" :key="(exp, index)" class="border mt-3 shadow-sm">
                                    <b-col cols=11 class="mt-2">
                                        <span>Wpis nr: {{ index + 1}}</span>
                                    </b-col>
                                    <b-col cols=1 class="mt-2">
                                        <b-button variant="danger" size="sm" @click="removeExperience(index)">Usuń</b-button>
                                    </b-col>
                                    <b-col cols=12>
                                        <b-row class="mt-1">
                                            <b-col cols=3>
                                                <b-form-input v-model="exp.startDate" :type="date" placeholder="MM-RRRR"></b-form-input>
                                            </b-col>    
                                            <b-col cols=3>
                                                <b-form-input v-model="exp.endDate" :type="date" placeholder="MM-RRRR"></b-form-input>
                                            </b-col>
                                            <b-col cols=6>
                                                <b-form-input v-model="exp.company" :type="date" placeholder="Nazwa firmy"></b-form-input>
                                            </b-col>                                          
                                        </b-row>
                                        <b-row class="mt-2">
                                            <b-col cols=12>
                                                <b-form-textarea v-model="exp.description" placeholder="Opisz czym się zajmowałeś" class="mb-3"></b-form-textarea>
                                            </b-col>
                                        </b-row>
                                    </b-col>
                                </b-form-row>
                                <b-button variant="primary" size="sm" @click="addNewExperience" class="mt-2">Dodaj nowy wpis</b-button>
                            </b-form-group>
                            <hr>
                            <b-form-group label="Twoje umiejętności:">
                                <b-form-row v-for="(skill, index) in skills" :key="(skill, index)" class="border mt-3 shadow-sm">
                                    <b-col cols=11 class="mt-2">
                                        <span>Wpis nr: {{ index + 1}}</span>
                                    </b-col>
                                    <b-col cols=1 class="mt-2">
                                        <b-button variant="danger" size="sm" @click="removeSkill(index)">Usuń</b-button>
                                    </b-col>
                                    <b-col cols=12 class="mt-2 mb-3">
                                        <b-row>
                                            <b-col cols=6>
                                                <b-form-input v-model="skill.name" :type="text" placeholder="Nazwa technologii"></b-form-input>
                                            </b-col>
                                            <b-col cols=6>
                                                <b-form-select v-model="skill.level" :options="levels"></b-form-select>
                                            </b-col>
                                        </b-row>
                                    </b-col>
                                </b-form-row>
                                <b-button variant="primary" size="sm" @click="addNewSkill" class="mt-2">Dodaj nową umiejętność</b-button>
                            </b-form-group>
                        </b-form>
                    </b-col>
                </b-row>  
                <b-row>
                    <b-col cols=10 offset=1>
                        <hr>
                        <b-button variant="success" size="sm" @click="saveCV">Zapisz</b-button>
                    </b-col>
                </b-row>
            </div>
            <!-- Komunikat w przypadku braku CV -->
            <div v-else>
                <b-row>
                    <b-col class="text-center">
                        <h4>Nie masz jeszcze CV</h4>
                    </b-col>
                </b-row>
                <b-row class="mt-2" align-h="center">
                    <b-col cols=4 class="text-center">
                        <b-button variant="success" size="sm" @click="showCreatorHandler">Nowe CV</b-button>
                    </b-col>
                </b-row>
            </div>             
        </div>        
    </div>    
</template>

<script>
export default {
    data() {
        return {
            hasCV: "",
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
        this.hasCV = !(this.$store.state.currentUser.user.cv === undefined || // jesli pole cv jest undefined lub null, wtedy hasCV = false
                       this.$store.state.currentUser.user.cv === null) 
        console.log(this.hasCV)
        this.isCreating = false
        this.isEditing = false
    },

    methods: {
        showCreatorHandler() {
            this.isCreating = true;
            console.log(this.isCreating)
        },

        showEditorHandler() {
            this.isEditing = true
            this.skills = this.skillsCV
            this.experiences = this.experienceCV
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
           let skills = this.serializeSkillsArray()          
           let experiences = this.serializeExperiencesArray()
           
           console.log(skills)
           console.log(experiences)
           
           this.$store.dispatch('createCV', {
               skills: skills,
               experiences: experiences
           }).then(() => {
               console.log("CV zostalo zapisane")
               alert("Zapisano CV")
               this.$router.push({name: 'ProfileSettings'})
           }).catch(() => {
               alert("Nie udalo sie zapisac CV")
           })
        },

        deleteCV() {
            let isSure = confirm("Czy na pewno chcesz usunac CV?")

            if(isSure) {
                this.$store.dispatch('deleteCV').then(() => {
                    alert("Zakonczono procedure usuwania CV")
                    this.$router.push("/profile")
                }).catch(() => {
                    alert("Niestety nie udalo sie usunac CV")
                })
            }
        },

        /* 
           z kazdego elementu tablicy this.skills, utworz String postaci 'name level' i ze wszytkich tych stringow utworz 1 string
           ktorego elementy oddzielone sa przecinkami
        */
        serializeSkillsArray() {
            return this.skills.map(skill => skill.name + " " + skill.level).join(",")
        },

        /*
           z kazdego elementu tablicy this.experiences utworz String postaci 'startDate, endDate, company, description'
           i ze wszytkich tych stringow utworz 1 string ktorego elementy oddzielone sa srednikami
        */
        serializeExperiencesArray() {
            return this.experiences.map(experience => {
               let expString = "";
               for(let property of ['startDate', 'endDate', 'company', 'description']) {                   
                   expString += experience[property].trim() + ","
               }
               return expString.trim()
           }).join(";")
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
