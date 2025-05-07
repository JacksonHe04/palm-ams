// import { computed, ref } from 'vue'
import type { ComputedRef } from 'vue'
import { useApplyStore } from '@/stores/applyStore'

export const usePercentageCalculation = (formData: ComputedRef<Record<string, any>>) => {
  const applyStore = useApplyStore()

  // 计算百分比
  const calculatePercentage = () => {
    const rank = Number(formData.value.rank)
    const majorCount = Number(formData.value.majorCount)
    if (!isNaN(rank) && !isNaN(majorCount) && majorCount !== 0) {
      const percentage = Math.floor(rank / majorCount * 100)
      applyStore.updateField('percentage', `${percentage}%`)
      return `${percentage}%`
    }
    return ''
  }

  // // 贡献度数据
  // const contributionFields = ['award1_contribution', 'award2_contribution', 'award3_contribution']
  // const contributionData = ref({
  //   award1_contribution: { rank: '', total: '' },
  //   award2_contribution: { rank: '', total: '' },
  //   award3_contribution: { rank: '', total: '' }
  // })

  // // 更新贡献度
  // const updateContribution = (fieldName: string, data: { rank: string | number, total: string | number }) => {
  //   // 更新本地数据
  //   contributionData.value[fieldName] = data
    
  //   // 更新 store 中的值
  //   if (data.rank && data.total) {
  //     const formattedValue = `${data.rank}/${data.total}`
  //     applyStore.updateField(fieldName, formattedValue)
  //     return formattedValue
  //   }
  //   applyStore.updateField(fieldName, '')
  //   return ''
  // }

  return {
    calculatePercentage,
    // updateContribution,
    // contributionData
  }
}