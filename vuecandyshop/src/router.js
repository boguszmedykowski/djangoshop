import { createRouter, createWebHistory } from 'vue-router';
import AddProduct from './components/AddProduct.vue';
import ProductList from './components/ProductList.vue'; // Upewnij się, że ścieżka do pliku jest prawidłowa
import CandyCart from './components/CandyCart.vue';
import UserLogin from './components/UserLogin.vue'
import UserRegister from './components/UserRegister.vue'

const routes = [
    {
        path: '/addProduct',
        name: 'AddProduct',
        component: AddProduct
    },
    {
        path: '/',
        name: '/',
        component: ProductList
    },
    {
        path: '/ProductList',
        name: 'ProductList',
        component: ProductList
    },
    {
        path: '/CandyCart',
        name: 'CandyCart',
        component: CandyCart
    },
    {
        path: '/UserLogin',
        name: 'UserLogin',
        component: UserLogin
    },
    {
        path: '/UserRegister',
        name: 'UserRegister',
        component: UserRegister
    }
    // Możesz dodać inne trasy tutaj
];

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes,
});

export default router;
