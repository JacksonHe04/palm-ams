<script setup>
import { ref, watch } from "vue";
import DividerLine from "@/views/Apply/components/tools/DividerLine.vue";
import { useApplyStore } from "@/stores/applyStore.js";

const props = defineProps({
  modelValue: Object
});

const emit = defineEmits(['update:modelValue']);

const applyStore = useApplyStore();

// 监听 applyStore.papers 的变化
watch(
  () => applyStore.papers,
  (newVal) => {
    emit('update:modelValue', {
      ...props.modelValue,
      papers: newVal
    });
  },
  { deep: true }
);

// 初始化 papers
if (!applyStore.papers.length) {
  applyStore.updateField('papers', [{ id: 1, publicationTime: "", journalConference: "", paperName: "", ccfLevel: "" }]);
}

// 添加新条目的函数
const addPaper = () => {
  const newId = applyStore.papers.length + 1; // 新ID
  const newPapers = [...applyStore.papers, { id: newId, publicationTime: "", journalConference: "", paperName: "", ccfLevel: "" }];
  applyStore.updateField('papers', newPapers);
};

// 移除最后一条记录的函数（确保至少保留一条记录）
const removePaper = () => {
  if (applyStore.papers.length > 1) {
    const newPapers = applyStore.papers.slice(0, -1);
    applyStore.updateField('papers', newPapers);
  }
};
</script>

<template>
  <div class="p-5">
    <p class="infoClassTitle">论文发表</p>

    <div v-for="(paper, index) in applyStore.papers" :key="paper.id" class="grid grid-cols-12 gap-4 mb-4 items-center">
      <label class="col-span-1 text-right whitespace-nowrap">发表时间</label>
      <div class="col-span-2">
        <div class="input-group date">
          <input
            type="text"
            class="form-control"
            :name="`time_paper${paper.id}`"
            v-model="paper.publicationTime"
            placeholder="无"
          />
          <span class="input-group-addon">
            <span class="glyphicon glyphicon-calendar"></span>
          </span>
        </div>
      </div>

      <label class="col-span-1 text-right whitespace-nowrap">期刊/会议名</label>
      <div class="col-span-2">
        <input
          type="text"
          class="form-control"
          :name="`journal_name${paper.id}`"
          v-model="paper.journalConference"
          placeholder="无"
        />
      </div>

      <label class="col-span-1 text-right whitespace-nowrap">论文名称</label>
      <div class="col-span-2">
        <input
          type="text"
          class="form-control"
          :name="`paper_name${paper.id}`"
          v-model="paper.paperName"
          placeholder="无"
        />
      </div>

      <label class="col-span-1 text-right whitespace-nowrap">CCF 等级</label>
      <div class="col-span-2">
        <select
          class="form-control"
          :name="`ccf_level${paper.id}`"
          v-model="paper.ccfLevel"
        >
          <option value="" disabled selected>请选择</option>
          <option value="CCF-A">CCF-A</option>
          <option value="CCF-B">CCF-B</option>
          <option value="CCF-C">CCF-C</option>
          <option value="其他">其他</option>
        </select>
      </div>

      <!-- 仅在当前最后一条填写行的下方显示加号和减号按钮 -->
      <div v-if="index === applyStore.papers.length - 1" class="col-span-12 text-center mt-2">
        <button @click="addPaper" class="btn btn-apply">+</button>
        <button v-if="applyStore.papers.length > 1" @click="removePaper" class="btn btn-danger ml-2">-</button>
      </div>
    </div>
  </div>
  <DividerLine />
</template>

<style scoped>
.mt-2 {
  margin-top: 0.5rem;
}
.ml-2 {
  margin-left: 0.5rem;
}
</style>
