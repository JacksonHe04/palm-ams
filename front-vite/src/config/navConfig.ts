import { computed } from 'vue'

// 定义导航项的类型
interface NavItem {
  name: string
  to: string
}

/**
 * 创建导航菜单配置
 * @param currentYear 当前招生年份
 * @returns 导航菜单项数组
 */
export const createNavItems = (currentYear: number = new Date().getFullYear()) => {
    return [
    { name: 'Home', to: '/home' },
    { name: 'Contact Us', to: '/contact' },
    { name: `${currentYear} Join Us`, to: '/read' },
  ]
}