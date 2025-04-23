<template>
  <div class="join-container mt-24">
    <div class="recruitment-grid">
      <!-- 保研通道 -->
      <RouterLink to="/apply">
        <!-- 考研招生 -->
        <div class="recruitment-card">
          <div class="card-content">
            <div class="icon">
              <img
                src="@/assets/svg/保研.svg"
                alt="保研通道"
                class="svg-icon"
              />
            </div>
            <div class="text-content">
              <h3>保研通道</h3>
              <div class="info">
                <p>面向人群:</p>
                <p>应届优秀本科毕业生</p>
              </div>
              <div class="arrow">→</div>
            </div>
          </div>
        </div>
      </RouterLink>

      <!-- 直博项目 -->
      <div class="recruitment-card">
        <div class="card-content">
          <div class="icon">
            <img src="@/assets/svg/直博.svg" alt="直博项目" class="svg-icon" />
          </div>
          <div class="text-content">
            <h3>直博项目</h3>
            <div class="info">
              <p>招收对象:</p>
              <p>优秀应届本科生</p>
            </div>
            <div class="arrow">→</div>
          </div>
        </div>
      </div>

      <!-- 考研招生 -->
      <div class="recruitment-card">
        <div class="card-content">
          <div class="icon">
            <img src="@/assets/svg/考研.svg" alt="考研招生" class="svg-icon" />
          </div>
          <div class="text-content">
            <h3>考研招生</h3>
            <div class="info">
              <p>招收方向:</p>
              <p>计算机、人工智能等相关专业</p>
            </div>
            <div class="arrow">→</div>
          </div>
        </div>
      </div>

      <!-- 博士招生 -->
      <div class="recruitment-card">
        <div class="card-content">
          <div class="icon">
            <img src="@/assets/svg/博士.svg" alt="博士招生" class="svg-icon" />
          </div>
          <div class="text-content">
            <h3>博士招生</h3>
            <div class="info">
              <p>全年招收优秀博士研究生</p>
            </div>
            <div class="arrow">→</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

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

.recruitment-card {
  border-radius: 12px;
  padding: 20px;
  position: relative;
  cursor: pointer;
  transition: all 0.3s ease;
  background-color: #fff;
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
  padding-right: 30px;
}

h3 {
  font-size: 20px;
  color: #2c3e50;
  margin-bottom: 15px;
}

.info {
  color: #5c6b7f;
  font-size: 14px;
  line-height: 1.6;
}

.info p:first-child {
  color: #3a4b5c;
  font-weight: 500;
  margin-bottom: 4px;
}

.arrow {
  position: absolute;
  right: 0;
  bottom: 0;
  color: #409eff;
  font-size: 20px;
  transition: transform 0.3s ease;
}

.recruitment-card:hover .arrow {
  transform: translateX(5px);
}

@media (max-width: 768px) {
  .recruitment-grid {
    grid-template-columns: 1fr;
  }
}
</style>
