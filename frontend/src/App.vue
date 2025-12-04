<template>
  <div class="app">
    <header class="app-header">
      <div class="container header-inner">
        <h1 class="logo">Мій блог</h1>
        <nav class="nav">
          <RouterLink to="/" class="nav-link">Головна</RouterLink>
        </nav>
      </div>
    </header>

    <main class="main">
      <div class="container">
        <RouterView />
      </div>
    </main>
  </div>
</template>

<script setup>
import { RouterView, RouterLink } from 'vue-router'
</script>

<style scoped>
.app-header {
  background-color: #1976d2;
  color: #fff;
  padding: 16px 0;
  margin-bottom: 32px;
}

.header-inner {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.logo {
  margin: 0;
  font-size: 24px;
  font-weight: 700;
}

.nav-link {
  color: #fff;
  text-decoration: none;
  font-weight: 500;
}

.nav-link:hover {
  text-decoration: underline;
}

.main {
  padding-bottom: 40px;
}
</style>
