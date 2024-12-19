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
  <div class="form-group">
    <div class="col-xs-1 col-sm-1 col-md-1 col-lg-1"></div>

    <!-- 学校选择 -->
    <label class="col-xs-1 col-sm-1 col-md-1 col-lg-1 control-label">
      {{ label }}学校
    </label>
    <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2">
      <SchoolList
        :id="`${label.toLowerCase()}-university-input`"
        @schoolSelected="handleSchoolSelect"
        :placeholder="showAdvisor ? '本科生不填写此项' : ''"
        :required="label === '本科'"
      />
    </div>

    <!-- 评级显示 -->
    <div class="col-xs-1 col-sm-1 col-md-1 col-lg-1 control-label ratingLabel">
      <span v-if="rating" class="ratingResult">{{ rating }}</span>
    </div>

    <!-- 专业选择 -->
    <label class="col-xs-1 col-sm-1 col-md-1 col-lg-1 control-label">
      专业
    </label>
    <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2">
      <input
        type="text"
        class="form-control"
        name="major_input"
        list="major-input"
        :placeholder="label === '硕士' ? '本科生不填写此项' : ''"
        @change="handleMajorChange"
        :required="label === '本科'"
      />
      <MajorList />
    </div>

    <!-- 硕士导师信息 -->
    <div v-if="showAdvisor" class="col-lg-4">
      <label class="col-lg-3 control-label" style="white-space: nowrap">
        导师
      </label>
      <div class="col-lg-6">
        <input
          class="form-control"
          type="text"
          placeholder="本科生不填写此项"
          @change="handleAdvisorChange"
          :required="label === '本科'"
        />
      </div>
      <div class="col-lg-3"></div>
    </div>
  </div>
</template>

<style scoped>
.form-group .ratingLabel {
  padding-top: 6px;
  text-align: left;
  padding-left: 0;
}

.ratingResult {
  display: inline;
  border-radius: 30%;
  background-color: #fff;
  color: cornflowerblue;
  font-size: 14px;
  vertical-align: middle;
  border: 2px solid #ccc;
  padding: 5px 8px;
}
</style>
