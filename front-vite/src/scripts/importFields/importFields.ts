import { FieldItem } from '@/apis/field'
import { useFieldStore } from '@/stores/fieldStore'

export const importFields = async () => {
  const fieldStore = useFieldStore()

  // 从studentsStore.ts中提取的字段
  const fields: Omit<FieldItem, 'id'>[] = [
    // 论文字段
    {
      name: '论文一发表时间',
      description: '第一篇论文发表时间',
      showInTable: false,
      showInFilter: false,
      showInApply: true
    },
    {
      name: '论文一期刊会议',
      description: '第一篇论文发表期刊或会议名称',
      showInTable: false,
      showInFilter: false,
      showInApply: true
    },
    {
      name: '论文一名称',
      description: '第一篇论文标题',
      showInTable: false,
      showInFilter: false,
      showInApply: true
    },
    {
      name: '论文一CCF等级',
      description: '第一篇论文CCF等级',
      showInTable: false,
      showInFilter: false,
      showInApply: true
    },
    {
      name: '论文一获奖类别',
      description: '第一篇论文获奖情况',
      showInTable: false,
      showInFilter: false,
      showInApply: true
    },


    // 奖项字段
    {
      name: '奖项一是否负责人',
      description: '第一个奖项是否为负责人',
      showInTable: false,
      showInFilter: false,
      showInApply: true
    },
    {
      name: '奖项一获奖时间',
      description: '第一个奖项获奖时间',
      showInTable: false,
      showInFilter: false,
      showInApply: true
    },
    {
      name: '奖项一名称',
      description: '第一个奖项名称',
      showInTable: false,
      showInFilter: false,
      showInApply: true
    },
    {
      name: '奖项一等级排名',
      description: '第一个奖项等级排名',
      showInTable: false,
      showInFilter: false,
      showInApply: true
    },
    {
      name: '奖项一获奖排名',
      description: '第一个奖项获奖排名',
      showInTable: false,
      showInFilter: false,
      showInApply: true
    },
    // 论文字段
    {
      name: '论文二发表时间',
      description: '第二篇论文发表时间',
      showInTable: false,
      showInFilter: false,
      showInApply: true
    },
    {
      name: '论文二期刊会议',
      description: '第二篇论文发表期刊或会议名称',
      showInTable: false,
      showInFilter: false,
      showInApply: true
    },
    {
      name: '论文二名称',
      description: '第二篇论文标题',
      showInTable: false,
      showInFilter: false,
      showInApply: true
    },
    {
      name: '论文二CCF等级',
      description: '第二篇论文CCF等级',
      showInTable: false,
      showInFilter: false,
      showInApply: true
    },
    {
      name: '论文二获奖类别',
      description: '第二篇论文获奖情况',
      showInTable: false,
      showInFilter: false,
      showInApply: true
    },


    // 奖项字段
    {
      name: '奖项二是否负责人',
      description: '第二个奖项是否为负责人',
      showInTable: false,
      showInFilter: false,
      showInApply: true
    },
    {
      name: '奖项二获奖时间',
      description: '第二个奖项获奖时间',
      showInTable: false,
      showInFilter: false,
      showInApply: true
    },
    {
      name: '奖项二名称',
      description: '第二个奖项名称',
      showInTable: false,
      showInFilter: false,
      showInApply: true
    },
    {
      name: '奖项二等级排名',
      description: '第二个奖项等级排名',
      showInTable: false,
      showInFilter: false,
      showInApply: true
    },
    {
      name: '奖项二获奖排名',
      description: '第二个奖项获奖排名',
      showInTable: false,
      showInFilter: false,
      showInApply: true
    },
    {
      name: '论文三发表时间',
      description: '第三篇论文发表时间',
      showInTable: false,
      showInFilter: false,
      showInApply: true
    },
    {
      name: '论文三期刊会议',
      description: '第三篇论文发表期刊或会议名称',
      showInTable: false,
      showInFilter: false,
      showInApply: true
    },
    {
      name: '论文三名称',
      description: '第三篇论文标题',
      showInTable: false,
      showInFilter: false,
      showInApply: true
    },
    {
      name: '论文三CCF等级',
      description: '第三篇论文CCF等级',
      showInTable: false,
      showInFilter: false,
      showInApply: true
    },
    {
      name: '论文三获奖类别',
      description: '第三篇论文获奖情况',
      showInTable: false,
      showInFilter: false,
      showInApply: true
    },


    // 奖项字段
    {
      name: '奖项三是否负责人',
      description: '第三个奖项是否为负责人',
      showInTable: false,
      showInFilter: false,
      showInApply: true
    },
    {
      name: '奖项三获奖时间',
      description: '第三个奖项获奖时间',
      showInTable: false,
      showInFilter: false,
      showInApply: true
    },
    {
      name: '奖项三名称',
      description: '第三个奖项名称',
      showInTable: false,
      showInFilter: false,
      showInApply: true
    },
    {
      name: '奖项三等级排名',
      description: '第三个奖项等级排名',
      showInTable: false,
      showInFilter: false,
      showInApply: true
    },
    {
      name: '奖项三获奖排名',
      description: '第三个奖项获奖排名',
      showInTable: false,
      showInFilter: false,
      showInApply: true
    },
  ]

  // 批量导入字段
  for (const field of fields) {
    try {
      await fieldStore.createField(field)
      console.log(`成功导入字段: ${field.name}`)
    } catch (error) {
      console.error(`导入字段失败: ${field.name}`, error)
    }
  }

  console.log('字段导入完成')
}

export default importFields