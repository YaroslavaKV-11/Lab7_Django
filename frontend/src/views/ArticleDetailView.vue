<template>
  <div v-if="store.loading">Завантаження...</div>
  <div v-else-if="store.error" class="error">{{ store.error }}</div>
  <div v-else-if="!store.currentArticle">Стаття не знайдена</div>
  <div v-else class="article">
    <button class="back" @click="$router.push('/')">← Назад до списку</button>

    <h2 class="title">{{ article.title }}</h2>

    <div class="meta">
      <span v-if="article.category">Категорія: {{ article.category }}</span>
      <span>Дата: {{ article.publication_date }}</span>
      <span v-if="article.author">Автор: {{ article.author }}</span>
    </div>

    <img
      v-if="article.image"
      :src="article.image"
      :alt="article.title"
      class="image"
    />

    <p class="text">
      {{ article.text }}
    </p>

    <section class="comments">
      <h3>Коментарі ({{ article.comments.length }})</h3>

      <div v-if="!article.comments.length">
        Ще немає коментарів.
      </div>

      <article
        v-for="comment in article.comments"
        :key="comment.id"
        class="comment"
      >
        <div class="comment-meta">
          <strong>{{ comment.author || 'Анонім' }}</strong>
          <span>{{ comment.publication_date }}</span>
        </div>
        <p>{{ comment.text }}</p>
      </article>
    </section>
  </div>
</template>

<script setup>
import { computed, onMounted, watch } from 'vue'
import { useRoute } from 'vue-router'
import { useArticleStore } from '../stores/articleStore'

const route = useRoute()
const store = useArticleStore()

const loadArticle = () => {
  const id = route.params.id
  if (id) {
    store.fetchArticle(id)
  }
}

onMounted(loadArticle)
watch(() => route.params.id, loadArticle)

const article = computed(() => store.currentArticle)
</script>

<style scoped>
.article {
  max-width: 800px;
  margin: 0 auto;
}

.back {
  margin-bottom: 1rem;
  background: none;
  border: none;
  color: #0d6efd;
  cursor: pointer;
}

.title {
  margin-bottom: 0.5rem;
}

.meta {
  display: flex;
  flex-wrap: wrap;
  gap: 0.75rem;
  font-size: 0.9rem;
  color: #666;
  margin-bottom: 1rem;
}

.image {
  width: 100%;
  max-height: 400px;
  object-fit: cover;
  margin-bottom: 1rem;
  border-radius: 6px;
}

.text {
  font-size: 1rem;
  line-height: 1.6;
  margin-bottom: 2rem;
}

.comments {
  border-top: 1px solid #ddd;
  padding-top: 1rem;
}

.comment {
  padding: 0.75rem 0;
  border-bottom: 1px solid #eee;
}

.comment-meta {
  display: flex;
  justify-content: space-between;
  font-size: 0.85rem;
  color: #555;
}

.error {
  color: red;
}
</style>
