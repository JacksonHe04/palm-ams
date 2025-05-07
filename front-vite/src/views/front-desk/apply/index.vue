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

          <!-- 论文情况的特殊处理 -->
          <template v-if="region === '论文情况'">
            <div class="sub-sections-wrapper">
              <div
                v-for="index in paperCount"
                :key="`paper${index}`"
                class="sub-section"
              >
                <div class="sub-section-header">
                  <h3 class="sub-section-title">论文 {{ index }}</h3>
                  <div class="button-group">
                    <el-button
                      v-if="paperCount > 1"
                      type="danger"
                      link
                      @click="removePaper(index)"
                    >
                      <el-icon><Delete /></el-icon>删除
                    </el-button>
                    <el-button
                      v-if="index === paperCount && paperCount < 3"
                      type="primary"
                      link
                      @click="paperCount++"
                    >
                      <el-icon><Plus /></el-icon>添加论文
                    </el-button>
                  </div>
                </div>
                <div class="form-item-container">
                  <FormField
                    v-for="field in getPaperFields(index)"
                    :key="field.id"
                    :field="field"
                    v-model="formData[field.variableName]"
                    :required="isFieldRequired(field.variableName)"
                    :options="getSelectOptions(field.name)"
                  />
                </div>
              </div>
            </div>
          </template>

          <!-- 奖项的特殊处理 -->
          <template v-else-if="region === '奖项'">
            <div class="sub-sections-wrapper">
              <div
                v-for="index in awardCount"
                :key="`award${index}`"
                class="sub-section"
              >
                <div class="sub-section-header">
                  <h3 class="sub-section-title">奖项 {{ index }}</h3>
                  <div class="button-group">
                    <el-button
                      v-if="awardCount > 1"
                      type="danger"
                      link
                      @click="removeAward(index)"
                    >
                      <el-icon><Delete /></el-icon>删除
                    </el-button>
                    <el-button
                      v-if="index === awardCount && awardCount < 3"
                      type="primary"
                      link
                      @click="awardCount++"
                    >
                      <el-icon><Plus /></el-icon>添加奖项
                    </el-button>
                  </div>
                </div>
                <div class="form-item-container">
                  <FormField
                    v-for="field in getAwardFields(index)"
                    :key="field.id"
                    :field="field"
                    v-model="formData[field.variableName]"
                    :required="isFieldRequired(field.variableName)"
                    :options="getSelectOptions(field.name)"
                  />
                </div>
              </div>
            </div>
          </template>

          <template v-else>
            <div class="form-item-container">
              <FormField
                v-for="field in getFieldsByRegion(region)"
                :key="field.id"
                :field="field"
                v-model="formData[field.variableName]"
                :required="isFieldRequired(field.variableName)"
                :options="getSelectOptions(field.name)"
              />
            </div>
          </template>
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
import { ref, onMounted, computed, watch } from "vue";
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
  gender,
} from "./composables/formConfig";

// 选项配置对象
const selectOptions = computed(() => ({
  "论文一 CCF等级": ccfLevel,
  "论文二 CCF等级": ccfLevel,
  "论文三 CCF等级": ccfLevel,
  "奖项一 等级": awardLevel,
  "奖项二 等级": awardLevel,
  "奖项三 等级": awardLevel,
  "奖项一 获奖情况": awardRanking,
  "奖项二 获奖情况": awardRanking,
  "奖项三 获奖情况": awardRanking,
  性别: gender,
  本科学校: settingStore.universities.map((uni) => ({
    value: uni.name,
    label: uni.name,
  })),
  硕士学校: settingStore.universities.map((uni) => ({
    value: uni.name,
    label: uni.name,
  })),
  本科专业: settingStore.majors.map((major) => ({
    value: major.name,
    label: major.name,
  })),
  硕士专业: settingStore.majors.map((major) => ({
    value: major.name,
    label: major.name,
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
const { calculatePercentage } = usePercentageCalculation(formData);

// 添加监听器来处理百分比的计算
watch(
  () => [formData.value.rank, formData.value.majorCount],
  () => {
    calculatePercentage();
  },
  { immediate: true }
);

// 初始化表单数据
const initFormData = () => {
  const initialData = {
    id: uuidv4(),
  };

  applyFields.value.forEach((field) => {
    if (field.variableName === "isAdjustable") {
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

import FormField from "./components/FormField.vue";

// 获取特定论文序号的相关字段
const getPaperFields = (paperIndex: number) => {
  return applyFields.value.filter((field) => {
    return (
      field.regionInForm === "论文情况" &&
      field.variableName.startsWith(`paper${paperIndex}`)
    );
  });
};

// 获取特定奖项序号的相关字段
const getAwardFields = (awardIndex: number) => {
  return applyFields.value.filter((field) => {
    return (
      field.regionInForm === "奖项" &&
      field.variableName.startsWith(`award${awardIndex}`)
    );
  });
};

// 添加论文和奖项计数器
const paperCount = ref(1)
const awardCount = ref(1)

/**
 * 删除指定序号的论文
 * @param index 要删除的论文序号
 */
const removePaper = (index: number) => {
  // 获取所有论文相关字段
  const allPaperFields = applyFields.value.filter(
    field => field.regionInForm === '论文情况'
  )

  // 将要删除的论文之后的论文数据前移
  for (let i = index; i < paperCount.value; i++) {
    allPaperFields.forEach(field => {
      const currentKey = `paper${i}`
      const nextKey = `paper${i + 1}`
      if (field.variableName.startsWith(currentKey)) {
        const nextField = field.variableName.replace(currentKey, nextKey)
        formData.value[field.variableName] = formData.value[nextField]
      }
    })
  }

  // 清空最后一个论文的数据
  allPaperFields.forEach(field => {
    if (field.variableName.startsWith(`paper${paperCount.value}`)) {
      formData.value[field.variableName] = ''
    }
  })

  paperCount.value--
}

/**
 * 删除指定序号的奖项
 * @param index 要删除的奖项序号
 */
const removeAward = (index: number) => {
  // 获取所有奖项相关字段
  const allAwardFields = applyFields.value.filter(
    field => field.regionInForm === '奖项'
  )

  // 将要删除的奖项之后的奖项数据前移
  for (let i = index; i < awardCount.value; i++) {
    allAwardFields.forEach(field => {
      const currentKey = `award${i}`
      const nextKey = `award${i + 1}`
      if (field.variableName.startsWith(currentKey)) {
        const nextField = field.variableName.replace(currentKey, nextKey)
        formData.value[field.variableName] = formData.value[nextField]
      }
    })
  }

  // 清空最后一个奖项的数据
  allAwardFields.forEach(field => {
    if (field.variableName.startsWith(`award${awardCount.value}`)) {
      formData.value[field.variableName] = ''
    }
  })

  awardCount.value--
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

.sub-sections-wrapper {
  @apply flex flex-col gap-6;
}

.sub-section {
  @apply mb-0 p-4 bg-gray-50 rounded-lg;

  .sub-section-header {
    @apply flex justify-between items-center mb-4;
  }

  .sub-section-title {
    @apply text-lg font-semibold text-gray-700;
  }
}
</style>
