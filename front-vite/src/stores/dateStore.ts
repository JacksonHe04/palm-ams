import { defineStore } from 'pinia';
import { ref } from 'vue';
import type { AdmissionDate } from '@/apis/date';
import {
  getAdmissionDates,
  updateAdmissionDates,
  getAdmissionDatesByYear,
  updateAdmissionDatesByYear
} from '@/apis/date';
import { ElMessage } from 'element-plus';

export const useDateStore = defineStore('date', () => {
  // 状态定义
  const admissionDates = ref<AdmissionDate[]>([]);
  const currentYear = ref<number>(new Date().getFullYear());
  const isLoading = ref<boolean>(false);

  /**
   * 获取指定年份的招生时间配置
   * @param year - 年份
   */
  const fetchAdmissionDatesByYear = async (year: number) => {
    isLoading.value = true;
    try {
      const response = await getAdmissionDatesByYear(year);
      admissionDates.value = response.data;
      currentYear.value = year;
    } catch (error) {
      console.error('获取招生时间配置失败:', error);
      ElMessage.error('获取招生时间配置失败');
    } finally {
      isLoading.value = false;
    }
  };

  /**
   * 保存指定年份的招生时间配置
   * @param year - 年份
   */
  const saveAdmissionDatesByYear = async (year: number) => {
    isLoading.value = true;
    try {
      await updateAdmissionDatesByYear(year, admissionDates.value);
      ElMessage.success('保存成功');
    } catch (error) {
      console.error('保存招生时间配置失败:', error);
      ElMessage.error('保存失败');
      throw error;
    } finally {
      isLoading.value = false;
    }
  };

  /**
   * 初始化默认招生时间配置
   */
  const initializeAdmissionDates = () => {
    admissionDates.value = [
      {
        type: '推免硕士',
        startTime: '',
        endTime: ''
      },
      {
        type: '考研硕士',
        startTime: '',
        endTime: ''
      },
      {
        type: '博士',
        startTime: '',
        endTime: ''
      },
      {
        type: '直博',
        startTime: '',
        endTime: ''
      }
    ];
  };

  return {
    admissionDates,
    currentYear,
    isLoading,
    fetchAdmissionDatesByYear,
    saveAdmissionDatesByYear,
    initializeAdmissionDates
  };
});