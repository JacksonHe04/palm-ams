<template>
  <form-settings
    :fields="store.allFields"
    :visible-fields="store.visibleFields"
    :table-data="filteredStudents"
    :field-props="store.fieldProps"
    :onFilter="onFilter"
    @update-visible-fields="updateVisibleFields"
    @update-sort="updateSort"
  />

  <div class="students-form">
    <div class="table-container">
      <el-table
        :data="filteredStudents"
        style="width: 100%"
        border
        :table-layout="'auto'"
        :default-sort="{ prop: selectedSort, order: 'ascending' }"
      >
        <!-- 写一个序号列，从1开始 -->
        <el-table-column type="index" label="#" width="50" />
        <!-- 动态生成常规列 -->
        <el-table-column
          v-for="field in store.visibleFields"
          :key="field"
          :prop="store.fieldProps[field]"
          :label="field"
          v-if="!store.isPaperOrAwardField(field)"
          :min-width="150"
        >
          <template #default="{ row }">
            <span>{{
              row[store.fieldProps[field]] !== undefined &&
              row[store.fieldProps[field]] !== null &&
              row[store.fieldProps[field]] !== ""
                ? row[store.fieldProps[field]]
                : ""
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
      <div v-if="selectedDetails">
        <div
          v-for="(value, key) in selectedDetails"
          :key="key"
          class="detail-item"
        >
          <strong>{{ key }}:</strong> {{ value }}
        </div>
      </div>
      <span slot="footer" class="dialog-footer">
        <h1 />
        <el-button @click="dialogVisible = false">关闭</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted, watch } from "vue";
import { useStudentsStore } from "@/stores/studentsStore.js";
import FormSettings from "./FormSettings.vue"; // 引入新的组件

// 数据存储和初始化
const store = useStudentsStore();
onMounted(() => {
  store.fetchStudents();
});

// 过滤和排序相关的数据
const filterText = ref("");
const selectedSort = ref("ID"); // 初始化默认排序字段

// 计算属性
const students = computed(() => store.students || []);
const filteredStudents = computed(() => {
  // 首先过滤掉“硕士等级”为“无”的记录（仅在排序字段为“硕士等级”时生效）
  let filtered = students.value;
  if (selectedSort.value === "硕士等级") {
    filtered = filtered.filter(student => {
      const fieldKey = store.fieldProps[selectedSort.value];
      const value = student[fieldKey];
      return value !== ""; // 过滤掉“无”的记录
    });
  }

  // 然后进行搜索过滤
  filtered = filtered.filter(student => searchInObject(student, filterText.value));

  // 最后进行排序
  return filtered.sort((a, b) => {
    if (!selectedSort.value) return 0;
    const fieldKey = store.fieldProps[selectedSort.value]; // 获取正确的字段名
    let aValue = a[fieldKey];
    let bValue = b[fieldKey];

    // 检查是否为百分比形式的字符串
    const isPercentage = (value) =>
      typeof value === "string" && value.endsWith("%");

    if (isPercentage(aValue) && isPercentage(bValue)) {
      aValue = parseFloat(aValue.replace("%", ""));
      bValue = parseFloat(bValue.replace("%", ""));
      return aValue - bValue;
    }

    // 使用 levelOrder 进行等级比较
    if (store.levelOrder[aValue] !== undefined && store.levelOrder[bValue] !== undefined) {
      return store.levelOrder[aValue] - store.levelOrder[bValue];
    }

    // 确保 aValue 和 bValue 是可比较的类型
    if (typeof aValue === "string" && typeof bValue === "string") {
      return aValue.localeCompare(bValue);
    } else if (typeof aValue === "number" && typeof bValue === "number") {
      return aValue - bValue;
    } else {
      return 0; // 如果类型不匹配，返回 0
    }
  });
});


function searchInObject(obj, searchText) {
  for (const key in obj) {
    if (obj.hasOwnProperty(key)) {
      const value = obj[key];
      if (typeof value === "string" && value.includes(searchText)) {
        return true;
      } else if (Array.isArray(value)) {
        for (const item of value) {
          if (typeof item === "object" && searchInObject(item, searchText)) {
            return true;
          }
        }
      } else if (typeof value === "object" && value !== null) {
        if (searchInObject(value, searchText)) {
          return true;
        }
      }
    }
  }
  return false;
}

const updateSort = (sortField) => {
  selectedSort.value = sortField;
};

// 方法
// 更新可见字段
const updateVisibleFields = (fields) => {
  store.visibleFields = fields;
};

// 奖项、论文详情弹窗
const dialogVisible = ref(false);
const selectedDetails = ref({});
const dialogWidth = ref("50%");

const showDetails = (type, details) => {
  selectedDetails.value = details;
  dialogWidth.value = type === "paper" ? "20%" : "20%";
  dialogVisible.value = true;
};

const onFilter = (value) => {
  filterText.value = value;
};

// 调试输出
watch(selectedSort, (newVal) => {
  console.log("Selected Sort:", newVal);
});

watch(filteredStudents, (newVal) => {
  console.log("Filtered field:", filterText.value);
});
</script>

<style scoped lang="scss">
.students-form {
  width: 100%;
  margin-top: 5rem;
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
  height: 100%;
  overflow-y: auto;
}

.expandable-cell {
  color: #409eff;
  cursor: pointer;
  text-decoration: underline;
}
</style>
