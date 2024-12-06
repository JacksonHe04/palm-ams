<template>
  <div class="students-form">
    <el-row class="form-settings">
      <el-col :span="8">
        <field-selector
          :fields="allFields"
          :visible-fields="visibleFields"
          @update-visible-fields="updateVisibleFields"
        />
      </el-col>
      <el-col :span="16" class="search-filter">
        <el-input
          v-model="filterText"
          placeholder="搜索姓名、邮箱或手机号"
          @input="onFilter"
        />
        <el-select v-model="selectedSort" placeholder="排序">
          <el-option
            v-for="option in sortOptions"
            :key="option.value"
            :label="option.label"
            :value="option.value"
          />
        </el-select>

        <!-- 导出按钮 -->
        <ExportButton
          :tableData="filteredStudents"
          :visible-fields="visibleFields"
          :field-props="fieldProps"
        />
      </el-col>
    </el-row>

    <div class="table-container">
      <el-table
        :data="filteredStudents"
        style="width: 100%"
        border
        :table-layout="'auto'"
        :default-sort="{ prop: selectedSort, order: 'ascending' }"
      >
        <!-- 动态生成常规列 -->
        <el-table-column
          v-for="field in visibleFields"
          :key="field"
          :prop="fieldProps[field]"
          :label="field"
          v-if="!isPaperOrAwardField(field)"
          :min-width="100"
        >
          <template #default="{ row }">
            <span>{{
              row[fieldProps[field]] !== undefined &&
              row[fieldProps[field]] !== null &&
              row[fieldProps[field]] !== ""
                ? row[fieldProps[field]]
                : "无"
            }}</span>
          </template>
        </el-table-column>

        <!-- 论文列 -->
        <template
          v-for="(paperField, index) in paperFields"
          :key="`论文-${index}`"
        >
          <el-table-column :label="`论文${index + 1}`">
            <template #default="{ row }">
              <span
                v-if="row.papers && row.papers[index]"
                @click="showDetails('paper', row.papers[index])"
                class="expandable-cell"
              >
                {{ row.papers[index].ccfLevel }}
              </span>
              <span v-else>无</span>
            </template>
          </el-table-column>
        </template>

        <!-- 奖项列 -->
        <template
          v-for="(awardField, index) in awardFields"
          :key="`奖项-${index}`"
        >
          <el-table-column :label="`奖项${index + 1}`">
            <template #default="{ row }">
              <span
                v-if="row.awards && row.awards[index]"
                @click="showDetails('award', row.awards[index])"
                class="expandable-cell"
              >
                {{ row.awards[index].levelRanking }}
              </span>
              <span v-else>无</span>
            </template>
          </el-table-column>
        </template>
      </el-table>
    </div>

    <!-- 详情弹窗 -->
    <el-dialog v-model="dialogVisible" title="详细信息" :width="dialogWidth">
      <pre>{{ selectedDetails }}</pre>
      <span slot="footer" class="dialog-footer">
        <el-button @click="dialogVisible = false">关闭</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>
import { ref, computed, onMounted } from "vue";
import { useStudentsStore } from "@/stores/students";
import FieldSelector from "./FieldSelector.vue";
import ExportButton from "@/views/Admin/Students/components/ExportButton.vue";

export default {
  components: { ExportButton, FieldSelector },
  setup() {
    const store = useStudentsStore();
    onMounted(() => {
      store.fetchStudents();
    });

    const filterText = ref("");
    const selectedSort = ref("");
    const dialogVisible = ref(false);
    const selectedDetails = ref({});
    const dialogWidth = ref("50%");

    const allFields = [
      "ID",
      "姓名",
      "报名类型",
      "毕业年份",
      "本科学校",
      "本科专业",
      "专业人数",
      "排名",
      "百分比",
      "硕士学校",
      "硕士专业",
      "导师",
      "性别",
      "出生年月",
      "照片",
      "手机号码",
      "电子邮箱",
      "第一志愿",
      "第二志愿",
      "第三志愿",
      "是否服从调剂",
      "简历文件",
      "证明材料",
      "状态",
    ];

    const visibleFields = computed(() => store.visibleFields);

    // 字段映射
    const fieldProps = {
      ID: "id",
      姓名: "name",
      毕业年份: "graduationYear",
      性别: "gender",
      出生年月: "birthDate",
      照片: "photo",
      本科学校: "university",
      本科专业: "major",
      专业人数: "majorCount",
      排名: "rank",
      百分比: "percentage",
      硕士学校: "masterUniversity",
      硕士专业: "masterMajor",
      导师: "tutor",
      手机号码: "phone",
      电子邮箱: "email",
      报名类型: "applicationType",
      第一志愿: "firstChoice",
      第二志愿: "secondChoice",
      第三志愿: "thirdChoice",
      是否服从调剂: "isAdjustable",
      简历文件: "resume",
      证明材料: "proofs",
      状态: "status",
    };

    // 筛选学生数据
    const students = computed(() => store.students || []);
    const filteredStudents = computed(() =>
      students.value.filter((student) =>
        Object.values(student).some((value) =>
          value.toString().includes(filterText.value),
        ),
      ),
    );

    const onFilter = () => {};

    const updateVisibleFields = (fields) => {
      store.visibleFields = fields;
    };

    // 动态生成的论文和奖项字段
    const paperFields = ["论文一", "论文二", "论文三"];
    const awardFields = ["奖项一", "奖项二", "奖项三"];

    // 判断是否是论文或奖项字段
    const isPaperOrAwardField = (field) =>
      paperFields.includes(field) || awardFields.includes(field);

    // 点击展开详情
    const showDetails = (type, details) => {
      selectedDetails.value = details;
      dialogWidth.value = type === "paper" ? "50%" : "40%";
      dialogVisible.value = true;
    };

    return {
      filterText,
      selectedSort,
      allFields,
      visibleFields,
      fieldProps,
      filteredStudents,
      paperFields,
      awardFields,
      isPaperOrAwardField, // 添加这一行
      dialogVisible,
      selectedDetails,
      showDetails,
      onFilter,
      updateVisibleFields,
    };
  },
};
</script>

<style scoped>
.students-form {
  margin: 20px 0 20px 10px;
  width: 100%;
}

.form-settings {
  display: flex;
  align-items: stretch;
  z-index: 1000;
  width: 40%;
  margin-left: 1rem;
  margin-bottom: 10px;
}

.field-selector {
  margin-left: 3rem;
}

.el-input {
  height: 100%;
  margin-left: 3rem;
}

.el-select {
  margin-left: 3rem;
  margin-right: 3rem;
}

.table-container {
  height: 600px;
  overflow-y: auto;
}

.expandable-cell {
  color: #409eff;
  cursor: pointer;
  text-decoration: underline;
}
</style>
