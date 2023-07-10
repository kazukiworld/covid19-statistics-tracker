import { createRouter, createWebHistory} from 'vue-router';
import type { RouteRecordRaw, Router } from 'vue-router'
import HomeView from '../views/HomeView.vue';
import StatisticView from '../views/StatisticView.vue';
import ContactView from '../views/ContactView.vue';

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    redirect: '/home'
  },
  {
    path: '/home',
    name: 'home',
    component: HomeView
  },
  {
    path: '/statistics',
    name: 'statistics',
    component: StatisticView
  },
  {
    path: '/contact',
    name: 'contact',
    component: ContactView
  }
];

const baseURL: string = import.meta.env.BASE_URL;

const router: Router = createRouter({
  history: createWebHistory(baseURL),
  routes,
  linkActiveClass: 'text-white',
});

export default router;