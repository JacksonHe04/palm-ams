<template>
  <el-button
    type="success"
    :loading="exporting"
    @click="exportToExcel"
  >
    {{ exporting ? '正在导出...' : '导出当前表格为Excel' }}
  </el-button>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { ElMessage } from 'element-plus';
import * as XLSX from 'xlsx';

// 定义组件的 props
const props = defineProps<{
  data: any[];
  columnConfig: Record<string, { label: string; width: string }>;
  applicationType: string;
}>();

// 导出状态
const exporting = ref(false);

/**
 * 导出Excel文件
 * 将当前标签页的表格数据导出为Excel文件
 */
async function exportToExcel() {
  if (!props.data.length) {
    ElMessage.warning('没有可导出的数据');
    return;
  }

  exporting.value = true;
  try {
    // 准备表格数据
    const exportData = props.data.map((student, index) => {
      const row: Record<string, any> = {
        '序号': index + 1
      };
      
      // 添加动态列数据
      Object.entries(props.columnConfig).forEach(([key, config]) => {
        row[config.label] = student[key] === true ? '是' : 
                           student[key] === false ? '否' : 
                           student[key] || '无';
      });

      // 添加论文数据
      row['论文'] = [student.paper1_journalConference, student.paper2_journalConference, student.paper3_journalConference]
        .filter(journal => journal && journal.trim() !== '')
        .join(';') || '无';

      // 添加奖项数据
      row['奖项'] = [student.award1_awardName, student.award2_awardName, student.award3_awardName]
        .filter(award => award && award.trim() !== '')
        .join(';') || '无';

      return row;
    });

    // 创建工作表
    const ws = XLSX.utils.json_to_sheet(exportData);
    const wb = XLSX.utils.book_new();
    XLSX.utils.book_append_sheet(wb, ws, '学生信息');

    // 导出文件
    XLSX.writeFile(wb, `学生信息表_${props.applicationType}_${new Date().toLocaleDateString()}.xlsx`);
    ElMessage.success('导出成功');
  } catch (error) {
    console.error('导出Excel时出错:', error);
    ElMessage.error('导出Excel时出错');
  } finally {
    exporting.value = false;
  }
}
</script>