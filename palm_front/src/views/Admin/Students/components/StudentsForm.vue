<template>
  <div class="students-form">
    <el-row>
      <el-col :span="6">
        <field-selector
            :fields="allFields"
            :visible-fields="visibleFields"
            @update-visible-fields="updateVisibleFields" />
      </el-col>
      <el-col :span="18" class="search-filter">
        <el-input
            v-model="filterText"
            placeholder="搜索姓名、邮箱或手机号"
            @input="onFilter" />
        <el-select v-model="selectedSort" placeholder="排序">
          <el-option
              v-for="option in sortOptions"
              :key="option.value"
              :label="option.label"
              :value="option.value" />
        </el-select>
      </el-col>
    </el-row>

    <el-table
        :data="filteredStudents"
        style="width: 100%"
        :default-sort="{ prop: selectedSort, order: 'ascending' }">
      <el-table-column
          v-for="field in visibleFields"
          :key="field"
          :prop="fieldProps[field]"
          :label="field" />
      <el-table-column label="操作" width="150">
        <template #default="{ row }">
          <el-button type="text" @click="editStudent(row)">编辑</el-button>
          <el-button type="text" @click="deleteStudent(row)">删除</el-button>
        </template>
      </el-table-column>
    </el-table>

    <!--<pagination-->
    <!--    :total="students.length"-->
    <!--    :current-page="currentPage"-->
    <!--    :page-size="pageSize"-->
    <!--    @page-change="onPageChange" />-->
  </div>
</template>

<script>
import { ref, computed } from 'vue';
import { useStudentsStore } from '@/stores/students';
import FieldSelector from './FieldSelector.vue';
import Pagination from './Pagination.vue';

export default {
  components: { FieldSelector, Pagination },
  setup() {
    const store = useStudentsStore();
    const filterText = ref('');
    const currentPage = ref(1);
    const pageSize = ref(10);
    const selectedSort = ref('');

    const allFields = [
      '序号', '照片', '姓名', '昵称', '邮箱', '手机号', '本科院校',
      '本科专业', '百分比', '专业人数', '排名', '硕士院校', '硕士专业',
      '硕士导师', '性别', '出生年月', '报名类型', '第一志愿', '第二志愿',
      '第三志愿', '服从调剂', '论文发表', '奖项荣誉', '简历', '证明材料',
      '状态', '创建时间', '操作'
    ];

    const visibleFields = computed(() => store.visibleFields);
    const fieldProps = {
      '序号': 'id', '姓名': 'name', '邮箱': 'email', '状态': 'status', '操作': '',
      // 其余字段自行映射...
    };

    const students = computed(() => store.students || []);

    const filteredStudents = computed(() => {
      return students.value
          .filter(student =>
              Object.values(student)
                  .some(value => value.toString().includes(filterText.value)))
          .slice((currentPage.value - 1) * pageSize.value, currentPage.value * pageSize.value);
    });

    const onFilter = () => {
      currentPage.value = 1; // 每次筛选时回到第一页
    };

    const updateVisibleFields = (fields) => {
      store.visibleFields = fields;
    };

    const onPageChange = (page) => {
      currentPage.value = page;
    };

    return {
      filterText, currentPage, pageSize, selectedSort,
      allFields, visibleFields, fieldProps, filteredStudents,
      onFilter, updateVisibleFields, onPageChange
    };
  }
};
</script>

<style scoped>
.students-form {
  margin: 20px;
  /* height: 800px; */
  /* width: 1800px; */
}
.search-filter {
  display: flex;
  justify-content: flex-end;
}
</style>