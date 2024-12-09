<template>
  <div class="students-form">
    <el-row class="form-settings">
      <el-col :span="8">
        <field-selector
          :fields="store.allFields"
          :visible-fields="store.visibleFields"
          @update-visible-fields="updateVisibleFields"
        />
      </el-col>
      <el-col :span="16" class="search-filter">
        <el-input
          v-model="filterText"
          placeholder="智能筛选您输入的内容"
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
          :visible-fields="store.visibleFields"
          :field-props="store.fieldProps"
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
          v-for="field in store.visibleFields"
          :key="field"
          :prop="store.fieldProps[field]"
          :label="field"
          v-if="!store.isPaperOrAwardField(field)"
          :min-width="100"
        >
          <template #default="{ row }">
            <span>{{
              row[store.fieldProps[field]] !== undefined &&
              row[store.fieldProps[field]] !== null &&
              row[store.fieldProps[field]] !== ""
                ? row[store.fieldProps[field]]
                : "无"
            }}</span>
          </template>
        </el-table-column>

        <!-- 论文列 -->
        <template
          v-for="(paperField, index) in store.paperFields"
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
          v-for="(awardField, index) in store.awardFields"
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
import { useStudentsStore } from "@/stores/studentsStore.js";
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

    // 点击展开详情
    const showDetails = (type, details) => {
      selectedDetails.value = details;
      dialogWidth.value = type === "paper" ? "50%" : "40%";
      dialogVisible.value = true;
    };

    return {
      store,
      filterText,
      selectedSort,
      filteredStudents,
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
