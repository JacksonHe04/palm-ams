<script setup>
import { ref, watch } from "vue";
import DividerLine from "@/views/Apply/components/tools/DividerLine.vue";
import { useApplyStore } from "@/stores/applyStore.js";

const props = defineProps({
  modelValue: Object
});

const emit = defineEmits(['update:modelValue']);

const applyStore = useApplyStore();

// 监听 applyStore.awards 的变化
watch(
  () => applyStore.awards,
  (newVal) => {
    emit('update:modelValue', {
      ...props.modelValue,
      awards: newVal
    });
  },
  { deep: true }
);

// 初始化 awards
if (!applyStore.awards.length) {
  applyStore.updateField('awards', [{ awardTime: "", awardName: "", levelRanking: "", isLeader: false }]);
}

// 奖项类别选项
const awardGrades = ["世界级", "国家级", "省级", "市级", "校级", "院级"];

// 切换是否为负责人的开关
const toggleSwitch = (index) => {
  const newAwards = [...applyStore.awards];
  newAwards[index].isLeader = !newAwards[index].isLeader;
  applyStore.updateField('awards', newAwards);
};

// 添加新奖项
const addAward = () => {
  const newAwards = [...applyStore.awards, { awardTime: "", awardName: "", levelRanking: "", isLeader: false, awardRanking: ""}];
  applyStore.updateField('awards', newAwards);
};

// 移除最后一条奖项，保留至少一条
const removeAward = () => {
  if (applyStore.awards.length > 1) {
    const newAwards = applyStore.awards.slice(0, -1);
    applyStore.updateField('awards', newAwards);
  }
};
</script>

<template>
  <div>
    <p class="infoClassTitle">奖项荣誉</p>

    <div v-for="(award, index) in applyStore.awards" :key="index" class="form-group">
      <!-- 第一行: 获奖时间、奖项类别、是否为负责人 -->
      <div class="award-row">
        <div class="col-xs-1 col-sm-1 col-md-1 col-lg-1"></div>

        <label class="col-xs-1 col-sm-1 col-md-1 col-lg-1 control-label" style="white-space: nowrap">
          奖项类别
        </label>
        <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2">
          <input
              type="text"
              class="form-control"
              :name="`award_grade${index + 1}`"
              v-model="award.levelRanking"
              :list="`award-grade${index + 1}`"
              placeholder="请选择"
          />
          <datalist :id="`award-grade${index + 1}`" style="display: none">
            <option v-for="grade in awardGrades" :value="grade" :key="grade">
              {{ grade }}
            </option>
          </datalist>
        </div>

        <label class="col-xs-1 col-sm-1 col-md-1 col-lg-1 control-label" style="white-space: nowrap">
          是否为负责人
        </label>
        <div class="col-xs-1 col-sm-1 col-md-1 col-lg-1 control-label">
          <div class="switch" :class="{ 'switch-on': award.isLeader }" @click="toggleSwitch(index)">
            <span class="switch-handle"></span>
          </div>
        </div>

        <label class="col-xs-1 col-sm-1 col-md-1 col-lg-1 control-label" style="white-space: nowrap">
          获奖时间
        </label>
        <div class="col-xs-3 col-sm-3 col-md-3 col-lg-3">
          <div class="input-group date" :id="`datetimepicker-award${index + 1}`">
            <input
                type="text"
                class="form-control"
                :name="`time_award${index + 1}`"
                v-model="award.awardTime"
                placeholder="无"
            />
            <span class="input-group-addon">
              <span class="glyphicon glyphicon-calendar"></span>
            </span>
          </div>
        </div>
      </div>

      <!-- 第二行: 奖项名称、等级与排名 -->
      <div class="clearfix"></div>
      <div class="col-xs-1 col-sm-1 col-md-1 col-lg-1"></div>
      <label class="col-xs-1 col-sm-1 col-md-1 col-lg-1 control-label" style="white-space: nowrap">
        奖项名称
      </label>
      <div class="col-xs-4 col-sm-4 col-md-4 col-lg-4">
        <input
            type="text"
            class="form-control"
            :name="`award_name${index + 1}`"
            v-model="award.awardName"
            placeholder="如：诺贝尔物理学奖"
        />
      </div>

      <label class="col-xs-1 col-sm-1 col-md-1 col-lg-1 control-label" style="white-space: nowrap">
        等级与排名
      </label>
      <div class="col-xs-3 col-sm-3 col-md-3 col-lg-3">
        <input
            type="text"
            class="form-control"
            :name="`award_rank${index + 1}`"
            v-model="award.awardRanking"
            placeholder="如：一等奖/第一名"
        />
      </div>
      <div class="col-xs-1 col-sm-1 col-md-1 col-lg-1"></div>

      <!-- 分隔线 -->
      <div class="col-xs-12 col-sm-12 col-md-12 col-lg-12">
        <hr class="divider"/>
      </div>

      <!-- 加号和减号按钮，仅在最后一条记录下方显示 -->
      <div v-if="index === applyStore.awards.length - 1" class="col-xs-12 text-center mt-2">
        <button @click="addAward" class="btn btn-apply">+</button>
        <button v-if="applyStore.awards.length > 1" @click="removeAward" class="btn btn-danger ml-2">-</button>
      </div>
    </div>
  </div>
  <DividerLine />
</template>

<style scoped>
.award-row {
  margin-bottom: 10px;
  display: flex;
}

.switch {
  position: relative;
  width: 50px;
  height: 24px;
  background-color: #ccc;
  border-radius: 12px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.switch-on {
  background-color: #4caf50;
}

.switch-handle {
  position: absolute;
  top: 2px;
  left: 2px;
  width: 20px;
  height: 20px;
  background-color: white;
  border-radius: 50%;
  transition: transform 0.3s;
}

.switch-on .switch-handle {
  transform: translateX(26px);
}

.divider {
  border: none;
  border-top: 1px solid #ffffff;
  width: 80%;
  margin: 20px auto 5px auto;
}

.mt-2 {
  margin-top: 10px;
}

.ml-2 {
  margin-left: 10px;
}
</style>
