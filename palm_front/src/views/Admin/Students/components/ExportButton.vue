<!-- ExportButton.vue -->
<template>
  <el-button type="primary" @click="exportTable">导出表格</el-button>
</template>

<script>
import * as XLSX from "xlsx";

export default {
  props: {
    tableData: {
      type: Array,
      required: true,
    },
    visibleFields: {
      type: Array,
      required: true,
    },
    fieldProps: {
      type: Object,
      required: true,
    },
    store: { // 添加这一行
      type: Object,
      required: true,
    },
  },
  methods: {
    exportTable() {
      // 处理可见字段
      const visibleHeaders = this.visibleFields.map((field) => field);
      const visibleRows = this.tableData.map((row) =>
        this.visibleFields.reduce((acc, field) => {
          acc[field] =
            row[this.fieldProps[field]] !== undefined &&
            row[this.fieldProps[field]] !== null
              ? row[this.fieldProps[field]]
              : "无";
          return acc;
        }, {}),
      );

      // 处理论文字段
      const paperHeaders = this.store.paperFields.map(
        (_, index) => `论文${index + 1}`,
      );
      const paperRows = this.tableData.map((row) =>
        this.store.paperFields.reduce((acc, _, index) => {
          acc[`论文${index + 1}`] =
            row.papers && row.papers[index] ? row.papers[index].ccfLevel : "无";
          return acc;
        }, {}),
      );

      // 处理奖项字段
      const awardHeaders = this.store.awardFields.map(
        (_, index) => `奖项${index + 1}`,
      );
      const awardRows = this.tableData.map((row) =>
        this.store.awardFields.reduce((acc, _, index) => {
          acc[`奖项${index + 1}`] =
            row.awards && row.awards[index]
              ? row.awards[index].levelRanking
              : "无";
          return acc;
        }, {}),
      );

      // 合并所有数据
      const headers = [...visibleHeaders, ...paperHeaders, ...awardHeaders];
      const rows = this.tableData.map((_, index) => ({
        ...visibleRows[index],
        ...paperRows[index],
        ...awardRows[index],
      }));

      // 创建工作表和工作簿
      const worksheet = XLSX.utils.json_to_sheet(rows, { header: headers });
      const workbook = XLSX.utils.book_new();
      XLSX.utils.book_append_sheet(workbook, worksheet, "表格数据");
      XLSX.writeFile(workbook, "学生信息表格.xlsx");
    },
  },
};
</script>
