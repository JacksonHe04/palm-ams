<template>
  <div class="new-apply-container">
    <!-- 开发阶段提示信息 -->
    <div class="dev-notice">
      <el-alert
        title="开发阶段提示"
        type="warning"
        description="本网站目前处于开发阶段，可能存在一些问题。如遇到任何问题，请发送邮件至 palmapplication@163.com，我们会尽快处理。"
        :closable="false"
        show-icon
      />
    </div>
    <form @submit.prevent="handleSubmit" class="apply-form">
      <template
        v-for="region in [
          '个人信息',
          '学历信息',
          '申请志愿',
          '论文情况',
          '奖项',
          '其他',
        ]"
        :key="region"
      >
        <div v-if="getFieldsByRegion(region).length > 0" class="form-region">
          <h2 class="region-title">{{ region }}</h2>
          <div class="form-item-container">
            <FormField
              v-for="field in getFieldsByRegion(region)"
              :key="field.id"
              :field="field"
              v-model="formData[field.variableName]"
              :required="isFieldRequired(field.variableName)"
              :options="getSelectOptions(field.name)"
              :contribution-data="
                isContributionField(field.variableName)
                  ? contributionData[field.variableName]
                  : undefined
              "
              @input="
                field.variableName === 'rank' ||
                field.variableName === 'majorCount'
                  ? calculatePercentage()
                  : null
              "
              @contribution-change="
                (data) => updateContribution(field.variableName, data)
              "
            />
          </div>
        </div>
      </template>

      <!-- 上传简历 -->
      <UploadResume />

      <!-- 证明文件上传 -->
      <UploadFile :applicant-id="formData.id" />

      <button type="submit" class="submit-button">提交申请</button>
    </form>
  </div>
</template>

<script setup lang="ts">
import { onMounted, computed } from "vue";
import { useRoute, useRouter } from "vue-router";
import { ElMessage } from "element-plus";
import { v4 as uuidv4 } from "uuid";

import { useFieldStore } from "@/stores/fieldStore";
import { useSettingStore } from "@/stores/settingStore";
import { useFormValidation } from "./composables/useFormValidation";
import { usePercentageCalculation } from "./composables/usePercentageCalculation";
import { useApplyStore } from "@/stores/applyStore";

import UploadFile from "./components/UploadFile.vue";
import UploadResume from "./components/UploadResume.vue";

const fieldStore = useFieldStore();
const settingStore = useSettingStore();

import {
  ccfLevel,
  awardLevel,
  awardRanking,
  // applicationType,
  gender,
} from "./composables/formConfig";

// 选项配置对象
const selectOptions = computed(() => ({
  // 报名类型: applicationType,
  性别: gender,
  论文一CCF等级: ccfLevel,
  论文二CCF等级: ccfLevel,
  论文三CCF等级: ccfLevel,
  奖项一等级: awardLevel,
  奖项二等级: awardLevel,
  奖项三等级: awardLevel,
  奖项一获奖等级: awardRanking,
  奖项二获奖等级: awardRanking,
  奖项三获奖等级: awardRanking,
  本科学校: settingStore.universities.map((uni) => ({
    value: uni.name,
    label: uni.name,
  })),
  硕士学校: settingStore.universities.map((uni) => ({
    value: uni.name,
    label: uni.name,
  })),
  第一志愿: settingStore.personnel.map((person) => ({
    value: person.name,
    label: `${person.name} (${person.research_direction})`,
  })),
  第二志愿: settingStore.personnel.map((person) => ({
    value: person.name,
    label: `${person.name} (${person.research_direction})`,
  })),
  第三志愿: settingStore.personnel.map((person) => ({
    value: person.name,
    label: `${person.name} (${person.research_direction})`,
  })),
  本科专业: settingStore.majors.map((major) => ({
    value: major.name,
    label: major.name,
  })),
  硕士专业: settingStore.majors.map((major) => ({
    value: major.name,
    label: major.name,
  })),
}));

// 获取下拉选项
const getSelectOptions = (fieldName: string) => {
  return selectOptions.value[fieldName] || [];
};

// 获取需要在申请表单中显示的字段
import { useFieldsSort } from "./composables/useFieldsSort";

const route = useRoute();
const router = useRouter();

// 根据路由路径选择对应显示的字段
const applyFields = computed(() => {
  const routePath = route.path;
  const fields = fieldStore.fields.filter((field) => {
    switch (routePath) {
      case "/apply/recommend-master":
        return field.showInRecommendMaster;
      case "/apply/exam-master":
        return field.showInExamMaster;
      case "/apply/phd":
        return field.showInPhd;
      case "/apply/direct-phd":
        return field.showInDirectPhd;
      default:
        return false;
    }
  });

  // 按照 regionInForm 对字段进行排序
  return useFieldsSort(fields).sortedFields.value;
});

// 根据区域获取字段
const getFieldsByRegion = (region: string) => {
  return applyFields.value.filter((field) => field.regionInForm === region);
};

// 导入表单验证组合式函数
const { isFieldRequired, validateForm } = useFormValidation();

// 提交表单
const handleSubmit = async () => {
  try {
    validateForm(formData.value, applyFields.value);
    await applyStore.submitForm();
    ElMessage.success("申请提交成功");
    router.push("/wait");
  } catch (error) {
    ElMessage.error(error.message || applyStore.submitError || "提交失败");
  }
};

const applyStore = useApplyStore();
const formData = computed(() => applyStore.formData);

// 导入百分比计算组合式函数
const { calculatePercentage, contributionData, updateContribution } =
  usePercentageCalculation(formData);

// 初始化表单数据
const initFormData = () => {
  const initialData = {
    id: uuidv4(),
  };
  // 先初始化贡献度数据
  contributionData.value = {
    award1_contribution: { rank: "", total: "" },
    award2_contribution: { rank: "", total: "" },
    award3_contribution: { rank: "", total: "" },
  };

  applyFields.value.forEach((field) => {
    if (
      [
        "award1_contribution",
        "award2_contribution",
        "award3_contribution",
      ].includes(field.variableName)
    ) {
      initialData[field.variableName] = "";
    } else if (field.variableName === "isAdjustable") {
      initialData[field.variableName] = true;
    } else {
      initialData[field.variableName] = field.type === "boolean" ? false : "";
    }
  });
  applyStore.setFormData(initialData);
};

// 初始化表单字段
onMounted(async () => {
  await Promise.all([
    fieldStore.fetchFields(),
    settingStore.fetchUniversities(),
    settingStore.fetchMajors(),
    settingStore.fetchPersonnel(),
  ]);
  initFormData();
});

import FormField from './components/FormField.vue'

// 新增辅助函数
const isContributionField = (variableName: string) => {
  return [
    'award1_contribution',
    'award2_contribution',
    'award3_contribution'
  ].includes(variableName)
}
</script>

<style lang="scss" scoped>
@use "./index.scss";

.dev-notice {
  @apply mb-6;
}

.form-region {
  @apply mb-8 p-6 bg-white rounded-lg shadow;

  .region-title {
    @apply text-xl font-bold mb-6 text-gray-800 pb-2 border-b border-gray-200;
  }

  .form-item {
    @apply mb-4;
  }
}
</style>
