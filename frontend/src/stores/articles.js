// frontend/src/stores/articles.js
import { defineStore } from 'pinia'
import { fetchArticles as apiFetchArticles } from '../api/articles'

export const useArticlesStore = defineStore('articles', {
  state: () => ({
    articles: [],
    loading: false,
    error: null,
  }),

  actions: {
    // Дія з потрібною назвою
    async fetchArticles() {
      this.loading = true
      this.error = null

      try {
        const data = await apiFetchArticles()
        this.articles = data
      } catch (err) {
        console.error('Помилка при завантаженні статей:', err)
        this.error = 'Сервер не відповідає'
      } finally {
        this.loading = false
      }
    },
  },
})
