import ListingTab from './components/ListingTab.vue'
import LoginForm from './components/LoginForm.vue'
import RegisterForm from './components/RegisterForm.vue'
import PostCreator from './components/PostCreator.vue'

export default [
    {path: '/', component: ListingTab},
    {path: '/login', name: 'Login', component: LoginForm},
    {path: '/register', name: 'Register', component:RegisterForm},
    {path: '/post/new', name: 'NewPost', component: PostCreator}
]