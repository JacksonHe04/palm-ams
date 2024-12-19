<script setup>
import { ref, watch } from "vue";
import DividerLine from "@/views/Apply/components/tools/DividerLine.vue";
import { useApplyStore } from "@/stores/applyStore.js";

const applyStore = useApplyStore();

// 定义本地 ref 并初始化为 Pinia 中的值
const registrationType = ref(applyStore.applicationType);
const firstChoice = ref(applyStore.firstChoice);
const secondChoice = ref(applyStore.secondChoice);
const thirdChoice = ref(applyStore.thirdChoice);
const isAdjustable = ref(applyStore.isAdjustable);

// 监听本地 ref 的变化，并更新 Pinia 中的状态
watch(registrationType, (newValue) => {
  applyStore.updateField('applicationType', newValue);
});

watch(firstChoice, (newValue) => {
  applyStore.updateField('firstChoice', newValue);
});

watch(secondChoice, (newValue) => {
  applyStore.updateField('secondChoice', newValue);
});

watch(thirdChoice, (newValue) => {
  applyStore.updateField('thirdChoice', newValue);
});

watch(isAdjustable, (newValue) => {
  applyStore.updateField('isAdjustable', newValue === '是' ? true : false);
});
</script>

<template>
<div>
  <p class="infoClassTitle">
    意向选择
  </p>

  <div class="form-group">
    <div class="col-xs-1 col-sm-1 col-md-1 col-lg-1"></div>

    <label
        class="col-xs-1 col-sm-1 col-md-1 col-lg-1 control-label"
        style="white-space: nowrap"
    >报名类型</label
    >
    <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2">
      <select
          class="form-control"
          v-model="registrationType"
          required
      >
        <option value="请选择">请选择</option>
        <option value="硕士">硕士</option>
        <option value="博士">博士</option>
        <option value="直博">直博</option>
      </select>
    </div>
  </div>

  <div class="form-group">
    <div class="col-xs-1 col-sm-1 col-md-1 col-lg-1"></div>

    <label
        class="col-xs-1 col-sm-1 col-md-1 col-lg-1 control-label"
        style="white-space: nowrap"
    >第一志愿</label
    >
    <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2">
      <select
          class="form-control"
          v-model="firstChoice"
          required
      >
        <option value="请选择">请选择</option>
        <option value="耿新">耿新(博导)</option>
        <option value="张敏灵">张敏灵(博导)</option>
        <option value="周德宇">周德宇(博导)</option>
        <option value="薛晖">薛晖(博导)</option>
        <option value="张宇">张宇(博导)</option>
        <option value="魏秀参">魏秀参(博导)</option>
        <option value="闫亚萍">闫亚萍</option>
        <option value="贾育衡">贾育衡(博导)</option>
        <option value="周毅">周毅(博导)</option>
        <option value="陈浩">陈浩(博导)</option>
        <option value="宋沫飞">宋沫飞(博导)</option>
        <option value="李竹颖">李竹颖</option>
        <option value="杨旭">杨旭(博导)</option>
        <option value="魏通">魏通(博导)</option>
        <option value="时霄">时霄</option>
        <option value="祁磊">祁磊</option>
        <option value="徐宁">徐宁</option>
        <option value="王洪松">王洪松</option>
        <option value="乔伊果">乔伊果</option>
        <option value="方鹏飞">方鹏飞</option>
        <option value="吕佳祺">吕佳祺</option>
        <option value="王靖">王靖</option>
        <option value="石楚涵">石楚涵</option>
      </select>
    </div>

    <div class="col-xs-1 col-sm-1 col-md-1 col-lg-1"></div>

    <label
        class="col-xs-1 col-sm-1 col-md-1 col-lg-1 control-label"
        style="white-space: nowrap"
    >第二志愿</label
    >
    <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2">
      <select
          class="form-control"
          v-model="secondChoice"
          required
      >
        <option value="请选择">请选择</option>
        <option value="耿新">耿新(博导)</option>
        <option value="张敏灵">张敏灵(博导)</option>
        <option value="周德宇">周德宇(博导)</option>
        <option value="薛晖">薛晖(博导)</option>
        <option value="张宇">张宇(博导)</option>
        <option value="魏秀参">魏秀参(博导)</option>
        <option value="闫亚萍">闫亚萍</option>
        <option value="贾育衡">贾育衡(博导)</option>
        <option value="周毅">周毅(博导)</option>
        <option value="陈浩">陈浩(博导)</option>
        <option value="宋沫飞">宋沫飞(博导)</option>
        <option value="李竹颖">李竹颖</option>
        <option value="杨旭">杨旭(博导)</option>
        <option value="魏通">魏通(博导)</option>
        <option value="时霄">时霄</option>
        <option value="祁磊">祁磊</option>
        <option value="徐宁">徐宁</option>
        <option value="王洪松">王洪松</option>
        <option value="乔伊果">乔伊果</option>
        <option value="方鹏飞">方鹏飞</option>
        <option value="吕佳祺">吕佳祺</option>
        <option value="王靖">王靖</option>
        <option value="石楚涵">石楚涵</option>
      </select>
    </div>
  </div>

  <div class="form-group">
    <div class="col-xs-1 col-sm-1 col-md-1 col-lg-1"></div>

    <label
        class="col-xs-1 col-sm-1 col-md-1 col-lg-1 control-label"
        style="white-space: nowrap"
    >第三志愿</label
    >
    <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2">
      <select
          class="form-control"
          v-model="thirdChoice"
          required
      >
        <option value="请选择">请选择</option>
        <option value="耿新">耿新(博导)</option>
        <option value="张敏灵">张敏灵(博导)</option>
        <option value="周德宇">周德宇(博导)</option>
        <option value="薛晖">薛晖(博导)</option>
        <option value="张宇">张宇(博导)</option>
        <option value="魏秀参">魏秀参(博导)</option>
        <option value="闫亚萍">闫亚萍</option>
        <option value="贾育衡">贾育衡(博导)</option>
        <option value="周毅">周毅(博导)</option>
        <option value="陈浩">陈浩(博导)</option>
        <option value="宋沫飞">宋沫飞(博导)</option>
        <option value="李竹颖">李竹颖</option>
        <option value="杨旭">杨旭(博导)</option>
        <option value="魏通">魏通(博导)</option>
        <option value="时霄">时霄</option>
        <option value="祁磊">祁磊</option>
        <option value="徐宁">徐宁</option>
        <option value="王洪松">王洪松</option>
        <option value="乔伊果">乔伊果</option>
        <option value="方鹏飞">方鹏飞</option>
        <option value="吕佳祺">吕佳祺</option>
        <option value="王靖">王靖</option>
        <option value="石楚涵">石楚涵</option>
      </select>
    </div>

    <div class="col-xs-1 col-sm-1 col-md-1 col-lg-1"></div>

    <label
        class="col-xs-1 col-sm-1 col-md-1 col-lg-1 control-label"
        style="white-space: nowrap"
    >服从调剂</label
    >
    <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2">
      <select
          class="form-control"
          v-model="isAdjustable"
          required
      >
        <option value="请选择">请选择</option>
        <option value="是">是</option>
        <option value="否">否</option>
      </select>
      <span class="help-block">如果意向导师无法接收，调剂到其他导师</span>
    </div>
  </div>
</div>
  <DividerLine />
</template>
