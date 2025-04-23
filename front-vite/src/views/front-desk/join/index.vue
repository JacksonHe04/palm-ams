<template>
  <div class="join-container mt-24">
    <div class="recruitment-grid">
      <JoinCard
        v-for="card in recruitmentCards"
        :key="card.title"
        v-bind="card"
      />
    </div>
  </div>
</template>

<script setup lang="ts">
import JoinCard from './components/JoinCard.vue';
import BaoyanIcon from '@/assets/svg/保研.svg';
import ZhiboIcon from '@/assets/svg/直博.svg';
import KaoyanIcon from '@/assets/svg/考研.svg';
import BoshiIcon from '@/assets/svg/博士.svg';

const recruitmentCards = [
  {
    iconSrc: BaoyanIcon,
    title: '硕士推免招生',
    labelText: '招收对象',
    description: '获得推免资格的优秀本科应届生'
  },
  {
    iconSrc: ZhiboIcon,
    title: '直博招生',
    labelText: '招收对象',
    description: '获得推免资格的优秀本科应届生'
  },
  {
    iconSrc: KaoyanIcon,
    title: '考研招生',
    labelText: '招收方向',
    description: '全国硕士研究生统一招生考试招生'
  },
  {
    iconSrc: BoshiIcon,
    title: '博士招生',
    labelText: '招收对象',
    description: '全年招收优秀博士研究生'
  }
];
</script>

<style scoped>
.join-container {
  padding: 40px 20px;
  min-height: 100vh;
}

.recruitment-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 30px;
  max-width: 1200px;
  margin: 0 auto;
}

@media (max-width: 768px) {
  .recruitment-grid {
    grid-template-columns: 1fr;
  }
}
</style>
