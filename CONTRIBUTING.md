# 🤝 贡献指南

欢迎为OpenClaw教程项目做出贡献！以下是参与项目的指南。

## 🎯 贡献方式

### 1. 报告问题
- 发现bug或有改进建议？
- 在 [Issues](https://github.com/lsq-web17/OpenClaw-Tutorial/issues) 页面创建新issue
- 清晰描述问题和复现步骤

### 2. 提交代码
- 修复bug或添加新功能
- 确保代码质量和规范
- 添加相应的测试

### 3. 改进文档
- 修正错别字或语法错误
- 补充遗漏的信息
- 优化文档结构

### 4. 翻译工作
- 将文档翻译成其他语言
- 保持翻译准确性和一致性

## 🚀 开发流程

### 1. Fork仓库
- 点击GitHub页面右上角的Fork按钮
- 克隆您的fork到本地：
  ```bash
  git clone https://github.com/您的用户名/OpenClaw-Tutorial.git
  cd OpenClaw-Tutorial
  ```

### 2. 创建分支
- 为新功能或bug修复创建分支：
  ```bash
  git checkout -b feature/您的功能名称
  # 或
  git checkout -b fix/修复的问题描述
  ```

### 3. 开发测试
- 编写代码
- 运行测试确保无误：
  ```bash
  # 运行所有测试
  python -m pytest
  
  # 运行特定测试
  python -m pytest tests/test_hello.py
  
  # 生成测试覆盖率报告
  python -m pytest --cov=.
  ```

### 4. 提交代码
- 提交您的更改：
  ```bash
  git add .
  git commit -m "描述您的更改"
  ```

### 5. 推送代码
- 推送到您的fork：
  ```bash
  git push origin feature/您的功能名称
  ```

### 6. 创建Pull Request
- 在GitHub页面创建Pull Request
- 描述您的更改内容和原因
- 关联相关的issue（如果有）

## 📝 代码规范

### Python代码规范
- 遵循 [PEP 8](https://www.python.org/dev/peps/pep-0008/) 规范
- 使用有意义的变量和函数名
- 添加适当的注释和文档字符串

### 文档规范
- 使用Markdown格式
- 保持一致的格式和风格
- 图片使用相对路径

### 提交信息规范
- 使用中文或英文
- 格式：`类型: 描述`
- 类型：feat, fix, docs, style, refactor, test, chore

## 🧪 测试要求

### 单元测试
- 为新功能添加单元测试
- 测试覆盖率保持在80%以上
- 测试文件命名：`test_*.py`

### 集成测试
- 确保各模块协同工作正常
- 测试边界条件和异常情况

### 代码质量
- 使用flake8检查代码规范
- 使用mypy进行类型检查（可选）

## 🔧 开发环境

### 推荐工具
- **编辑器**: VS Code, PyCharm
- **Python版本**: 3.8+
- **包管理**: pip, poetry（可选）

### 环境设置
```bash
# 克隆项目
git clone https://github.com/lsq-web17/OpenClaw-Tutorial.git
cd OpenClaw-Tutorial

# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

# 安装依赖
pip install -r requirements.txt

# 安装开发依赖
pip install pytest flake8
```

## 📚 文档结构

### 项目文档
```
docs/
├── tutorials/       # 教程文档
├── api/            # API文档
├── guides/         # 指南文档
└── resources/      # 资源文档
```

### 代码文档
- 类和方法使用docstring
- 复杂逻辑添加注释
- 保持文档与代码同步

## 🏆 贡献者权益

### 认可贡献
- 贡献者将被列在README中
- 重要贡献者会成为项目维护者
- 建立贡献者荣誉墙

### 学习机会
- 学习OpenClaw开发技术
- 参与开源社区建设
- 获得技术指导和反馈

## 📞 寻求帮助

### 社区支持
- 在 [Discussions](https://github.com/lsq-web17/OpenClaw-Tutorial/discussions) 提问
- 加入相关技术社群
- 查看常见问题解答

### 技术指导
- 项目维护者提供技术支持
- 定期举办技术分享会
- 提供学习资源推荐

## 🤔 行为准则

### 基本准则
- 尊重他人，友好交流
- 乐于分享，互相帮助
- 遵守规则，维护秩序

### 沟通方式
- 使用清晰准确的语言
- 保持耐心和理解
- 提供建设性反馈

---

感谢您为OpenClaw教程项目做出贡献！🎉

如果您有任何问题或建议，请随时联系我们。

[📖 查看项目文档](docs/)
[🐛 报告问题](https://github.com/lsq-web17/OpenClaw-Tutorial/issues)
[💬 参与讨论](https://github.com/lsq-web17/OpenClaw-Tutorial/discussions)