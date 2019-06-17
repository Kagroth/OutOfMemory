/*
    Plik reprezentuje tablice ze sciezkami do widokow     
*/
import ListingTab from './components/ListingTab.vue'
import LoginForm from './components/LoginForm.vue'
import RegisterForm from './components/RegisterForm.vue'
import PostCreator from './components/PostCreator.vue'
import PostDetails from './components/PostDetails.vue'
import Profile from './components/Profile.vue'
import CV from './components/CV.vue'
import JobOfferForm from "./components/JobOfferForm"
import JobOfferDetails from "./components/JobOfferDetails"
import JobOfferEditForm from "./components/JobOfferEditForm";

export default [
  {path: '/', component: ListingTab},
  {path: '/login', name: 'Login', component: LoginForm},
  {path: '/register', name: 'Register', component: RegisterForm},
  {path: '/post/new', name: 'NewPost', component: PostCreator},
  {path: '/post/:pk', name: 'PostDetails', component: PostDetails},
  {path: '/profile', name: 'Profile', component: Profile},
  {path: '/profile/cv', name: "CV", component: CV},
  {path: '/job/new', name: "NewJobOffer", component: JobOfferForm},
  {path: '/job/:pk', name: 'JobOfferDetails', component: JobOfferDetails},
  {path: '/job/edit/:pk', name: 'JobOfferEdit', component: JobOfferEditForm}
]
