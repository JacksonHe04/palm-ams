<template>
  <div class="filter-config-container">
    <el-card class="filter-card">
      <template #header>
        <div class="card-header">
          <h2>表格过滤配置</h2>
          <el-button type="primary" @click="saveScheme">保存方案</el-button>
        </div>
      </template>

      <el-form :model="filterConfig" label-position="top">
        <el-form-item label="方案名称">
          <el-input v-model="schemeName" placeholder="输入方案名称"></el-input>
        </el-form-item>

        <el-form-item label="选择要过滤的字段">
          <el-select
            v-model="selectedFields"
            multiple
            collapse-tags
            collapse-tags-tooltip
            :max-collapse-tags="3"
            placeholder="选择字段"
          >
            <el-option
              v-for="field in availableFields"
              :key="field.name"
              :label="field.label"
              :value="field.name"
            ></el-option>
          </el-select>
        </el-form-item>

        <el-collapse v-model="activeNames">
          <el-collapse-item
            v-for="field in selectedFields"
            :key="field"
            :title="getFieldLabel(field)"
            :name="field"
          >
            <div class="field-filter">
              <template v-if="getFieldType(field) === 'string'">
                <el-select
                  v-model="filterConfig[field].operator"
                  placeholder="选择操作符"
                >
                  <el-option label="包含" value="contains"></el-option>
                  <el-option label="等于" value="equals"></el-option>
                  <el-option label="以...开头" value="startsWith"></el-option>
                  <el-option label="以...结尾" value="endsWith"></el-option>
                </el-select>
                <el-input
                  v-model="filterConfig[field].value"
                  placeholder="输入值"
                ></el-input>
              </template>
              <template v-else-if="getFieldType(field) === 'number'">
                <el-select
                  v-model="filterConfig[field].operator"
                  placeholder="选择操作符"
                >
                  <el-option label="大于" value="gt"></el-option>
                  <el-option label="小于" value="lt"></el-option>
                  <el-option label="等于" value="eq"></el-option>
                  <el-option label="不等于" value="neq"></el-option>
                </el-select>
                <el-input-number
                  v-model="filterConfig[field].value"
                  :controls="false"
                  placeholder="输入值"
                ></el-input-number>
              </template>
            </div>
          </el-collapse-item>
        </el-collapse>
      </el-form>
    </el-card>

    <el-card class="scheme-card">
      <template #header>
        <h3>已保存方案</h3>
      </template>
      <el-table :data="savedSchemes" style="width: 100%">
        <el-table-column prop="name" label="方案名称"></el-table-column>
        <el-table-column label="操作" width="200">
          <template #default="{ row }">
            <el-button @click="loadScheme(row)" type="primary" plain size="small">加载</el-button>
            <el-button @click="editScheme(row)" type="warning" plain size="small">编辑</el-button>
            <el-button @click="deleteScheme(row)" type="danger" plain size="small">删除</el-button>
          </template>
        </el-table-column>
      </el-table>
    </el-card>
  </div>
</template>


<script setup>
import { ref, reactive, computed, watch } from 'vue';
import { ElMessage } from 'element-plus'

// Sample available fields (replace with your actual fields)
const availableFields = [
  { name: 'name', label: 'Name', type: 'string' },
  { name: 'age', label: 'Age', type: 'number' },
  { name: 'email', label: 'Email', type: 'string' },
  { name: 'salary', label: 'Salary', type: 'number' },
  // Add more fields as needed
]

const schemeName = ref('')
const selectedFields = ref([])
const activeNames = ref([])
const filterConfig = reactive({})
const savedSchemes = ref([])

const getFieldLabel = (fieldName) => {
  const field = availableFields.find(f => f.name === fieldName)
  return field ? field.label : fieldName
}

const getFieldType = (fieldName) => {
  const field = availableFields.find(f => f.name === fieldName)
  return field ? field.type : 'string'
}

const saveScheme = () => {
  if (!schemeName.value) {
    ElMessage.warning('Please enter a scheme name')
    return
  }

  const scheme = {
    name: schemeName.value,
    fields: selectedFields.value,
    config: JSON.parse(JSON.stringify(filterConfig))
  }

  const existingIndex = savedSchemes.value.findIndex(s => s.name === scheme.name)
  if (existingIndex !== -1) {
    savedSchemes.value[existingIndex] = scheme
    ElMessage.success('Scheme updated successfully')
  } else {
    savedSchemes.value.push(scheme)
    ElMessage.success('Scheme saved successfully')
  }

  schemeName.value = ''
}

const loadScheme = (scheme) => {
  schemeName.value = scheme.name
  selectedFields.value = scheme.fields
  Object.assign(filterConfig, scheme.config)
  activeNames.value = scheme.fields
  ElMessage.success('Scheme loaded successfully')
}

const editScheme = (scheme) => {
  loadScheme(scheme)
}

const deleteScheme = (scheme) => {
  const index = savedSchemes.value.findIndex(s => s.name === scheme.name)
  if (index !== -1) {
    savedSchemes.value.splice(index, 1)
    ElMessage.success('Scheme deleted successfully')
  }
}

// Watch for changes in selectedFields to update filterConfig
watch(selectedFields, (newFields) => {
  const newConfig = {}
  newFields.forEach(field => {
    if (!filterConfig[field]) {
      newConfig[field] = { operator: '', value: '' }
    } else {
      newConfig[field] = filterConfig[field]
    }
  })
  Object.assign(filterConfig, newConfig)
})
</script>

<style scoped>
.filter-config-container {
  display: flex;
  gap: 20px;
  padding: 20px;
  background-color: #f0f2f5;
  min-height: 100vh;
}

.filter-card, .scheme-card {
  flex: 1;
  max-width: 600px;
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.field-filter {
  display: flex;
  gap: 10px;
  margin-bottom: 10px;
}

.el-select {
  width: 150px;
}

.el-input, .el-input-number {
  width: 200px;
}

.el-collapse-item {
  margin-bottom: 10px;
}
</style>