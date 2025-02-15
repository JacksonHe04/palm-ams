import { defineStore } from "pinia";
import { ref } from "vue";
import type {
  University,
  Major,
  Personnel,
  AdmissionPeriod,
} from "@/apis/setting";
import {
  getUniversities,
  updateUniversities,
  getMajors,
  updateMajors,
  getPersonnel,
  updatePersonnel,
  getAdmissionPeriod,
  updateAdmissionPeriod,
} from "@/apis/setting";

export const useSettingStore = defineStore("setting", () => {
  const universities = ref<University[]>([]);
  const majors = ref<Major[]>([]);
  const personnel = ref<Personnel[]>([]);
  const admissionPeriod = ref<AdmissionPeriod>({
    startDate: "",
    endDate: "",
  });

  // 院校相关操作
  const fetchUniversities = async () => {
    try {
      const response = await getUniversities();
      universities.value = response.data;
    } catch (error) {
      console.error("获取院校配置失败:", error);
    }
  };

  const saveUniversities = async () => {
    try {
      await updateUniversities(universities.value);
    } catch (error) {
      console.error("保存院校配置失败:", error);
      throw error;
    }
  };

  // 专业相关操作
  const fetchMajors = async () => {
    try {
      const response = await getMajors();
      majors.value = response.data;
    } catch (error) {
      console.error("获取专业配置失败:", error);
    }
  };

  const saveMajors = async () => {
    try {
      await updateMajors(majors.value);
    } catch (error) {
      console.error("保存专业配置失败:", error);
      throw error;
    }
  };

  // 人员相关操作
  const fetchPersonnel = async () => {
    try {
      const response = await getPersonnel();
      personnel.value = response.data;
    } catch (error) {
      console.error("获取人员配置失败:", error);
    }
  };

  const savePersonnel = async () => {
    try {
      await updatePersonnel(personnel.value);
    } catch (error) {
      console.error("保存人员配置失败:", error);
      throw error;
    }
  };

  // 招生时间相关操作
  const fetchAdmissionPeriod = async () => {
    try {
      const response = await getAdmissionPeriod();
      admissionPeriod.value = response.data;
    } catch (error) {
      console.error("获取招生时间配置失败:", error);
    }
  };

  const saveAdmissionPeriod = async () => {
    try {
      await updateAdmissionPeriod(admissionPeriod.value);
    } catch (error) {
      console.error("保存招生时间配置失败:", error);
      throw error;
    }
  };

  return {
    universities,
    majors,
    personnel,
    admissionPeriod,
    fetchUniversities,
    saveUniversities,
    fetchMajors,
    saveMajors,
    fetchPersonnel,
    savePersonnel,
    fetchAdmissionPeriod,
    saveAdmissionPeriod,
  };
});
