module.exports = {
  extends: ["@commitlint/config-conventional"],
  rules: {
    "type-enum": [
      2,
      "always",
      [
        "feat", // 新功能
        "fix", // 修复bug
        "docs", // 文档更新
        "style", // 代码格式（不影响代码运行的变动）
        "refactor", // 重构
        "perf", // 性能优化
        "test", // 增加测试
        "chore", // 构建过程或辅助工具的变动
        "revert", // 回退
        "build", // 打包
        "ci", // CI/CD 相关变更
        "types", // 类型定义文件更改
        "sec", // 安全
        "wip", // 开发中
        "sync", // 同步
        "merge", // 合并分支
        "revert", // 回退
        "release", // 发布
      ],
    ],
    "type-case": [2, "always", "lowerCase"],
    "subject-case": [0],
  },
};
