<template>
  <div class="hero">
    <div class="hero-content">
      <h1 class="hero-title">PAttern Learning and Mining(PALM) Lab</h1>
      <p class="hero-description">
        PALM
        实验室隶属东南大学计算机科学与工程学院，地点位于东南大学九龙湖校区计算机楼，主要从事数据挖掘与知识发现、机器学习、模式识别以及相关领域的基础性、前沿性、创新性的研究工作。
      </p>
      <div class="email-form">
        <RouterLink to="/join">
          <el-button type="primary" size="large">申请加入我们</el-button>
        </RouterLink>
      </div>
      <!-- <p class="trial-text">
        ✉️ We will send an email to notify you after your resume is approved.
      </p> -->
    </div>

    <div class="hero-image">
      <div class="achievement-badge">
        <div style="display: flex; align-items: center; gap: 8px">
          <div>
            <div style="font-weight: bold; font-size: 20px">100+</div>
            <div style="font-size: 14px; color: #6b7280">Students</div>
          </div>
        </div>
      </div>
      <img src="/lib.png" alt="home-img" class="home-img" />
      <div class="users-badge">
        <div style="font-weight: bold; font-size: 20px">25+</div>
        <div style="font-size: 14px; color: #6b7280">Mentors</div>
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

.hero {
  padding: 60px 0;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 48px;
  align-items: center;
}

.hero-content {
  max-width: 600px;
}

.hero-title {
  font-size: 48px;
  line-height: 1.2;
  color: $secondary-color;
  margin-bottom: 24px;
  text-align: left;
  font-weight: bold;
}

.hero-description {
  font-size: 18px;
  color: $text-color;
  margin-bottom: 22px;
  line-height: 1.6;
  text-align: left;
}

.email-form {
  display: flex;
  gap: 16px;
  margin-bottom: 16px;
  max-width: 480px;
}

.trial-text {
  color: $text-color;
  font-size: 14px;
  display: flex;
  align-items: center;
  gap: 8px;
}

.hero-image {
  position: relative;
}

.achievement-badge {
  position: absolute;
  top: 0;
  right: 0;
  background: $white-color;
  padding: 16px;
  border-radius: 12px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.users-badge {
  position: absolute;
  bottom: 0;
  right: 0;
  background: $white-color;
  padding: 16px;
  border-radius: 12px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  text-align: center;
}

.home-img {
  width: 100%;
  max-width: 600px;
  height: auto;
  border-radius: 12px;
}

@media (max-width: 768px) {
  .hero {
    grid-template-columns: 1fr;
  }

  .hero-title {
    font-size: 36px;
  }
}
</style>
<script setup lang="ts"></script>
