<script setup>
import { ref, onMounted } from 'vue'
import { useUserStore } from '@/stores/userStore'
import { ElMessage } from 'element-plus'

const userStore = useUserStore()
const showPasswordCard = ref(false)
const autoLoginDays = ref(userStore.autoLoginDays)

const userForm = ref({
  username: userStore.user?.username || '',
  phone: userStore.userInfo.phone || '',
  email: userStore.userInfo.email || '',
  oldPassword: '',
  newPassword: '',
  confirmPassword: ''
})

const handleSave = async () => {
  try {
    const updateData = {
      phone: userForm.value.phone,
      email: userForm.value.email,
      auto_login_days: autoLoginDays.value
    }

    if (showPasswordCard.value && userForm.value.newPassword) {
      if (userForm.value.newPassword !== userForm.value.confirmPassword) {
        ElMessage.error('两次输入的密码不一致')
        return
      }
      updateData.old_password = userForm.value.oldPassword
      updateData.new_password = userForm.value.newPassword
    }

    const success = await userStore.updateUserInfo(updateData)
    if (success) {
      ElMessage.success('保存成功')
      if (showPasswordCard.value) {
        resetPasswordForm()
      }
    } else {
      ElMessage.error('保存失败')
    }
  } catch (error) {
    ElMessage.error('保存失败')
  }
}

const handleLogout = () => {
  userStore.logout()
  ElMessage.success('退出登录成功')
}

const resetPasswordForm = () => {
  userForm.value.oldPassword = ''
  userForm.value.newPassword = ''
  userForm.value.confirmPassword = ''
  showPasswordCard.value = false
}

const incrementDays = () => {
  if (autoLoginDays.value < 30) {
    autoLoginDays.value++
  }
}

const decrementDays = () => {
  if (autoLoginDays.value > 1) {
    autoLoginDays.value--
  }
}

onMounted(async () => {
  await userStore.fetchUserInfo()
  userForm.value.phone = userStore.userInfo.phone
  userForm.value.email = userStore.userInfo.email
  autoLoginDays.value = userStore.autoLoginDays
})
</script>

<template>
  <div class="p-6">
    <el-card>
      <template #header>
        <div class="flex justify-between items-center">
          <div class="flex items-start flex-col">
            <span class="text-xl font-bold">账号设置</span>
            <div class="text-gray-500 text-sm mt-1">
              管理您的账户信息和安全设置
            </div>
          </div>
          <div class="flex gap-2">
            <el-button 
              type="primary" 
              @click="() => {
                showPasswordCard = true
                ElMessage.info('请填写密码信息')
              }"
              :disabled="showPasswordCard"
            >
              修改密码
            </el-button>
            <el-button type="danger" @click="handleLogout">
              退出登录
            </el-button>
          </div>
        </div>
      </template>

      <el-row :gutter="20">
        <el-col :span="12">
          <!-- 基本信息卡片 -->
          <el-card class="box-card">
            <template #header>
              <div class="card-header">
                <h3>基本信息</h3>
                <p class="text-secondary">管理您的个人资料</p>
              </div>
            </template>
            
            <el-form @submit.prevent="handleSave" label-position="top">
              <el-form-item label="用户名">
                <el-input v-model="userForm.username" disabled />
              </el-form-item>

              <el-form-item label="手机号码">
                <el-input v-model="userForm.phone" placeholder="请输入手机号码" />
              </el-form-item>

              <el-form-item label="邮箱地址">
                <el-input v-model="userForm.email" placeholder="请输入邮箱" type="email" />
              </el-form-item>

                  <div class="flex justify-between items-center mb-4">
                    <span class="text-base font-medium">自动登录设置</span>
                  </div>
                  <div class="flex justify-between items-center">
                  <el-form-item>
                    <el-input-number 
                      v-model="autoLoginDays"
                      :min="1"
                      :max="30"
                      controls-position="right"
                    />
                    <span class="days-text">天</span>
                  </el-form-item>
                <el-button type="primary" @click="handleSave">保存修改</el-button>
              </div>
            </el-form>
          </el-card>
        </el-col>

        <el-col :span="12">
          <!-- 修改密码卡片 -->
          <el-card v-if="showPasswordCard" class="box-card password-card">
            <template #header>
              <div class="card-header">
                <h3>修改密码</h3>
                <p class="text-secondary">设置新的账号密码</p>
              </div>
            </template>

            <el-form @submit.prevent="handleSave" label-position="top">
              <el-form-item label="原密码">
                <el-input 
                  v-model="userForm.oldPassword" 
                  type="password"
                  placeholder="请输入原密码"
                  show-password
                />
              </el-form-item>

              <el-form-item label="新密码">
                <el-input 
                  v-model="userForm.newPassword" 
                  type="password"
                  placeholder="请输入新密码"
                  show-password
                />
              </el-form-item>

              <el-form-item label="确认新密码">
                <el-input 
                  v-model="userForm.confirmPassword" 
                  type="password"
                  placeholder="请再次输入新密码"
                  show-password
                />
              </el-form-item>

              <div class="button-group">
                <el-button @click="resetPasswordForm">取消修改</el-button>
                <el-button type="primary" native-type="submit">确认修改</el-button>
              </div>
            </el-form>
          </el-card>
        </el-col>
      </el-row>
    </el-card>
  </div>
</template>

<style scoped>
.container {
  padding: 20px;
  background-color: #f5f7fa;
  min-height: 100vh;
}

.box-card {
  margin-bottom: 20px;
}

.card-header {
  margin-bottom: 20px;
}

.card-header h3 {
  margin: 0;
  font-size: 18px;
  font-weight: bold;
  color: #303133;
}

.text-secondary {
  color: #909399;
  font-size: 14px;
  margin-top: 4px;
}

.button-group {
  display: flex;
  justify-content: flex-end;
  gap: 12px;
  margin-top: 24px;
  padding-top: 24px;
  border-top: 1px solid #ebeef5;
}

.days-text {
  margin-left: 8px;
  color: #606266;
}

.password-card {
  transition: all 0.3s ease-in-out;
}
</style>
