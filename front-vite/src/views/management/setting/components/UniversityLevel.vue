<template>
  <div>
    <div class="grid grid-cols-3 gap-4">
      <div v-for="(university, index) in store.universities" :key="index" class="border p-4 rounded">
        <div class="flex items-center gap-2">
          <el-input v-model="university.name" placeholder="请输入院校名称"></el-input>
          <el-select v-model="university.level" placeholder="选择等级" style="width: 120px">
            <el-option label="A" value="A"></el-option>
            <el-option label="B" value="B"></el-option>
            <el-option label="C" value="C"></el-option>
            <el-option label="国际前100" value="国际前100"></el-option>
            <el-option label="国际前200" value="国际前200"></el-option>
          </el-select>
          <el-button type="danger" @click="removeUniversity(index)" size="small">删除</el-button>
        </div>
      </div>
    </div>

    <div v-if="store.universities.length === 0" class="text-center py-8 text-gray-500">
      {{ store.isInitializing ? '加载中...' : '暂无数据' }}
    </div>

    <div class="mt-4 flex justify-between">
      <div class="flex gap-4">
        <el-button type="primary" @click="addUniversity">新增院校</el-button>
        <el-button type="warning" @click="handleInitialize">初始化</el-button>
      </div>
      <el-button type="success" @click="handleSaveUniversities">提交更改</el-button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { watch } from 'vue';
import { useSettingStore } from '@/stores/settingStore';
import { ElMessage, ElMessageBox } from 'element-plus';
import { onMounted } from 'vue';

const store = useSettingStore();

onMounted(async () => {
  try {
    await store.fetchUniversities();
  } catch (error) {
    ElMessage.error('加载院校数据失败');
  }
});

const addUniversity = () => {
  store.universities.push({ name: '', level: '' });
};

const removeUniversity = async (index: number) => {
  store.universities.splice(index, 1);
  await store.saveUniversities();
};

const handleInitialize = async () => {
  try {
    await ElMessageBox.confirm(
      '确定要初始化院校数据吗？这将覆盖当前所有数据。',
      '警告',
      {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning',
      }
    );
    await store.initializeUniversities();
    ElMessage.success('院校数据初始化成功');
  } catch (error) {
    if (error !== 'cancel') {
      ElMessage.error('院校数据初始化失败');
    }
  }
};

const handleSaveUniversities = async () => {
  try {
    await store.saveUniversities();
    ElMessage.success('院校数据提交成功');
  } catch (error) {
    ElMessage.error('院校数据提交失败');
  }
};

watch(() => store.universities, () => {
  if (!store.isInitializing) {
    ElMessage.warning('您已修改院校数据，请记得提交更改');
  }
}, { deep: true });
</script>