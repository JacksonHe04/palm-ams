import { FieldItem } from '@/apis/field'
import { useFieldStore } from '@/stores/fieldStore'
import fieldsData from './fields.json'

export const importFields = async () => {
  const fieldStore = useFieldStore()

  // 导入字段数据
  const fields: Omit<FieldItem, 'id'>[] = fieldsData

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