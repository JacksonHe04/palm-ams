import { computed } from 'vue'
import { useRoute } from 'vue-router'
import { useApplyStore } from '@/stores/applyStore'
import { useSettingStore } from '@/stores/settingStore'

/**
 * 处理申请类型的 composable
 * 根据当前路由自动设置申请类型，并同步到 store
 */
export const useApplicationType = () => {
  const route = useRoute()
  const applyStore = useApplyStore()
  const settingStore = useSettingStore()

  // 根据路由计算申请类型
  const getApplicationType = computed(() => {
    const routePath = route.path
    let applicationType = ''
    
    switch (routePath) {
      case '/apply/recommend-master':
        applicationType = '推免硕士'
        break
      case '/apply/exam-master':
        applicationType = '考研硕士'
        break
      case '/apply/phd':
        applicationType = '博士'
        break
      case '/apply/direct-phd':
        applicationType = '直博'
        break
      default:
        applicationType = ''
    }

    // 更新 store 中的值
    applyStore.updateField('applicationType', applicationType)
    // 同时更新 year 字段
    applyStore.updateField('year', settingStore.year.year)
    return applicationType
  })

  return {
    getApplicationType
  }
}