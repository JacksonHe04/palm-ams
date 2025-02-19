import { defineStore } from 'pinia';
import { ref } from 'vue';
import { getPercent, updatePercent, type PercentData } from '../apis/percent';
import { ElMessage } from 'element-plus';

export const usePercentStore = defineStore('percent', () => {
  const percentData = ref<PercentData>({
    pOfA: 0,
    pOfB: 0,
    pOfC: 0,
    pOfATop: 0,
    pOfBTop: 0,
    pOfCTop: 0,
    pOfATalent: 0,
    pOfBTalent: 0,
    pOfCTalent: 0
  });

  // 获取百分比数据
  const fetchPercentData = async () => {
    try {
      const response = await getPercent();
      percentData.value = response.data;
    } catch (error) {
      console.error('获取百分比数据失败:', error);
      ElMessage.error('获取百分比数据失败');
    }
  };

  // 更新百分比数据
  const updatePercentData = async (data: PercentData) => {
    try {
      const response = await updatePercent(data);
      percentData.value = response.data;
      ElMessage.success('更新百分比数据成功');
    } catch (error) {
      console.error('更新百分比数据失败:', error);
      ElMessage.error('更新百分比数据失败');
    }
  };

  return {
    percentData,
    fetchPercentData,
    updatePercentData
  };
});