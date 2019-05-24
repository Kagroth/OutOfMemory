<template>
    <!--
        if posiada CV:
            pokaz CV i udostepnij tryb edycji
        else:
            pokaz przycisk z tworzeniem CV
    -->
    <div>
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
        <div v-else>
            Twoje CV:    
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
            hasCV: false,
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
        }
    }
}
</script>

<style scoped>

</style>
