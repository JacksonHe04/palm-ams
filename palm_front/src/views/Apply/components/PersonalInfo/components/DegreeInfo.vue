<!-- DegreeInfo.vue -->
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

const rating = ref("");

const handleSchoolSelect = (data) => {
  rating.value = data.rating;
};
</script>

<template>
  <div class="form-group">
    <div class="col-xs-1 col-sm-1 col-md-1 col-lg-1"></div>

    <!-- 学校选择 -->
    <label class="col-xs-1 col-sm-1 col-md-1 col-lg-1 control-label">
      {{ label }}学校 <span style="color: red">* </span>
    </label>
    <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2">
      <SchoolList
        :id="`${label.toLowerCase()}-university-input`"
        @schoolSelected="handleSchoolSelect"
        :placeholder="showAdvisor ? '本科生不填写此项' : ''"
      />
    </div>

    <!-- 评级显示 -->
    <div class="col-xs-1 col-sm-1 col-md-1 col-lg-1 control-label ratingLabel">
      <span v-if="rating" class="ratingResult">{{ rating }}</span>
    </div>

    <!-- 专业选择 -->
    <label class="col-xs-1 col-sm-1 col-md-1 col-lg-1 control-label">
      专业 <span style="color: red">* </span>
    </label>
    <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2">
      <input
        type="text"
        class="form-control"
        name="major_input"
        list="major-input"
        required
        :placeholder="label === '硕士' ? '本科生不填写此项' : ''"
      />
      <MajorList />
    </div>

    <!-- 硕士导师信息 -->
    <div v-if="showAdvisor" class="col-lg-4">
      <label class="col-lg-3 control-label" style="white-space: nowrap"
        >导师</label
      >
      <div class="col-lg-6">
        <input
          class="form-control"
          type="text"
          placeholder="本科生不填写此项"
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
