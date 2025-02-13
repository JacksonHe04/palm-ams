<!-- SchoolList,vue -->
<script setup>
import { ref } from 'vue';

const props = defineProps({
  id: {
    type: String,
    required: true
  },
  placeholder: {
    type: String,
    default: ""
  }
});

// emit事件函数
const emit = defineEmits(['schoolSelected']);

// 学校评级数据
const schoolRatings = {
  "北京大学": "A", "中国人民大学": "A", "清华大学": "A", "北京航空航天大学": "A", "北京理工大学": "A", "中国农业大学": "B", "北京师范大学": "A", "中央民族大学": "B", "南开大学": "A", "天津大学": "A", "大连理工大学": "A", "吉林大学": "A", "哈尔滨工业大学": "A", "复旦大学": "A", "同济大学": "A", "上海交通大学": "A", "华东师范大学": "A", "南京大学": "A", "东南大学": "A", "浙江大学": "A", "中国科学技术大学": "A", "厦门大学": "A", "山东大学": "A", "中国海洋大学": "B", "武汉大学": "A", "华中科技大学": "A", "中南大学": "A", "中山大学": "A", "华南理工大学": "A", "四川大学": "A", "重庆大学": "A", "电子科技大学": "A", "西安交通大学": "A", "西北工业大学": "A", "兰州大学": "B", "中国人民解放军国防科技大学": "A", "东北大学": "A", "郑州大学": "B", "湖南大学": "A", "云南大学": "B", "西北农林科技大学": "B", "新疆大学": "B", "北京邮电大学": "A", "北京交通大学": "B", "西安电子科技大学": "A", "解放军信息工程大学": "B", "北京工业大学": "C", "北京科技大学": "B", "哈尔滨工程大学": "B", "南京航空航天大学": "B", "南京理工大学": "B", "杭州电子科技大学": "B", "合肥工业大学": "B", "西南交通大学": "B", "重庆邮电大学": "B", "解放军理工大学": "B", "天津理工大学": "C", "山西大学": "C", "大连海事大学": "C", "长春理工大学": "C", "哈尔滨理工大学": "C", "燕山大学": "C", "华东理工大学": "B", "上海大学": "B", "苏州大学": "B", "中国矿业大学": "C", "河海大学": "C", "江苏大学": "C", "南京信息工程大学": "C", "浙江工业大学": "C", "安徽大学": "C", "中国地质大学": "C", "武汉理工大学": "C", "暨南大学": "C", "深圳大学": "B", "西南大学": "C", "火箭军工程大学": "C", "西北大学": "C", "南京邮电大学": "B", "江南大学": "C", "南方科技大学": "A", "上海科技大学": "A", "中国科学院大学": "A"
};

// 存储当前选择的学校
const selectedSchool = ref('');

// 处理学校选择的函数
const handleSchoolSelect = (event) => {
  const school = event.target.value;
  selectedSchool.value = school;
  const schoolRating = schoolRatings[school] || '';

  // 通过emit向父组件传递选择的学校和评级
  emit('schoolSelected', { school, rating: schoolRating });
};
</script>

<template>
  <datalist :id="props.id" style="display: none">
    <option value="北京大学">北京大学</option>
    <option value="中国人民大学">中国人民大学</option>
    <option value="清华大学">清华大学</option>
    <option value="北京航空航天大学">北京航空航天大学</option>
    <option value="北京理工大学">北京理工大学</option>
    <option value="中国农业大学">中国农业大学</option>
    <option value="北京师范大学">北京师范大学</option>
    <option value="中央民族大学">中央民族大学</option>
    <option value="南开大学">南开大学</option>
    <option value="天津大学">天津大学</option>
    <option value="大连理工大学">大连理工大学</option>
    <option value="吉林大学">吉林大学</option>
    <option value="哈尔滨工业大学">哈尔滨工业大学</option>
    <option value="复旦大学">复旦大学</option>
    <option value="同济大学">同济大学</option>
    <option value="上海交通大学">上海交通大学</option>
    <option value="华东师范大学">华东师范大学</option>
    <option value="南京大学">南京大学</option>
    <option value="东南大学">东南大学</option>
    <option value="浙江大学">浙江大学</option>
    <option value="中国科学技术大学">中国科学技术大学</option>
    <option value="厦门大学">厦门大学</option>
    <option value="山东大学">山东大学</option>
    <option value="中国海洋大学">中国海洋大学</option>
    <option value="武汉大学">武汉大学</option>
    <option value="华中科技大学">华中科技大学</option>
    <option value="中南大学">中南大学</option>
    <option value="中山大学">中山大学</option>
    <option value="华南理工大学">华南理工大学</option>
    <option value="四川大学">四川大学</option>
    <option value="重庆大学">重庆大学</option>
    <option value="电子科技大学">电子科技大学</option>
    <option value="西安交通大学">西安交通大学</option>
    <option value="西北工业大学">西北工业大学</option>
    <option value="兰州大学">兰州大学</option>
    <option value="中国人民解放军国防科技大学"></option>
    <option value="东北大学">东北大学</option>
    <option value="郑州大学">郑州大学</option>
    <option value="湖南大学">湖南大学</option>
    <option value="云南大学">云南大学</option>
    <option value="西北农林科技大学">西北农林科技大学</option>
    <option value="新疆大学">新疆大学</option>
    <option value="北京邮电大学">北京邮电大学</option>
    <option value="北京交通大学">北京交通大学</option>
    <option value="西安电子科技大学">西安电子科技大学</option>
    <option value="解放军信息工程大学"></option>
    <option value="北京工业大学">北京工业大学</option>
    <option value="北京科技大学">北京科技大学</option>
    <option value="哈尔滨工程大学">哈尔滨工程大学</option>
    <option value="南京航空航天大学">南京航空航天大学</option>
    <option value="南京理工大学">南京理工大学</option>
    <option value="杭州电子科技大学">杭州电子科技大学</option>
    <option value="合肥工业大学">合肥工业大学</option>
    <option value="西南交通大学">西南交通大学</option>
    <option value="重庆邮电大学">重庆邮电大学</option>
    <option value="解放军理工大学">解放军理工大学</option>
    <option value="天津理工大学">天津理工大学</option>
    <option value="山西大学">山西大学</option>
    <option value="大连海事大学">大连海事大学</option>
    <option value="长春理工大学">长春理工大学</option>
    <option value="哈尔滨理工大学"></option>
    <option value="燕山大学">燕山大学</option>
    <option value="华东理工大学">华东理工大学</option>
    <option value="上海大学">上海大学</option>
    <option value="苏州大学">苏州大学</option>
    <option value="中国矿业大学">中国矿业大学</option>
    <option value="河海大学">河海大学</option>
    <option value="江苏大学">江苏大学</option>
    <option value="南京信息工程大学">南京信息工程大学</option>
    <option value="浙江工业大学">浙江工业大学</option>
    <option value="安徽大学">安徽大学</option>
    <option value="中国地质大学">中国地质大学</option>
    <option value="武汉理工大学">武汉理工大学</option>
    <option value="暨南大学">暨南大学</option>
    <option value="深圳大学">深圳大学</option>
    <option value="西南大学">西南大学</option>
    <option value="火箭军工程大学">火箭军工程大学</option>
    <option value="西北大学">西北大学</option>
    <option value="南京邮电大学">南京邮电大学</option>
    <option value="江南大学">江南大学</option>
    <option value="南方科技大学">南方科技大学</option>
    <option value="上海科技大学">上海科技大学</option>
    <option value="中国科学院大学">中国科学院大学</option>
  </datalist>
  <input
      type="text"
      class="form-control"
      @input="handleSchoolSelect"
      :list="props.id"
      :placeholder="placeholder"
      :required="$attrs.required"
  />
</template>
