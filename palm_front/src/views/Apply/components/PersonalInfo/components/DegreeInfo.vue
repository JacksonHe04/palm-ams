<script setup>
import { ref } from "vue";
import MajorList from "@/views/Apply/components/PersonalInfo/components/MajorList.vue";
import SchoolList from "@/views/Apply/components/PersonalInfo/components/SchoolList.vue";

const props = defineProps({
  label: {
    type: String,
    required: true,
  },
  showAdvisor: {
    type: Boolean,
    default: false,
  },
});

const emit = defineEmits(["degreeInfoUpdated"]);

const school = ref("");
const rating = ref("");
const major = ref("");
const advisor = ref("");

const handleSchoolSelect = (data) => {
  school.value = data.school;
  rating.value = data.rating;
  emitData();
};

const handleMajorChange = (event) => {
  major.value = event.target.value;
  emitData();
};

const handleAdvisorChange = (event) => {
  advisor.value = event.target.value;
  emitData();
};

const emitData = () => {
  emit("degreeInfoUpdated", {
    label: props.label,
    school: school.value,
    rating: rating.value,
    major: major.value,
    advisor: advisor.value,
  });
};
</script>

<template>
  <div class="grid grid-cols-12 items-center">
    <!-- 学校选择 -->
    <label :class="['col-start-2 col-span-1', 'text-right mr-2']">
      {{ label }}院校
    </label>
    <div :class="['col-span-2']">
      <SchoolList
        :id="`${label.toLowerCase()}-university-input`"
        @schoolSelected="handleSchoolSelect"
        :placeholder="showAdvisor ? '本科生不填写此项' : ''"
        :required="label === '本科'"
      />
    </div>

    <!-- 评级显示 -->
    <div :class="['col-span-1']">
      <span v-if="rating" class="inline-block px-2 py-1 bg-white text-cornflowerblue text-sm rounded-full border border-gray-300">
        {{ rating }}
      </span>
    </div>

    <!-- 专业选择 -->
    <label :class="['col-span-1', 'text-right mr-2']">
      专业
    </label>
    <div :class="['col-span-2']">
      <input
        type="text"
        class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
        name="major_input"
        list="major-input"
        :placeholder="label === '硕士' ? '本科生不填写此项' : ''"
        @change="handleMajorChange"
        :required="label === '本科'"
      />
      <MajorList />
    </div>

    <!-- 硕士导师信息 -->

      <label v-if="showAdvisor" :class="['col-span-2', 'text-right mr-2', 'whitespace-nowrap']">
        导师
      </label>
      <div v-if="showAdvisor" :class="['col-span-2']">
        <input
          class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
          type="text"
          placeholder="本科生不填写此项"
          @change="handleAdvisorChange"
          :required="label === '本科'"
        />

    </div>
  </div>
</template>

