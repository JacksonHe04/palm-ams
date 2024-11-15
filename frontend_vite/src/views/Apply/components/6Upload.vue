<script setup>
import { ref } from "vue";
import DividerLine from "@/views/Apply/components/tools/DividerLine.vue";

const file1 = ref(null);
const file2 = ref(null);

const handleFileUpload = (event, fileRef) => {
  const file = event.target.files[0];
  if (file) {
    fileRef.value = file;
    // 模拟文件上传成功
    setTimeout(() => {
      console.log("文件上传成功");
    }, 1000);
  }
};
</script>

<template>
  <div class="upload">
    <div class="file-upload">
      <span>请上传你的简历</span>
      <input type="file" @change="(e) => handleFileUpload(e, file1)" />

    </div>
    <div class="file-upload">
      <span>请上传证明材料</span>
      <input type="file" @change="(e) => handleFileUpload(e, file2)" />

    </div>
  </div>
  <DividerLine />
</template>

<style scoped>

.upload {
  justify-content: center;
  padding: 20px 300px 0;
}

.file-upload {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-bottom: 16px;

  background-color: #ffffff; /* 白色背景 */
  border: 1px solid #d9d9d9; /* 边框 */
  border-radius: 20px; /* 圆角 */
  padding: 12px 16px; /* 内边距 */
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* 阴影效果 */
}

.file-upload input {
  margin-right: 8px;
  margin-left: 20px;
  padding: 8px 15px 8px 15px; /* 输入框内边距 */
  border: 1px solid #d9d9d9; /* 输入框边框 */
  border-radius: 15px; /* 输入框圆角 */
}

.file-upload span {
  margin-left: 8px;
  font-size: 14px; /* 字体大小 */
  color: #333333; /* 字体颜色 */
  font-weight: 700;
}
</style>
