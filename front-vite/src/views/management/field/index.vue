<script setup lang="ts">
import { ref, computed } from "vue";
import {
  ElTable,
  ElTableColumn,
  ElSwitch,
  ElButton,
  ElDialog,
  ElForm,
  ElFormItem,
  ElInput,
  ElSelect,
  ElOption,
  ElMessageBox,
} from "element-plus";
import { ElMessage } from "element-plus";
import { useFieldStore } from "@/stores/fieldStore";
import type { FieldItem } from "@/apis/field";
import { importFields } from "@/scripts/importFields/importFields";

const store = useFieldStore();

// 初始化获取字段列表
store.fetchFields().then(() => {
  const fieldsInfo = store.fields.map(field => ({
    variableName: field.variableName,
    type: field.type
  }));
  console.log('Fields Info:', fieldsInfo);
});

// 字段类型选项
const fieldTypes = [
  { value: 'string', label: '字符串' },
  { value: 'percent', label: '百分比' },
  { value: 'boolean', label: '布尔值' },
  { value: 'select', label: '单选' },
  { value: 'date', label: '日期' },
  { value: 'number', label: '数字' },
];

// 表单区域选项
const regionOptions = [
  { value: '个人信息', label: '个人信息' },
  { value: '学历信息', label: '学历信息' },
  { value: '申请志愿', label: '申请志愿' },
  { value: '论文情况', label: '论文情况' },
  { value: '奖项', label: '奖项' },
  { value: '其他', label: '其他' },
];

// 对话框相关
const dialogVisible = ref(false);
const dialogTitle = ref("新增字段");
const editingField = ref<FieldItem>({
  id: 0,
  name: "",
  description: "",
  type: "text",
  showInTable: true,
  showInFilter: true,
  showInApply: true,
  showInRecommendMaster: true,
  showInExamMaster: true,
  showInPhd: true,
  showInDirectPhd: true,
  regionInForm: "其他",
});

// 打开新增对话框
const openAddDialog = () => {
  dialogTitle.value = "新增字段";
  editingField.value = {
    id: 0,
    name: "",
    description: "",
    showInTable: true,
    showInFilter: true,
    showInApply: true,
    showInRecommendMaster: true,
    showInExamMaster: true,
    showInPhd: true,
    showInDirectPhd: true,
    regionInForm: "其他",
  };
  isEditing.value = false;
  dialogVisible.value = true;
};
const isEditing = ref(false);

// 打开编辑对话框
const openEditDialog = (row: FieldItem) => {
  dialogTitle.value = "编辑字段";
  editingField.value = { ...row };
  isEditing.value = true;
  dialogVisible.value = true;
};

// 保存字段
const saveField = async () => {
  if (!editingField.value.name || !editingField.value.description) {
    ElMessage.warning("请填写完整信息");
    return;
  }

  const success = isEditing.value
    ? await store.editField(editingField.value)
    : await store.createField(editingField.value);

  if (success) {
    dialogVisible.value = false;
    await store.fetchFields(); // 添加这一行：成功保存后重新获取字段列表
  }
};

// 删除字段
const deleteField = async (row: FieldItem) => {
  await store.removeField(row.id);
};

// 添加新的处理函数
const handleSwitchChange = async (row: FieldItem) => {
  const success = await store.editField(row);
  if (success) {
    await store.fetchFields();
  }
};

// 初始化字段
const initializeFields = async () => {
  try {
    const result = await ElMessageBox.confirm(
      '此操作将清除所有现有字段并导入预设字段，是否继续？',
      '警告',
      {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning',
      }
    );

    if (result === 'confirm') {
      // 删除所有现有字段，使用Promise.all等待所有删除操作完成
      await Promise.all(store.fields.map(field => store.removeField(field.id)));
      
      // 导入预设字段
      await importFields();
      
      // 刷新字段列表
      await store.fetchFields();
      
      ElMessage.success('字段初始化完成');
    }
  } catch (error) {
    // 用户取消操作，不做任何处理
  }
};


// 计算不同区域的字段
const groupedFields = computed(() => {
  const groups: Record<string, FieldItem[]> = {};
  regionOptions.forEach(option => {
    groups[option.value] = store.fields.filter(field => field.regionInForm === option.value);
  });
  return groups;
});

// 当前激活的标签
const activeTab = ref('个人信息');
</script>

<template>
  <div class="p-6">
    <el-card>
      <template #header>
        <div class="flex justify-between items-center">
          <div class="flex items-start flex-col">
            <span class="text-xl font-bold">字段管理</span>
            <div class="text-gray-500 text-sm mt-1">
              前台申请表单与后台管理系统中使用的所有字段及其显示设置
            </div>
          </div>
          <div class="flex gap-2">
            <el-button type="warning" @click="initializeFields">初始化</el-button>
            <el-button type="primary" @click="openAddDialog">新增字段</el-button>
          </div>
        </div>
      </template>

      <el-tabs v-model="activeTab">
        <el-tab-pane
          v-for="option in regionOptions"
          :key="option.value"
          :label="option.label"
          :name="option.value"
        >
          <el-table :data="groupedFields[option.value]" border class="w-full">
            <el-table-column label="ID" min-width="80" type="index" :index="1" />
            <el-table-column prop="name" label="字段名称" min-width="120" />
            <el-table-column
              prop="description"
              label="描述"
              min-width="150"
              show-overflow-tooltip
            />
            <el-table-column label="字段类型" min-width="100">
              <template #default="{ row }">
                {{ fieldTypes.find(type => type.value === row.type)?.label || row.type }}
              </template>
            </el-table-column>
            <el-table-column label="在表格中显示" min-width="120" align="center">
              <template #default="{ row }">
                <el-switch v-model="row.showInTable" @change="() => handleSwitchChange(row)" />
              </template>
            </el-table-column>
            <el-table-column label="在申请页面显示" min-width="150" align="center">
              <template #default="{ row }">
                <el-switch v-model="row.showInApply" @change="() => handleSwitchChange(row)" />
              </template>
            </el-table-column>
            <el-table-column label="操作" min-width="150" align="center">
              <template #default="{ row }">
                <el-button type="primary" size="small" @click="openEditDialog(row)">编辑</el-button>
                <el-button type="danger" size="small" @click="deleteField(row)">删除</el-button>
              </template>
            </el-table-column>
          </el-table>
        </el-tab-pane>
      </el-tabs>
    </el-card>

    <!-- 新增/编辑对话框 -->
    <el-dialog
      v-model="dialogVisible"
      :title="dialogTitle"
      width="500px"
      destroy-on-close
    >
      <el-form :model="editingField" label-width="100px">
        <el-form-item label="字段名称" required>
          <el-input v-model="editingField.name" placeholder="请输入字段名称" />
        </el-form-item>
        <el-form-item label="描述" required>
          <el-input
            v-model="editingField.description"
            placeholder="请输入字段描述"
          />
        </el-form-item>
        <el-form-item label="字段类型" required>
          <el-select v-model="editingField.type" placeholder="请选择字段类型">
            <el-option
              v-for="type in fieldTypes"
              :key="type.value"
              :label="type.label"
              :value="type.value"
            />
          </el-select>
        </el-form-item>
        <el-form-item label="显示设置">
          <div class="flex gap-4 flex-wrap">
            <el-switch
              v-model="editingField.showInTable"
              active-text="表格显示"
            />
            <el-switch
              v-model="editingField.showInFilter"
              active-text="筛选显示"
            />
            <el-switch
              v-model="editingField.showInApply"
              active-text="申请显示"
            />
            <el-switch
              v-model="editingField.showInRecommendMaster"
              active-text="推免显示"
            />
            <el-switch
              v-model="editingField.showInExamMaster"
              active-text="考研显示"
            />
            <el-switch
              v-model="editingField.showInPhd"
              active-text="博士显示"
            />
            <el-switch
              v-model="editingField.showInDirectPhd"
              active-text="直博显示"
            />
          </div>
        </el-form-item>
        <el-form-item label="表单区域">
          <el-select
            v-model="editingField.regionInForm"
            placeholder="请选择表单区域"
          >
            <el-option
              v-for="option in regionOptions"
              :key="option.value"
              :label="option.label"
              :value="option.value"
            />
          </el-select>
        </el-form-item>
      </el-form>
      <template #footer>
        <div class="flex justify-end gap-2">
          <el-button @click="dialogVisible = false">取消</el-button>
          <el-button type="primary" @click="saveField">确定</el-button>
        </div>
      </template>
    </el-dialog>
  </div>
</template>

<style lang="scss" scoped>
.el-table {
  --el-table-border-color: #dcdfe6;
  --el-table-header-bg-color: #f5f7fa;

  :deep(th) {
    font-weight: 600;
    color: #606266;
  }
}

.el-dialog {
  :deep(.el-form-item__label) {
    font-weight: 500;
  }
}

.el-tabs {
  :deep(.el-tabs__header) {
    margin-bottom: 16px;
  }
}
</style>
