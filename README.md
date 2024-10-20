# 东南大学PALM实验室招生系统开发项目

t此项目的目标是对东南大学PALM实验室的招生系统进行重做，主要任务包括页面美化、功能增减以及后续的算法归一化打分机制。该系统由前台和后台组成，前台用于申请者填写申请信息，后台用于PALM实验室的老师进行数据管理。

## 项目成员

- **刘宇轩**（组长）：大二
- **何锦诚**：大三
- **戴雨成**：大一
- **胡瀚**：大一

## 项目架构

该项目使用`Django`框架搭建，后端负责处理数据库操作和业务逻辑，前端部分主要负责用户交互界面。

### 主要文件说明

- `ApplicationSystem/`: 主应用程序目录，包含项目的配置文件和WSGI入口。
- `Apply/`: 招生系统的业务逻辑处理模块，包含数据库模型（`models.py`）、视图（`views.py`）、管理页面（`admin.py`）等。
- `manage.py`: Django的管理工具，用于执行数据库迁移、启动服务器等操作。
- `static/`: 静态文件目录，包含前端使用的静态资源如图片、JavaScript文件。
- `templates/`: 模板文件目录，存放HTML模板文件，控制页面布局和展示内容。

### 数据库

当前系统使用`MySQL`作为默认数据库，以便更好地支持大规模数据管理。数据库迁移文件位于`Apply/migrations/`目录下。

## 任务分工与开发计划

1. **页面美化**：
   - 对现有的前端页面进行优化，采用更现代化的设计，提高用户体验。
   - 使用`Vue.js`框架进行前后端分离，实现更流畅的交互。

2. **功能增减**：
   - 添加新的表单字段，以便申请者可以提供更多的个人信息。
   - 后台添加简历和面试评分管理功能，实现申请者评分的自动化。

3. **算法打分机制**：
   - 后期将引入算法对申请者的简历和面试进行自动评分。评分机制的算法将在后端实现，结果将展示在后台页面中。

---

## Intro Meeting at 19:00 on 2024-10-20 in Mei Canteen

### 1. 项目简介
- **项目目标**：更新东南大学PALM实验室招生系统，主要任务包括页面美化、功能增减以及算法归一化打分机制。
- **项目架构**：基于Django框架，前端使用Vue.js，后端处理数据库与业务逻辑。

#### 通过项目可以学到的内容
- JetBrains 编辑器基本操作
- Git 版本管理与 GitHub 多人协作
- 常用的终端命令行指令
- Python 基本语法
- 主流 Python 框架 Django
- 前端三件套 HTML + CSS + JavaScript
- 前端主流框架 Vue.js
- 主流数据库管理工具 MySQL
- 常用的数据处理与机器学习 Python 库
- Web 项目的打包、部署与上线
- 基于语雀文档管理的团队协作

### 2. 操作指导

根据README.md提供的指示，以下是项目运行的基本步骤：

1. **注册JetBrains账号**
   - 注册：[JetBrains账号注册](https://account.jetbrains.com/)
   - 认证学生身份：[JetBrains学生身份认证](https://www.jetbrains.com/community/education/#students/)
   - 通过东南大学邮箱确认学生认证信息：[邮箱确认](https://mail.seu.edu.cn/)

2. **安装MySQL并进行数据库初始化**
   - 下载并安装MySQL：[MySQL官方安装指南](https://downloads.mysql.com/archives/installer/)
   - 参考教程：[MySQL安装教程](https://blog.csdn.net/m0_71422677/article/details/136007088)
   - 设置默认账号`root`和密码`123456`，通过命令行启动MySQL服务并登录：
     ```bash
     mysql -u root -p
     ```
     输入密码`123456`。

   - 创建项目数据库：
     ```sql
     CREATE DATABASE palm_apply;
     ```

3. **克隆项目仓库并配置数据库**
   - 克隆仓库：
     ```bash
     git clone https://github.com/jacksonhe04/PalmAdmissionsSystem.git
     ```

   - 打开PyCharm，选择**Database**工具窗口，配置MySQL连接：
      - **Host**: `localhost`
      - **Port**: `3306`
      - **User**: `root`
      - **Password**: `123456`
      - **Database**: `palm_apply`

4. **安装Python与Anaconda**
   - 下载Python 3.12：[Python下载](https://www.anaconda.com/download/success)
   - 安装PyCharm专业版：[PyCharm下载](https://www.jetbrains.com/pycharm/download/)

5. **配置项目环境并安装依赖**
   - 在项目目录下安装依赖：
     ```bash
     pip install -r requirements.txt
     ```

6. **进行数据库迁移**
   - 确保MySQL已配置好，执行数据库迁移：
     ```bash
     python manage.py migrate
     ```

7. **启动项目服务器**
   - 启动开发服务器：
     ```bash
     python manage.py runserver
     ```

   - 如果出现缺失包提示，安装相关包：
     ```bash
     pip install <包名>
     ```

8. **下载与配置语雀**
   - [下载语雀](https://www.yuque.com/download)并认证学生身份：[语雀学生认证](https://www.yuque.com/about/welfare)

9. **使用语雀进行项目协作**
   - 登录语雀桌面版，加入项目知识库。

### 3. 任务分工讨论
- **A 软工作**：汇报、PPT、文档工作，参与每个环节，但无需承担纯代码工作。
- **B 前端Vue重构**：重构前台页面并优化UI设计，建立Vite框架和Vue路由。
- **C 前端新增功能**：新增如简历上传按钮，后台管理的新功能，需与B合作。
- **D 基于Django的后端开发**：为新增功能提供后端接口，需与B、C合作。

### 4. 确定会议频率
- 确定每周会议频率与交流方式。

### 5. 开发计划

**第一阶段（截至11月2日）**
- 建立`vue + vite`框架
- 重构单个HTML页面为Vue 3
- 完成前台页面美化及表单调整

---

## 未来工作

- Vue.js重构前端页面
- 优化Django后端，提升后台数据管理
- 实现自动评分系统