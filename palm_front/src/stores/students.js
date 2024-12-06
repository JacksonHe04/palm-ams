import { defineStore } from "pinia";

export const useStudentsStore = defineStore("students", {
  state: () => ({
    students: [], // 学生数据
    visibleFields: [
      "ID",
      "姓名",
      // "性别",
      // "出生年月",
      // "照片",
      "本科学校",
      "本科专业",
      // "专业人数",
      // "排名",
      "百分比",
      "硕士学校",
      "硕士专业",
      "导师",
      "手机号码",
      "电子邮箱",
      "报名类型",
      "毕业年份",
      // "第一志愿",
      // "第二志愿",
      // "第三志愿",
      // "是否服从调剂",
      "简历文件",
      // "证明材料",
      "状态",
    ], // 默认可见字段
  }),
  actions: {
    async fetchStudents() {
      this.students = [
        {
          id: 1, // ID
          name: "小明", // 姓名
          graduationYear: 2023, // 毕业年份
          gender: "男", // 性别
          birthDate: "1999-01", // 出生年月
          photo: "path/to/photo1.jpg", // 照片
          university: "东南大学", // 本科学校
          major: "计算机科学", // 本科专业
          majorCount: 100, // 专业人数
          rank: 5, // 排名
          percentage: "5%", // 百分比
          masterUniversity: "斯坦福大学", // 硕士学校
          masterMajor: "人工智能", // 硕士专业
          tutor: "张三教授", // 导师
          phone: "13800138000", // 手机号码
          email: "xiaoming@example.com", // 电子邮箱
          applicationType: "硕士", // 报名类型
          firstChoice: "张敏灵", // 第一志愿
          secondChoice: "薛晖", // 第二志愿
          thirdChoice: "耿新", // 第三志愿
          isAdjustable: true, // 是否服从调剂
          papers: [
            {
              publicationTime: "2022-01",
              journalConference: "AI Journal",
              paperName: "Vol.1",
              ccfLevel: "CCF-A",
              awardCategory: "最佳论文",
            },
            {
              publicationTime: "2022-02",
              journalConference: "AI Conference",
              paperName: "Vol.2",
              ccfLevel: "CCF-B",
              awardCategory: "优秀论文",
            },
            {
              publicationTime: "2022-03",
              journalConference: "AI Symposium",
              paperName: "Vol.3",
              ccfLevel: "CCF-C",
              awardCategory: "创新论文",
            },
          ],
          awards: [
            {
              isLeader: true,
              awardTime: "2021-01",
              awardName: "ACM竞赛一等奖",
              levelRanking: "一等奖",
            },
            {
              isLeader: false,
              awardTime: "2021-02",
              awardName: "电子设计竞赛二等奖",
              levelRanking: "二等奖",
            },
            {
              isLeader: true,
              awardTime: "2021-03",
              awardName: "编程大赛三等奖",
              levelRanking: "三等奖",
            },
          ],
          resume: "path/to/resume1.pdf", // 简历文件
          proofs: "path/to/proof1.zip", // 证明材料
          status: "待审核", // 状态
        },
        {
          id: 2, // ID
          name: "小红", // 姓名
          graduationYear: 2024, // 毕业年份
          gender: "女", // 性别
          birthDate: "2000-05", // 出生年月
          photo: "path/to/photo2.jpg", // 照片
          university: "清华大学", // 本科学校
          major: "电子工程", // 本科专业
          majorCount: 80, // 专业人数
          rank: 12, // 排名
          percentage: "15%", // 百分比
          masterUniversity: "", // 硕士学校
          masterMajor: "", // 硕士专业
          tutor: "", // 导师
          phone: "13900139000", // 手机号码
          email: "xiaohong@example.com", // 电子邮箱
          applicationType: "直博", // 报名类型
          firstChoice: "贾育衡", // 第一志愿
          secondChoice: "杨旭", // 第二志愿
          thirdChoice: "张敏灵", // 第三志愿
          isAdjustable: false, // 是否服从调剂
          papers: [
            {
              publicationTime: "2023-01",
              journalConference: "Control Systems Journal",
              paperName: "Vol.3",
              ccfLevel: "CCF-A",
              awardCategory: "最佳论文",
            },
            {
              publicationTime: "2023-02",
              journalConference: "Control Systems Conference",
              paperName: "Vol.4",
              ccfLevel: "CCF-B",
              awardCategory: "优秀论文",
            },
            {
              publicationTime: "2023-03",
              journalConference: "Control Systems Symposium",
              paperName: "Vol.5",
              ccfLevel: "CCF-C",
              awardCategory: "创新论文",
            },
          ],
          awards: [
            {
              isLeader: true,
              awardTime: "2022-01",
              awardName: "电子设计竞赛二等奖",
              levelRanking: "二等奖",
            },
            {
              isLeader: false,
              awardTime: "2022-02",
              awardName: "编程大赛三等奖",
              levelRanking: "三等奖",
            },
            {
              isLeader: true,
              awardTime: "2022-03",
              awardName: "ACM竞赛一等奖",
              levelRanking: "一等奖",
            },
          ],
          resume: "path/to/resume2.pdf", // 简历文件
          proofs: "path/to/proof2.zip", // 证明材料
          status: "待审核", // 状态
        },
        // 可以继续添加更多模拟数据...
        {
          id: 3,
          name: "小明",
        },

        {
          id: 4,
          name: "小明",
        },
        {
          id: 5,
          name: "小明",
        },
        {
          id: 6,
          name: "小明",
        },
        {
          id: 7,
          name: "小明",
        },
        {
          id: 8,
          name: "小明",
        },
        {
          id: 9,
          name: "小明",
        },
        {
          id: 10,
          name: "小明",
        },
        {
          id: 11,
          name: "小明",
        },
        {
          id: 12,
          name: "小明",
        },
        {
          id: 13,
          name: "小明",
        },
        {
          id: 14,
          name: "小明",
        },
        {
          id: 15,
          name: "小明",
        }
      ];
    },
  },
});
