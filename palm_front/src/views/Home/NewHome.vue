<template>
  <div class="container">
    <!-- Hero Section -->
    <div class="hero">
      <div class="hero-content">
        <h1 class="hero-title">PAttern Learning and Mining(PALM) Lab</h1>
        <p class="hero-description">
          PALM
          实验室隶属东南大学计算机科学与工程学院，地点位于东南大学九龙湖校区计算机楼，主要从事数据挖掘与知识发现、机器学习、模式识别以及相关领域的基础性、前沿性、创新性的研究工作。
        </p>
        <div class="email-form">
          <RouterLink to="/apply"
            ><button class="btn btn-primary">申请加入我们</button></RouterLink
          >
        </div>
        <p class="trial-text">
          ✉️ We will send an email to notify you after your resume is approved.
        </p>
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

    <!-- 左边的块 -->
    <div class="features-grid">
      <div class="stats-card">
        <div class="stats-number">2025<br />Join Us</div>
        <div>请阅读PALM实验室招生说明</div>
        <RouterLink to="/read"
          ><div style="color: #93c5fd; margin-top: 8px">
            点击阅读
          </div></RouterLink
        >
      </div>

      <div class="features-bubble">
        <div class="bubble-item">🤖 Machine Learning</div>
        <div class="bubble-item">🔍 Pattern Recognition</div>
        <div class="bubble-item">🔨 Data Mining</div>
        <div class="bubble-item">👓 Computer Vision</div>
        <div class="bubble-item">✏️ Natural Language Processing</div>
        <div class="bubble-item">💻 ......</div>
      </div>

      <div class="features-list">
        <a href="https://palm.seu.edu.cn/palm_cn.html">
          <div class="ai-suggestion">
            <div style="display: flex; gap: 12px">
              <div
                style="
                  width: 32px;
                  height: 32px;
                  background: #e6f3ff;
                  border-radius: 50%;
                  display: flex;
                  align-items: center;
                  justify-content: center;
                "
              >
                🤖
              </div>
              <div>
                <div style="font-weight: 600">
                  计算机网络和信息集成教育部重点实验室
                </div>
                <p style="font-size: 14px; color: #6b7280; margin-top: 4px">
                  模式分析与挖掘研究所<br />
                  （东南大学）
                </p>
                <button class="btn btn-ghost" style="margin-top: 8px">
                  了解详情
                </button>
              </div>
            </div>
          </div>
        </a>

        <div class="feature-icons">
          <a href="https://palm.seu.edu.cn/palm_cn_arch.html">
            <div class="feature-icon">
              <span style="font-size: 24px">👥</span>
              <div style="font-size: 14px; margin-top: 8px">实验室组织架构</div>
            </div>
          </a>
          <a href="https://palm.seu.edu.cn/members.html">
            <div class="feature-icon">
              <span style="font-size: 24px">👩‍🎓</span>
              <div style="font-size: 14px; margin-top: 8px">
                研究队伍及人才培养
              </div>
            </div>
          </a>
          <a href="https://palm.seu.edu.cn/publication.html">
            <div class="feature-icon">
              <span style="font-size: 24px">🎓</span>
              <div style="font-size: 14px; margin-top: 8px">
                科学研究及主要成果
              </div>
            </div>
          </a>
          <a href="https://palm.seu.edu.cn/projects.html">
            <div class="feature-icon">
              <span style="font-size: 24px">📚️</span>
              <div style="font-size: 14px; margin-top: 8px">科研资源共享</div>
            </div>
          </a>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen,
    Ubuntu, Cantarell, sans-serif;
}

body {
  background: url("/home-bg.jpg") no-repeat center center fixed;
  background-size: cover;
  min-height: 100vh;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

/* Hero Section */
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
  color: #1f2937;
  margin-bottom: 24px;
  text-align: left;
  font-weight: bold;
}

.hero-description {
  font-size: 18px;
  color: #6b7280;
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

.email-input {
  flex: 1;
  padding: 12px 16px;
  border: 1px solid #e5e7eb;
  border-radius: 6px;
  font-size: 16px;
}

.trial-text {
  color: #6b7280;
  font-size: 14px;
  display: flex;
  align-items: center;
  gap: 8px;
}

/* Right Side Content */
.hero-image {
  position: relative;
}

.achievement-badge {
  position: absolute;
  top: 0;
  right: 0;
  background: white;
  padding: 16px;
  border-radius: 12px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.users-badge {
  position: absolute;
  bottom: 0;
  right: 0;
  background: white;
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

/* Features Grid */
.features-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 32px;
  margin-top: 64px;
}

.stats-card {
  background: #1f2937;
  color: white;
  padding: 32px;
  border-radius: 16px;
}

.stats-number {
  font-size: 36px;
  font-weight: bold;
  margin-bottom: 16px;
}

.features-bubble {
  background: #3b82f6;
  padding: 32px;
  border-radius: 16px;
  color: white;
}

.bubble-item {
  background: rgba(255, 255, 255, 0.2);
  padding: 8px 16px;
  border-radius: 20px;
  margin-bottom: 12px;
  display: inline-block;
}

.features-list {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.ai-suggestion {
  background: white;
  padding: 16px;
  border-radius: 12px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
.ai-suggestion:hover {
  background: wheat;
}

.feature-icons {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 16px;
}
.feature-icon:hover {
  background: wheat;
}

.feature-icon {
  background: white;
  padding: 16px;
  border-radius: 12px;
  text-align: center;
  a:hover {
    background: transparent;
  }
}

/* Responsive Design */
@media (max-width: 768px) {
  .hero {
    grid-template-columns: 1fr;
  }

  .features-grid {
    grid-template-columns: 1fr;
  }

  .hero-title {
    font-size: 36px;
  }

  .email-form {
    flex-direction: column;
  }
}
</style>

<script setup></script>
