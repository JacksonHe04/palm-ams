import { defineStore } from "pinia";
import { getStudents } from "../apis/students";

export const useStudentsStore = defineStore("students", {
  state: () => ({
    students: [], // 学生数据
    visibleFields: [
      // "ID",
      "姓名",
      // "性别",
      // "出生年月",
      // "照片",
      "报名类型",
      "本科学校",
      "本科等级",
      "本科专业",
      // "专业人数",
      // "排名",
      "百分比",
      "硕士学校",
      "硕士等级",
      "硕士专业",
      "导师",
      "手机号码",
      "电子邮箱",
      "毕业年份",
      // "第一志愿",
      // "第二志愿",
      // "第三志愿",
      // "是否服从调剂",
      // "简历文件",
      // "证明材料",
      "状态",
    ], // 默认可见字段
    allFields: [
      "ID",
      "姓名",
      "报名类型",
      "毕业年份",
      "本科学校",
      "本科等级",
      "本科专业",
      "专业人数",
      "排名",
      "百分比",
      "硕士学校",
      "硕士等级",
      "硕士专业",
      "导师",
      "性别",
      "出生年月",
      "照片",
      "手机号码",
      "电子邮箱",
      "第一志愿",
      "第二志愿",
      "第三志愿",
      "是否服从调剂",
      "简历文件",
      "证明材料",
      "状态",
    ],
    fieldProps: {
      ID: "id",
      姓名: "name",
      报名类型: "applicationType",
      毕业年份: "graduationYear",
      性别: "gender",
      出生年月: "birthDate",
      照片: "photo",
      本科学校: "university",
      本科等级: "universityLevel",
      本科专业: "major",
      专业人数: "majorCount",
      排名: "rank",
      百分比: "percentage",
      硕士学校: "masterUniversity",
      硕士等级: "masterUniversityLevel",
      硕士专业: "masterMajor",
      导师: "tutor",
      手机号码: "phone",
      电子邮箱: "email",
      第一志愿: "firstChoice",
      第二志愿: "secondChoice",
      第三志愿: "thirdChoice",
      是否服从调剂: "isAdjustable",
      简历文件: "resume",
      证明材料: "proofs",
      状态: "status",
    },
    paperFields: ["论文一", "论文二", "论文三"],
    awardFields: ["奖项一", "奖项二", "奖项三"],
    sortableFields: [
      "百分比",
      "本科等级",
      "硕士等级",
      "ID",
      "报名类型",
      "毕业年份",
      "本科专业",
      "硕士专业",
    ],
    levelOrder: {
      A: 1,
      B: 2,
      C: 3
    },
  }),
  actions: {
    async fetchStudents() {
      try {
        this.students = await getStudents();
      } catch (error) {
        console.error("Failed to fetch students:", error);
      }
    },
    isPaperOrAwardField(field) {
      return (
        this.paperFields.includes(field) || this.awardFields.includes(field)
      );
    },
  },
});
