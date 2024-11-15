<!-- LayoutHeader.vue -->
<script setup>
</script>

<template>
  <header class="app-header">
    <div class="container">
      <ul class="app-header-nav-left">
        <li class="manager">
          <RouterLink to="/home">PalmAdmissionsSystem</RouterLink>
        </li>
      </ul>
      <ul class="app-header-nav">
        <li>
          <a href="https://www.seu.edu.cn" class="active"
            >东南大学</a
          >
        </li>
        <li>
          <a href="https://palm.seu.edu.cn/" class="active">PALM实验室</a>
        </li>
        <li>
          <RouterLink to="/test">开发者测试</RouterLink>
        </li>
        <li class="home">
          <RouterLink to="/">管理</RouterLink>
        </li>
      </ul>
    </div>
  </header>
</template>

<style scoped>
.app-header {
  background-image: linear-gradient(
    15deg,
    rgba(10, 24, 85, 0.6) 0%,
    rgba(136, 194, 213, 0.6) 100%
  );
  /* border-bottom: 2px solid #e0e0e0; */

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
        background-color: #e0e0e0;
        vertical-align: bottom;
        margin-left: 20px;
        margin-right: 20px;
      }
      a {
        font-size: 16px;
        line-height: 32px;
        height: 32px;
        display: inline-block;
        font-weight: bold;
        color: #d8d8d8;
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
        background-color: #e0e0e0;
        vertical-align: bottom;
        margin-left: 20px;
        margin-right: 20px;
      }

      a {
        font-size: 16px;
        line-height: 32px;
        height: 32px;
        display: inline-block;
        font-weight: bold;
        color: #707070;
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
