<template>
  <RouterLink :to="path">
    <div class="recruitment-card">
      <div class="card-content">
        <div class="icon">
          <img :src="iconSrc" :alt="title" class="svg-icon" />
        </div>
        <div class="text-content">
          <h3>{{ title }}</h3>
          <div class="info">
            <template v-if="labelText">
              <p>{{ labelText }}:</p>
              <p>{{ description }}</p>
            </template>
            <template v-else>
              <p>{{ description }}</p>
            </template>
          </div>
          <div class="arrow">
            <p class="apply-text">立即申请</p>
            <p class="arrow-icon">→</p>
          </div>
        </div>
      </div>
    </div>
  </RouterLink>
</template>

<script setup lang="ts">
defineProps<{
  iconSrc: string;
  title: string;
  labelText?: string;
  description: string;
  path: string;
}>();
</script>

<style scoped>
.recruitment-card {
  border-radius: 12px;
  padding: 20px;
  position: relative;
  cursor: pointer;
  transition: all 0.3s ease;
  background-color: rgba(255, 255, 255, 0.8);
  border: 1px solid #eaedf2;
}

.recruitment-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
}

.card-content {
  display: flex;
  align-items: center;
  gap: 20px;
}

.icon {
  flex-shrink: 0;
  width: 160px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.svg-icon {
  height: 120px;
  width: auto;
  transition: transform 0.3s ease;
}

.recruitment-card:hover .svg-icon {
  transform: scale(1.05);
}

.text-content {
  flex-grow: 1;
  position: relative;
  padding-right: 0;
}

h3 {
  font-size: 20px;
  color: #2c3e50;
  margin-bottom: 15px;
  font-weight: 600;
  text-align: left;
}

.info {
  color: #5c6b7f;
  font-size: 14px;
  line-height: 1.6;
  text-align: left;
  margin-bottom: 20px;
}

.info p:first-child {
  color: #3a4b5c;
  font-weight: 500;
  margin-bottom: 4px;
}

.arrow {
  position: static;
  color: #5c6b7f;
  font-size: 15px;
  transition: all 0.5s ease;
  display: flex;
  justify-content: flex-start;
  align-items: center;
  padding: 4px 12px;
  width: 70%;
  border-radius: 15px;
  border: 1px solid #e0e0e0;
  margin-top: 10px;
}

.apply-text {
  margin: 0;
  text-align: left;
}

.arrow-icon {
  margin: 0;
  transform: translateX(10px);
  font-size: 20px;
  transition: all 0.3s ease;
}

.recruitment-card:hover .arrow-icon {
  transform: translateX(30px);
}

.recruitment-card:hover .arrow {
  border-color: #409eff;
  color: #409eff;
}
</style>