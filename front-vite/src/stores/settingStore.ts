import { defineStore } from "pinia";
import { ref } from "vue";
import type {
  University,
  Major,
  Personnel,
  AdmissionPeriod,
  Award,
  Year
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
  getAwards,
  updateAwards,
  getYears,
  updateYears
} from "@/apis/setting";
import defaultUniversities from '@/scripts/importSettings/importUniversities/universities.json';
// 在文件顶部添加导入
import defaultMajors from '@/scripts/importSettings/importMajors/majors.json';
// 在文件顶部添加导入
import defaultPersons from '@/scripts/importSettings/importPersons/persons.json';

export const useSettingStore = defineStore("setting", () => {
  const universities = ref<University[]>([]);
  const majors = ref<Major[]>([]);
  const personnel = ref<Personnel[]>([]);
  const admissionPeriod = ref<AdmissionPeriod>({
    startDate: "",
    endDate: "",
  });
  const awards = ref<Award[]>([]);
  const years = ref<Year[]>([]);

  // 添加状态标记
  const isInitializing = ref(true);

  // 院校相关操作
  const fetchUniversities = async () => {
    try {
      const response = await getUniversities();
      universities.value = response.data;
    } catch (error) {
      console.error("获取院校配置失败:", error);
    }
  };

  // 修改所有fetch方法，在完成后将isInitializing设置为false
  const initializeData = async () => {
    isInitializing.value = true;
    await Promise.all([
      fetchUniversities(),
      fetchMajors(),
      fetchPersonnel(),
      fetchAdmissionPeriod(),
      fetchAwards(),
      fetchYears()
    ]);
    isInitializing.value = false;
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
      if (response && response.data) {
        admissionPeriod.value = {
          startDate: response.data[0].start_date || "",
          endDate: response.data[0].end_date || ""
        };
      }
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

  // 奖项相关操作
  const fetchAwards = async () => {
    try {
      const response = await getAwards();
      awards.value = response.data;
    } catch (error) {
      console.error("获取奖项配置失败:", error);
    }
  };

  const saveAwards = async () => {
    try {
      await updateAwards(awards.value);
    } catch (error) {
      console.error("保存奖项配置失败:", error);
      throw error;
    }
  };

  // 年份相关操作
  const fetchYears = async () => {
    try {
      const response = await getYears();
      years.value = response.data;
    } catch (error) {
      console.error("获取年份配置失败:", error);
    }
  };

  const saveYears = async () => {
    try {
      await updateYears(years.value);
    } catch (error) {
      console.error("保存年份配置失败:", error);
      throw error;
    }
  };

  const initializeUniversities = async () => {
    try {
      universities.value = defaultUniversities;
      await saveUniversities();
    } catch (error) {
      console.error("初始化院校配置失败:", error);
      throw error;
    }
  };

  const initializeMajors = async () => {
    try {
      majors.value = defaultMajors;
      await saveMajors();
    } catch (error) {
      console.error("初始化专业配置失败:", error);
      throw error;
    }
  };

  // 人员相关操作
  const addPersonnel = () => {
    personnel.value.push({
      name: '',
      recruitment_type: '',
      department: '',
      research_direction: ''
    });
  };
  
  const initializePersonnel = async () => {
    try {
      const formattedPersonnel = defaultPersons.map(person => ({
        name: person.name,
        recruitment_type: person.recruitmentType,
        department: person.department,
        research_direction: person.researchDirection
      }));
      personnel.value = formattedPersonnel;
      await savePersonnel();
    } catch (error) {
      console.error("初始化人员配置失败:", error);
      throw error;
    }
  };

  return {
    universities,
    majors,
    personnel,
    admissionPeriod,
    awards,
    years,
    isInitializing,
    fetchUniversities,
    saveUniversities,
    fetchMajors,
    saveMajors,
    fetchPersonnel,
    savePersonnel,
    fetchAdmissionPeriod,
    saveAdmissionPeriod,
    fetchAwards,
    saveAwards,
    fetchYears,
    saveYears,
    initializeUniversities,
    initializeMajors,
    initializeData,
    initializePersonnel,
  };
});
