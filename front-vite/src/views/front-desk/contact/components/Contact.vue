<script setup lang="ts">
import { ElCard, ElDivider } from "element-plus";
import FrontMain from "@/views/front-desk/components/FrontMain.vue";
</script>

<template>
  <FrontMain>
    <div class="contact-container">
      <ElCard class="contact-card">
        <div class="contact-content">
          <h2 class="text-2xl font-bold mb-6 text-center text-gray-800">
            联系我们
          </h2>

          <div class="email-section">
            <p class="text-lg font-medium mb-2">邮箱地址</p>
            <p class="text-xl font-semibold text-blue-600 mb-4">
              palmapplication@163.com
            </p>
          </div>

          <ElDivider />

          <div class="instruction-section">
            <h3 class="text-lg font-medium mb-3">发送邮件须知</h3>
            <ul class="text-gray-700 space-y-2 text-left">
              <li>• 请在邮件中注明您的基本信息：</li>
              <li class="ml-4">- 学校</li>
              <li class="ml-4">- 姓名</li>
              <li class="ml-4">- 申请类型</li>
              <li>• 详细描述您遇到的问题、建议或看法</li>
              <li>• 请在邮件中附上相关材料，如截图等</li>
            </ul>
          </div>

          <ElDivider />

          <div class="promise-section text-center">
            <p class="text-gray-700 mb-2">我们会尽快回复并解决您提出的问题</p>
            <p class="text-gray-600">感谢您的支持与建议！</p>
          </div>
        </div>
      </ElCard>
    </div>
  </FrontMain>
</template>

<style scoped lang="scss">
.contact-container {
  @apply p-4 max-w-3xl mx-auto;

  .contact-card {
    @apply bg-white rounded-lg shadow-md;

    .contact-content {
      @apply p-6;
    }

    .email-section {
      @apply text-center mb-6;
    }

    .instruction-section {
      @apply mb-6;
    }

    .promise-section {
      @apply mt-6;
    }
  }
}

/* 移动端适配 */
@media (max-width: 640px) {
  .contact-container {
    @apply p-2;

    .contact-card {
      .contact-content {
        @apply p-4;
      }
    }
  }
}
</style>
