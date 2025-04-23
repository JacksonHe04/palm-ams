import { defineStore } from 'pinia';
import http from '../utils/http';

export const useResultStore = defineStore('result', {
  state: () => ({
    filteredStudents: [],
    failedStudents: [],
    loading: false,
    error: null
  }),

  actions: {
    async fetchFilteredStudents() {
      this.loading = true;
      this.error = null;
      try {
        const response = await http.get('/api/result/filter/');
        this.filteredStudents = response.data.passed_students;
      } catch (err) {
        this.error = err.message || '获取筛选学生数据失败';
        console.error('获取筛选学生数据失败:', err);
      } finally {
        this.loading = false;
      }
    },

    async fetchFailedStudents() {
      this.loading = true;
      this.error = null;
      try {
        const response = await http.get('/api/result/failed/');
        this.failedStudents = response.data.failed_students;
      } catch (err) {
        this.error = err.message || '获取未通过筛选学生数据失败';
        console.error('获取未通过筛选学生数据失败:', err);
      } finally {
        this.loading = false;
      }
    }
  }
});