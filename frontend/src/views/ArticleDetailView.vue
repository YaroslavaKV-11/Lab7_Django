<template>
  <main class="detail-page">
    <section class="detail-inner" v-if="!loading && !error && article">
      <header class="detail-header">
        <p class="detail-meta">
          <span class="detail-date">
            {{ formatDate(article.publication_date) }}
          </span>
          <span class="detail-dot">•</span>
          <span class="detail-author">{{ article.author }}</span>
          <span v-if="article.category" class="detail-category">
            {{ article.category }}
          </span>
        </p>

        <h1 class="detail-title">{{ article.title }}</h1>
      </header>

      <div v-if="article.image" class="detail-image-wrapper">
        <img :src="article.image" :alt="article.title" class="detail-image" />
      </div>

      <article class="detail-content">
        <p
          v-for="(paragraph, index) in paragraphs"
          :key="index"
          class="detail-paragraph"
        >
          {{ paragraph }}
        </p>
      </article>

      <section class="comments">
        <h2 class="comments-title">
          Коментарі
          <span class="comments-count">
            ({{ article.comments ? article.comments.length : 0 }})
          </span>
        </h2>

        <p v-if="!article.comments || article.comments.length === 0" class="comments-empty">
          Коментарів поки немає.
        </p>

        <ul v-else class="comments-list">
          <li
            v-for="comment in article.comments"
            :key="comment.id"
            class="comment-item"
          >
            <p class="comment-header">
              <span class="comment-author">{{ comment.author }}</span>
              <span class="comment-date">
                {{ formatDate(comment.publication_date) }}
              </span>
            </p>
            <p class="comment-text">
              {{ comment.text }}
            </p>
          </li>
        </ul>
      </section>
    </section>

    <section class="detail-inner" v-if="loading">
      <div class="status status-info">Завантаження статті…</div>
    </section>

    <section class="detail-inner" v-if="error">
      <div class="status status-error">
        Не вдалося завантажити статтю
        <span class="status-details">{{ error }}</span>
      </div>
    </section>
  </main>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import axios from 'axios'

const route = useRoute()

const article = ref(null)
const loading = ref(false)
const error = ref(null)

const fetchArticle = async () => {
  loading.value = true
  error.value = null

  try {
    const { id } = route.params
    const response = await axios.get(`http://localhost/api/articles/${id}/`)
    article.value = response.data
  } catch (err) {
    console.error('Помилка при завантаженні статті:', err)
    error.value = 'Сервер не відповідає'
  } finally {
    loading.value = false
  }
}

onMounted(fetchArticle)

const formatDate = (value) => {
  if (!value) return ''
  return new Date(value).toLocaleDateString('uk-UA', {
    day: 'numeric',
    month: 'short',
    year: 'numeric',
  })
}

const paragraphs = computed(() => {
  if (!article.value || !article.value.text) return []
  // розбиваємо текст за переносами рядків
  return article.value.text.split(/\r?\n/).filter((p) => p.trim().length > 0)
})
</script>

<style scoped>
.detail-page {
  min-height: calc(100vh - 64px);
  background: radial-gradient(circle at top, #f5f7ff 0, #f3f4f6 45%, #eef1f5 100%);
  padding: 32px 0 40px;
}

.detail-inner {
  max-width: 860px;
  margin: 0 auto;
  padding: 0 20px;
}

.detail-header {
  margin-bottom: 18px;
}

.detail-meta {
  font-size: 14px;
  color: #6b7280;
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  gap: 6px;
  margin: 0 0 6px;
}

.detail-dot {
  opacity: 0.6;
}

.detail-category {
  padding: 4px 10px;
  border-radius: 999px;
  background: rgba(37, 99, 235, 0.08);
  color: #1d4ed8;
  font-size: 12px;
  font-weight: 500;
}

.detail-title {
  font-size: 30px;
  line-height: 1.2;
  font-weight: 800;
  margin: 0;
  color: #111827;
}

.detail-image-wrapper {
  margin: 22px 0 18px;
  border-radius: 18px;
  overflow: hidden;
  box-shadow: 0 18px 45px rgba(15, 23, 42, 0.16);
}

.detail-image {
  width: 100%;
  height: 360px;
  object-fit: cover;
  display: block;
}

.detail-content {
  background: #ffffff;
  border-radius: 18px;
  padding: 20px 22px;
  box-shadow: 0 14px 35px rgba(15, 23, 42, 0.08);
}

.detail-paragraph {
  margin: 0 0 12px;
  font-size: 15px;
  line-height: 1.7;
  color: #111827;
}

.detail-paragraph:last-child {
  margin-bottom: 0;
}

/* Коментарі */
.comments {
  margin-top: 28px;
}

.comments-title {
  font-size: 20px;
  font-weight: 700;
  margin: 0 0 10px;
  display: flex;
  align-items: baseline;
  gap: 6px;
}

.comments-count {
  font-size: 14px;
  color: #6b7280;
}

.comments-empty {
  font-size: 14px;
  color: #6b7280;
}

.comments-list {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.comment-item {
  background: #ffffff;
  border-radius: 14px;
  padding: 10px 14px;
  box-shadow: 0 8px 20px rgba(15, 23, 42, 0.06);
}

.comment-header {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  margin-bottom: 4px;
}

.comment-author {
  font-weight: 600;
  font-size: 14px;
  color: #111827;
}

.comment-date {
  font-size: 12px;
  color: #9ca3af;
}

.comment-text {
  margin: 0;
  font-size: 14px;
  color: #374151;
}

/* Статуси */
.status {
  padding: 14px 16px;
  border-radius: 10px;
  font-size: 14px;
  margin-top: 12px;
}

.status-info {
  background: rgba(59, 130, 246, 0.06);
  color: #1f2933;
  border: 1px solid rgba(59, 130, 246, 0.18);
}

.status-error {
  background: rgba(220, 38, 38, 0.05);
  color: #b91c1c;
  border: 1px solid rgba(220, 38, 38, 0.18);
}

.status-details {
  display: block;
  font-size: 12px;
  color: #6b7280;
  margin-top: 3px;
}

@media (max-width: 768px) {
  .detail-page {
    padding-top: 20px;
  }

  .detail-title {
    font-size: 24px;
  }

  .detail-image {
    height: 240px;
  }

  .detail-content {
    padding: 16px 16px;
  }
}
</style>
