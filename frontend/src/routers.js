import { createRouter, createWebHistory } from "vue-router";
import HomePage from './components/HomePage'
import CreatePage from './components/CreatePage'
import UserLogin from './components/UserLogin'
import SelectDaysComponent from './components/SelectDaysComponent'
import CheckoutComponent from './components/CheckoutComponent'
import FinalComponent from './components/FinalComponent'

//Acá definimos las rutas
const routes = [
    {
        path: '/', //para la home page
        name: 'home',
        component:HomePage
    },
    {
        path: '/create', //para la create page
        name: 'create',
        component:CreatePage
    },
    {
        path: '/login', //para la create page
        name: 'login',
        component: UserLogin
    },
    {
        path: '/select-days', 
        name: 'selectdays',
        component: SelectDaysComponent 
    },
    {
        path: '/checkout', 
        name: 'checkout',
        component: CheckoutComponent  
    },
    {
        path: '/final-component',
        name:'finalComponent',
        component: FinalComponent
    },


]

const router = createRouter({
    history:createWebHistory(), //Navegación por defecto
    routes,
}) 

export default router;