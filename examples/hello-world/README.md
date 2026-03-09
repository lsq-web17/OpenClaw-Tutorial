# 👋 Hello World 技能示例

> 最简单的OpenClaw技能示例，适合初学者入门

## 📋 项目简介

这是一个最简单的OpenClaw技能示例，展示了如何创建一个基本的技能，并响应简单的消息。

## 🛠️ 文件结构

```
hello-world/
├── hello_skill.py      # 主技能文件
├── SKILL.md           # 技能说明文档
├── requirements.txt   # Python依赖
├── test_hello.py      # 测试脚本
└── README.md          # 项目说明
```

## 🚀 快速开始

### 1. 安装依赖
```bash
# 进入项目目录
cd hello-world

# 创建虚拟环境（可选）
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate   # Windows

# 安装依赖
pip install -r requirements.txt
```

### 2. 运行技能
```bash
# 直接运行
python hello_skill.py "你好"

# 或者交互式运行
python hello_skill.py
# 然后输入消息
```

### 3. 测试技能
```bash
# 运行测试
python test_hello.py
```

## 📖 技能功能

### 支持的消息
- **问候类**：`hello`、`你好`、`hi`、`嗨`
- **时间类**：`time`、`时间`、`现在几点`、`当前时间`
- **帮助类**：`help`、`帮助`、`功能`、`你能做什么`
- **其他**：`ping`、`测试`、`echo`、`重复`

### 响应示例
```
输入：你好
输出：👋 你好！当前时间是 2026-03-10 00:40:00

输入：现在几点
输出：🕐 当前时间：2026-03-10 00:40:05

输入：help
输出：📋 我能做：
      • 问候回复
      • 时间查询
      • 简单对话
      输入"hello"或"时间"试试看！

输入：ping
输出：🏓 pong! 服务正常
```

## 🔧 代码解析

### 主技能文件：`hello_skill.py`

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime
import sys

def handle_message(message):
    """处理消息的核心函数"""
    # 转换为小写方便匹配
    msg = message.lower().strip()
    
    # 问候类消息
    if any(word in msg for word in ['hello', '你好', 'hi', '嗨']):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f"👋 你好！当前时间是 {current_time}"
    
    # 时间类消息
    if any(word in msg for word in ['time', '时间', '几点', '现在']):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f"🕐 当前时间：{current_time}"
    
    # 帮助类消息
    if any(word in msg for word in ['help', '帮助', '功能', '你能做什么']):
        return '''📋 我能做：
• 问候回复 - 说"hello"或"你好"
• 时间查询 - 说"time"或"时间"
• 简单对话 - 说"ping"或"测试"
输入"hello"或"时间"试试看！'''
    
    # Ping测试
    if any(word in msg for word in ['ping', '测试', 'echo']):
        return "🏓 pong! 服务正常"
    
    # 默认回复
    return "🤔 抱歉，我不明白您的意思。输入'help'查看我能做什么。"

if __name__ == "__main__":
    # 从命令行参数获取消息
    if len(sys.argv) > 1:
        message = ' '.join(sys.argv[1:])
        response = handle_message(message)
        print(response)
    else:
        # 交互模式
        print("💬 Hello World 技能已启动！")
        print("输入消息（输入'quit'或'退出'结束）：")
        
        while True:
            try:
                message = input("> ").strip()
                
                if message.lower() in ['quit', '退出', 'exit', 'q']:
                    print("👋 再见！")
                    break
                
                if message:
                    response = handle_message(message)
                    print(f"🤖 {response}")
                else:
                    print("📝 请输入消息")
                    
            except KeyboardInterrupt:
                print("\n👋 再见！")
                break
            except EOFError:
                print("\n👋 再见！")
                break
```

### 测试文件：`test_hello.py`

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from datetime import datetime
from hello_skill import handle_message

class TestHelloSkill(unittest.TestCase):
    """测试Hello World技能"""
    
    def test_greeting(self):
        """测试问候功能"""
        response = handle_message("hello")
        self.assertIn("你好", response)
        self.assertIn("当前时间", response)
        
        response = handle_message("你好")
        self.assertIn("你好", response)
    
    def test_time(self):
        """测试时间功能"""
        response = handle_message("time")
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.assertIn(current_time[:13], response)  # 检查日期和时间
        
        response = handle_message("现在几点")
        self.assertIn("当前时间", response)
    
    def test_help(self):
        """测试帮助功能"""
        response = handle_message("help")
        self.assertIn("我能做", response)
        self.assertIn("问候回复", response)
        self.assertIn("时间查询", response)
    
    def test_ping(self):
        """测试Ping功能"""
        response = handle_message("ping")
        self.assertEqual("🏓 pong! 服务正常", response)
        
        response = handle_message("测试")
        self.assertEqual("🏓 pong! 服务正常", response)
    
    def test_unknown(self):
        """测试未知消息"""
        response = handle_message("随便说点什么")
        self.assertIn("抱歉", response)
        self.assertIn("help", response)

if __name__ == '__main__':
    unittest.main()
```

## 📝 技能说明：`SKILL.md`

```markdown
# Hello World 技能

## 功能描述
这是一个最简单的OpenClaw技能示例，用于演示技能的基本结构和功能。

## 使用方法
1. 直接运行：`python hello_skill.py "消息"`
2. 交互模式：`python hello_skill.py`

## 支持的消息类型
- 问候：hello、你好、hi、嗨
- 时间查询：time、时间、现在几点
- 帮助：help、帮助、功能
- 测试：ping、测试、echo

## 扩展建议
1. 添加更多回复类型
2. 集成外部API（如天气、新闻）
3. 添加持久化存储
4. 支持多语言

## 技术要点
- 使用Python标准库
- 简单的消息匹配逻辑
- 清晰的代码结构
- 完整的测试覆盖
```

## 🎯 如何集成到OpenClaw

### 方法1：直接调用
```python
# 在其他Python代码中调用
from hello_skill import handle_message

response = handle_message("hello")
print(response)
```

### 方法2：作为OpenClaw技能
1. 将技能目录复制到OpenClaw工作空间的`skills/`目录
2. 在OpenClaw配置中启用技能
3. 通过OpenClaw接口调用

### 方法3：Web服务
```python
from flask import Flask, request, jsonify
from hello_skill import handle_message

app = Flask(__name__)

@app.route('/hello', methods=['POST'])
def hello_api():
    data = request.json
    message = data.get('message', '')
    response = handle_message(message)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(port=5000)
```

## 🔄 扩展开发

### 添加新功能
```python
def handle_message(message):
    # 现有代码...
    
    # 添加天气查询
    if '天气' in message or 'weather' in message.lower():
        return "🌤️ 天气功能开发中..."
    
    # 添加笑话功能
    if '笑话' in message or 'joke' in message.lower():
        jokes = [
            "为什么程序员喜欢黑暗？因为光吸引bug！",
            "程序员最讨厌的单词：undefined",
            "如果生活给了你柠檬，就写一个算法来优化柠檬汁生产！"
        ]
        import random
        return random.choice(jokes)
    
    # 现有代码...
```

### 添加配置支持
```python
import json
import os

class HelloSkill:
    def __init__(self, config_file='config.json'):
        self.config = self.load_config(config_file)
        
    def load_config(self, config_file):
        if os.path.exists(config_file):
            with open(config_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {
            'greeting': '👋 你好！',
            'time_format': '%Y-%m-%d %H:%M:%S',
            'enable_jokes': True
        }
    
    def handle_message(self, message):
        # 使用配置
        msg = message.lower().strip()
        
        if 'hello' in msg:
            current_time = datetime.now().strftime(self.config['time_format'])
            return f"{self.config['greeting']} 当前时间是 {current_time}"
        
        # 其他处理...
```

## 📊 性能优化

### 1. 缓存时间
```python
from datetime import datetime, timedelta

class HelloSkill:
    def __init__(self):
        self.last_time_update = None
        self.cached_time = None
        self.cache_duration = timedelta(seconds=1)
    
    def get_current_time(self):
        now = datetime.now()
        if (self.last_time_update is None or 
            now - self.last_time_update > self.cache_duration):
            self.cached_time = now.strftime("%Y-%m-%d %H:%M:%S")
            self.last_time_update = now
        return self.cached_time
```

### 2. 预编译正则表达式
```python
import re

class HelloSkill:
    def __init__(self):
        self.patterns = {
            'greeting': re.compile(r'(hello|你好|hi|嗨)', re.IGNORECASE),
            'time': re.compile(r'(time|时间|几点|现在)', re.IGNORECASE),
            'help': re.compile(r'(help|帮助|功能|你能做什么)', re.IGNORECASE),
            'ping': re.compile(r'(ping|测试|echo)', re.IGNORECASE)
        }
    
    def handle_message(self, message):
        if self.patterns['greeting'].search(message):
            # 处理问候...
```

## 🧪 测试覆盖率

运行测试：
```bash
# 运行所有测试
python -m pytest test_hello.py -v

# 生成测试覆盖率报告
python -m pytest test_hello.py --cov=hello_skill --cov-report=html

# 查看覆盖率
open htmlcov/index.html  # macOS
start htmlcov/index.html # Windows
```

## 📚 学习资源

- [OpenClaw官方文档](https://docs.openclaw.ai)
- [Python官方教程](https://docs.python.org/3/tutorial/)
- [单元测试指南](https://docs.python.org/3/library/unittest.html)
- [正则表达式教程](https://docs.python.org/3/library/re.html)

## 🤝 贡献指南

1. Fork本仓库
2. 创建功能分支
3. 提交更改
4. 推送到分支
5. 创建Pull Request

## 📄 许可证

MIT License - 详见 [LICENSE](../LICENSE) 文件

---

**祝您学习愉快！如果有任何问题，欢迎在GitHub Issues中提出。**