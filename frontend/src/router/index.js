import { createRouter, createWebHistory } from 'vue-router'
import ArticleListView from '../views/ArticleListView.vue'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      name: 'home',
      component: ArticleListView,
    },
  ],
})

export default router
