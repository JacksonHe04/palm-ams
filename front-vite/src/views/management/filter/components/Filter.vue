<script setup lang="ts">
import { ref, onMounted, computed } from 'vue'
import { useFieldStore } from '@/stores/fieldStore'
import { useFilterStore } from '@/stores/filterStore'
import type { FieldItem } from '@/apis/field'
import {
  ElCard,
  ElButton,
  ElSwitch,
  ElDialog,
  ElForm,
  ElFormItem,
  ElInput,
  ElSelect,
  ElOption,
  ElInputNumber,
  ElTag,
} from 'element-plus'
import { initializeFilterSchemes } from '@/scripts/filterInit/filterInit'

const fieldStore = useFieldStore()
const filterStore = useFilterStore()

// 初始化时获取筛选方案列表
onMounted(() => {
  filterStore.fetchSchemes()
  fieldStore.fetchFields()
})

// 筛选方案列表
const filterSchemes = computed(() => filterStore.schemes)

// 对话框控制
const dialogVisible = ref(false)
const dialogTitle = ref('新增筛选方案')
const isEditing = ref(false)

// 当前编辑的方案
const currentScheme = ref<FilterScheme>({
  id: 0,
  name: '',
  enabled: true,
  conditions: []
})

// 打开新增对话框
const openAddDialog = () => {
  dialogTitle.value = '新增筛选方案'
  currentScheme.value = {
    id: filterSchemes.value.length + 1,
    name: '',
    enabled: true,
    conditions: []
  }
  isEditing.value = false
  dialogVisible.value = true
}

// 打开编辑对话框
const openEditDialog = (scheme: FilterScheme) => {
  dialogTitle.value = '编辑筛选方案'
  currentScheme.value = JSON.parse(JSON.stringify(scheme))
  isEditing.value = true
  dialogVisible.value = true
}

// 保存筛选方案
const saveScheme = async () => {
  const schemeData = {
    name: currentScheme.value.name,
    enabled: currentScheme.value.enabled,
    conditions: currentScheme.value.conditions
  }

  if (isEditing.value) {
    await filterStore.updateScheme(currentScheme.value.id, schemeData)
  } else {
    await filterStore.createScheme(schemeData)
  }
  dialogVisible.value = false
}

// 删除筛选方案
const deleteScheme = async (scheme: FilterScheme) => {
  await filterStore.deleteScheme(scheme.id)
}

// 切换方案启用状态
const toggleScheme = async (scheme: FilterScheme) => {
  await filterStore.toggleScheme(scheme.id, !scheme.enabled)
}
// 初始化筛选方案
const initializeSchemes = async () => {
  try {
    await ElMessageBox.confirm(
      '确定要初始化筛选方案吗？这将覆盖当前所有数据。',
      '警告',
      {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning',
      }
    );
    const success = await initializeFilterSchemes()
    if (success) {
      ElMessage.success('筛选方案初始化成功')
      filterStore.fetchSchemes()
    } else {
      ElMessage.error('筛选方案初始化失败')
    }
  } catch (error) {
    if (error !== 'cancel') {
      ElMessage.error('筛选方案初始化失败')
    }
  }
}

// 操作符选项
const operatorOptions = [
  { value: '=', label: '等于' },
  { value: '!=', label: '不等于' },
  { value: '>', label: '大于' },
  { value: '>=', label: '大于等于' },
  { value: '<', label: '小于' },
  { value: '<=', label: '小于等于' },
  { value: 'in', label: '包含' },
  { value: 'not in', label: '不包含' }
]

// 可筛选字段
const filterableFields = computed(() => {
  return fieldStore.fields.filter(field => field.showInFilter)
})

// 获取字段类型
const getFieldType = (fieldName: string) => {
  const field = filterableFields.value.find(f => f.name === fieldName)
  return field ? field.type : 'string'
}

// 添加条件
const addCondition = () => {
  currentScheme.value.conditions.push({
    field: '',
    operator: '=',
    value: ''
  })
}

// 移除条件
const removeCondition = (index: number) => {
  currentScheme.value.conditions.splice(index, 1)
}
</script>

<template>
  <div class="p-6">
    <div class="flex justify-between items-center mb-6">
      <h2 class="text-2xl font-bold">筛选方案管理</h2>
      <div class="flex gap-2">
        <el-button type="info" @click="$router.push('filtered')">进入筛选后的表格</el-button>
        <el-button type="primary" @click="openAddDialog">新增方案</el-button>
        <el-button type="success" @click="initializeSchemes">初始化</el-button>
      </div>
    </div>

    <div class="grid gap-4">
      <el-card v-for="scheme in filterSchemes" :key="scheme.id" class="scheme-card">
        <div class="flex justify-between items-center mb-4">
          <div class="flex items-center gap-4">
            <h3 class="text-lg font-semibold">{{ scheme.name }}</h3>
            <el-switch v-model="scheme.enabled" @change="() => toggleScheme(scheme)" />
          </div>
          <div class="flex gap-2">
            <el-button type="primary" size="small" @click="openEditDialog(scheme)">编辑</el-button>
            <el-button type="danger" size="small" @click="deleteScheme(scheme)">删除</el-button>
          </div>
        </div>
        <div class="conditions-container">
          <el-tag
            v-for="(condition, index) in scheme.conditions"
            :key="index"
            class="mr-2 mb-2"
          >
            {{ condition.field }} {{ condition.operator }} {{ Array.isArray(condition.value) ? condition.value.join('、') : condition.value }}
          </el-tag>
        </div>
      </el-card>
    </div>

    <!-- 新增/编辑对话框 -->
    <el-dialog
      v-model="dialogVisible"
      :title="dialogTitle"
      width="800px"
      destroy-on-close
    >
      <el-form :model="currentScheme" label-width="100px">
        <el-form-item label="方案名称" required>
          <el-input v-model="currentScheme.name" placeholder="请输入方案名称" />
        </el-form-item>
        <el-form-item label="启用状态">
          <el-switch v-model="currentScheme.enabled" />
        </el-form-item>
        <el-form-item label="筛选条件">
          <div class="conditions-editor">
            <div v-for="(condition, index) in currentScheme.conditions" :key="index" class="condition-item">
              <el-select v-model="condition.field" placeholder="选择字段" class="field-select">
                <el-option
                  v-for="field in filterableFields"
                  :key="field.name"
                  :label="field.name"
                  :value="field.name"
                />
              </el-select>
              <el-select v-model="condition.operator" placeholder="选择操作符" class="operator-select">
                <el-option
                  v-for="op in operatorOptions"
                  :key="op.value"
                  :label="op.label"
                  :value="op.value"
                />
              </el-select>
              <template v-if="condition.operator === 'in' || condition.operator === 'not in'">
                <el-select
                  v-model="condition.value"
                  multiple
                  filterable
                  allow-create
                  default-first-option
                  placeholder="输入值"
                  class="value-input"
                />
              </template>
              <template v-else-if="getFieldType(condition.field) === 'number'">
                <el-input-number
                  v-model="condition.value"
                  :controls="false"
                  placeholder="输入值"
                  class="value-input"
                />
              </template>
              <template v-else>
                <el-input
                  v-model="condition.value"
                  placeholder="输入值"
                  class="value-input"
                />
              </template>
              <el-button
                type="danger"
                circle
                size="small"
                @click="removeCondition(index)"
              >
                <i class="el-icon-delete">×</i>
              </el-button>
            </div>
            <el-button type="primary" plain @click="addCondition">添加条件</el-button>
          </div>
        </el-form-item>
      </el-form>
      <template #footer>
        <div class="flex justify-end gap-2">
          <el-button @click="dialogVisible = false">取消</el-button>
          <el-button type="primary" @click="saveScheme">确定</el-button>
        </div>
      </template>
    </el-dialog>
  </div>
</template>

<style lang="scss" scoped>
.scheme-card {
  @apply bg-white rounded-lg shadow-sm;

  .conditions-container {
    min-height: 32px;
  }
}

.conditions-editor {
  .condition-item {
    @apply flex items-center gap-3 mb-3;
    flex-wrap: wrap;
    padding: 10px;
    background-color: #f5f7fa;
    border-radius: 8px;
  }

  .field-select {
    width: 200px;
  }

  .operator-select {
    width: 150px;
  }

  .value-input {
    width: 300px;
    max-width: 100%;
  }
}
</style>