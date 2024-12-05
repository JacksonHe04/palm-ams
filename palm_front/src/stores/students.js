import { defineStore } from 'pinia';

export const useStudentsStore = defineStore('students', {
  state: () => ({
    students: [], // 学生数据
    visibleFields: [
      '序号', '照片', '姓名', '邮箱', '手机号', '本科院校', '专业人数',
      '百分比', '状态', '操作',
    ], // 默认可见字段
  }),
  actions: {
    async fetchStudents() {
      try {
        const response = await api.get('/students');
        this.students = response.data || [];
      } catch (error) {
        console.error('获取学生数据失败:', error);
      }
    },
  },
});