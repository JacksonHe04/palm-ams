<template>
  <div class="wait">
    <div class="wait-content">
      <div class="success-icon">
        <svg class="h-24 w-24 text-green-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
        </svg>
      </div>
      <h1 class="wait-title">申请提交成功！</h1>
      <p class="wait-description">
        您的申请已成功提交，我们将尽快进行审核。<br>
        审核结果将通过邮件通知您，请注意查收。
      </p>
      <div class="action-form">
        <RouterLink to="/">
          <el-button type="primary" size="large">返回首页</el-button>
        </RouterLink>
      </div>
    </div>
  </div>
</template>

<style scoped lang="scss">
$primary-color: #3b82f6;
$secondary-color: #1f2937;
$text-color: #6b7280;
$white-color: white;
$success-color: #10b981;

.wait {
  padding: 60px 0;
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 60vh;
}

.wait-content {
  max-width: 600px;
}

.success-icon {
  margin-bottom: 24px;
  color: $success-color;
  display: flex;
  justify-content: flex-start;
}

.wait-title {
  font-size: 24px;
  line-height: 1.2;
  color: $secondary-color;
  margin-bottom: 24px;
  text-align: left;
  font-weight: bold;
}

.wait-description {
  font-size: 24px;
  color: $text-color;
  margin-bottom: 22px;
  line-height: 1.6;
  text-align: left;
}

.action-form {
  display: flex;
  gap: 16px;
  margin-bottom: 16px;
  max-width: 480px;
}

@media (max-width: 768px) {
  .wait {
    grid-template-columns: 1fr;
    text-align: center;
  }

  .wait-title {
    font-size: 48px;
    text-align: center;
  }

  .wait-description {
    text-align: center;
  }

  .success-icon {
    justify-content: center;
  }

  .action-form {
    justify-content: center;
  }
}
</style>
