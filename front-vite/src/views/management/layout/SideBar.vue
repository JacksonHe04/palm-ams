<template>
  <aside :class="['sidebar', { collapsed: isCollapsed }]">
    <div class="button-container">
      <button @click="toggleSidebar" class="toggle-button">
        <i :data-feather="isCollapsed ? 'chevrons-right' : 'chevrons-left'"></i>
      </button>
    </div>
    <ul v-if="!isCollapsed" class="menu">
      <template v-for="(category, index) in menuItems" :key="index">
        <li class="category-name">{{ category.category }}</li>
        <li v-for="item in category.items" :key="item.name" class="menu-item">
          <RouterLink :to="item.path" class="menu-link" active-class="active">
            <span class="icon">{{ item.icon }}</span>
            <span class="label">{{ item.label }}</span>
          </RouterLink>
        </li>
        <li v-if="index !== menuItems.length - 1" class="divider"></li>
      </template>
    </ul>
  </aside>
</template>

<script setup>
import { ref } from "vue";
import { defineProps, defineEmits } from "vue";
import feather from "feather-icons";

const props = defineProps({
  isCollapsed: Boolean,
});

const emit = defineEmits(["toggle"]);

const menuItems = ref([
  {
    category: "可视化",
    items: [
      {
        name: "dashboard",
        label: "仪表盘",
        path: "dashboard",
        icon: "📊",
      },
      {
        name: "analytics",
        label: "数据分析",
        path: "analysis",
        icon: "📈",
      },
    ],
  },
  {
    category: "表格总览",
    items: [
      {
        name: "users",
        label: "学生表格",
        path: "students",
        icon: "👤",
      },
      {
        name: "interview",
        label: "面试打分",
        path: "interview",
        icon: "📋",
      },
    ],
  },
  {
    category: "招生自定义",
    items: [
      {
        name: "percent",
        label: "筛选方案",
        path: "percent",
        icon: "🔍",
      },
      {
        name: "setting",
        label: "规则设置",
        path: "setting",
        icon: "⚙️",
      },
    ],
  },
  {
    category: "系统设置",
    items: [
      {
        name: "field",
        label: "字段配置",
        path: "field",
        icon: "📝",
      },
      {
        name: "account",
        label: "账号设置",
        path: "account",
        icon: "👩🏻‍💻️",
      },
    ],
  },
]);

const toggleSidebar = () => {
  emit("toggle");
  // 更新Feather图标
  feather.replace();
};

// 监听props变化
watch(
  () => props.isCollapsed,
  () => {
    // 当折叠状态改变时更新图标
    feather.replace();
  },
);

// 初始化Feather Icons
import { onMounted, watch } from "vue";

onMounted(() => {
  feather.replace();
});
</script>

<style scoped lang="scss">
.sidebar {
  display: flex;
  flex-direction: column;
  height: 100%;
  padding: 0;
  background-color: white;
  transition: width 0.3s ease;
  width: 100%; // 添加固定宽度
  box-shadow: 2px 0 8px rgba(0, 0, 0, 0.1); // 添加阴影效果

  &.collapsed {
    width: 40px;
    padding: 0;
    overflow: hidden;

    .label {
      display: none;
    }

    .icon {
      margin-right: 0;
    }

    .menu {
      display: none;
    }
  }

  .button-container {
    padding: 0;
    position: relative;
    height: 44px;
    border-bottom: 1px solid #f0f0f0; // 添加底部边框
    
    .toggle-button {
      position: absolute;
      top: 10px;
      left: 8px;
      background-color: white;
      border: 1px solid $admin-border;
      border-radius: 4px;
      padding: 0;
      cursor: pointer;
      z-index: 1000;
      font-size: 16px;
      height: 24px;

      i {
        color: #808080;
      }
    }
  }

  .menu {
    list-style: none;
    padding: 12px 8px; // 增加整体内边距
    margin: 0;

    .menu-item {
      margin-bottom: 8px; // 减小项目间距

      .menu-link {
        text-decoration: none;
        display: flex;
        align-items: center;
        padding: 10px 16px; // 增加内边距
        border-radius: 6px; // 增加圆角
        transition: all 1s ease;

        &:hover {
          background-color: #f0f8ff;
          color: #2980b9;
        }

        &.active {
          background-color: #e0f7fa;
          color: #009688;
          font-weight: 500; // 激活时文字加粗
        }

        .icon {
          margin-right: 12px; // 调整图标间距
          font-size: 18px; // 增加图标大小
          width: 24px; // 固定图标宽度
          text-align: center; // 图标居中对齐
        }

        .label {
          font-size: 14px; // 设置文字大小
        }
      }
    }

    .category-name {
      font-size: 12px;
      color: #999;
      padding: 8px 16px;
      margin-top: 8px;
      text-align: left;
    }

    .divider {
      height: 1px;
      background-color: #f0f0f0;
      margin: 8px 16px;
      list-style: none;
    }
  }
}
</style>
