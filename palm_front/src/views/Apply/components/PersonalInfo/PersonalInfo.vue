<!-- PersonalInfo.vue -->
<script setup>
import MajorList from "@/views/Apply/components/PersonalInfo/components/MajorList.vue";
import { ref } from 'vue';
import SchoolList from "@/views/Apply/components/PersonalInfo/components/SchoolList.vue";
import Avatar from "@/views/Apply/components/PersonalInfo/components/Avatar.vue";
import DegreeInfo from "@/views/Apply/components/PersonalInfo/components/DegreeInfo.vue";
import DividerLine from "@/views/Apply/components/tools/DividerLine.vue";

// 存储选择的学校评级
const rating = ref('');

// 处理子组件传递的数据
const handleSchoolSelect = (data) => {
  rating.value = data.rating;
};
</script>

<template>
  <div>
    <p class="infoClassTitle">个人基本信息</p>

    <!-- 姓名；性别；籍贯；出生日期 -->
    <div class="form-group">
      <div class="col-xs-1 col-sm-1 col-md-1 col-lg-1"></div>

      <div class="col-xs-3 col-sm-3 col-md-3 col-lg-3">
        <div class="form-group">
          <label class="col-xs-4 col-sm-4 col-md-4 col-lg-4 control-label"
            >姓 名 <span style="color: red">* </span></label
          >
          <div class="col-xs-8 col-sm-8 col-md-8 col-lg-8">
            <input
              type="text"
              class="form-control"
              name="name_input"
              required
            />
          </div>
        </div>

        <div class="form-group">
          <label class="col-xs-4 col-sm-4 col-md-4 col-lg-4 control-label"
            >性 别 <span style="color: red">* </span></label
          >
          <div class="col-xs-8 col-sm-8 col-md-8 col-lg-8">
            <select class="form-control" name="sex_input" id="form_sex">
              <option value="请选择">请选择</option>
              <option value="男">男</option>
              <option value="女">女</option>
            </select>
          </div>
        </div>

        <div class="form-group">
          <label
            class="col-xs-4 col-sm-4 col-md-4 col-lg-4 control-label"
            style="white-space: nowrap"
            >出生年月 <span style="color: red">* </span></label
          >
          <div class="col-xs-8 col-sm-8 col-md-8 col-lg-8">
            <div class="input-group date" id="datetimepicker1">
              <input
                type="text"
                class="form-control"
                name="birthday"
                required
              />
              <span class="input-group-addon">
                <span class="glyphicon glyphicon-calendar"></span>
              </span>
            </div>
          </div>
        </div>
      </div>

      <div class="col-xs-1 col-sm-1 col-md-1 col-lg-1"></div>

      <div class="col-xs-3 col-sm-3 col-md-3 col-lg-3">
        <div data-toggle="distpicker">
          <div class="form-group">
            <label class="col-xs-4 col-sm-4 col-md-4 col-lg-4 control-label"
              >籍 贯 <span style="color: red">* </span></label
            >
            <div class="col-xs-8 col-sm-8 col-md-8 col-lg-8">
              <label class="sr-only" for="province1">Province</label>
              <select
                class="form-control"
                name="province"
                id="province1"
              ></select>
            </div>
          </div>

          <div class="form-group">
            <div class="col-xs-4 col-sm-4 col-md-4 col-lg-4"></div>
            <div class="col-xs-8 col-sm-8 col-md-8 col-lg-8">
              <label class="sr-only" for="city1">City</label>
              <select class="form-control" name="city" id="city1"></select>
            </div>
          </div>

          <div class="form-group">
            <div class="col-xs-4 col-sm-4 col-md-4 col-lg-4"></div>
            <div class="col-xs-8 col-sm-8 col-md-8 col-lg-8">
              <label class="sr-only" for="district1">District</label>
              <select
                class="form-control"
                name="district"
                id="district1"
              ></select>
            </div>
          </div>
        </div>
      </div>

      <div class="col-xs-1 col-sm-1 col-md-1 col-lg-1"></div>

      <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2">
        <Avatar />
      </div>

    </div>

    <!-- 本科信息 -->
    <DegreeInfo label="本科" />

    <!-- 硕士信息，包含导师字段 -->
    <DegreeInfo label="硕士" :showAdvisor="true" />

    <!-- 专业排名 -->
    <div class="form-group">
      <div class="col-xs-1 col-sm-1 col-md-1 col-lg-1"></div>

      <label
        class="col-xs-1 col-sm-1 col-md-1 col-lg-1 control-label"
        style="white-space: nowrap"
        >专业人数 <span style="color: red">* </span></label
      >
      <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2">
        <input
          type="number"
          class="form-control"
          name="gradepeople_input"
          v-model.number="gradePeople"
          min="1"
          required
        />
      </div>

      <div class="col-xs-1 col-sm-1 col-md-1 col-lg-1"></div>

      <label class="col-xs-1 col-sm-1 col-md-1 col-lg-1 control-label"
        >排 名 <span style="color: red">* </span></label
      >
      <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2">
        <input
          type="number"
          class="form-control"
          name="grade_input"
          v-model.number="grade"
          min="1"
          required
        />
      </div>

      <div class="col-lg-4">
        <label class="col-lg-3 control-label"
        >百分比</label
        >
        <div class="col-lg-6">
          <input
              type="text"
              class="form-control"
              :value="percentageRank"
              readonly
              placeholder="自动计算"
          />
        </div>
        <div class="col-lg-3"></div>
      </div>
    </div>

    <!-- 电话；邮箱 -->
    <div class="form-group">
      <div class="col-xs-1 col-sm-1 col-md-1 col-lg-1"></div>

      <label
        class="col-xs-1 col-sm-1 col-md-1 col-lg-1 control-label"
        style="white-space: nowrap"
        >手机号码 <span style="color: red">* </span></label
      >
      <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2">
        <input
          type="text"
          class="form-control"
          name="phonenumber_input"
          id="form_phonenumber"
          required
        />
      </div>

      <div class="col-xs-1 col-sm-1 col-md-1 col-lg-1"></div>

      <label
        class="col-xs-1 col-sm-1 col-md-1 col-lg-1 control-label"
        style="white-space: nowrap"
        >电子邮箱 <span style="color: red">* </span></label
      >
      <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2">
        <input
          type="text"
          class="form-control"
          name="email_input"
          id="form_email"
          required
        />
      </div>
    </div>
  </div>
  <DividerLine />
</template>

<script>
export default {
  data() {
    return {
      gradePeople: null,
      grade: null
    };
  },
  computed: {
    percentageRank() {
      if (this.gradePeople && this.grade) {
        const percentage = (this.grade / this.gradePeople) * 100;
        return `${percentage.toFixed(2)}%`;
      }
      return '';
    }
  }
};
</script>

