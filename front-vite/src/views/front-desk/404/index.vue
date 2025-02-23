<template>
  <div class="not-found">
    <div class="not-found-content">
      <h1 class="not-found-title">404</h1>
      <p class="not-found-description">
        抱歉，您访问的页面不存在
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
$hover-bg-color: wheat;

.not-found {
  padding: 60px 0;
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 60vh;
}

.not-found-content {
  max-width: 600px;
}

.not-found-title {
  font-size: 72px;
  line-height: 1.2;
  color: $secondary-color;
  margin-bottom: 24px;
  text-align: left;
  font-weight: bold;
}

.not-found-description {
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
  .not-found {
    grid-template-columns: 1fr;
    text-align: center;
  }

  .not-found-title {
    font-size: 48px;
    text-align: center;
  }

  .not-found-description {
    text-align: center;
  }

  .action-form {
    justify-content: center;
  }
}
</style>