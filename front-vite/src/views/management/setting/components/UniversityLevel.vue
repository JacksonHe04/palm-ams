<template>
  <div>
    <el-table :data="store.universities" style="width: 100%" :empty-text="store.isInitializing ? '加载中...' : '暂无数据'">
      <el-table-column prop="name" label="院校名称">
        <template #default="{ row }">
          <el-input v-model="row.name" placeholder="请输入院校名称"></el-input>
        </template>
      </el-table-column>
      <el-table-column prop="level" label="等级">
        <template #default="{ row }">
          <el-select v-model="row.level" placeholder="选择等级">
            <el-option label="A" value="A"></el-option>
            <el-option label="B" value="B"></el-option>
            <el-option label="C" value="C"></el-option>
            <el-option label="国际前100" value="国际前100"></el-option>
            <el-option label="国际前200" value="国际前200"></el-option>
          </el-select>
        </template>
      </el-table-column>
      <el-table-column label="操作">
        <template #default="{ $index }">
          <el-button type="danger" @click="removeUniversity($index)" size="small">删除</el-button>
        </template>
      </el-table-column>
    </el-table>
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

const store = useSettingStore();

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