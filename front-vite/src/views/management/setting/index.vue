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
          <div class="flex gap-4">
            <el-button type="primary" @click="addUniversity">新增院校</el-button>
            <el-button type="warning" @click="handleInitialize">初始化</el-button>
          </div>
          <el-button type="success" @click="handleSaveUniversities">提交更改</el-button>
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
                <el-option label="限制专业" value="限制专业"></el-option>
                <el-option label="数学类" value="数学类"></el-option>
                <el-option label="电子信息类" value="电子信息类"></el-option>
                <el-option label="自动化类" value="自动化类"></el-option>
                <el-option label="其他工科" value="其他工科"></el-option>
                <el-option label="理科（非数学）" value="理科（非数学）"></el-option>
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
          <div class="flex gap-4">
            <el-button type="primary" @click="addMajor">新增专业</el-button>
            <el-button type="warning" @click="handleInitializeMajors">初始化</el-button>
          </div>
          <el-button type="success" @click="handleSaveMajors">提交更改</el-button>
        </div>
      </el-tab-pane>

      <el-tab-pane label="人员身份调整">
        <el-table :data="store.personnel" style="width: 100%">
          <el-table-column prop="name" label="姓名">
            <template #default="{ row }">
              <el-input v-model="row.name" placeholder="请输入姓名"></el-input>
            </template>
          </el-table-column>
          <el-table-column prop="recruitment_type" label="招生类型">
            <template #default="{ row }">
              <el-select v-model="row.recruitment_type" placeholder="选择招生类型">
                <el-option label="博士生、直博生、硕士生" value="博士生、直博生、硕士生"></el-option>
                <el-option label="硕士生" value="硕士生"></el-option>
                <el-option label="博士生、直博生" value="博士生、直博生"></el-option>
                <el-option label="暂不招生" value="暂不招生"></el-option>
              </el-select>
            </template>
          </el-table-column>
          <el-table-column prop="department" label="所属院系">
            <template #default="{ row }">
              <el-input v-model="row.department" placeholder="请输入所属院系"></el-input>
            </template>
          </el-table-column>
          <el-table-column prop="research_direction" label="研究方向">
            <template #default="{ row }">
              <el-input v-model="row.research_direction" placeholder="请输入研究方向"></el-input>
            </template>
          </el-table-column>
          <el-table-column label="操作">
            <template #default="{ $index }">
              <el-button type="danger" @click="removePersonnel($index)" size="small">删除</el-button>
            </template>
          </el-table-column>
        </el-table>
        <div class="mt-4 flex justify-between">
          <div class="flex gap-4">
            <el-button type="primary" @click="addPersonnel">新增人员</el-button>
            <el-button type="warning" @click="handleInitializePersonnel">初始化</el-button>
          </div>
          <el-button type="success" @click="handleSavePersonnel">提交更改</el-button>
        </div>
      </el-tab-pane>

      <el-tab-pane label="招生年份和时间调整">
        <el-form :model="store.admissionPeriod" label-width="120px">
          <el-form-item label="开始日期">
            <div class="flex items-center gap-4">
              <el-date-picker
                v-model="store.admissionPeriod.startDate"
                type="date"
                value-format="YYYY-MM-DD"
                placeholder="选择开始日期"
              ></el-date-picker>
            </div>
          </el-form-item>
          <el-form-item label="结束日期">
            <div class="flex items-center gap-4">
              <el-date-picker
                v-model="store.admissionPeriod.endDate"
                type="date"
                value-format="YYYY-MM-DD"
                placeholder="选择结束日期"
              ></el-date-picker>
            </div>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="handleSaveAdmissionPeriod">提交</el-button>
          </el-form-item>
        </el-form>
      </el-tab-pane>

      <el-tab-pane label="奖项配置">
        <el-table :data="store.awards" style="width: 100%">
          <el-table-column prop="name" label="奖项名称">
            <template #default="{ row }">
              <el-input v-model="row.name" placeholder="请输入奖项名称"></el-input>
            </template>
          </el-table-column>
          <el-table-column prop="level" label="奖项等级">
            <template #default="{ row }">
              <el-select v-model="row.level" placeholder="选择奖项等级">
                <el-option label="国家级" value="国家级"></el-option>
                <el-option label="省部级" value="省部级"></el-option>
                <el-option label="校级" value="校级"></el-option>
              </el-select>
            </template>
          </el-table-column>
          <el-table-column prop="category" label="奖项类别">
            <template #default="{ row }">
              <el-input v-model="row.category" placeholder="请输入奖项类别"></el-input>
            </template>
          </el-table-column>
          <el-table-column label="操作">
            <template #default="{ $index }">
              <el-button type="danger" @click="removeAward($index)" size="small">删除</el-button>
            </template>
          </el-table-column>
        </el-table>
        <div class="mt-4 flex justify-between">
          <el-button type="primary" @click="addAward">新增奖项</el-button>
          <el-button type="success" @click="handleSaveAwards">提交更改</el-button>
        </div>
      </el-tab-pane>

      <el-tab-pane label="年份配置">
        <el-table :data="store.years" style="width: 100%">
          <el-table-column prop="year" label="年份">
            <template #default="{ row }">
              <el-input v-model="row.year" placeholder="请输入年份"></el-input>
            </template>
          </el-table-column>
          <el-table-column prop="status" label="状态">
            <template #default="{ row }">
              <el-select v-model="row.status" placeholder="选择状态">
                <el-option label="启用" value="启用"></el-option>
                <el-option label="禁用" value="禁用"></el-option>
              </el-select>
            </template>
          </el-table-column>
          <el-table-column label="操作">
            <template #default="{ $index }">
              <el-button type="danger" @click="removeYear($index)" size="small">删除</el-button>
            </template>
          </el-table-column>
        </el-table>
        <div class="mt-4 flex justify-between">
          <el-button type="primary" @click="addYear">新增年份</el-button>
          <el-button type="success" @click="handleSaveYears">提交更改</el-button>
        </div>
      </el-tab-pane>
    </el-tabs>
  </div>
</template>

<script setup lang="ts">
import { onMounted, watch } from 'vue';
import { useSettingStore } from '@/stores/settingStore';
import { ElMessage, ElMessageBox } from 'element-plus';

const store = useSettingStore();

// 初始化数据
onMounted(() => {
  store.initializeData();
});

// 院校相关操作
const addUniversity = () => {
  store.universities.push({ name: '', level: '' });
};

const removeUniversity = async (index: number) => {
  store.universities.splice(index, 1);
  await store.saveUniversities();
};

// 专业相关操作
const addMajor = () => {
  store.majors.push({ name: '', category: '' });
};

const removeMajor = async (index: number) => {
  store.majors.splice(index, 1);
  await store.saveMajors();
};

// 人员相关操作
const addPersonnel = () => {
  store.personnel.push({ name: '', recruitment_type: '', department: '', research_direction: '' });
};

const removePersonnel = async (index: number) => {
  store.personnel.splice(index, 1);
  await store.savePersonnel();
};

// 奖项相关操作
const addAward = () => {
  store.awards.push({ name: '', level: '', category: '' });
};

const removeAward = async (index: number) => {
  store.awards.splice(index, 1);
  await store.saveAwards();
};

const handleSaveAwards = async () => {
  await store.saveAwards();
  ElMessage.success('奖项配置保存成功');
};

// 年份相关操作
const addYear = () => {
  store.years.push({ year: '', status: '' });
};

const removeYear = async (index: number) => {
  store.years.splice(index, 1);
  await store.saveYears();
};

const handleSaveYears = async () => {
  await store.saveYears();
  ElMessage.success('年份配置保存成功');
};

const handleInitialize = async () => {
  try {
    await ElMessageBox.confirm(
      '确定要初始化院校数据吗？这将覆盖当前所有数据。',
      '警告',
      {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning',
      }
    );
    await store.initializeUniversities();
    ElMessage.success('院校数据初始化成功');
  } catch (error) {
    if (error !== 'cancel') {
      ElMessage.error('院校数据初始化失败');
    }
  }
};

const handleInitializeMajors = async () => {
  try {
    await ElMessageBox.confirm(
      '确定要初始化专业数据吗？这将覆盖当前所有数据。',
      '警告',
      {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning',
      }
    );
    await store.initializeMajors();
    ElMessage.success('专业数据初始化成功');
  } catch (error) {
    if (error !== 'cancel') {
      ElMessage.error('专业数据初始化失败');
    }
  }
};

const handleInitializePersonnel = async () => {
  try {
    await ElMessageBox.confirm(
      '确定要初始化人员数据吗？这将覆盖当前所有数据。',
      '警告',
      {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning',
      }
    );
    await store.initializePersonnel();
    ElMessage.success('人员数据初始化成功');
  } catch (error) {
    if (error !== 'cancel') {
      ElMessage.error('人员数据初始化失败');
    }
  }
};

// 添加数据变化监听
watch(() => store.universities, () => {
  if (!store.isInitializing) {
    ElMessage.warning('您已修改院校数据，请记得提交更改');
  }
}, { deep: true });

watch(() => store.majors, () => {
  if (!store.isInitializing) {
    ElMessage.warning('您已修改专业数据，请记得提交更改');
  }
}, { deep: true });

watch(() => store.personnel, () => {
  if (!store.isInitializing) {
    ElMessage.warning('您已修改人员数据，请记得提交更改');
  }
}, { deep: true });

watch([() => store.admissionPeriod.startDate, () => store.admissionPeriod.endDate], () => {
  if (!store.isInitializing) {
    ElMessage.warning('您已修改招生时间，请记得提交更改');
  }
});

// 修改提交方法
const handleSaveUniversities = async () => {
  try {
    await store.saveUniversities();
    ElMessage.success('院校数据提交成功');
  } catch (error) {
    ElMessage.error('院校数据提交失败');
  }
};

const handleSaveMajors = async () => {
  try {
    await store.saveMajors();
    ElMessage.success('专业数据提交成功');
  } catch (error) {
    ElMessage.error('专业数据提交失败');
  }
};

const handleSavePersonnel = async () => {
  try {
    await store.savePersonnel();
    ElMessage.success('人员数据提交成功');
  } catch (error) {
    ElMessage.error('人员数据提交失败');
  }
};

const handleSaveAdmissionPeriod = async () => {
  try {
    await store.saveAdmissionPeriod();
    ElMessage.success('招生时间提交成功');
  } catch (error) {
    ElMessage.error('招生时间提交失败');
  }
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