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
  },
  methods: {
    exportTable() {
      const headers = this.visibleFields.map((field) => field);
      const rows = this.tableData.map((row) =>
          this.visibleFields.reduce((acc, field) => {
            acc[field] =
                row[this.fieldProps[field]] !== undefined &&
                row[this.fieldProps[field]] !== null
                    ? row[this.fieldProps[field]]
                    : "无";
            return acc;
          }, {})
      );

      const worksheet = XLSX.utils.json_to_sheet(rows, { header: headers });
      const workbook = XLSX.utils.book_new();
      XLSX.utils.book_append_sheet(workbook, worksheet, "表格数据");
      XLSX.writeFile(workbook, "学生信息表格.xlsx");
    },
  },
};
</script>