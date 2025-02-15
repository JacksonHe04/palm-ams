<script setup>
import { ref } from 'vue'
import { useUserStore } from '@/stores/userStore'

const userStore = useUserStore()
const showPasswordCard = ref(false)
const autoLoginDays = ref(7)

const userForm = ref({
  username: 'admin',
  phone: '',
  email: '',
  oldPassword: '',
  newPassword: '',
  confirmPassword: ''
})

const handleSave = async () => {
  try {
    if (showPasswordCard.value && userForm.value.newPassword) {
      if (userForm.value.newPassword !== userForm.value.confirmPassword) {
        alert('两次输入的密码不一致')
        return
      }
      // 这里添加修改密码的逻辑
    }
    // 这里添加保存用户信息的逻辑
    alert('保存成功')
    if (showPasswordCard.value) {
      resetPasswordForm()
    }
  } catch (error) {
    alert('保存失败')
  }
}

const handleLogout = () => {
  // 添加登出逻辑
  userStore.logout()
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
</script>

<template>
  <div class="min-h-screen bg-gray-50 py-8">
    <div class="max-w-6xl mx-auto px-4">
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
        <!-- 基本信息卡片 -->
        <div class="bg-white rounded-xl shadow-sm border border-gray-100">
          <div class="p-6 border-b border-gray-100">
            <h2 class="text-xl font-semibold text-gray-800">基本信息</h2>
            <p class="text-gray-500 text-sm mt-1">管理您的个人资料</p>
          </div>
          <div class="p-6">
            <form @submit.prevent="handleSave">
              <div class="flex flex-col items-center space-y-6">
                <div class="w-full flex flex-col items-center">
                  <label class="text-gray-700 font-medium mb-2 text-center w-full">用户名</label>
                  <div class="flex justify-center"> <!-- 添加此行 -->
                    <input
                      v-model="userForm.username"
                      type="text"
                      disabled
                      class="max-w-xs w-full px-4 py-2 rounded-lg bg-gray-100 border border-gray-200 focus:outline-none"
                    />
                  </div>
                </div>

                <div class="w-full flex flex-col items-center">
                  <label class="text-gray-700 font-medium mb-2 text-center w-full">手机号码</label>
                  <div class="flex justify-center"> <!-- 添加此行 -->
                    <input
                      v-model="userForm.phone"
                      type="tel"
                      placeholder="请输入手机号码"
                      class="max-w-xs w-full px-4 py-2 rounded-lg bg-gray-50 border border-gray-200 focus:outline-none focus:border-blue-500 hover:border-gray-300"
                    />
                  </div>
                </div>

                <div class="w-full flex flex-col items-center">
                  <label class="text-gray-700 font-medium mb-2 text-center w-full">邮箱地址</label>
                  <div class="flex justify-center"> <!-- 添加此行 -->
                    <input
                      v-model="userForm.email"
                      type="email"
                      placeholder="请输入邮箱"
                      class="max-w-xs w-full px-4 py-2 rounded-lg bg-gray-50 border border-gray-200 focus:outline-none focus:border-blue-500 hover:border-gray-300"
                    />
                  </div>
                </div>

                <div class="w-full flex flex-col items-center">
                  <label class="text-gray-700 font-medium mb-2 text-center w-full">自动登录设置</label>
                  <div class="flex items-center justify-center">
                    <div class="flex items-center border border-gray-200 rounded-lg bg-gray-50">
                      <button
                        type="button"
                        @click="decrementDays"
                        class="px-3 py-2 hover:bg-gray-100 rounded-l-lg"
                      >
                        -
                      </button>
                      <input
                        v-model="autoLoginDays"
                        type="number"
                        min="1"
                        max="30"
                        class="w-16 text-center bg-transparent border-0 focus:outline-none"
                      />
                      <button
                        type="button"
                        @click="incrementDays"
                        class="px-3 py-2 hover:bg-gray-100 rounded-r-lg"
                      >
                        +
                      </button>
                    </div>
                    <span class="ml-2 text-gray-600">天</span>
                  </div>
                </div>
              </div>

              <div class="flex items-center justify-between mt-8 pt-4 border-t border-gray-100 w-full">
                <button
                  type="button"
                  @click="showPasswordCard = true"
                  :disabled="showPasswordCard"
                  class="flex-1 mr-4 max-w-[160px] px-4 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600 disabled:opacity-50 disabled:cursor-not-allowed"
                >
                  修改密码
                </button>
                <button
                  type="button"
                  @click="handleLogout"
                  class="flex-1 max-w-[160px] px-4 py-2 bg-red-500 text-white rounded-lg hover:bg-red-600"
                >
                  退出登录
                </button>
              </div>
            </form>
          </div>
        </div>

        <!-- 修改密码卡片 -->
        <Transition
          enter-active-class="transition ease-out duration-200"
          enter-from-class="opacity-0 translate-x-4"
          enter-to-class="opacity-100 translate-x-0"
          leave-active-class="transition ease-in duration-150"
          leave-from-class="opacity-100 translate-x-0"
          leave-to-class="opacity-0 translate-x-4"
        >
          <div v-if="showPasswordCard" class="relative bg-white rounded-xl shadow-sm border border-gray-100">
            <div class="p-6 border-b border-gray-100 flex justify-center">
              <div class="flex items-center justify-between">
                <div>
                  <h2 class="text-xl font-semibold text-gray-800">修改密码</h2>
                  <p class="text-gray-500 text-sm mt-1">设置新的账号密码</p>
                </div>
              </div>
            </div>
            <div class="p-6">
              <form @submit.prevent="handleSave">
                <div class="flex flex-col items-center space-y-6">
                  <div class="w-full flex flex-col items-center">
                    <label class="text-gray-700 font-medium mb-2 text-center w-full">原密码</label>
                    <div class="flex justify-center"> <!-- 添加此行 -->
                      <input
                        v-model="userForm.oldPassword"
                        type="password"
                        placeholder="请输入原密码"
                        class="w-full px-4 py-2 rounded-lg bg-gray-50 border border-gray-200 focus:outline-none focus:border-blue-500 hover:border-gray-300"
                      />
                    </div>
                  </div>

                  <div class="w-full flex flex-col items-center">
                    <label class="text-gray-700 font-medium mb-2 text-center w-full">新密码</label>
                    <div class="flex justify-center"> <!-- 添加此行 -->
                      <input
                        v-model="userForm.newPassword"
                        type="password"
                        placeholder="请输入新密码"
                        class="w-full px-4 py-2 rounded-lg bg-gray-50 border border-gray-200 focus:outline-none focus:border-blue-500 hover:border-gray-300"
                      />
                    </div>
                  </div>

                  <div class="w-full flex flex-col items-center">
                    <label class="text-gray-700 font-medium mb-2 text-center w-full">确认新密码</label>
                    <div class="flex justify-center"> <!-- 添加此行 -->
                      <input
                        v-model="userForm.confirmPassword"
                        type="password"
                        placeholder="请再次输入新密码"
                        class="w-full px-4 py-2 rounded-lg bg-gray-50 border border-gray-200 focus:outline-none focus:border-blue-500 hover:border-gray-300"
                      />
                    </div>
                  </div>
                </div>

                <div class="absolute bottom-6 right-0 flex items-center justify-end gap-4 mt-8 pt-4 border-t border-gray-100 w-full"> <!-- 添加 w-full -->
                  <button
                    type="button"
                    @click="resetPasswordForm"
                    class="min-w-[100px] mr-6 px-4 py-2 border border-gray-200 rounded-lg hover:bg-gray-50"
                  >
                    取消修改
                  </button>
                  <button
                    type="submit"
                    class="min-w-[100px] mr-6 px-4 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600"
                  >
                    确认修改
                  </button>
                </div>
              </form>
            </div>
          </div>
        </Transition>
      </div>
    </div>
  </div>
</template>
