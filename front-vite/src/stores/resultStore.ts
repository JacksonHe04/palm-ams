import { defineStore } from 'pinia';
import http from '../utils/http';

export const useResultStore = defineStore('result', {
  state: () => ({
    filteredStudents: [],
    loading: false,
    error: null
  }),

  actions: {
    async fetchFilteredStudents() {
      this.loading = true;
      this.error = null;
      try {
        const response = await http.get('/api/result/filter/');
        this.filteredStudents = response.data;
      } catch (err) {
        this.error = err.message || '获取筛选学生数据失败';
        console.error('获取筛选学生数据失败:', err);
      } finally {
        this.loading = false;
      }
    }
  }
});