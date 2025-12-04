import { defineStore } from 'pinia'
import axios from 'axios'

export const useArticlesStore = defineStore('articles', {
  state: () => ({
    items: [],
    isLoading: false,
    error: null,
  }),
  actions: {
    async fetchArticles() {
      this.isLoading = true
      this.error = null

      try {
        const response = await axios.get('http://localhost/api/articles/')
        this.items = response.data
      } catch (err) {
        console.error('Помилка завантаження статей:', err)
        this.error = 'Не вдалося завантажити статті'
      } finally {
        this.isLoading = false
      }
    },
  },
})
