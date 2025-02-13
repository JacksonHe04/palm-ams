<script setup>
</script>

<template>
  <div>
    <p class="infoClassTitle">
      个人陈述与研究计划
    </p>

    <div class="form-group">
      <div class="col-xs-1 col-sm-1 col-md-1 col-lg-1"></div>

      <label
          class="col-xs-1 col-sm-1 col-md-1 col-lg-1 control-label"
          style="white-space: nowrap"
      >个人陈述 <span style="color: red">* </span></label
      >
      <div class="col-xs-8 col-sm-8 col-md-8 col-lg-8">
          <textarea
              class="form-control"
              rows="10"
              name="statement_input"
              maxlength="500"
              placeholder="个人陈述(不超过500字)"
              required
          ></textarea>
      </div>
    </div>

    <div class="form-group">
      <div class="col-xs-1 col-sm-1 col-md-1 col-lg-1"></div>

      <label
          class="col-xs-1 col-sm-1 col-md-1 col-lg-1 control-label"
          style="white-space: nowrap"
      >研究计划 <span style="color: red">* </span></label
      >
      <div class="col-xs-8 col-sm-8 col-md-8 col-lg-8">
          <textarea
              class="form-control"
              rows="10"
              name="researchplan_input"
              maxlength="500"
              placeholder="研究计划(不超过500字)"
              required
          ></textarea>
      </div>
    </div>

    <div class="form-group">
      <label
          class="col-xs-12 col-sm-12 col-md-12 col-lg-12 control-label"
          style="font-size: xx-small; color: red; text-align: center"
      >填写完报名系统后，请将申请材料压缩发送至邮箱palmwebsite@163.com，申请材料要求见实验室网站招生页面</label
      >
    </div>
  </div>
</template>

<style scoped></style>
