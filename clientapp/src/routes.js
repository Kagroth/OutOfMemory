import ListingTab from './components/ListingTab.vue'
import LoginForm from './components/LoginForm.vue'
import RegisterForm from './components/RegisterForm.vue'

export default [
    {path: '/', component: ListingTab},
    {path: '/login', name: 'Login', component: LoginForm},
    {path: '/register', name: 'Register', component:RegisterForm}
]