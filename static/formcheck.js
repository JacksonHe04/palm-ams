// static/formcheck.js
// 在表单提交前对申请者的填写情况进行一系列验证
// 确保所有必填项都已正确填写且符合格式要求
// 最后提示用户报名成功并关注邮件通知

function formSubmit() {
  var sex = document.getElementById("form_sex").value;
  if (sex === "请选择") {
    alert("请输入性别！");
    return false;
  }

  var reg_phone = /^1\d{10}$/;
  var phonenumber = document.getElementById("form_phonenumber").value;
  if (!reg_phone.test(phonenumber)) {
    alert("手机号格式不正确！");
    return false;
  }

  var reg_email = new RegExp(
    "^[a-z0-9]+([._\\-]*[a-z0-9])*@([a-z0-9]+[-a-z0-9]*[a-z0-9]+.){1,63}[a-z0-9]+$",
  );
  var email = document.getElementById("form_email").value;
  if (!reg_email.test(email)) {
    alert("邮箱格式不正确！");
    return false;
  }

  var registrationtype = document.getElementById("form_registrationtype").value;
  if (registrationtype === "请选择") {
    alert("请选择报名类型！");
    return false;
  }

  var tutor_first = document.getElementById("form_tutor_first").value;
  var tutor_second = document.getElementById("form_tutor_second").value;
  var tutor_third = document.getElementById("form_tutor_third").value;
  if (
    tutor_first === "请选择" ||
    tutor_second === "请选择" ||
    tutor_third === "请选择"
  ) {
    alert("请选择志愿导师！");
    return false;
  }
  if (
    tutor_first === tutor_second ||
    tutor_first === tutor_third ||
    tutor_second === tutor_third
  ) {
    alert("志愿导师不能重复！");
    return false;
  }

  var ajustment = document.getElementById("form_ajustment").value;
  if (ajustment === "请选择") {
    alert("请选择是否服从调剂！");
    return false;
  }

  var fileDom = document.getElementById("photo");
  var file = fileDom.files[0];
  if (!file || file.type.indexOf("image/") < 0) {
    alert("请上传个人证件照");
    return false;
  }

  alert("感谢您报名PALM实验室！后续请关注邮件通知！");
  return true;
}
