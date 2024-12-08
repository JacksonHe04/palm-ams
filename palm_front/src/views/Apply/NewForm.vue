<script setup>
// function formSubmit() {
//   var sex = document.getElementById("form_sex").value;
//   if (sex === "请选择") {
//     alert("请输入性别！");
//     return false;
//   }
//
//   var reg_phone = /^1\d{10}$/;
//   var phonenumber = document.getElementById("form_phonenumber").value;
//   if (!reg_phone.test(phonenumber)) {
//     alert("手机号格式不正确！");
//     return false;
//   }
//
//   var reg_email = new RegExp(
//       "^[a-z0-9]+([._\\-]*[a-z0-9])*@([a-z0-9]+[-a-z0-9]*[a-z0-9]+.){1,63}[a-z0-9]+$",
//   );
//   var email = document.getElementById("form_email").value;
//   if (!reg_email.test(email)) {
//     alert("邮箱格式不正确！");
//     return false;
//   }
//
//   var registrationtype = document.getElementById("form_registrationtype").value;
//   if (registrationtype === "请选择") {
//     alert("请选择报名类型！");
//     return false;
//   }
//
//   var tutor_first = document.getElementById("form_tutor_first").value;
//   var tutor_second = document.getElementById("form_tutor_second").value;
//   var tutor_third = document.getElementById("form_tutor_third").value;
//   if (
//       tutor_first === "请选择" ||
//       tutor_second === "请选择" ||
//       tutor_third === "请选择"
//   ) {
//     alert("请选择志愿导师！");
//     return false;
//   }
//   if (
//       tutor_first === tutor_second ||
//       tutor_first === tutor_third ||
//       tutor_second === tutor_third
//   ) {
//     alert("志愿导师不能重复！");
//     return false;
//   }
//
//   var ajustment = document.getElementById("form_ajustment").value;
//   if (ajustment === "请选择") {
//     alert("请选择是否服从调剂！");
//     return false;
//   }
//
//   var fileDom = document.getElementById("photo");
//   var file = fileDom.files[0];
//   if (!file || file.type.indexOf("image/") < 0) {
//     alert("请上传个人证件照");
//     return false;
//   }
//
//   alert("感谢您报名PALM实验室！后续请关注邮件通知！");
//   return true;
// }

import { ref } from "vue";
import PersonalInfo from "@/views/Apply/components/PersonalInfo/PersonalInfo.vue";
import WillingChoice from "@/views/Apply/components/2WillingChoice.vue";
import Papers from "@/views/Apply/components/3Papers.vue";
import Awards from "@/views/Apply/components/4Awards.vue";
import Upload from "@/views/Apply/components/6Upload.vue";
import Submit from "@/views/Apply/components/7Submit.vue";
import DividerLine from "@/views/Apply/components/tools/DividerLine.vue";
import { postData } from "@/utils/http.js"; // 引入 postData 方法

import Test from "@/views/Apply/components/Test.vue";

const formData = ref({
  personalInfo: {},
  willingChoice: {},
  papers: {},
  awards: {},
  upload: {},
  submit: {},
  test: {},
});

const testComponent = ref(null);

function formSubmit() {
  // 转换数据格式
  const formattedData = {
    id: 1, // 可以根据实际情况生成或获取ID
    name: formData.value.personalInfo.name,
    graduationYear: formData.value.personalInfo.graduationYear,
    gender: formData.value.personalInfo.sex,
    birthDate: formData.value.personalInfo.birthDate,
    photo: formData.value.upload.file ? formData.value.upload.file.name : null,
    university: formData.value.personalInfo.university,
    major: formData.value.personalInfo.major,
    majorCount: formData.value.personalInfo.majorCount,
    rank: formData.value.personalInfo.rank,
    percentage: formData.value.personalInfo.percentage,
    masterUniversity: formData.value.personalInfo.masterUniversity,
    masterMajor: formData.value.personalInfo.masterMajor,
    tutor: formData.value.personalInfo.tutor,
    phone: formData.value.personalInfo.phonenumber,
    email: formData.value.personalInfo.email,
    applicationType: formData.value.personalInfo.registrationtype,
    firstChoice: formData.value.willingChoice.tutor_first,
    secondChoice: formData.value.willingChoice.tutor_second,
    thirdChoice: formData.value.willingChoice.tutor_third,
    isAdjustable: formData.value.submit.ajustment === '是',
    papers: formData.value.papers.map(paper => ({
      publicationTime: paper.publicationTime,
      journalConference: paper.journalConference,
      paperName: paper.paperName,
      ccfLevel: paper.ccfLevel,
      awardCategory: paper.awardCategory,
    })),
    awards: formData.value.awards.map(award => ({
      isLeader: award.isLeader,
      awardTime: award.awardTime,
      awardName: award.awardName,
      levelRanking: award.levelRanking,
    })),
    resume: formData.value.upload.resume ? formData.value.upload.resume.name : null,
    proofs: formData.value.upload.proofs ? formData.value.upload.proofs.name : null,
    status: "待审核",
  };

  // 发送数据到后端
  postData('/api/apply', formattedData)
      .then(response => {
        console.log('Success:', response);
        alert("感谢您报名PALM实验室！后续请关注邮件通知！");
      })
      .catch(error => {
        console.error('Error:', error);
        alert("报名失败，请重试！");
      });

  return false; // 阻止表单默认提交行为
}

// function validateFormData(data) {
//   // 验证逻辑示例
//   if (!data.personalInfo.sex) {
//     alert("请输入性别！");
//     return false;
//   }
//
//   const reg_phone = /^1\d{10}$/;
//   if (!reg_phone.test(data.personalInfo.phonenumber)) {
//     alert("手机号格式不正确！");
//     return false;
//   }
//
//   const reg_email = new RegExp(
//     "^[a-z0-9]+([._\\-]*[a-z0-9])*@([a-z0-9]+[-a-z0-9]*[a-z0-9]+.){1,63}[a-z0-9]+$",
//   );
//   if (!reg_email.test(data.personalInfo.email)) {
//     alert("邮箱格式不正确！");
//     return false;
//   }
//
//   if (!data.personalInfo.registrationtype) {
//     alert("请选择报名类型！");
//     return false;
//   }
//
//   if (
//     !data.willingChoice.tutor_first ||
//     !data.willingChoice.tutor_second ||
//     !data.willingChoice.tutor_third
//   ) {
//     alert("请选择志愿导师！");
//     return false;
//   }
//
//   if (
//     data.willingChoice.tutor_first === data.willingChoice.tutor_second ||
//     data.willingChoice.tutor_first === data.willingChoice.tutor_third ||
//     data.willingChoice.tutor_second === data.willingChoice.tutor_third
//   ) {
//     alert("志愿导师不能重复！");
//     return false;
//   }
//
//   if (!data.submit.ajustment) {
//     alert("请选择是否服从调剂！");
//     return false;
//   }
//
//   if (!data.upload.file || data.upload.file.type.indexOf("image/") < 0) {
//     alert("请上传个人证件照");
//     return false;
//   }
//
//   return true;
// }
</script>

<template>
  <div class="container">
    <p id="website-title">东南大学PALM实验室申请系统</p>
    <DividerLine />
    <form
      class="form-horizontal"
      method="post"
      role="form"
      enctype="multipart/form-data"
      @submit.prevent="formSubmit"
    >
      <PersonalInfo v-model="formData.personalInfo" />
      <WillingChoice v-model="formData.willingChoice" />
      <Papers v-model="formData.papers" />
      <Awards v-model="formData.awards" />
      <Upload v-model="formData.upload" />
      <Submit v-model="formData.submit" />
      <!--<Test v-model="formData.test" ref="testComponent"/>-->
      <button type="submit">提交</button>
    </form>
  </div>
</template>


<style scoped>
@import url("https://cdn.staticfile.org/twitter-bootstrap/3.3.7/css/bootstrap.min.css");
@import url("https://cdn.bootcss.com/bootstrap-datetimepicker/4.17.47/css/bootstrap-datetimepicker.min.css");

#website-title {
  letter-spacing: 8px;
  font-size: 50px;
  text-align: center;
  padding: 10px;
  color: slategrey;
  font-weight: bold;
}

.container {
  background-color: rgba(255, 255, 255, 0.5);
  width: 80%;
  padding: 30px;
  margin: 50px auto;
  border-radius: 50px;

  opacity: 0.8;
  filter: Alpha(opacity=50);
  box-shadow: 4px 4px 8px #666666;
}
</style>

<style>
.form-control {
  border-radius: 15px;
}

.infoClassTitle {
  font-size: x-large;
  font-weight: bold;
}
</style>
