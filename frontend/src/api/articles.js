import axios from 'axios'

const apiClient = axios.create({
  baseURL: 'http://localhost/api/', 
  timeout: 5000,
})

export async function fetchArticles() {
  const response = await apiClient.get('articles/')
  return response.data
}
