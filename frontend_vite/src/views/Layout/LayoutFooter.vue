<template>
  <footer class="app_footer">
    <div class="contact">
      <div class="container">
        <dl>
          <dt>项目开源</dt>
          <dd>
            <a href="https://github.com/JacksonHe04" target="_blank">
              <i class="iconfont icon-github"></i>个人项目
            </a>
          </dd>
          <dd>
            <a
                href="https://gitee.com/JacksonHe04/PalmAdmissionsSystem"
                target="_blank"
            >
              <i class="iconfont icon-github"></i> Gitee 仓库
            </a>
          </dd>
          <dd>
            <a
                href="https://github.com/JacksonHe04/PalmAdmissionsSystem"
                target="_blank"
            >
              <i class="iconfont icon-github"></i> GitHub 仓库
            </a>
          </dd>
        </dl>

        <dl>
          <dt>联系我们</dt>
            <!--<img src="@/assets/images/wechat_black.png" alt="wx" />-->
          <dd class="download">
            <a href="">联系管理员</a>
          </dd>
          <dd class="download">
            <a href="">联系开发者</a>
          </dd>
        </dl>

        <dl>
          <dt>更多网站</dt>
          <dd>
            <a href="https://www.seu.edu.cn/" target="_blank">东南大学官网</a>
          </dd>
          <dd>
            <a href="https://cs.sdu.edu.cn/" target="_blank">东南大学计算机学院</a>
          </dd>
          <dd>
            <a href="https://seucseweb.github.io/" target="_blank">东大计软智导航</a>
          </dd>
        </dl>

        <dl>
          <dt>关于PALM</dt>
          <dd>
            <a href="https://palm.seu.edu.cn/" target="_blank">东南大学PALM实验室</a>
          </dd>
          <dd>
            <a href="https://palm.seu.edu.cn/application.html" target="_blank">研究生申请指南
            </a>
          </dd>
          <dd>
            <a href="https://palm.seu.edu.cn/members.html" target="_blank">实验室成员</a>
          </dd>
        </dl>
      </div>
    </div>

    <div class="extra">
      <!-- 版权分隔线 -->
      <div class="seperator"></div>
      <div class="container">
        <!-- 版权信息 -->
        <div class="copyright">
          <p>CopyRight © 何锦诚，刘宇轩，戴雨成，胡瀚 2025 All rights reserved.</p>
          <h2></h2>
          <p>东南大学2025年创业实践项目作品</p>
        </div>
      </div>
    </div>
  </footer>
</template>

<style scoped>
.app_footer {
  background-image: linear-gradient(
      15deg,
      rgba(10, 24, 85, 0.6) 0%,
      rgba(136, 194, 213, 0.6) 100%
  );
  padding: 40px 0 0 0;
  color: #333;
}

.contact .container {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  max-width: 1200px;
  margin: 0 auto;
}

.contact dt {
  font-size: 18px;
  font-weight: bold;
  margin-bottom: 10px;
}

.contact dd {
  margin: 5px 0;
}

.contact a {
  color: #333;
  text-decoration: none;
}

a:hover {
  color: #5d7faa;
  text-decoration: none;
}

.contact .qrcode img {
  width: 100px;
  height: 100px;
}

.contact .download span {
  display: block;
  margin-bottom: 5px;
}

.extra {
  padding: 30px 0 20px 0;
}

.seperator {
  width: 40%;
  height: 1px;
  background-color: #cccccc;
  display: block;
  margin: 0 auto 30px auto;
}

.copyright p {
  font-size: 14px;
  line-height: 1.5;
  text-align: center;
}
</style>