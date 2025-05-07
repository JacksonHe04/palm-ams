<template>
  <div>
    <el-table 
      :data="store.personnel" 
      style="width: 100%"
      row-key="name"
      :row-class-name="tableRowClassName"
    >
      <el-table-column width="40">
        <template #default>
          <el-icon class="move-icon cursor-move"><Rank /></el-icon>
        </template>
      </el-table-column>
      <el-table-column prop="order" label="序号" width="60">
        <template #default="{ row }">
          {{ row.order + 1 }}
        </template>
      </el-table-column>
      <el-table-column prop="name" label="姓名">
        <template #default="{ row }">
          <el-input v-model="row.name" placeholder="请输入姓名"></el-input>
        </template>
      </el-table-column>
      <el-table-column prop="recruitment_type" label="招生类型">
        <template #default="{ row }">
          <el-select v-model="row.recruitment_type" placeholder="选择招生类型">
            <el-option label="博士生、直博生、硕士生" value="博士生、直博生、硕士生"></el-option>
            <el-option label="硕士生" value="硕士生"></el-option>
            <el-option label="博士生、直博生" value="博士生、直博生"></el-option>
            <el-option label="暂不招生" value="暂不招生"></el-option>
          </el-select>
        </template>
      </el-table-column>
      <el-table-column prop="department" label="所属院系">
        <template #default="{ row }">
          <el-input v-model="row.department" placeholder="请输入所属院系"></el-input>
        </template>
      </el-table-column>
      <el-table-column prop="research_direction" label="研究方向">
        <template #default="{ row }">
          <el-input v-model="row.research_direction" placeholder="请输入研究方向"></el-input>
        </template>
      </el-table-column>
      <el-table-column label="操作">
        <template #default="{ $index }">
          <el-button type="danger" @click="removePersonnel($index)" size="small">删除</el-button>
        </template>
      </el-table-column>
    </el-table>
    <div class="mt-4 flex justify-between">
      <div class="flex gap-4">
        <el-button type="primary" @click="addPersonnel">新增人员</el-button>
      </div>
      <el-button type="success" @click="handleSavePersonnel">提交更改</el-button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { watch, onMounted, ref } from 'vue';
import { useSettingStore } from '@/stores/settingStore';
import { ElMessage, ElMessageBox } from 'element-plus';
import { Rank } from '@element-plus/icons-vue';
import Sortable from 'sortablejs';

const store = useSettingStore();

onMounted(async () => {
  try {
    await store.fetchPersonnel();
  } catch (error) {
    ElMessage.error('加载专业数据失败');
  }
});

const addPersonnel = () => {
  store.personnel.push({
    name: '',
    recruitment_type: '',
    department: '',
    research_direction: '',
    order: store.personnel.length  // 将order设置为当前数组长度
  });
};

const removePersonnel = async (index: number) => {
  store.personnel.splice(index, 1);
  await store.savePersonnel();
};

const handleSavePersonnel = async () => {
  try {
    await store.savePersonnel();
    ElMessage.success('人员数据提交成功');
  } catch (error) {
    ElMessage.error('人员数据提交失败');
  }
};

// 初始化拖拽排序功能
onMounted(() => {
  const tbody = document.querySelector('.el-table__body-wrapper tbody');
  if (tbody) {
    new Sortable(tbody, {
      handle: '.move-icon',
      animation: 150,
      onEnd: ({ newIndex, oldIndex }) => {
        if (typeof newIndex === 'number' && typeof oldIndex === 'number') {
          const currRow = store.personnel.splice(oldIndex, 1)[0];
          store.personnel.splice(newIndex, 0, currRow);
          
          // 更新所有人员的order属性
          store.personnel.forEach((person, index) => {
            person.order = index;
          });
          
          ElMessage.warning('您已修改人员顺序，请记得提交更改');
        }
      },
    });
  }
});

// 添加表格行的类名，用于拖拽样式
const tableRowClassName = () => {
  return 'draggable-row';
};

watch(() => store.personnel, () => {
  if (!store.isInitializing) {
    ElMessage.warning('您已修改人员数据，请记得提交更改');
  }
}, { deep: true });
</script>

<style scoped>
.move-icon {
  cursor: move;
  font-size: 16px;
  color: #909399;
}

.draggable-row {
  cursor: move;
}

.draggable-row:hover {
  background-color: #f5f7fa;
}

:deep(.el-table__row.sortable-ghost) {
  background-color: #e6f1fe;
}
</style>