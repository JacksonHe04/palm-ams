<!-- LayoutHeader.vue -->
<script setup>
</script>

<template>
  <header class="app-header">
    <div class="container">
      <ul class="app-header-nav-left">
        <li class="manager">
          <RouterLink to="/">东南大学 PALM 实验室申请系统</RouterLink>
        </li>
      </ul>
      <ul class="app-header-nav">

        <!--<li>-->
        <!--  <a href="https://www.seu.edu.cn" class="active"-->
        <!--    >东南大学</a-->
        <!--  >-->
        <!--</li>-->
        <!--<li><a href="https://cs.seu.edu.cn" class="active">计算机学院</a></li>-->
        <li>
          <a href="https://palm.seu.edu.cn/" class="active">PALM实验室</a>
        </li>
        <li>
          <RouterLink to="/test">开发者测试</RouterLink>
        </li>
        <li>
          <RouterLink to="/apply">申请</RouterLink>
        </li>
        <li class="home">
          <RouterLink to="/admin">管理</RouterLink>
        </li>
      </ul>
    </div>
  </header>
</template>

<style scoped>
a {
  color: #777777;
}

.app-header {
  height: fit-content;

  .container {
    display: flex;
    align-items: center;
    height: 60px;
    margin: 0;
    width: 100%;
  }

  .app-header-nav-left {
    display: flex;
    margin-right: auto; /* 靠左对齐 */
    li {
      text-align: center;
      &::after {
        content: "";
        display: inline-block;
        width: 1px;
        height: 90%;
        background-color: #cacaca;
        vertical-align: bottom;
        margin-left: 20px;
        margin-right: 20px;
      }
      a {
        font-size: 16px;
        line-height: 32px;
        height: 32px;
        display: inline-block;
        text-decoration: none;
        transition: color 0.5s ease;
        &:hover {
          color: #8ebdf8;
          text-decoration: none;
        }
      }
      &:last-child::after {
        content: none;
      }
    }
  }

  .app-header-nav {
    width: 450px;
    display: flex;
    padding-left: 0;
    position: relative;
    z-index: 998;
    margin-left: auto;

    li {
      text-align: center;

      &::after {
        content: "";
        display: inline-block;
        width: 1px;
        height: 90%;
        background-color: #cacaca;
        vertical-align: bottom;
        margin-left: 20px;
        margin-right: 20px;
      }

      a {
        font-size: 16px;
        line-height: 32px;
        height: 32px;
        display: inline-block;
        text-decoration: none;
        transition: color 0.5s ease;

        &:hover {
          color: #5d7faa;
          text-decoration: none;
        }
      }

      &:last-child::after {
        content: none;
      }
    }
  }
}

ol,
ul {
  margin-top: 0;
  margin-bottom: 0;
  list-style-type: none;
}
</style>
