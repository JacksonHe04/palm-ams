<template>
  <div class="p-6 bg-gray-100 min-h-screen">
    <el-tabs type="border-card" class="bg-white rounded-lg shadow-lg">
      <el-tab-pane label="院校等级调整">
        <el-table :data="store.universities" style="width: 100%">
          <el-table-column prop="name" label="院校名称">
            <template #default="{ row }">
              <el-input v-model="row.name" placeholder="请输入院校名称"></el-input>
            </template>
          </el-table-column>
          <el-table-column prop="level" label="等级">
            <template #default="{ row }">
              <el-select v-model="row.level" placeholder="选择等级">
                <el-option label="A" value="A"></el-option>
                <el-option label="B" value="B"></el-option>
                <el-option label="C" value="C"></el-option>
                <el-option label="国际前100" value="国际前100"></el-option>
                <el-option label="国际前200" value="国际前200"></el-option>
              </el-select>
            </template>
          </el-table-column>
          <el-table-column label="操作">
            <template #default="{ $index }">
              <el-button type="danger" @click="removeUniversity($index)" size="small">删除</el-button>
            </template>
          </el-table-column>
        </el-table>
        <div class="mt-4 flex justify-between">
          <el-button type="primary" @click="addUniversity">新增院校</el-button>
          <el-button type="success" @click="store.saveUniversities">保存更改</el-button>
        </div>
      </el-tab-pane>

      <el-tab-pane label="专业分类调整">
        <el-table :data="store.majors" style="width: 100%">
          <el-table-column prop="name" label="专业名称">
            <template #default="{ row }">
              <el-input v-model="row.name" placeholder="请输入专业名称"></el-input>
            </template>
          </el-table-column>
          <el-table-column prop="category" label="分类">
            <template #default="{ row }">
              <el-select v-model="row.category" placeholder="选择分类">
                <el-option label="EECS" value="EECS"></el-option>
                <el-option label="传统工科" value="传统工科"></el-option>
                <el-option label="理科" value="理科"></el-option>
                <el-option label="文商科" value="文商科"></el-option>
              </el-select>
            </template>
          </el-table-column>
          <el-table-column label="操作">
            <template #default="{ $index }">
              <el-button type="danger" @click="removeMajor($index)" size="small">删除</el-button>
            </template>
          </el-table-column>
        </el-table>
        <div class="mt-4 flex justify-between">
          <el-button type="primary" @click="addMajor">新增专业</el-button>
          <el-button type="success" @click="store.saveMajors">保存更改</el-button>
        </div>
      </el-tab-pane>

      <el-tab-pane label="人员身份调整">
        <el-table :data="store.personnel" style="width: 100%">
          <el-table-column prop="name" label="姓名">
            <template #default="{ row }">
              <el-input v-model="row.name" placeholder="请输入姓名"></el-input>
            </template>
          </el-table-column>
          <el-table-column prop="recruitmentType" label="招生类型">
            <template #default="{ row }">
              <el-select v-model="row.recruitmentType" placeholder="选择招生类型">
                <el-option label="硕士生" value="硕士生"></el-option>
                <el-option label="博士生" value="博士生"></el-option>
                <el-option label="硕士生和博士生" value="硕士生和博士生"></el-option>
                <el-option label="暂不招生" value="暂不招生"></el-option>
              </el-select>
            </template>
          </el-table-column>
          <el-table-column label="操作">
            <template #default="{ $index }">
              <el-button type="danger" @click="removePersonnel($index)" size="small">删除</el-button>
            </template>
          </el-table-column>
        </el-table>
        <div class="mt-4 flex justify-between">
          <el-button type="primary" @click="addPersonnel">新增人员</el-button>
          <el-button type="success" @click="store.savePersonnel">保存更改</el-button>
        </div>
      </el-tab-pane>

      <el-tab-pane label="招生年份和时间调整">
        <el-form :model="store.admissionPeriod" label-width="120px">
          <el-form-item label="开始日期">
            <el-date-picker v-model="store.admissionPeriod.startDate" type="date" placeholder="选择开始日期"></el-date-picker>
          </el-form-item>
          <el-form-item label="结束日期">
            <el-date-picker v-model="store.admissionPeriod.endDate" type="date" placeholder="选择结束日期"></el-date-picker>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="store.saveAdmissionPeriod">保存</el-button>
          </el-form-item>
        </el-form>
      </el-tab-pane>
    </el-tabs>
  </div>
</template>

<script setup lang="ts">
import { onMounted } from 'vue';
import { useSettingStore } from '@/stores/settingStore';

const store = useSettingStore();

// 初始化数据
onMounted(() => {
  store.fetchUniversities();
  store.fetchMajors();
  store.fetchPersonnel();
  store.fetchAdmissionPeriod();
});

// 院校相关操作
const addUniversity = () => {
  store.universities.push({ name: '', level: '' });
};

const removeUniversity = (index: number) => {
  store.universities.splice(index, 1);
};

// 专业相关操作
const addMajor = () => {
  store.majors.push({ name: '', category: '' });
};

const removeMajor = (index: number) => {
  store.majors.splice(index, 1);
};

// 人员相关操作
const addPersonnel = () => {
  store.personnel.push({ name: '', recruitmentType: '' });
};

const removePersonnel = (index: number) => {
  store.personnel.splice(index, 1);
};
</script>

<style scoped>
.el-tabs {
  @apply shadow-md rounded-lg;
}

.el-tab-pane {
  @apply p-6;
}

.el-button {
  @apply transition-colors duration-200;
}

.el-button:hover {
  @apply opacity-80;
}

.el-table {
  @apply rounded-lg overflow-hidden;
}
</style>