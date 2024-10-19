# 东南大学PALM实验室招生系统开发项目

此项目的目标是对东南大学PALM实验室的招生系统进行重做，主要任务包括页面美化、功能增减以及后续的算法归一化打分机制。该系统由前台和后台组成，前台用于申请者填写申请信息，后台用于PALM实验室的老师进行数据管理。

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

## 运行项目

以下是项目的基本运行步骤：

---

1. **克隆仓库**：
   ```bash
   git clone https://github.com/jacksonhe04/PalmAdmissionsSystem.git
   cd PalmAdmissionsSystem
   ```
   
2. **安装MySQL并进行数据库初始化**：

   1. 下载并安装MySQL：[MySQL官方安装指南](https://dev.mysql.com/downloads/installer/)。

   2. 安装完成后，使用默认账号`root`，设置密码为`123456`。

   3. 启动MySQL服务，并通过命令行登录MySQL：
      ```bash
      mysql -u root -p
      ```
      输入密码`123456`。

   4. 创建项目所需的数据库：
      ```sql
      CREATE DATABASE PalmAdmissionsSystem;
      ```

   5. 打开PyCharm，选择**Database**工具窗口，点击左上角的"+"号，选择**Data Source -> MySQL**。

   6. 在弹出的配置窗口中，输入以下内容：

      - **Host**: `localhost`
      - **Port**: `3306`
      - **User**: `root`
      - **Password**: `123456`
      - **Database**: `PalmAdmissionsSystem`

      点击**Test Connection**测试连接，成功后点击**OK**保存配置。

3. **安装Python解释器**：
   - 访问Python官方网站 [python.org](https://www.python.org/)。
   - 导航至下载页面，选择适合您操作系统的最新版本进行下载。
   - 安装过程中，请确保勾选“Add Python to PATH”选项，以便于在命令行中直接使用Python。

4. **在PyCharm中配置Python解释器**：
   - 打开PyCharm，进入 `File` > `Settings`（或者在Mac上 `PyCharm` > `Preferences`）。
   - 在左侧菜单中选择 `Project: <项目名称>` > `Python Interpreter`。
   - 点击右上角的齿轮图标，选择 `Add`。
   - 选择 `Existing environment`，然后点击右侧的 `...` 按钮浏览并选择您的Python解释器路径。
   - 确认选择后，点击 `OK` 完成配置。

5. **安装依赖**：
   ```bash
   pip install -r requirements.txt
   ```

6. **运行数据库迁移**：
   执行数据库迁移命令，初始化数据库：
   ```bash
   python manage.py migrate
   ```

7. **运行服务器**：
   启动Django开发服务器：
   ```bash
   python manage.py runserver
   ```
   如果终端报错提示缺少某些包，请根据终端提示使用以下命令安装缺失的包：
   ```bash
   pip install <包名>
   ```

8. **访问项目**：
   在浏览器中访问`http://127.0.0.1:8000`即可查看前台页面。

---

## 未来工作

- 使用Vue.js重构系统的前端页面和JavaScript数据交互
- 深度重构Django后端以优化后台数据管理流程。
- 实现申请者简历和面试的自动评分系统。
- 提高系统的安全性和性能，支持更多的申请者并发访问。

## 开发建议

由于团队中大部分成员对`Django`框架并不熟悉，建议：
- 使用[Django官方文档](https://docs.djangoproject.com/zh-hans/5.1/)作为学习资源。
- 何锦诚同学可以为其他成员提供Django框架和数据库的使用指导，帮助他们尽快上手开发。

---

此README文件为团队内部参考，目的是帮助所有成员明确开发目标，了解项目结构并开始协作开发。如果有任何问题，请及时与组长或技术负责人沟通。