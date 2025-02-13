<script setup>
import { ref, watch } from "vue";
import DividerLine from "@/views/apply/components/tools/DividerLine.vue";
import { useApplyStore } from "@/stores/applyStore.js";

const applyStore = useApplyStore();

const mentors = [
  { value: "", text: "" },
  { value: "耿新", text: "耿新(博导)" },
  { value: "张敏灵", text: "张敏灵(博导)" },
  { value: "薛晖", text: "薛晖(博导)" },
  { value: "周德宇", text: "周德宇(博导)" },
  { value: "张宇", text: "张宇(博导)" },
  { value: "魏秀参", text: "魏秀参(博导)" },
  { value: "宋沫飞", text: "宋沫飞(博导)" },
  { value: "贾育衡", text: "贾育衡(博导)" },
  { value: "陈浩", text: "陈浩(博导)" },
  { value: "杨旭", text: "杨旭(博导)" },
  { value: "周毅", text: "周毅(博导)" },
  { value: "魏通", text: "魏通(博导)" },
  { value: "王洪松", text: "王洪松(博导)" },
  { value: "方鹏飞", text: "方鹏飞(博导)" },
  { value: "李竹颖", text: "李竹颖(博导)" },
  { value: "闫亚萍", text: "闫亚萍" },
  { value: "时霄", text: "时霄" },
  { value: "祁磊", text: "祁磊" },
  { value: "徐宁", text: "徐宁" },
  { value: "乔伊果", text: "乔伊果" },
  { value: "吕佳祺", text: "吕佳祺" },
  { value: "王靖", text: "王靖" },
  { value: "石楚涵", text: "石楚涵" },
];

// 定义本地 ref 并初始化为 Pinia 中的值
const registrationType = ref(applyStore.applicationType);
const firstChoice = ref(applyStore.firstChoice);
const secondChoice = ref(applyStore.secondChoice);
const thirdChoice = ref(applyStore.thirdChoice);
const isAdjustable = ref(applyStore.isAdjustable ? "是" : "否"); // 修改这里

// 监听本地 ref 的变化，并更新 Pinia 中的状态
watch(registrationType, (newValue) => {
  applyStore.updateField("applicationType", newValue);
});

watch(firstChoice, (newValue) => {
  applyStore.updateField("firstChoice", newValue);
});

watch(secondChoice, (newValue) => {
  applyStore.updateField("secondChoice", newValue);
});

watch(thirdChoice, (newValue) => {
  applyStore.updateField("thirdChoice", newValue);
});

watch(isAdjustable, (newValue) => {
  applyStore.updateField("isAdjustable", newValue === "是" ? true : false); // 修改这里
});

// 切换是否服从调剂的开关
const toggleAdjustable = () => {
  isAdjustable.value = isAdjustable.value === "是" ? "否" : "是";
};
</script>

<template>
  <div class="px-8">
    <!-- 文字大小为2xl，字体加粗，下方外边距为8 -->
    <p class="text-2xl font-bold mb-8">意向选择</p>
    <div class="grid grid-cols-12 mb-8">
      <!-- 报名类型 -->
      <div class="col-start-2 col-span-3 grid grid-cols-8 items-center">
        <!-- 文字靠右对齐，右侧外边距为4 -->
        <label class="col-span-3 text-right mr-4">报名类型</label>
        <!-- 表单控件，占据5列 -->
        <select
          class="col-span-5 form-control"
          v-model="registrationType"
          required
        >
          <option value="请选择">请选择</option>
          <option value="硕士">硕士</option>
          <option value="博士">博士</option>
          <option value="直博">直博</option>
        </select>
      </div>

      <!-- 占据3列 -->
      <div class="col-span-3 grid grid-cols-8 items-center">
        <!-- 文字靠右对齐，右侧外边距为4 -->
        <label class="col-span-3 text-right mr-4">服从调剂</label>
        <div class="col-span-5">
          <!-- 开关样式，如果isAdjustable为'是'则添加'switch-on'类 -->
          <div
            class="switch"
            :class="{ 'switch-on': isAdjustable === '是' }"
            @click="toggleAdjustable"
          >
            <span class="switch-handle"></span>
          </div>
        </div>
      </div>
      <!-- 文字大小为sm，文字颜色为灰色500，上方外边距为1 -->
      <transition name="fade">
        <div
          class="col-span-4 text-sm text-gray-500 flex items-center"
          v-if="isAdjustable === '是'"
        >
          如果意向导师无法接收，调剂到其他导师
        </div>
      </transition>
    </div>

    <div class="grid grid-cols-12 mb-8">
      <div class="col-start-2 col-span-3 grid grid-cols-8 items-center">
        <label class="col-span-3 text-right mr-4">第一志愿</label>
        <select class="col-span-5 form-control" v-model="firstChoice" required>
          <option
            v-for="mentor in mentors"
            :key="mentor.value"
            :value="mentor.value"
          >
            {{ mentor.text }}
          </option>
        </select>
      </div>

      <div class="col-span-3 grid grid-cols-8 items-center">
        <label class="col-span-3 text-right mr-4">第二志愿</label>
        <select class="col-span-5 form-control" v-model="secondChoice" required>
          <option
            v-for="mentor in mentors"
            :key="mentor.value"
            :value="mentor.value"
          >
            {{ mentor.text }}
          </option>
        </select>
      </div>

      <div class="col-span-3 grid grid-cols-8 items-center">
        <label class="col-span-3 text-right mr-4">第三志愿</label>
        <select class="col-span-5 form-control" v-model="thirdChoice" required>
          <option
            v-for="mentor in mentors"
            :key="mentor.value"
            :value="mentor.value"
          >
            {{ mentor.text }}
          </option>
        </select>
      </div>
    </div>
  </div>
  <DividerLine />
</template>

<style scoped>
.form-control {
  @apply px-3 py-2 rounded-lg border border-gray-300 focus:border-blue-500 focus:ring-1 focus:ring-blue-500;
}

.switch {
  @apply relative w-12 h-6 bg-gray-300 rounded-full cursor-pointer transition-colors duration-300;
}

.switch-on {
  @apply bg-green-500;
}

.switch-handle {
  @apply absolute top-0.5 left-0.5 w-5 h-5 bg-white rounded-full transition-transform duration-300;
}

.switch-on .switch-handle {
  @apply translate-x-6;
}

/* 添加过渡效果样式 */
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
