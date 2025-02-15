<template>
  <el-row class="form-settings">
    <!-- 字段选择 -->
    <div class="form-setting border-x p-1 form-filed-choose">
      <FieldSelector
        :fields="fields"
        :visible-fields="visibleFields"
        @update-visible-fields="updateVisibleFields"
      />
    </div>
    <!-- 搜索 -->
    <div class="form-setting form-search">
      <el-input v-model="filterText" placeholder="搜索" @input="onFilter" />
    </div>
    <!-- 排序 -->
    <div class="form-setting form-sort">
      <el-select v-model="selectedSort" placeholder="排序">
        <el-option
          v-for="option in sortOptions"
          :key="option.value"
          :label="option.label"
          :value="option.value"
        />
      </el-select>
    </div>
    <!-- 导出组件 -->
    <div class="form-setting form-export">
      <ExportButton
        :table-data="tableData"
        :visible-fields="visibleFields"
        :field-props="fieldProps"
        :store="store"
      />
    </div>
  </el-row>
</template>

<script setup>
import { ref, computed, watch } from "vue";
import { useStudentsStore } from "@/stores/studentsStore.js";
import FieldSelector from "./FieldSelector.vue";
import ExportButton from "@/views/management/table/components/ExportButton.vue";

const store = useStudentsStore();

// 过滤和排序相关的数据
const filterText = ref("");
const selectedSort = ref("ID"); // 初始化默认排序字段

// 接收父组件传递的 props
const props = defineProps({
  fields: {
    type: Array,
    required: true,
  },
  visibleFields: {
    type: Array,
    required: true,
  },
  tableData: {
    type: Array,
    required: true,
  },
  fieldProps: {
    type: Object,
    required: true,
  },
  onFilter: {
    type: Function,
    required: true,
  },
});

// 计算属性
const sortOptions = computed(() => {
  return store.sortableFields.map((field) => ({
    label: field,
    value: field,
  }));
});

// 方法
const onFilter = (value) => {
  props.onFilter(value);
};

// 更新可见字段
const updateVisibleFields = (fields) => {
  emit("update-visible-fields", fields);
};

// 调试输出
watch(selectedSort, (newVal) => {
  emit("update-sort", newVal);
  console.log("Selected Sort:", newVal);
});
const emit = defineEmits(["update-visible-fields", "update-sort"]);

</script>

<style scoped lang="scss">
.form-settings {
  position: fixed;
  z-index: 1000;
  width: 80%;
  padding: 10px;
  display: flex;
  flex-wrap: nowrap;
  align-items: center;
  background-color: $admin-bg-color;
  border: 1px solid $admin-border;
}
.form-setting {
  height: 100%;
  flex: 1;
}
.form-filed-choose {
  width: 10%;
}
.form-search {
  width: 25%;
}
.form-sort {
  width: 25%;
}
.form-export {
  width: 25%;
}
</style>
