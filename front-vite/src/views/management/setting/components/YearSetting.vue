<template>
  <div>
    <el-table :data="store.years" style="width: 100%">
      <el-table-column prop="year" label="年份">
        <template #default="{ row }">
          <el-input v-model="row.year" placeholder="请输入年份"></el-input>
        </template>
      </el-table-column>
      <el-table-column prop="status" label="状态">
        <template #default="{ row }">
          <el-select v-model="row.status" placeholder="选择状态">
            <el-option label="启用" value="启用"></el-option>
            <el-option label="禁用" value="禁用"></el-option>
          </el-select>
        </template>
      </el-table-column>
      <el-table-column label="操作">
        <template #default="{ $index }">
          <el-button type="danger" @click="removeYear($index)" size="small">删除</el-button>
        </template>
      </el-table-column>
    </el-table>
    <div class="mt-4 flex justify-between">
      <el-button type="primary" @click="addYear">新增年份</el-button>
      <el-button type="success" @click="handleSaveYears">提交更改</el-button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { watch, onMounted } from 'vue';
import { useSettingStore } from '@/stores/settingStore';
import { ElMessage } from 'element-plus';

const store = useSettingStore();

onMounted(async () => {
  try {
    await store.fetchYears();
  } catch (error) {
    ElMessage.error('加载年份数据失败');
  }
});

const addYear = () => {
  store.years.push({ year: '', status: '' });
};

const removeYear = async (index: number) => {
  store.years.splice(index, 1);
  await store.saveYears();
};

const handleSaveYears = async () => {
  try {
    await store.saveYears();
    ElMessage.success('年份配置保存成功');
  } catch (error) {
    ElMessage.error('年份配置保存失败');
  }
};

watch(() => store.years, () => {
  if (!store.isInitializing) {
    ElMessage.warning('您已修改年份数据，请记得提交更改');
  }
}, { deep: true });
</script>