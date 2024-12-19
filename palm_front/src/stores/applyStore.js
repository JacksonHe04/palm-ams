// src/stores/applyStore.js
import { defineStore } from "pinia";
import { v4 as uuidv4 } from "uuid";

export const useApplyStore = defineStore("apply", {
  state: () => ({
    id: uuidv4(),
    name: "",
    graduationYear: null,
    gender: "",
    birthDate: "",
    photo: "",
    university: "",
    universityLevel: "",
    major: "",
    majorCount: null,
    rank: null,
    percentage: "",
    masterUniversity: "",
    masterUniversityLevel: "",
    masterMajor: "",
    tutor: "",
    phone: "",
    email: "",
    applicationType: "",
    firstChoice: "",
    secondChoice: "",
    thirdChoice: "",
    isAdjustable: false,
    papers: [],
    awards: [],
    resume: "",
    proofs: "",
    status: "待审核",
  }),
  actions: {
    updateField(fieldName, value) {
      this[fieldName] = value;
    },
    resetFields() {
      this.$reset();
      this.id = uuidv4(); // 重置时重新生成ID
    },
  },
});
