<script setup>
import { ref, watch } from "vue";
import DividerLine from "@/views/apply/components/tools/DividerLine.vue";
import { useApplyStore } from "@/stores/applyStore.js";

const props = defineProps({
  modelValue: Object,
});

const emit = defineEmits(["update:modelValue"]);

const applyStore = useApplyStore();

// 监听 applyStore.awards 的变化
watch(
  () => applyStore.awards,
  (newVal) => {
    emit("update:modelValue", {
      ...props.modelValue,
      awards: newVal,
    });
  },
  { deep: true },
);

// 初始化 awards
if (!applyStore.awards.length) {
  applyStore.updateField("awards", [
    { awardTime: "", awardName: "", levelRanking: "", isLeader: false },
  ]);
}

// 奖项类别选项
const awardGrades = ["国家级", "省级", "市级", "校级"];

// 切换是否为负责人的开关
const toggleSwitch = (index) => {
  const newAwards = [...applyStore.awards];
  newAwards[index].isLeader = !newAwards[index].isLeader;
  applyStore.updateField("awards", newAwards);
};

// 添加新奖项
const addAward = () => {
  const newAwards = [
    ...applyStore.awards,
    {
      awardTime: "",
      awardName: "",
      levelRanking: "",
      isLeader: false,
      awardRanking: "",
    },
  ];
  applyStore.updateField("awards", newAwards);
};

// 移除最后一条奖项，保留至少一条
const removeAward = () => {
  if (applyStore.awards.length > 1) {
    const newAwards = applyStore.awards.slice(0, -1);
    applyStore.updateField("awards", newAwards);
  }
};
</script>

<template>
  <div>
    <p class="infoClassTitle">奖项荣誉</p>

    <div v-for="(award, index) in applyStore.awards" :key="index" class="mb-8">
      <!-- 第一行: 获奖时间、奖项类别、是否为负责人 -->
      <div class="grid grid-cols-12 gap-4 mb-4 items-center">
        <label class="col-start-2 col-span-1 text-right whitespace-nowrap block"
          >奖项类别</label
        >
        <input
          type="text"
          class="form-control col-span-2"
          :name="`award_grade${index + 1}`"
          v-model="award.levelRanking"
          :list="`award-grade${index + 1}`"
          placeholder="请选择"
        />
        <datalist :id="`award-grade${index + 1}`">
          <option v-for="grade in awardGrades" :value="grade" :key="grade">
            {{ grade }}
          </option>
        </datalist>

        <label class="col-span-2 text-right whitespace-nowrap block"
          >是否为负责人</label
        >
        <div
          class="switch"
          :class="{ 'switch-on': award.isLeader }"
          @click="toggleSwitch(index)"
        >
          <span class="col-span-1 switch-handle"></span>
        </div>

        <label class="col-span-1 text-right whitespace-nowrap block"
          >获奖时间</label
        >
        <div class=" col-span-2 input-group date">
          <input
            type="text"
            class="form-control"
            :name="`time_award${index + 1}`"
            v-model="award.awardTime"
            placeholder="无"
          />
          <!--<span class="input-group-addon">-->
          <!--  <span class="glyphicon glyphicon-calendar"></span>-->
          <!--</span>-->
        </div>
      </div>

      <!-- 第二行: 奖项名称、等级与排名 -->
      <div class="grid grid-cols-12 gap-4 items-center">
          <label class="col-start-2 col-span-1 text-right whitespace-nowrap block">奖项名称</label>
          <input
            type="text"
            class="col-span-3 form-control"
            :name="`award_name${index + 1}`"
            v-model="award.awardName"
            placeholder="如：诺贝尔物理学奖"
          />

          <label class="col-span-1 text-right whitespace-nowrap block">等级与排名</label>
          <input
            type="text"
            class="col-span-3 form-control"
            :name="`award_rank${index + 1}`"
            v-model="award.awardRanking"
            placeholder="如：一等奖/第一名"
          />
      </div>

      <!-- 分隔线 -->
      <div class="w-4/5 mx-auto my-5 border-t border-white"></div>

      <!-- 加号和减号按钮，仅在最后一条记录下方显示 -->
      <div
        v-if="index === applyStore.awards.length - 1"
        class="text-center mt-2"
      >
        <button @click="addAward" class="btn btn-apply">+</button>
        <button
          v-if="applyStore.awards.length > 1"
          @click="removeAward"
          class="btn btn-danger ml-2"
        >
          -
        </button>
      </div>
    </div>
  </div>
  <DividerLine />
</template>

<style scoped>
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
</style>
