import { ref } from 'vue'

// 定义菜单项的类型
interface MenuItem {
  name: string
  label: string
  path: string
  icon: string
}

interface MenuCategory {
  category: string
  items: MenuItem[]
}

// 导出菜单配置
export const menuItems = ref<MenuCategory[]>([
  {
    category: "申请阶段",
    items: [
      {
        name: "students",
        label: "学生表格",
        path: "students",
        icon: "🪪",
      },

      {
        name: "percent",
        label: "筛选方案",
        path: "percent",
        icon: "🔍",
      },
      {
        name: "result",
        label: "筛选结果",
        path: "result",
        icon: "📇",
      },
    ],
  },
  {
    category: "面试阶段",
    items: [
      {
        name: "interview",
        label: "面试打分",
        path: "interview",
        icon: "📋",
      },
    ],
  },
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
    category: "系统设置",
    items: [
      {
        name: "setting",
        label: "规则设置",
        path: "setting",
        icon: "⚙️",
      },
      {
        name: "field",
        label: "字段设置",
        path: "field",
        icon: "📝",
      },
      {
        name: "account",
        label: "账号设置",
        path: "account",
        icon: "👩🏻‍💻️",
      },
      {
        name: "database",
        label: "数据库  ",
        // path: "table",
        path: "database",
        icon: "🗄️",
      },
    ],
  },
])