<template>
  <div>
    <el-table :data="store.awards" style="width: 100%">
      <el-table-column prop="name" label="奖项名称">
        <template #default="{ row }">
          <el-input v-model="row.name" placeholder="请输入奖项名称"></el-input>
        </template>
      </el-table-column>
      <el-table-column prop="level" label="奖项等级">
        <template #default="{ row }">
          <el-select v-model="row.level" placeholder="选择奖项等级">
            <el-option label="国家级" value="国家级"></el-option>
            <el-option label="省部级" value="省部级"></el-option>
            <el-option label="校级" value="校级"></el-option>
          </el-select>
        </template>
      </el-table-column>
      <el-table-column prop="category" label="奖项类别">
        <template #default="{ row }">
          <el-input v-model="row.category" placeholder="请输入奖项类别"></el-input>
        </template>
      </el-table-column>
      <el-table-column label="操作">
        <template #default="{ $index }">
          <el-button type="danger" @click="removeAward($index)" size="small">删除</el-button>
        </template>
      </el-table-column>
    </el-table>
    <div class="mt-4 flex justify-between">
      <el-button type="primary" @click="addAward">新增奖项</el-button>
      <el-button type="success" @click="handleSaveAwards">提交更改</el-button>
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
    await store.fetchAwards();
  } catch (error) {
    ElMessage.error('加载奖项数据失败');
  }
});

const addAward = () => {
  store.awards.push({ name: '', level: '', category: '' });
};

const removeAward = async (index: number) => {
  store.awards.splice(index, 1);
  await store.saveAwards();
};

const handleSaveAwards = async () => {
  try {
    await store.saveAwards();
    ElMessage.success('奖项配置保存成功');
  } catch (error) {
    ElMessage.error('奖项配置保存失败');
  }
};

watch(() => store.awards, () => {
  if (!store.isInitializing) {
    ElMessage.warning('您已修改奖项数据，请记得提交更改');
  }
}, { deep: true });
</script>