<script setup>
import { ref } from 'vue';

const awards = ref([
  { time: '', grade: '', name: '', rank: '' },
  { time: '', grade: '', name: '', rank: '' },
  { time: '', grade: '', name: '', rank: '' },
  { time: '', grade: '', name: '', rank: '' },
  { time: '', grade: '', name: '', rank: '' }
]);

const awardGrades = ['世界级', '国家级', '省级', '市级', '校级', '院级'];
</script>

<template>
  <div>
    <p class="infoClassTitle">
      奖项荣誉
    </p>

    <div v-for="(award, index) in awards" :key="index" class="form-group">
      <label
          class="col-xs-1 col-sm-1 col-md-1 col-lg-1 control-label"
          style="white-space: nowrap"
      >获奖时间</label
      >
      <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2">
        <div class="input-group date" :id="`datetimepicker-award${index + 1}`">
          <input
              type="text"
              class="form-control"
              :name="`time_award${index + 1}`"
              v-model="award.time"
              placeholder="无"
          />
          <span class="input-group-addon">
              <span class="glyphicon glyphicon-calendar"></span>
            </span>
        </div>
      </div>

      <label
          class="col-xs-1 col-sm-1 col-md-1 col-lg-1 control-label"
          style="white-space: nowrap"
      >奖项类别</label
      >
      <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2">
        <input
            type="text"
            class="form-control"
            :name="`award_grade${index + 1}`"
            v-model="award.grade"
            :list="`award-grade${index + 1}`"
            placeholder="请选择"
        />
        <datalist :id="`award-grade${index + 1}`" style="display: none">
          <option v-for="grade in awardGrades" :value="grade" :key="grade">{{ grade }}</option>
        </datalist>
      </div>

      <label
          class="col-xs-1 col-sm-1 col-md-1 col-lg-1 control-label"
          style="white-space: nowrap"
      >奖项名称</label
      >
      <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2">
        <input
            type="text"
            class="form-control"
            :name="`award_name${index + 1}`"
            v-model="award.name"
            placeholder="如：诺贝尔物理学奖"
        />
      </div>

      <label
          class="col-xs-1 col-sm-1 col-md-1 col-lg-1 control-label"
          style="white-space: nowrap"
      >等级与排名</label
      >
      <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2">
        <input
            type="text"
            class="form-control"
            :name="`award_rank${index + 1}`"
            v-model="award.rank"
            placeholder="如：一等奖/第一名"
        />
      </div>
    </div>
  </div>
</template>

<style scoped></style>
