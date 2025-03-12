<template>
  <div>
    <el-table :data="store.majors" style="width: 100%">
      <el-table-column prop="name" label="专业名称">
        <template #default="{ row }">
          <el-input v-model="row.name" placeholder="请输入专业名称"></el-input>
        </template>
      </el-table-column>
      <el-table-column prop="category" label="分类">
        <template #default="{ row }">
          <el-select v-model="row.category" placeholder="选择分类">
            <el-option label="限制专业" value="限制专业"></el-option>
            <el-option label="数学类" value="数学类"></el-option>
            <el-option label="电子信息类" value="电子信息类"></el-option>
            <el-option label="自动化类" value="自动化类"></el-option>
            <el-option label="其他工科" value="其他工科"></el-option>
            <el-option label="理科（非数学）" value="理科（非数学）"></el-option>
            <el-option label="文商科" value="文商科"></el-option>
          </el-select>
        </template>
      </el-table-column>
      <el-table-column label="操作">
        <template #default="{ $index }">
          <el-button type="danger" @click="removeMajor($index)" size="small">删除</el-button>
        </template>
      </el-table-column>
    </el-table>
    <div class="mt-4 flex justify-between">
      <div class="flex gap-4">
        <el-button type="primary" @click="addMajor">新增专业</el-button>
        <el-button type="warning" @click="handleInitializeMajors">初始化</el-button>
      </div>
      <el-button type="success" @click="handleSaveMajors">提交更改</el-button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { watch, onMounted } from 'vue';
import { useSettingStore } from '@/stores/settingStore';
import { ElMessage, ElMessageBox } from 'element-plus';

const store = useSettingStore();

onMounted(async () => {
  try {
    await store.fetchMajors();
  } catch (error) {
    ElMessage.error('加载专业数据失败');
  }
});

const addMajor = () => {
  store.majors.push({ name: '', category: '' });
};

const removeMajor = async (index: number) => {
  store.majors.splice(index, 1);
  await store.saveMajors();
};

const handleInitializeMajors = async () => {
  try {
    await ElMessageBox.confirm(
      '确定要初始化专业数据吗？这将覆盖当前所有数据。',
      '警告',
      {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning',
      }
    );
    await store.initializeMajors();
    ElMessage.success('专业数据初始化成功');
  } catch (error) {
    if (error !== 'cancel') {
      ElMessage.error('专业数据初始化失败');
    }
  }
};

const handleSaveMajors = async () => {
  try {
    await store.saveMajors();
    ElMessage.success('专业数据提交成功');
  } catch (error) {
    ElMessage.error('专业数据提交失败');
  }
};

watch(() => store.majors, () => {
  if (!store.isInitializing) {
    ElMessage.warning('您已修改专业数据，请记得提交更改');
  }
}, { deep: true });
</script>