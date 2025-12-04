<template>
  <main class="page">
    <section class="page-inner">
      <header class="page-header">
        <h2 class="page-title">Останні статті</h2>
        <p class="page-subtitle">
          Добірка корисних матеріалів про Django, Docker та веб-розробку
        </p>
      </header>

      <div v-if="loading" class="status status-info">
        Завантаження статей…
      </div>

      <div v-else-if="error" class="status status-error">
        Не вдалося завантажити статті
        <span class="status-details">{{ error }}</span>
      </div>

      <div v-else-if="articles.length === 0" class="status status-info">
        Наразі немає статей.
      </div>

      <div v-else class="articles-grid">
        <article
          v-for="article in articles"
          :key="article.id"
          class="article-card"
        >
          <div class="article-image-wrapper">
            <img
              v-if="article.image"
              :src="article.image"
              :alt="article.title"
              class="article-image"
            />
            <div v-else class="article-image article-image--placeholder">
              {{ article.title[0] || 'A' }}
            </div>
          </div>

          <div class="article-body">
            <p class="article-meta">
              <span class="article-date">
                {{ formatDate(article.publication_date) }}
              </span>
              <span class="article-dot">•</span>
              <span class="article-author">{{ article.author }}</span>
            </p>

            <h3 class="article-title">
              {{ article.title }}
            </h3>

            <p class="article-excerpt">
              {{ article.text.slice(0, 220) }}
              <span v-if="article.text.length > 220">…</span>
            </p>

            <div class="article-footer">
  <span class="article-chip" v-if="article.category">
    {{ article.category }}
  </span>

  <RouterLink
    class="article-button-link"
    :to="{ name: 'article-detail', params: { id: article.id } }"
  >
    Читати
  </RouterLink>
</div>
          </div>
        </article>
      </div>
    </section>
  </main>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const articles = ref([])
const loading = ref(false)
const error = ref(null)

const fetchArticles = async () => {
  loading.value = true
  error.value = null

  try {
    const response = await axios.get('http://localhost/api/articles/')
    articles.value = response.data
  } catch (err) {
    console.error('Помилка при завантаженні статей:', err)
    error.value = 'Сервер не відповідає'
  } finally {
    loading.value = false
  }
}

onMounted(fetchArticles)

const formatDate = (value) => {
  if (!value) return ''
  return new Date(value).toLocaleDateString('uk-UA', {
    day: 'numeric',
    month: 'short',
    year: 'numeric',
  })
}
</script>

<style scoped>
.page {
  min-height: calc(100vh - 64px);
  background: radial-gradient(circle at top, #f5f7ff 0, #f3f4f6 45%, #eef1f5 100%);
  padding: 32px 0 40px;
}

.page-inner {
  max-width: 1120px;
  margin: 0 auto;
  padding: 0 20px;
}

.page-header {
  margin-bottom: 24px;
}

.page-title {
  font-size: 32px;
  font-weight: 700;
  margin: 0 0 6px;
}

.page-subtitle {
  margin: 0;
  font-size: 14px;
  color: #6b7280;
}

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

.articles-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
  gap: 20px;
  margin-top: 20px;
}

.article-card {
  background: #ffffff;
  border-radius: 18px;
  box-shadow: 0 14px 35px rgba(15, 23, 42, 0.12);
  overflow: hidden;
  display: flex;
  flex-direction: column;
  transition: transform 0.18s ease, box-shadow 0.18s ease, translate 0.18s;
}

.article-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 18px 45px rgba(15, 23, 42, 0.18);
}

.article-image-wrapper {
  position: relative;
  overflow: hidden;
}

.article-image {
  width: 100%;
  height: 210px;
  object-fit: cover;
  display: block;
  transition: transform 0.25s ease;
}

.article-card:hover .article-image {
  transform: scale(1.04);
}

.article-image--placeholder {
  height: 210px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 64px;
  font-weight: 700;
  color: #e5edff;
  background: linear-gradient(135deg, #2563eb, #4f46e5);
}

.article-body {
  padding: 16px 18px 18px;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.article-meta {
  margin: 0;
  font-size: 13px;
  color: #6b7280;
  display: flex;
  align-items: center;
  gap: 6px;
}

.article-dot {
  font-size: 12px;
  opacity: 0.7;
}

.article-title {
  margin: 2px 0 0;
  font-size: 18px;
  line-height: 1.3;
  font-weight: 700;
  color: #111827;
}

.article-excerpt {
  margin: 4px 0 0;
  font-size: 14px;
  color: #374151;
  line-height: 1.4;
  max-height: 3.8em; /* ~3 рядки */
  overflow: hidden;
}

.article-footer {
  margin-top: 10px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 8px;
}

.article-chip {
  padding: 5px 10px;
  border-radius: 999px;
  background: rgba(37, 99, 235, 0.08);
  color: #1d4ed8;
  font-size: 12px;
  font-weight: 500;
}

.article-button {
  border: none;
  border-radius: 999px;
  padding: 7px 16px;
  font-size: 13px;
  font-weight: 500;
  cursor: pointer;
  background: linear-gradient(135deg, #2563eb, #1d4ed8);
  color: #ffffff;
  box-shadow: 0 6px 14px rgba(37, 99, 235, 0.35);
  transition: transform 0.16s ease, box-shadow 0.16s ease;
}

.article-button:hover {
  transform: translateY(-1px);
  box-shadow: 0 10px 22px rgba(37, 99, 235, 0.45);
}

.article-button:active {
  transform: translateY(0);
  box-shadow: 0 4px 10px rgba(37, 99, 235, 0.35);
}

.article-button-link {
  text-decoration: none;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border-radius: 999px;
  padding: 7px 16px;
  font-size: 13px;
  font-weight: 500;
  cursor: pointer;
  background: linear-gradient(135deg, #2563eb, #1d4ed8);
  color: #ffffff;
  box-shadow: 0 6px 14px rgba(37, 99, 235, 0.35);
  transition: transform 0.16s ease, box-shadow 0.16s ease;
}

.article-button-link:hover {
  transform: translateY(-1px);
  box-shadow: 0 10px 22px rgba(37, 99, 235, 0.45);
}

.article-button-link:active {
  transform: translateY(0);
  box-shadow: 0 4px 10px rgba(37, 99, 235, 0.35);
}


@media (max-width: 768px) {
  .page {
    padding-top: 20px;
  }

  .page-title {
    font-size: 26px;
  }

  .articles-grid {
    gap: 16px;
  }

  .article-body {
    padding: 14px 14px 16px;
  }
}
</style>
