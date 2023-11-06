import { createRouter, createWebHistory } from "vue-router";
import HomePage from './components/HomePage'
import CreatePage from './components/CreatePage'

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
    }

]

const router = createRouter({
    history:createWebHistory(), //Navegación por defecto
    routes,
}) 

export default router;