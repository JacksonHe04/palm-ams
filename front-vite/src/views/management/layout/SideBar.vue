<template>
  <aside :class="['sidebar', { collapsed: isCollapsed }]">
    <div class="button-container">
      <button @click="toggleSidebar" class="toggle-button">
        <i :data-feather="isCollapsed ? 'chevrons-right' : 'chevrons-left'"></i>
      </button>
    </div>
    <ul v-if="!isCollapsed" class="menu">
      <template v-for="(category, index) in menuItems" :key="index">
        <li class="category-header" @click="toggleCategory(index)">
          <span class="category-name">{{ category.category }}</span>
        </li>
        <ul
          v-if="!categoryCollapsed[index]"
          class="sub-menu"
          :class="{ expanded: !categoryCollapsed[index] }"
        >
          <li v-for="item in category.items" :key="item.name" class="menu-item">
            <RouterLink :to="item.path" class="menu-link" active-class="active">
              <span class="icon">{{ item.icon }}</span>
              <span class="label">{{ item.label }}</span>
            </RouterLink>
          </li>
        </ul>
        <li v-if="index !== menuItems.length - 1" class="divider"></li>
      </template>
    </ul>
  </aside>
</template>

<script setup lang="ts">
import { defineProps, defineEmits, ref } from "vue";
import feather from "feather-icons";
import { menuItems } from "@/config/menuConfig";

const props = defineProps({
  isCollapsed: Boolean,
});

const emit = defineEmits(["toggle"]);

const categoryCollapsed = ref(menuItems.value.map(() => false)); // 修改为false表示默认展开

const toggleSidebar = () => {
  emit("toggle");
  feather.replace();
};

const toggleCategory = (index: number) => {
  categoryCollapsed.value = categoryCollapsed.value.map((val, i) =>
    i === index ? !val : val
  );
  // feather.replace();
};

// watch(
//   () => props.isCollapsed,
//   () => {
//     feather.replace();
//   }
// );
</script>

<style scoped lang="scss">
.sidebar {
  display: flex;
  flex-direction: column;
  height: 100%;
  padding: 0;
  background-color: white;
  transition: width 0.3s ease;
  width: 100%;
  box-shadow: 2px 0 8px rgba(0, 0, 0, 0.1);

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
    border-bottom: 1px solid #f0f0f0;

    .toggle-button {
      position: absolute;
      top: 10px;
      left: 8px;
      background-color: white;
      border: 1px solid #ccc;
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
    padding: 12px 8px;
    margin: 0;

    .category-header {
      font-size: 12px;
      color: #999;
      padding: 8px 16px;
      margin-top: 8px;
      text-align: left;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: space-between;

      i {
        font-size: 12px;
        color: #999;
      }

      &:hover,
      &.hovered {
        color: #2980b9;
        background-color: #f0f8ff;
      }
    }

    .sub-menu {
      list-style: none;
      padding: 0;
      margin: 0;
      overflow: hidden;
      max-height: 0;
      transition: max-height 0.3s ease;

      &.expanded {
        max-height: 1000px;
      }
    }

    .menu-item {
      margin-bottom: 8px;

      .menu-link {
        text-decoration: none;
        display: flex;
        align-items: center;
        padding: 10px 16px;
        border-radius: 6px;
        transition: all 0.3s ease;

        &:hover {
          background-color: #f0f8ff;
          color: #2980b9;
        }

        &.active {
          background-color: #e0f7fa;
          color: #009688;
          font-weight: 500;
        }

        .icon {
          margin-right: 12px;
          font-size: 18px;
          width: 24px;
          text-align: center;
        }

        .label {
          font-size: 14px;
        }
      }
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
