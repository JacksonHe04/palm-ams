<script setup>

</script>

<template>
<div>
  <p class="infoClassTitle">
    意向选择
  </p>

  <div class="form-group">
    <div class="col-xs-1 col-sm-1 col-md-1 col-lg-1"></div>

    <label
        class="col-xs-1 col-sm-1 col-md-1 col-lg-1 control-label"
        style="white-space: nowrap"
    >报名类型 <span style="color: red">* </span></label
    >
    <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2">
      <select
          class="form-control"
          name="registrationtype_input"
          id="form_registrationtype"
          required
      >
        <option value="请选择">请选择</option>
        <option value="硕士">硕士</option>
        <option value="博士">博士</option>
        <option value="直博">直博</option>
      </select>
    </div>
  </div>

  <div class="form-group">
    <div class="col-xs-1 col-sm-1 col-md-1 col-lg-1"></div>

    <label
        class="col-xs-1 col-sm-1 col-md-1 col-lg-1 control-label"
        style="white-space: nowrap"
    >第一志愿 <span style="color: red">* </span></label
    >
    <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2">
      <select
          class="form-control"
          name="tutor_input_first"
          id="form_tutor_first"
          required
      >
        <option value="请选择">请选择</option>
        <option value="耿新">耿新(博导)</option>
        <option value="张敏灵">张敏灵(博导)</option>
        <option value="周德宇">周德宇(博导)</option>
        <option value="薛晖">薛晖(博导)</option>
        <option value="张宇">张宇(博导)</option>
        <option value="魏秀参">魏秀参(博导)</option>
        <option value="闫亚萍">闫亚萍</option>
        <option value="贾育衡">贾育衡(博导)</option>
        <option value="周毅">周毅(博导)</option>
        <option value="陈浩">陈浩(博导)</option>
        <option value="宋沫飞">宋沫飞(博导)</option>
        <option value="李竹颖">李竹颖</option>
        <option value="杨旭">杨旭(博导)</option>
        <option value="魏通">魏通(博导)</option>
        <option value="时霄">时霄</option>
        <option value="祁磊">祁磊</option>
        <option value="徐宁">徐宁</option>
        <option value="王洪松">王洪松</option>
        <option value="乔伊果">乔伊果</option>
        <option value="方鹏飞">方鹏飞</option>
        <option value="吕佳祺">吕佳祺</option>
        <option value="王靖">王靖</option>
        <option value="石楚涵">石楚涵</option>
      </select>
    </div>

    <div class="col-xs-1 col-sm-1 col-md-1 col-lg-1"></div>

    <label
        class="col-xs-1 col-sm-1 col-md-1 col-lg-1 control-label"
        style="white-space: nowrap"
    >第二志愿 <span style="color: red">* </span></label
    >
    <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2">
      <select
          class="form-control"
          name="tutor_input_second"
          id="form_tutor_second"
          required
      >
        <option value="请选择">请选择</option>
        <option value="耿新">耿新(博导)</option>
        <option value="张敏灵">张敏灵(博导)</option>
        <option value="周德宇">周德宇(博导)</option>
        <option value="薛晖">薛晖(博导)</option>
        <option value="张宇">张宇(博导)</option>
        <option value="魏秀参">魏秀参(博导)</option>
        <option value="闫亚萍">闫亚萍</option>
        <option value="贾育衡">贾育衡(博导)</option>
        <option value="周毅">周毅(博导)</option>
        <option value="陈浩">陈浩(博导)</option>
        <option value="宋沫飞">宋沫飞(博导)</option>
        <option value="李竹颖">李竹颖</option>
        <option value="杨旭">杨旭(博导)</option>
        <option value="魏通">魏通(博导)</option>
        <option value="时霄">时霄</option>
        <option value="祁磊">祁磊</option>
        <option value="徐宁">徐宁</option>
        <option value="王洪松">王洪松</option>
        <option value="乔伊果">乔伊果</option>
        <option value="方鹏飞">方鹏飞</option>
        <option value="吕佳祺">吕佳祺</option>
        <option value="王靖">王靖</option>
        <option value="石楚涵">石楚涵</option>
      </select>
    </div>
  </div>

  <div class="form-group">
    <div class="col-xs-1 col-sm-1 col-md-1 col-lg-1"></div>

    <label
        class="col-xs-1 col-sm-1 col-md-1 col-lg-1 control-label"
        style="white-space: nowrap"
    >第三志愿 <span style="color: red">* </span></label
    >
    <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2">
      <select
          class="form-control"
          name="tutor_input_third"
          id="form_tutor_third"
          required
      >
        <option value="请选择">请选择</option>
        <option value="耿新">耿新(博导)</option>
        <option value="张敏灵">张敏灵(博导)</option>
        <option value="周德宇">周德宇(博导)</option>
        <option value="薛晖">薛晖(博导)</option>
        <option value="张宇">张宇(博导)</option>
        <option value="魏秀参">魏秀参(博导)</option>
        <option value="闫亚萍">闫亚萍</option>
        <option value="贾育衡">贾育衡(博导)</option>
        <option value="周毅">周毅(博导)</option>
        <option value="陈浩">陈浩(博导)</option>
        <option value="宋沫飞">宋沫飞(博导)</option>
        <option value="李竹颖">李竹颖</option>
        <option value="杨旭">杨旭(博导)</option>
        <option value="魏通">魏通(博导)</option>
        <option value="时霄">时霄</option>
        <option value="祁磊">祁磊</option>
        <option value="徐宁">徐宁</option>
        <option value="王洪松">王洪松</option>
        <option value="乔伊果">乔伊果</option>
        <option value="方鹏飞">方鹏飞</option>
        <option value="吕佳祺">吕佳祺</option>
        <option value="王靖">王靖</option>
        <option value="石楚涵">石楚涵</option>
      </select>
    </div>

    <div class="col-xs-1 col-sm-1 col-md-1 col-lg-1"></div>

    <label
        class="col-xs-1 col-sm-1 col-md-1 col-lg-1 control-label"
        style="white-space: nowrap"
    >服从调剂 <span style="color: red">* </span></label
    >
    <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2">
      <select
          class="form-control"
          name="ajustment_input"
          id="form_ajustment"
          required
      >
        <option value="请选择">请选择</option>
        <option value="是">是</option>
        <option value="否">否</option>
      </select>
      <span class="help-block">如果意向导师无法接收，调剂到其他导师</span>
    </div>
  </div>
</div>
</template>

<style scoped>

</style>