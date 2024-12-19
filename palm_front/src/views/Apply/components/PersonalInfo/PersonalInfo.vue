<script setup>
import { ref, watch, computed } from "vue";
import { useApplyStore } from "@/stores/applyStore.js";
import Avatar from "@/views/Apply/components/PersonalInfo/components/Avatar.vue";
import DegreeInfo from "@/views/Apply/components/PersonalInfo/components/DegreeInfo.vue";
import DividerLine from "@/views/Apply/components/tools/DividerLine.vue";

const applyStore = useApplyStore();

// 处理子组件传递的数据
const handleDegreeInfoUpdate = (data) => {
  if (data.label === "本科") {
    applyStore.updateField("universityLevel", data.rating);
    applyStore.updateField("major", data.major);
    applyStore.updateField("university", data.school); // 更新学校名称
  } else if (data.label === "硕士") {
    applyStore.updateField("masterUniversityLevel", data.rating);
    applyStore.updateField("masterMajor", data.major);
    applyStore.updateField("masterUniversity", data.school); // 更新学校名称
    applyStore.updateField("tutor", data.advisor); // 更新导师信息
  }
};

// 使用 watch 监听数据变化并更新 Pinia
watch(
  () => applyStore.name,
  (newValue) => {
    // 如果需要额外处理，可以在这里添加逻辑
  },
);

// 计算属性
const percentageRank = computed(() => {
  if (!applyStore || !applyStore.majorCount || !applyStore.rank) {
    return "";
  }
  const percentage = (applyStore.rank / applyStore.majorCount) * 100;
  return `${percentage.toFixed(2)}%`;
});

// 监听 percentageRank 变化并更新 Pinia
watch(
  () => percentageRank.value,
  (newValue) => {
    applyStore.updateField("percentage", newValue);
  },
);
</script>

<template>
  <div>
    <p class="infoClassTitle">个人基本信息</p>

    <div class="form-group">
      <!-- 姓名；性别；毕业年份；出生日期 -->
      <div style="margin-top: 40px">
        <div class="col-xs-1 col-sm-1 col-md-1 col-lg-1"></div>
        <div class="col-xs-3 col-sm-3 col-md-3 col-lg-3">
          <!-- 姓名 -->
          <div class="form-group">
            <label class="col-xs-4 col-sm-4 col-md-4 col-lg-4 control-label"
              >姓 名</label
            >
            <div class="col-xs-8 col-sm-8 col-md-8 col-lg-8">
              <input
                type="text"
                class="form-control"
                v-model="applyStore.name"
                required
              />
            </div>
          </div>

          <!-- 性别 -->
          <div class="form-group">
            <label class="col-xs-4 col-sm-4 col-md-4 col-lg-4 control-label"
              >性 别</label
            >
            <div class="col-xs-8 col-sm-8 col-md-8 col-lg-8">
              <select
                class="form-control"
                v-model="applyStore.gender"
                id="form_sex"
                required
              >
                <option value="请选择">请选择</option>
                <option value="男">男</option>
                <option value="女">女</option>
              </select>
            </div>
          </div>
        </div>

        <div class="col-xs-1 col-sm-1 col-md-1 col-lg-1"></div>
        <div class="col-xs-3 col-sm-3 col-md-3 col-lg-3">
          <!-- 毕业年份 -->
          <div class="form-group">
            <label class="col-xs-4 col-sm-4 col-md-4 col-lg-4 control-label">
              毕业年份
            </label>
            <div class="col-xs-8 col-sm-8 col-md-8 col-lg-8">
              <select
                class="form-control"
                v-model="applyStore.graduationYear"
                required
              >
                <option value="2024">2024</option>
                <option value="2025" selected>2025</option>
                <option value="2026">2026</option>
                <option value="">其他</option>
              </select>
              <input
                v-if="applyStore.graduationYear === ''"
                type="number"
                class="form-control"
                v-model="applyStore.customRound"
                required
              />
            </div>
          </div>

          <!-- 出生日期 -->
          <div class="form-group">
            <label
              class="col-xs-4 col-sm-4 col-md-4 col-lg-4 control-label"
              style="white-space: nowrap"
              >出生年月</label
            >
            <div class="col-xs-8 col-sm-8 col-md-8 col-lg-8">
              <div
                class="input-group date form-control"
                id="datetimepicker1"
                style="padding: 0"
              >
                <input
                  type="date"
                  v-model="applyStore.birthDate"
                  required
                  style="margin-top: 5px; border: none; width: 80%"
                />
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="col-xs-1 col-sm-1 col-md-1 col-lg-1"></div>
      <div
        class="col-xs-3 col-sm-3 col-md-3 col-lg-3"
        style="margin-top: -60px"
      >
        <Avatar />
      </div>
    </div>

    <!-- 本科信息 -->
    <DegreeInfo label="本科" @degreeInfoUpdated="handleDegreeInfoUpdate" />

    <!-- 专业排名 -->
    <div class="form-group">
      <div class="col-xs-1 col-sm-1 col-md-1 col-lg-1"></div>

      <label
        class="col-xs-1 col-sm-1 col-md-1 col-lg-1 control-label"
        style="white-space: nowrap"
        >专业人数</label
      >
      <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2">
        <input
          type="text"
          class="form-control"
          v-model.number="applyStore.majorCount"
          min="1"
          required
        />
      </div>

      <div class="col-xs-1 col-sm-1 col-md-1 col-lg-1"></div>

      <label class="col-xs-1 col-sm-1 col-md-1 col-lg-1 control-label"
        >排 名</label
      >
      <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2">
        <input
          type="text"
          class="form-control"
          v-model.number="applyStore.rank"
          min="1"
          required
        />
      </div>

      <div class="col-lg-4">
        <label class="col-lg-3 control-label">百分比</label>
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

    <!-- 硕士信息，包含导师字段 -->
    <DegreeInfo
      label="硕士"
      :showAdvisor="true"
      @degreeInfoUpdated="handleDegreeInfoUpdate"
    />

    <!-- 电话；邮箱 -->
    <div class="form-group">
      <div class="col-xs-1 col-sm-1 col-md-1 col-lg-1"></div>

      <label
        class="col-xs-1 col-sm-1 col-md-1 col-lg-1 control-label"
        style="white-space: nowrap"
        >手机号码</label
      >
      <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2">
        <input
          type="text"
          class="form-control"
          v-model="applyStore.phone"
          id="form_phonenumber"
          required
        />
      </div>

      <div class="col-xs-1 col-sm-1 col-md-1 col-lg-1"></div>

      <label
        class="col-xs-1 col-sm-1 col-md-1 col-lg-1 control-label"
        style="white-space: nowrap"
        >电子邮箱</label
      >
      <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2">
        <input
          type="text"
          class="form-control"
          v-model="applyStore.email"
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
      selectedRound: "2025",
      customRound: null,
    };
  },
};
</script>
