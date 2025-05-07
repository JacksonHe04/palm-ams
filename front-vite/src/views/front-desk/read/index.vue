<template>
  <FrontMain>
    <div class="container">
      <h1 class="title">PALM实验室招收 2026 年秋季入学博士及硕士研究生</h1>
      <p class="welcome-message">
        欢迎报考计算机学院、软件学院、东-蒙联合研究生院的同学申请
      </p>
      <!-- <div class="part-big">
        <h3>重要日期</h3>
        <p>报名截止：暂无</p>
        <p>面试时间：7月5日~7月7日（第一批次）；7月17日~7月19日（第二批次）</p>
        <p>面试安排：具体见面试邮件通知</p>
        <h3>注意事项</h3> -->

      <ul class="notice-list">
        <li>
          申请前请首先阅读 PALM 实验室招生说明
          <a href="https://palm.seu.edu.cn/application.html"
            >https://palm.seu.edu.cn/application.html</a
          >。
        </li>
        <li>
          报名系统网址：<a href="https://palm.inon.space"
            >https://palm.inon.space</a
          >。
        </li>
        <!-- <li>
          填写完报名系统后，请将申请材料发送至邮箱palmwebsite@163.com，邮件标题为“姓名+拟申请学院及专业+2025博士（或硕士）”，申请材料包括：个人简历，本科成绩单（申请硕士研究生），论文、专利、获奖等证明材料。请将申请材料打包后作为附件上传，使用
          “学校-姓名.zip”格式命名。
        </li> -->
        <li>
          有关PALM实验室具体情况，请访问实验室官方网站：<a
            href="https://palm.seu.edu.cn"
            >https://palm.seu.edu.cn</a
          >。
        </li>
        <!-- <li>
            <b
              >所有最终进入PALM的学生都需经过相同的考查过程，具体导师安排将在通过考查之后双选确定。</b
            >
          </li>
        </ul> -->

        <!-- <h3>PALM实验室招生说明</h3>
        <p class="indent">
          首先感谢您有兴趣选择东南大学模式学习与挖掘（PALM）实验室作为您攻读博士/硕士学位的地方，为帮助您更加确信您的选择是否明智，请耐心阅读如下说明：
        </p>
        <ul class="recruitment-details">
          <li>
            <span class="important">重要：</span>
            您是否了解我们的研究方向？在大致了解的基础上，您是否确实对这些方向感兴趣？研究之路可能充满挫败感，如果没有足够的兴趣支撑，可能会感到痛苦。
          </li>
          <li>
            <span class="important">重要：</span>
            您是否有较大的经济压力？研究工作需要全心投入，在读期间还要考虑赚钱是件非常糟糕的事情。尽管我们会提供助研金作为生活补贴，但如果这是您的主要考虑，PALM实验室可能不是您的最佳选择。
          </li>
          <li>
            对于本科生申请者，相对于申请硕士研究生，我们更希望看到直博申请者。因为这给了我们更多时间规划更为长远而有意义的研究课题，并进行更为系统的科研训练。当然，这并不意味着我们不欢迎您申请硕士研究生。
          </li>
          <li>
            对我们来说，理想的申请者大致是这样的：扎实的数学基础、熟练的英文读写能力、过硬的编程能力，同时逻辑思维清晰、表达能力强，最好还能乐观积极、坚韧不拔、亲和力强。当然理想和现实我们也是分得清的，以上描述顺序大致代表重要程度。
          </li>
          <li>
            所有申请者都需要经过PALM实验室组织的面试才能被接受。面试的目的是给我们双方一个面对面了解对方的机会，以此来帮助您判断是否适合到PALM实验室工作和学习。因此，被接受并不意味着成功，没被接受当然也不是失败。
          </li>
          <li>
            需要注意的是，即使被PALM实验室接受，您仍需通过东南大学计算机科学与工程学院的正式考核，才能获得入学资格，二者之间没有直接联系。
          </li>
          <li>
            如果您认识PALM实验室老师的亲友、同事或领导，建议您不要通过他们与我们联系，这样不但不会加分，反而会造成不好的影响。最好的方式就是您本人直接联系意向导师。
          </li> -->
      </ul>

      <h3>2024年PALM实验室拟招生导师名单</h3>
      <table class="center-table">
        <thead>
          <tr>
            <th>拟招生导师</th>
            <th>拟招生对象</th>
            <th>招生院系</th>
            <th>研究方向</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(person, index) in personnel" :key="index">
            <td>{{ person.name }}</td>
            <td>{{ person.recruitment_type }}</td>
            <td>{{ person.department }}</td>
            <td>{{ person.research_direction }}</td>
          </tr>
        </tbody>
      </table>
    </div>
    <!-- </div> -->
  </FrontMain>
</template>

<script setup>
import FrontMain from "@/views/front-desk/components/FrontMain.vue";
import { useSettingStore } from "@/stores/settingStore";
import { onMounted } from "vue";
import { storeToRefs } from "pinia";

const settingStore = useSettingStore();
const { personnel } = storeToRefs(settingStore);

onMounted(async () => {
  await settingStore.fetchPersonnel();
});
</script>

<style scoped lang="scss">
a {
  color: $secondary-color;
  text-decoration: underline;
  transition: color 0.3s ease;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

.title {
  text-align: center;
  font-size: 2rem;
  margin-bottom: 20px;
}

.welcome-message {
  color: #d9534f;
  font-size: 1.2rem;
  text-align: center;
  margin-bottom: 20px;
}

.part-big {
  margin-top: 20px;
}

.indent {
  text-indent: 2em;
  margin-bottom: 10px;
}

.important {
  color: #d9534f;
  font-weight: bold;
}

.notice-list li,
.recruitment-details li {
  text-align: left;
  font-size: 1rem;
  line-height: 1.6;
  margin-bottom: 10px;
}

.center-table {
  width: 100%;
  border-collapse: collapse;
  margin: 20px 0;
  font-size: 1rem;
  min-width: 400px;
  box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
}

.center-table th,
.center-table td {
  padding: 12px 15px;
  text-align: center;
}

.center-table th {
  background-color: #f5f5f5;
  color: #333;
}

.center-table tbody tr:nth-of-type(even) {
  background-color: #f9f9f9;
}

.center-table tbody tr:hover {
  background-color: #f1f1f1;
}

@media (max-width: 768px) {
  .center-table {
    font-size: 0.9rem;
  }

  .center-table th,
  .center-table td {
    padding: 8px 12px;
  }
}
</style>
