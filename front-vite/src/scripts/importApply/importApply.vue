<template>
  <div class="import-container">
    <el-button :loading="isLoading" type="primary" @click="handleImport">
      导入申请数据
    </el-button>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { ElMessage } from 'element-plus';
import { submitApplication } from '@/apis/apply';
import { v4 as uuidv4 } from 'uuid';

const isLoading = ref(false);

const importJsonFiles = async () => {
  const jsonFiles = [
    'd1.json', 'd2.json', 'd3.json', 'd4.json', 'd5.json',
    'd6.json', 'd7.json', 'd8.json', 'd9.json', 'd10.json',
    'd12.json', 'd14.json', 'd15.json', 'd16.json', 'd17.json',
    'd18.json', 'd19.json', 'd20.json',
    'h1.json', 'h2.json', 'h3.json', 'h4.json', 'h5.json',
    'h6.json', 'h8.json', 'h9.json', 'h10.json', 'h11.json',
    'h12.json', 'h13.json'
  ];

  let successCount = 0;
  let failCount = 0;

  for (const fileName of jsonFiles) {
    try {
      const response = await fetch(`/src/scripts/importApply/${fileName}`);
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      const jsonData = await response.json();
      const dataWithId = {
        ...jsonData,
        id: uuidv4()
      };
      await submitApplication(dataWithId);
      successCount++;
    } catch (error) {
      console.error(`导入 ${fileName} 失败:`, error);
      failCount++;
    }
  }

  if (successCount > 0) {
    ElMessage.success(`成功导入 ${successCount} 个文件`);
  }
  if (failCount > 0) {
    ElMessage.warning(`${failCount} 个文件导入失败`);
  }
};

const handleImport = async () => {
  isLoading.value = true;
  try {
    await importJsonFiles();
  } catch (error) {
    ElMessage.error('批量导入失败：' + (error as Error).message);
  } finally {
    isLoading.value = false;
  }
};
</script>

<style scoped>
.import-container {
  padding: 20px;
}
</style>