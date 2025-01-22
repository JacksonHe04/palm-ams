<script setup>
import PersonalInfo from "@/views/Apply/components/PersonalInfo/PersonalInfo.vue";
import WillingChoice from "@/views/Apply/components/2WillingChoice.vue";
import Papers from "@/views/Apply/components/3Papers.vue";
import Awards from "@/views/Apply/components/4Awards.vue";
import Upload from "@/views/Apply/components/6Upload.vue";
import DividerLine from "@/views/Apply/components/tools/DividerLine.vue";

import { useApplyStore } from "@/stores/applyStore.js";
import { submitApplication } from "@/apis/apply";

const applyStore = useApplyStore();

const handleSubmit = async () => {
  try {
    const applicationData = {
      id: applyStore.id,
      name: applyStore.name,
      graduationYear: applyStore.graduationYear,
      gender: applyStore.gender,
      birthDate: applyStore.birthDate,
      photo: applyStore.photo,
      university: applyStore.university,
      universityLevel: applyStore.universityLevel,
      major: applyStore.major,
      majorCount: applyStore.majorCount,
      rank: applyStore.rank,
      percentage: applyStore.percentage,
      masterUniversity: applyStore.masterUniversity,
      masterUniversityLevel: applyStore.masterUniversityLevel,
      masterMajor: applyStore.masterMajor,
      tutor: applyStore.tutor,
      phone: applyStore.phone,
      email: applyStore.email,
      applicationType: applyStore.applicationType,
      firstChoice: applyStore.firstChoice,
      secondChoice: applyStore.secondChoice,
      thirdChoice: applyStore.thirdChoice,
      isAdjustable: applyStore.isAdjustable,
      papers: applyStore.papers,
      awards: applyStore.awards,
      resume: applyStore.resume,
      proofs: applyStore.proofs,
      status: applyStore.status,
    };
    await submitApplication(applicationData);
    alert("申请已成功提交！");
    applyStore.resetFields();
  } catch (error) {
    console.error("提交申请失败:", error);
    alert("申请提交失败，请重试。");
  }
};
</script>

<template>
  <div class="container">
    <p id="website-title">东南大学PALM实验室申请系统</p>
    <DividerLine />
    <form class="form-horizontal" @submit.prevent="handleSubmit">
      <PersonalInfo v-model="applyStore" id="personalInfo" />
      <WillingChoice v-model="applyStore" id="willingChoice" />
      <Papers v-model="applyStore" id="papers" />
      <Awards v-model="applyStore" id="awards" />
      <Upload v-model="applyStore" id="upload" />
      <div class="w-full flex justify-center">
        <div class="submit-button" @click="handleSubmit">提交</div>
      </div>
    </form>
  </div>
</template>

<style scoped>
/* @import url("https://cdn.staticfile.org/twitter-bootstrap/3.3.7/css/bootstrap.min.css"); */
/* @import url("https://cdn.bootcss.com/bootstrap-datetimepicker/4.17.47/css/bootstrap-datetimepicker.min.css"); */

#website-title {
  letter-spacing: 8px;
  font-size: 50px;
  text-align: center;
  padding: 10px;
  color: slategrey;
  font-weight: bold;
}

.container {
  width: 80%;
  padding: 30px;
  margin: 50px auto;

  /* 卡片样式 */
  background-color: rgba(255, 255, 255, 0.5);
  /* box-shadow: 4px 4px 8px #666666; */
  border-radius: 50px;
  opacity: 0.8;
  filter: Alpha(opacity=50);
}

.submit-button {
  cursor: pointer;
  background-color: black;
  color: white;
  padding: 10px 20px;
  border-radius: 15px;
  font-size: 16px;
  transition: background-color 0.3s;
  width: 10%;
}

.submit-button:hover {
  background-color: #0056b3;
}
</style>

<style>
.form-control {
  border-radius: 15px;
  opacity: 0.7;
  @apply px-3 py-2 w-11/12 rounded-lg border border-gray-300 focus:border-blue-500 focus:ring-1 focus:ring-blue-500;
}

.infoClassTitle {
  font-size: x-large;
  font-weight: bold;
}
</style>
