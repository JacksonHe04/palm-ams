<script setup>
import { ref } from 'vue';

const fileInput = ref(null);

const handleFileChange = (event) => {
  const file = event.target.files[0];
  if (file) {
    const reader = new FileReader();
    reader.onload = (e) => {
      document.getElementById('preview').src = e.target.result;
    };
    reader.readAsDataURL(file);
  }
};
</script>

<template>
  <div class="avatar">
    <div class="form-group-container">
      <div class="form-group">
        <img id="preview" alt="请上传：1寸证件照" />
      </div>
      <div class="form-group">
        <button @click="fileInput.click()">上传头像</button>
        <input type="file" accept="image/*" name="photo" id="photo" ref="fileInput" @change="handleFileChange" style="display: none;" />
      </div>
    </div>
  </div>
</template>

<style scoped>
.avatar {
  display: flex;
  align-items: flex-start;
}

img {
  border: 1px solid grey; /* 设置边框 */
  width: 2.5cm;
  height: 3.5cm;
  border-radius: 10px; /* 添加圆角 */
  padding: 10px;
}

.form-group-container {
  display: flex;
  align-items: center;
  gap: 60px; /* 调整间距 */
}

.form-group {
  display: flex;
  align-items: center;
}

button {
  background: white;
  border: 1px solid #ccc;
  border-radius: 3px;
  cursor: pointer;
  font-weight: 700;
  font-size: 10pt;
}

button:hover {
  background: rgba(129, 163, 198, 0.41);
}
</style>

