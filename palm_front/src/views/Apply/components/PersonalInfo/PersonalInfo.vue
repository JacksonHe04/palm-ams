<script setup>
import { ref, watch, computed } from "vue";
import { useApplyStore } from "@/stores/applyStore.js";
import Avatar from "@/views/Apply/components/PersonalInfo/components/Avatar.vue";
import DegreeInfo from "@/views/Apply/components/PersonalInfo/components/DegreeInfo.vue";
import DividerLine from "@/views/Apply/components/tools/DividerLine.vue";

const applyStore = useApplyStore();

// 处理子组件传递的数据
const handleDegreeInfoUpdate = (data) => {
  if (data.label === "本科") {
    applyStore.updateField("universityLevel", data.rating);
    applyStore.updateField("major", data.major);
    applyStore.updateField("university", data.school); // 更新学校名称
  } else if (data.label === "硕士") {
    applyStore.updateField("masterUniversityLevel", data.rating);
    applyStore.updateField("masterMajor", data.major);
    applyStore.updateField("masterUniversity", data.school); // 更新学校名称
    applyStore.updateField("tutor", data.advisor); // 更新导师信息
  }
};

// 使用 watch 监听数据变化并更新 Pinia
watch(
  () => applyStore.name,
  (newValue) => {
    // 如果需要额外处理，可以在这里添加逻辑
  },
);

// 计算属性
const percentageRank = computed(() => {
  if (!applyStore || !applyStore.majorCount || !applyStore.rank) {
    return "";
  }
  const percentage = (applyStore.rank / applyStore.majorCount) * 100;
  return `${percentage.toFixed(2)}%`;
});

// 监听 percentageRank 变化并更新 Pinia
watch(
  () => percentageRank.value,
  (newValue) => {
    applyStore.updateField("percentage", newValue);
  },
);
</script>

<template>
  <div class="px-8">
    <p class="text-2xl font-bold mb-8">个人基本信息</p>

    <div class="mb-8">
      <!-- 姓名；性别；毕业年份；出生日期 -->
      <div class="grid grid-cols-12 gap-8">
        <!-- 左侧信息 -->
        <div class="col-span-4 col-start-2 space-y-4">
          <!-- 姓名 -->
          <div class="grid grid-cols-8 items-center">
            <label class="col-span-2 text-right mr-4">姓 名</label>
            <input
              type="text"
              class="col-span-6 form-control"
              v-model="applyStore.name"
              required
            />
          </div>

          <!-- 性别 -->
          <div class="grid grid-cols-8 items-center">
            <label class="col-span-2 text-right mr-4">性 别</label>
            <select
              class="col-span-6 form-control"
              v-model="applyStore.gender"
              id="form_sex"
              required
            >
              <option value="请选择">请选择</option>
              <option value="男">男</option>
              <option value="女">女</option>
            </select>
          </div>
        </div>

        <!-- 中间信息 -->
        <div class="col-span-4 space-y-4">
          <!-- 毕业年份 -->
          <div class="grid grid-cols-8 items-center">
            <label class="col-span-3 text-right mr-4">毕业年份</label>
            <div class="col-span-5">
              <select
                class="form-control mb-2"
                v-model="applyStore.graduationYear"
                required
              >
                <option value="2024">2024</option>
                <option value="2025" selected>2025</option>
                <option value="2026">2026</option>
                <option value="">其他</option>
              </select>
              <input
                v-if="applyStore.graduationYear === ''"
                type="number"
                class="form-control"
                v-model="applyStore.customRound"
                required
              />
            </div>
          </div>

          <!-- 出生日期 -->
          <div class="grid grid-cols-8 items-center">
            <label class="col-span-3 text-right mr-4">出生年月</label>
            <div class="col-span-5">
              <input
                type="date"
                v-model="applyStore.birthDate"
                required
                class="form-control"
              />
            </div>
          </div>
        </div>

        <!-- 头像上传 -->
        <div class="col-span-2">
          <Avatar />
        </div>
      </div>
    </div>

    <!-- 本科信息 -->
    <DegreeInfo label="本科" @degreeInfoUpdated="handleDegreeInfoUpdate" />

    <!-- 专业排名 -->
    <div class="grid grid-cols-12 mb-8 items-center">
      <div class="col-start-2 col-span-3 grid grid-cols-8 items-center">
        <label class="col-span-3 text-right mr-4">专业人数</label>
        <input
          type="text"
          class="col-span-5 form-control"
          v-model.number="applyStore.majorCount"
          min="1"
          required
        />
      </div>
      <div class="col-span-1"></div>

      <label class="col-span-1 text-right mr-4">排 名</label>
      <input
        type="text"
        class="col-span-2 form-control"
        v-model.number="applyStore.rank"
        min="1"
        required
      />

      <div class="col-span-1"></div>
      <label class="col-span-1 text-right mr-4">百分比</label>
      <input
        type="text"
        class="col-span-2 form-control"
        :value="percentageRank"
        readonly
        placeholder="自动计算"
      />
    </div>

    <!-- 硕士信息 -->
    <DegreeInfo
      label="硕士"
      :showAdvisor="true"
      @degreeInfoUpdated="handleDegreeInfoUpdate"
    />

    <!-- 电话；邮箱 -->
    <div class="grid grid-cols-12 mb-8 items-center">
      <div class="col-start-2 col-span-3 grid grid-cols-8 items-center">
        <label class="col-span-3 text-right mr-4">手机号码</label>
        <input
          type="text"
          class="col-span-5 form-control"
          v-model="applyStore.phone"
          id="form_phonenumber"
          required
        />
      </div>
      <div class="col-span-1"></div>
      <div class="col-span-3 grid grid-cols-8 items-center">
        <label class="col-span-3 text-right mr-4">电子邮箱</label>
        <input
          type="text"
          class="col-span-5 form-control"
          v-model="applyStore.email"
          id="form_email"
          required
        />
      </div>
    </div>
  </div>
  <DividerLine />
</template>

<style scoped>
.form-control {
  @apply px-3 py-2 rounded-lg border border-gray-300 focus:border-blue-500 focus:ring-1 focus:ring-blue-500;
}
</style>

<script>
export default {
  data() {
    return {
      selectedRound: "2025",
      customRound: null,
    };
  },
};
</script>
