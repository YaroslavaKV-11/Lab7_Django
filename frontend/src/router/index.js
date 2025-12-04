import { createRouter, createWebHistory } from 'vue-router'
import ArticleListView from '../views/ArticleListView.vue'
import ArticleDetailView from '../views/ArticleDetailView.vue'

const routes = [
  {
    path: '/',
    name: 'articles',
    component: ArticleListView,
  },
  {
    path: '/articles/:id',
    name: 'article-detail',
    component: ArticleDetailView,
    props: true,
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
