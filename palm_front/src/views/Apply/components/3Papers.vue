<script setup>
import { ref } from "vue";
import DividerLine from "@/views/Apply/components/tools/DividerLine.vue";

// 初始化为一条记录
const papers = ref([{ id: 1, time: "", journalName: "", paperName: "", ccfLevel: "" }]);

// 添加新条目的函数
const addPaper = () => {
  const newId = papers.value.length + 1; // 新ID
  papers.value.push({ id: newId, time: "", journalName: "", paperName: "", ccfLevel: "" });
};

// 移除最后一条记录的函数（确保至少保留一条记录）
const removePaper = () => {
  if (papers.value.length > 1) {
    papers.value.pop();
  }
};
</script>

<template>
  <div class="infoClass">
    <p class="infoClassTitle">论文发表</p>

    <div v-for="(paper, index) in papers" :key="paper.id" class="form-group row">
      <label class="col-xs-1 col-sm-1 col-md-1 col-lg-1 control-label" style="white-space: nowrap">发表时间</label>
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

      <label class="col-xs-1 col-sm-1 col-md-1 col-lg-1 control-label" style="white-space: nowrap">期刊/会议名</label>
      <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2">
        <input
            type="text"
            class="form-control"
            :name="`journal_name${paper.id}`"
            v-model="paper.journalName"
            placeholder="无"
        />
      </div>

      <label class="col-xs-1 col-sm-1 col-md-1 col-lg-1 control-label" style="white-space: nowrap">论文名称</label>
      <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2">
        <input
            type="text"
            class="form-control"
            :name="`paper_name${paper.id}`"
            v-model="paper.paperName"
            placeholder="无"
        />
      </div>

      <label class="col-xs-1 col-sm-1 col-md-1 col-lg-1 control-label" style="white-space: nowrap">CCF 等级</label>
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

      <!-- 仅在当前最后一条填写行的下方显示加号和减号按钮 -->
      <div v-if="index === papers.length - 1" class="col-xs-12 text-center mt-2">
        <button @click="addPaper" class="btn btn-primary">+</button>
        <button v-if="papers.length > 1" @click="removePaper" class="btn btn-danger ml-2">-</button>
      </div>
    </div>
  </div>
  <DividerLine />
</template>

<style scoped>
.infoClass {
  padding: 20px;
}
.mt-2 {
  margin-top: 10px;
}
.ml-2 {
  margin-left: 10px;
}
</style>
