<template>
  <div class="dev-notice">
    <el-alert
      title="开发阶段提示"
      type="warning"
      description="本网站目前处于开发阶段，可能存在一些问题。如遇到任何问题，请发送邮件至 palmapplication@163.com，我们会尽快处理。"
      :closable="false"
      show-icon
    />
  </div>
</template>

<script setup lang="ts">
// 这是一个简单的开发阶段提示组件
</script>

<style lang="scss" scoped>
.dev-notice {
  @apply mb-6;
}
</style>