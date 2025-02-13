<template>
  <el-collapse>
    <el-collapse-item title="选择字段" name="1">
      <div class="floating-container">
        <el-checkbox-group
            v-model="checkedFields"
            @change="updateFields">
          <div class="checkbox-row">
            <el-checkbox
                v-for="field in fields"
                :key="field"
                :label="field"
                class="horizontal-checkbox">
              {{ field }}
            </el-checkbox>
          </div>
        </el-checkbox-group>
      </div>
    </el-collapse-item>
  </el-collapse>
</template>

<script>
import { ref, watch } from 'vue';

export default {
  props: {
    fields: Array,
    visibleFields: Array,
  },
  emits: ['update-visible-fields'],
  setup(props, { emit }) {
    const checkedFields = ref([...props.visibleFields]);

    watch(() => props.visibleFields, (newVal) => {
      checkedFields.value = [...newVal];
    });

    const updateFields = () => {
      emit('update-visible-fields', checkedFields.value);
    };

    return { checkedFields, updateFields };
  }
};
</script>

<style scoped>
.el-collapse-item__content {
  position: relative;
}

.floating-container {
  position: absolute;
  z-index: 1000; /* 确保它在其他元素之上 */
  background-color: white; /* 根据需要设置背景颜色 */
  border: 1px solid #dcdcdc; /* 根据需要设置边框 */
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1); /* 添加阴影效果 */
  width: 100%; /* 根据需要调整宽度 */
  padding: 15px 0 0 15px;
  border-radius: 10px;
}

.checkbox-row {
  display: flex;
  flex-wrap: wrap;
}

.horizontal-checkbox {
  display: inline-block;
  margin-right: 10px; /* 可以根据需要调整间距 */
  margin-bottom: 10px; /* 可以根据需要调整间距 */
}
</style>
