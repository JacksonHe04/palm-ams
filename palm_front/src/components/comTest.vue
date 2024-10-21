<script setup>
import "https://cdn.staticfile.org/jquery/2.0.0/jquery.min.js";
import "https://cdn.staticfile.org/twitter-bootstrap/3.3.7/js/bootstrap.min.js";
import "https://cdnjs.cloudflare.com/ajax/libs/moment.js/2.29.1/moment.min.js";
import "https://cdn.bootcss.com/bootstrap-datetimepicker/4.17.47/js/bootstrap-datetimepicker.min.js";
import "../static/formcheck.js";
import "http://www.jq22.com/jquery/bootstrap-3.3.4.js";
import "../static/distpicker/js/distpicker.data.js";
import "../static/distpicker/js/distpicker.js";

$(function () {
  $("#datetimepicker1").datetimepicker({
    format: "YYYY-MM-DD",
    locale: moment.locale("zh-CN"),
  });
});

var fileDom = document.getElementById("photo");
var previewDom = document.getElementById("preview");
fileDom.addEventListener("change", (e) => {
  var file = fileDom.files[0];

  if (file.size > 1024 * 300) {
    alert("照片大小不能超过300KB");
    fileDom.value = "";
    previewDom.src = "";
    return;
  }

  // check if input contains a valid image file
  if (!file || file.type.indexOf("image/") < 0) {
    fileDom.value = "";
    previewDom.src = "";
    return;
  }

  // use FileReader to load image and show preview of the image
  var fileReader = new FileReader();
  fileReader.onload = (e) => {
    previewDom.src = e.target.result;
  };
  fileReader.readAsDataURL(file);
});

$(function () {
  $("#datetimepicker-paper1").datetimepicker({
    format: "YYYY-MM-DD",
    locale: moment.locale("zh-CN"),
  });
});

$(function () {
  $("#datetimepicker-paper2").datetimepicker({
    format: "YYYY-MM-DD",
    locale: moment.locale("zh-CN"),
  });
});

$(function () {
  $("#datetimepicker-paper3").datetimepicker({
    format: "YYYY-MM-DD",
    locale: moment.locale("zh-CN"),
  });
});

$(function () {
  $("#datetimepicker-award1").datetimepicker({
    format: "YYYY-MM-DD",
    locale: moment.locale("zh-CN"),
  });
});

$(function () {
  $("#datetimepicker-award2").datetimepicker({
    format: "YYYY-MM-DD",
    locale: moment.locale("zh-CN"),
  });
});

$(function () {
  $("#datetimepicker-award3").datetimepicker({
    format: "YYYY-MM-DD",
    locale: moment.locale("zh-CN"),
  });
});

$(function () {
  $("#datetimepicker-award4").datetimepicker({
    format: "YYYY-MM-DD",
    locale: moment.locale("zh-CN"),
  });
});

$(function () {
  $("#datetimepicker-award5").datetimepicker({
    format: "YYYY-MM-DD",
    locale: moment.locale("zh-CN"),
  });
});
</script>

<template>
  <head>
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <title>东南大学PALM实验室申请系统</title>
  </head>
</template>
