<template>
  <el-pagination
      @current-change="onPageChange"
      :current-page="currentPage"
      :page-size="pageSize"
      :total="total"
      layout="prev, pager, next" />
</template>

<script>
export default {
  props: {
    total: Number,
    currentPage: Number,
    pageSize: Number,
  },
  emits: ['page-change'],
  setup(_, { emit }) {
    const onPageChange = (page) => {
      emit('page-change', page);
    };

    return { onPageChange };
  }
};
</script>