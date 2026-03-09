# 📦 OpenClaw环境准备与安装部署

> 本文是OpenClaw实战教程系列的第一篇，将带您从零开始完成OpenClaw的安装和基础配置。

## 📋 系统要求

### 最低配置
- **操作系统**: Ubuntu 20.04+ / CentOS 8+ / macOS 12+
- **内存**: 4GB RAM
- **存储**: 10GB 可用空间
- **网络**: 稳定的互联网连接

### 推荐配置
- **操作系统**: Ubuntu 22.04 LTS
- **内存**: 8GB RAM 或以上
- **存储**: 20GB+ 可用空间
- **CPU**: 4核或以上

## 🔧 安装步骤

### 1. 系统依赖安装

#### Ubuntu/Debian系统
```bash
# 更新系统
sudo apt update
sudo apt upgrade -y

# 安装基础依赖
sudo apt install -y curl git wget python3 python3-pip python3-venv \
    build-essential libssl-dev libffi-dev python3-dev \
    nodejs npm yarn
```

#### CentOS/RHEL系统
```bash
# 更新系统
sudo yum update -y

# 安装基础依赖
sudo yum install -y curl git wget python3 python3-pip python3-devel \
    gcc-c++ make openssl-devel libffi-devel \
    nodejs npm
```

#### macOS系统
```bash
# 安装Homebrew（如果未安装）
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# 安装依赖
brew install python3 node git curl wget
```

### 2. 安装OpenClaw

#### 方法一：官方安装脚本（推荐）
```bash
# 下载安装脚本
curl -fsSL https://openclaw.ai/install.sh -o install-openclaw.sh

# 执行安装
chmod +x install-openclaw.sh
sudo ./install-openclaw.sh

# 或者一行命令
curl -fsSL https://openclaw.ai/install.sh | sudo bash
```

#### 方法二：npm安装
```bash
# 使用npm全局安装
sudo npm install -g openclaw

# 或者使用yarn
sudo yarn global add openclaw
```

#### 方法三：源码编译安装
```bash
# 克隆源码
git clone https://github.com/openclaw/openclaw.git
cd openclaw

# 安装依赖
npm install

# 构建
npm run build

# 链接到全局
sudo npm link
```

### 3. 验证安装

```bash
# 查看版本
openclaw --version

# 查看帮助
openclaw --help

# 检查状态
openclaw status
```

正常输出应该类似：
```
OpenClaw v1.0.0
Node.js v18.20.0
Platform: linux/x64
Gateway: running
```

### 4. 初始化配置

```bash
# 创建工作空间目录
mkdir -p ~/.openclaw/workspace
cd ~/.openclaw/workspace

# 初始化配置文件
openclaw init

# 或者手动创建配置文件
cat > ~/.openclaw/config.json << EOF
{
  "workspace": "~/.openclaw/workspace",
  "logs": "~/.openclaw/logs",
  "plugins": {
    "feishu": {
      "enabled": true
    },
    "telegram": {
      "enabled": false
    }
  },
  "model": "ark/deepseek-v3.2"
}
EOF
```

## 🛠️ 基础配置

### 1. 配置环境变量

```bash
# 编辑bash配置文件
nano ~/.bashrc
# 或
nano ~/.zshrc
```

添加以下内容：
```bash
# OpenClaw环境变量
export OPENCLAW_HOME="$HOME/.openclaw"
export PATH="$OPENCLAW_HOME/bin:$PATH"
export NODE_PATH="$(npm root -g)"
```

应用配置：
```bash
source ~/.bashrc
# 或
source ~/.zshrc
```

### 2. 创建第一个技能

```bash
# 进入工作空间
cd ~/.openclaw/workspace

# 创建技能目录
mkdir -p my-first-skill
cd my-first-skill

# 创建技能配置文件
cat > SKILL.md << EOF
# 我的第一个技能

这是一个简单的Hello World技能。

## 功能
- 响应问候语
- 返回当前时间

## 使用方法
当用户说"hello"或"你好"时，返回问候信息。
EOF

# 创建Python实现
cat > hello_skill.py << 'EOF'
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime
import sys

def handle_message(message):
    """处理消息"""
    if 'hello' in message.lower() or '你好' in message:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f"👋 你好！当前时间是 {current_time}"
    
    if 'time' in message.lower() or '时间' in message:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f"🕐 当前时间：{current_time}"
    
    return "🤔 抱歉，我不明白您的意思"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        message = sys.argv[1]
        response = handle_message(message)
        print(response)
    else:
        print("📝 请输入消息")
EOF

# 设置执行权限
chmod +x hello_skill.py
```

### 3. 测试技能

```bash
# 直接运行测试
python3 hello_skill.py "hello"

# 应该输出类似：
# 👋 你好！当前时间是 2026-03-10 00:35:00
```

## 🐳 Docker安装（可选）

如果您熟悉Docker，可以使用容器化部署：

```bash
# 拉取官方镜像
docker pull openclaw/openclaw:latest

# 运行容器
docker run -d \
  --name openclaw \
  -p 3000:3000 \
  -v ~/.openclaw/workspace:/workspace \
  -v ~/.openclaw/config:/config \
  openclaw/openclaw:latest

# 进入容器
docker exec -it openclaw bash

# 查看日志
docker logs openclaw
```

## 🔍 故障排除

### 常见问题1：安装脚本失败
```bash
# 检查网络连接
ping openclaw.ai

# 手动下载安装包
wget https://openclaw.ai/releases/openclaw-latest.tar.gz
tar -xzf openclaw-latest.tar.gz
cd openclaw-*
sudo ./install.sh
```

### 常见问题2：权限不足
```bash
# 使用sudo
sudo openclaw --version

# 或者修复权限
sudo chown -R $USER:$USER ~/.openclaw
sudo chmod -R 755 ~/.openclaw
```

### 常见问题3：Node.js版本过低
```bash
# 升级Node.js
# 使用nvm（推荐）
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
nvm install 18
nvm use 18

# 或使用apt
sudo apt install -y nodejs npm
sudo npm install -g n
sudo n stable
```

### 常见问题4：Python环境问题
```bash
# 创建虚拟环境
python3 -m venv venv
source venv/bin/activate

# 安装OpenClaw
pip install openclaw-python
```

## ✅ 验证安装成功

运行以下命令验证所有组件：
```bash
# 检查OpenClaw
openclaw --version

# 检查Node.js
node --version

# 检查Python
python3 --version
pip3 --version

# 检查git
git --version

# 检查npm
npm --version
```

所有命令都应正常返回版本信息。

## 🎯 下一步

成功安装OpenClaw后，您可以：

1. **学习基础配置** - 下一篇教程：[工作空间配置与管理](./02-workspace-config.md)
2. **创建第一个技能** - 尝试修改hello_skill.py添加更多功能
3. **探索插件** - 安装飞书、Telegram等插件
4. **加入社区** - 访问[OpenClaw官方社区](https://discord.com/invite/clawd)

## 📞 获取帮助

如果在安装过程中遇到问题：

1. **查看日志**：`cat ~/.openclaw/logs/install.log`
2. **官方文档**：[https://docs.openclaw.ai](https://docs.openclaw.ai)
3. **GitHub Issues**：[https://github.com/openclaw/openclaw/issues](https://github.com/openclaw/openclaw/issues)
4. **Discord社区**：[https://discord.com/invite/clawd](https://discord.com/invite/clawd)

---

**恭喜！您已成功完成OpenClaw的安装部署！🎉**

接下来，我们将深入探索OpenClaw的核心功能和实战应用。