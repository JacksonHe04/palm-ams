<script setup>
import { ref } from "vue";

const papers = ref([
  { id: 1, time: "", journalName: "", paperName: "", ccfLevel: "" },
  { id: 2, time: "", journalName: "", paperName: "", ccfLevel: "" },
  { id: 3, time: "", journalName: "", paperName: "", ccfLevel: "" },
]);
</script>

<template>
  <div class="infoClass">
    <p class="infoClassTitle">论文发表</p>

    <div v-for="paper in papers" :key="paper.id" class="form-group row">
      <label
        class="col-xs-1 col-sm-1 col-md-1 col-lg-1 control-label"
        style="white-space: nowrap"
        >发表时间</label
      >
      <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2">
        <div class="input-group date" :id="`datetimepicker-paper${paper.id}`">
          <input
            type="text"
            class="form-control"
            :name="`time_paper${paper.id}`"
            v-model="paper.time"
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
        >期刊/会议名</label
      >
      <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2">
        <input
          type="text"
          class="form-control"
          :name="`journal_name${paper.id}`"
          v-model="paper.journalName"
          placeholder="无"
        />
      </div>

      <label
        class="col-xs-1 col-sm-1 col-md-1 col-lg-1 control-label"
        style="white-space: nowrap"
        >论文名称</label
      >
      <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2">
        <input
          type="text"
          class="form-control"
          :name="`paper_name${paper.id}`"
          v-model="paper.paperName"
          placeholder="无"
        />
      </div>

      <label
        class="col-xs-1 col-sm-1 col-md-1 col-lg-1 control-label"
        style="white-space: nowrap"
        >CCF 等级</label
      >
      <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2">
        <select
          class="form-control"
          :name="`ccf_level${paper.id}`"
          v-model="paper.ccfLevel"
        >
          <option value="" disabled selected>请选择</option>
          <option value="A">A</option>
          <option value="B">B</option>
          <option value="C">C</option>
          <option value="其他">其他</option>
        </select>
      </div>
    </div>
  </div>
</template>

<style scoped>
.infoClass {
  padding: 20px;
}
</style>
