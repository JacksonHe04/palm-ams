<template>
  <footer class="w-full mt-40 py-10 px-4 sm:px-6 lg:px-8">
    <div class="mx-auto px-60">
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
        <div v-for="(section, index) in footerSections" :key="index" class="footer-section">
          <h3 class="text-gray-500 font-bold mb-2">{{ section.title }}</h3>
          <ul class="space-y-2">
            <li v-for="(link, linkIndex) in section.links" :key="linkIndex">
              <a :href="link.url" target="_blank" class="text-gray-500">
                <i v-if="link.icon" :class="link.icon" class="mr-2"></i>{{ link.name }}
              </a>
            </li>
          </ul>
        </div>
      </div>

      <div class="mt-10 border-t border-white pt-10">
        <p class="text-center text-gray-500">
          CopyRight © 何锦诚，刘宇轩，戴雨成，胡瀚 2025 All rights reserved.
        </p>
        <p class="text-center text-gray-500 mt-1">
          东南大学2025年创业实践项目作品
        </p>
      </div>
    </div>
  </footer>
</template>

<style scoped>
footer {
  box-shadow: 0 -2px 4px rgba(0, 0, 0, 0.1);
}

.footer-link {
  color: #4b5563; /* text-gray-700 */
  transition: color 0.3s ease; /* hover effect */
}

.footer-link:hover {
  color: #63b3ed; /* hover:text-blue-500 */
}
</style>


<script>
export default {
  data() {
    return {
      footerSections: [
        {
          title: '项目开源',
          links: [
            {
              name: '个人项目',
              url: 'https://github.com/JacksonHe04',
              icon: 'i iconfont icon-github'
            },
            {
              name: 'Gitee 仓库',
              url: 'https://gitee.com/JacksonHe04/PalmAdmissionsSystem',
              icon: 'i iconfont icon-github'
            },
            {
              name: 'GitHub 仓库',
              url: 'https://github.com/JacksonHe04/PalmAdmissionsSystem',
              icon: 'i iconfont icon-github'
            }
          ]
        },
        {
          title: '联系我们',
          links: [
            {
              name: '联系管理员',
              url: ''
            },
            {
              name: '联系开发者',
              url: ''
            }
          ]
        },
        {
          title: '更多网站',
          links: [
            {
              name: '东南大学官网',
              url: 'https://www.seu.edu.cn/'
            },
            {
              name: '东南大学计算机学院',
              url: 'https://cs.sdu.edu.cn/'
            },
            {
              name: '东大计软智导航',
              url: 'https://seucseweb.github.io/'
            }
          ]
        },
        {
          title: '关于 PALM',
          links: [
            {
              name: '东南大学 PALM 实验室',
              url: 'https://palm.seu.edu.cn/'
            },
            {
              name: '研究生申请指南',
              url: 'https://palm.seu.edu.cn/application.html'
            },
            {
              name: '实验室成员',
              url: 'https://palm.seu.edu.cn/members.html'
            }
          ]
        }
      ]
    };
  }
};
</script>