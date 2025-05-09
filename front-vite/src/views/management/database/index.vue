<template>
    <div class="dev-notice">
    <el-alert
      title="开发阶段提示"
      type="warning"
      description="请勿对当前数据库中的数据进行修改，否则可能导致数据不一致。"
      :closable="false"
      show-icon
      center
    />
  </div>
  <div class="database-management">
    <!-- 顶部操作栏 -->
    <div class="operation-bar">
      <el-select v-model="currentDatabase" class="database-select" @change="handleDatabaseChange">
        <el-option label="Apply数据库" value="apply" />
        <el-option label="Files数据库" value="files" />
      </el-select>
      <el-button type="primary" @click="handleAdd">新增申请</el-button>
      <el-popover placement="bottom" :width="300" trigger="click">
        <template #reference>
          <el-button>列显示设置</el-button>
        </template>
        <el-checkbox-group v-model="selectedFields">
          <el-checkbox 
            v-for="field in fields" 
            :key="field.name" 
            :label="field.name"
          >
            {{ field.name }}
          </el-checkbox>
        </el-checkbox-group>
      </el-popover>
    </div>

    <!-- 数据表格 -->
    <el-table 
      :data="sortedRecords" 
      style="width: 100%"
      v-loading="loading"
      border
    >
      <el-table-column
        type="index"
        label="#"
        width="70"
        align="center"
        fixed="left"
      />
      <template v-for="field in fields" :key="field.name">
        <el-table-column
          v-if="selectedFields.includes(field.name)"
          :prop="field.name"
          :label="field.name"
          sortable
          show-overflow-tooltip
          :min-width="200"
          :width="field.name === 'id' ? 100 : null"
          :fixed="field.name === 'name' ? 'left' : null"
          >
          <template #default="scope">
            <template v-if="field.name === 'download_url' && currentDatabase === 'files'">
              <el-link 
                type="primary" 
                :href="getFileDownloadUrl(scope.row[field.name])"
                target="_blank"
              >
                {{ scope.row[field.name] || '下载文件' }}
              </el-link>
            </template>
            <span v-else>{{ scope.row[field.name] }}</span>
          </template>
        </el-table-column>
      </template>
      
      <el-table-column label="操作" width="180" fixed="right">
        <template #default="scope">
          <el-button-group>
            <el-button size="small" @click="handleEdit(scope.row)">编辑</el-button>
            <el-button 
              size="small" 
              type="danger" 
              @click="handleDelete(scope.row)"
            >删除</el-button>
          </el-button-group>
        </template>
      </el-table-column>
    </el-table>

    <!-- 编辑/新增对话框 -->
    <el-dialog
      v-model="dialogVisible"
      :title="dialogType === 'add' ? '新增申请' : '编辑申请'"
      width="50%"
    >
      <el-form 
        ref="formRef"
        :model="formData"
        label-width="120px"
      >
        <template v-for="field in fields" :key="field.name">
          <el-form-item 
            :label="field.name"
            :prop="field.name"
            v-if="field.name !== 'id'"
          >
            <el-input 
              v-model="formData[field.name]"
              :placeholder="`请输入${field.name}`"
              :disabled="field.name === 'id'"
            />
          </el-form-item>
        </template>
      </el-form>
      <template #footer>
        <span class="dialog-footer">
          <el-button @click="dialogVisible = false">取消</el-button>
          <el-button type="primary" @click="handleSubmit">确定</el-button>
        </span>
      </template>
    </el-dialog>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, computed } from 'vue'
import { ElMessage, ElMessageBox } from 'element-plus'
import request from '@/utils/http'
import {
  getAllApplyData,
  createApplyRecord,
  updateApplyRecord,
  deleteApplyRecord
} from '@/apis/databaseApply'
import { getFileDownloadUrl } from '@/apis/files';
// 假设我们有一个新的API文件用于files数据库操作
import {
  getAllFilesData,
  createFileRecord,
  updateFileRecord,
  deleteFileRecord
} from '@/apis/databaseFiles'
import type { ApplyField, ApplyRecord } from '@/apis/databaseApply'

// 数据状态
const currentDatabase = ref('apply') // 默认选择Apply数据库
const records = ref<ApplyRecord[]>([])
const fields = ref<ApplyField[]>([])
const loading = ref(false)
const selectedFields = ref<string[]>([])

// 对话框状态
const dialogVisible = ref(false)
const dialogType = ref<'add' | 'edit'>('add')
const formData = ref<Partial<ApplyRecord>>({})
const formRef = ref()

// 计算排序后的记录
const sortedRecords = computed(() => {
  return [...records.value]
})

// 处理数据库切换
const handleDatabaseChange = async () => {
  await initData()
}

// 初始化数据
const initData = async () => {
  loading.value = true
  try {
    let response
    if (currentDatabase.value === 'apply') {
      response = await getAllApplyData()
    } else {
      response = await getAllFilesData()
    }
    records.value = response.data.records
    fields.value = response.data.fields
    // 初始化选中所有字段
    selectedFields.value = response.data.fields.map(field => field.name)
  } catch (error) {
    ElMessage.error('获取数据失败')
  } finally {
    loading.value = false
  }
}

// 新增按钮处理
const handleAdd = () => {
  dialogType.value = 'add'
  formData.value = {}
  dialogVisible.value = true
}

// 编辑按钮处理
const handleEdit = (row: ApplyRecord) => {
  dialogType.value = 'edit'
  formData.value = { ...row }
  dialogVisible.value = true
}

// 提交表单处理
const handleSubmit = async () => {
  try {
    if (dialogType.value === 'add') {
      if (currentDatabase.value === 'apply') {
        await createApplyRecord(formData.value)
      } else {
        await createFileRecord(formData.value)
      }
      ElMessage.success('创建成功')
    } else {
      if (currentDatabase.value === 'apply') {
        await updateApplyRecord(formData.value.id!, formData.value)
      } else {
        await updateFileRecord(formData.value.id!, formData.value)
      }
      ElMessage.success('更新成功')
    }
    dialogVisible.value = false
    initData()
  } catch (error) {
    ElMessage.error('操作失败')
  }
}

// 删除按钮处理
const handleDelete = async (row: ApplyRecord) => {
  try {
    await ElMessageBox.confirm('确定要删除这条记录吗？', '警告', {
      type: 'warning'
    })
    if (currentDatabase.value === 'apply') {
      await deleteApplyRecord(row.id)
    } else {
      await deleteFileRecord(row.id)
    }
    ElMessage.success('删除成功')
    initData()
  } catch (error) {
    if (error !== 'cancel') {
      ElMessage.error('删除失败')
    }
  }
}

// 页面加载时获取数据
onMounted(() => {
  initData()
})
</script>

<style scoped>
.database-management {
  padding: 20px;
}

.operation-bar {
  margin-bottom: 20px;
  display: flex;
  gap: 10px;
}

.database-select {
  width: 160px;
}
</style>