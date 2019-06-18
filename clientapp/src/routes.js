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
import JobOfferDetailsApps from "./components/JobOfferDetailsApps"
import JobOfferEditForm from "./components/JobOfferEditForm"
import UserProfile from './components/UserProfile'
import ProfileSettings from "./components/ProfileSettings";
import CVDetails from "./components/CVDetails";


export default [
  {path: '/', component: ListingTab},
  {path: '/login', name: 'Login', component: LoginForm},
  {path: '/register', name: 'Register', component: RegisterForm},
  {path: '/post/new', name: 'NewPost', component: PostCreator},
  {path: '/post/:pk', name: 'PostDetails', component: PostDetails},
  {path: '/profile', name: 'Profile', component: Profile},
  {path: '/profile/cv', name: "CV", component: CV},
  {path: '/profile/:username', name: 'UserProfile', component: UserProfile},  
  {path: '/profile/:username/cv', name: 'CVDetails', component: CVDetails},
  {path: '/settings', name: 'ProfileSettings', component: ProfileSettings},
  {path: '/job/new', name: "NewJobOffer", component: JobOfferForm},
  {path: '/job/:pk', name: 'JobOfferDetails', component: JobOfferDetails},
  {path: '/job/:pk/applications', name: 'JobOfferDetailsApps', component: JobOfferDetailsApps},
  {path: '/job/edit/:pk', name: 'JobOfferEdit', component: JobOfferEditForm},
]
