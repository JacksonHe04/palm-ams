// 表单配置数据

// CCF等级选项
export const ccfLevel = [
  { value: 'A', label: 'A' },
  { value: 'B', label: 'B' },
  { value: 'C', label: 'C' },
  { value: '其他', label: '其他' }
]

// 奖项等级选项
export const awardLevel = [
  { value: '国家级', label: '国家级' },
  { value: '省级', label: '省级' },
  { value: '校级', label: '校级' },
  { value: '其他', label: '其他' }
]

// 获奖等级选项
export const awardRanking = [
  { value: '特等奖', label: '特等奖' },
  { value: '一等奖', label: '一等奖' },
  { value: '二等奖', label: '二等奖' },
  { value: '三等奖', label: '三等奖' },
  { value: '金奖', label: '金奖' },
  { value: '银奖', label: '银奖' },
  { value: '铜奖', label: '铜奖' }
]

// 报名类型选项
export const applicationType = [
  { value: '硕士', label: '硕士' },
  { value: '博士', label: '博士' },
  { value: '直博', label: '直博' }
]

// 性别选项
export const gender = [
  { value: '男', label: '男' },
  { value: '女', label: '女' }
]

// 选项映射对象
export const fieldOptionsMap = {
  '论文一 CCF等级': ccfLevel,
  '论文二 CCF等级': ccfLevel,
  '论文三 CCF等级': ccfLevel,
  '奖项一 等级': awardLevel,
  '奖项二 等级': awardLevel,
  '奖项三 等级': awardLevel,
  '奖项一 获奖情况': awardRanking,
  '奖项二 获奖情况': awardRanking,
  '奖项三 获奖情况': awardRanking,
}