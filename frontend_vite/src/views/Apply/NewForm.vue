<script setup>
import PersonalInfo from "@/views/Apply/components/PersonalInfo/PersonalInfo.vue";
import WillingChoice from "@/views/Apply/components/2WillingChoice.vue";
import Papers from "@/views/Apply/components/3Papers.vue";
import Awards from "@/views/Apply/components/4Awards.vue";
import Plan from "@/views/Apply/components/5Plan.vue";
import Upload from "@/views/Apply/components/6Upload.vue";
import Submit from "@/views/Apply/components/7Submit.vue";
import DividerLine from "@/views/Apply/components/tools/DividerLine.vue";

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
      onsubmit="return formSubmit()"
      action=""
    >
      <!--{% csrf_token %}-->
      <PersonalInfo />
      <WillingChoice />
      <Papers />
      <Awards />
      <Upload />
      <Submit />
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
  width: 1200px;
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
