#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
文件名: hello_skill_basic.py
描述: 基础版Hello World技能
课程: OpenClaw入门实战 - 第一章
作者: lsq-web17
日期: 2026-03-10
版本: v1.0.0

功能说明:
这是OpenClaw入门实战课程的第一个技能示例。
演示最基本的技能结构和消息处理机制。

学习目标:
1. 理解OpenClaw技能的基本结构
2. 掌握消息处理方法
3. 学会简单的条件判断
4. 掌握时间获取和格式化

使用示例:
>>> skill = HelloSkillBasic()
>>> response = skill.handle_message("hello")
>>> print(response)
👋 你好！我是你的OpenClaw助手！
"""

from datetime import datetime


class HelloSkillBasic:
    """基础版Hello World技能类"""
    
    def __init__(self):
        """初始化技能
        
        在这里设置技能的初始状态和配置。
        目前我们只设置了一个简单的问候语。
        """
        self.greeting = "👋 你好！我是你的OpenClaw助手！"
        print("✅ Hello World技能初始化完成！")
    
    def handle_message(self, message: str) -> str:
        """处理消息的核心函数
        
        这是技能最重要的方法，负责处理用户输入的消息。
        根据消息内容返回相应的响应。
        
        参数:
            message: 用户输入的消息文本
            
        返回:
            str: 技能返回的响应文本
        """
        # 1. 输入验证和清理
        if not message or not isinstance(message, str):
            return "⚠️ 请输入有效的消息文本"
        
        # 2. 转换为小写并去除首尾空格（标准化处理）
        msg = message.lower().strip()
        
        # 3. 问候类消息处理
        if any(word in msg for word in ['hello', '你好', 'hi', '嗨', '哈喽']):
            return self._get_greeting_response()
        
        # 4. 时间类消息处理
        if any(word in msg for word in ['time', '时间', '几点', '现在', '当前时间']):
            return self._get_time_response()
        
        # 5. 帮助类消息处理
        if any(word in msg for word in ['help', '帮助', '功能', '你能做什么']):
            return self._get_help_response()
        
        # 6. 默认回复（未知消息）
        return self._get_default_response()
    
    def _get_greeting_response(self) -> str:
        """获取问候响应
        
        返回格式化的问候语。
        """
        return self.greeting
    
    def _get_time_response(self) -> str:
        """获取时间响应
        
        返回当前时间的格式化字符串。
        学习重点：datetime模块的使用。
        """
        # 获取当前时间
        now = datetime.now()
        
        # 格式化时间字符串
        # %Y: 四位年份，%m: 两位月份，%d: 两位日期
        # %H: 24小时制小时，%M: 分钟，%S: 秒
        current_time = now.strftime('%Y-%m-%d %H:%M:%S')
        
        # 添加星期几
        weekdays = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
        weekday = weekdays[now.weekday()]
        
        return f"🕐 当前时间：{current_time} ({weekday})"
    
    def _get_help_response(self) -> str:
        """获取帮助响应
        
        返回技能的功能介绍和使用方法。
        """
        return '''📋 Hello World技能功能：

我能处理以下类型的消息：

1. 🎯 **问候类消息**
   - "hello"、"你好"、"hi"、"嗨"
   - 我会回复友好的问候

2. ⏰ **时间类消息**
   - "time"、"时间"、"几点"、"现在"
   - 我会告诉你当前的时间

3. ❓ **帮助类消息**
   - "help"、"帮助"、"功能"
   - 我会显示这个帮助信息

试试对我说点什么吧！'''
    
    def _get_default_response(self) -> str:
        """获取默认响应
        
        当消息无法识别时返回的响应。
        """
        return "🤔 抱歉，我不太明白。输入 'help' 查看我能做什么。"


def run_interactive_demo():
    """运行交互式演示
    
    在命令行中与技能进行交互测试。
    按Ctrl+C或输入'quit'、'退出'结束。
    """
    print("=" * 50)
    print("🤖 Hello World技能 - 交互演示")
    print("=" * 50)
    print("输入消息与我聊天（输入'quit'或'退出'结束）")
    print("提示：试试说'hello'、'时间'、'help'")
    print("-" * 50)
    
    # 创建技能实例
    skill = HelloSkillBasic()
    
    while True:
        try:
            # 获取用户输入
            message = input("💬 你: ").strip()
            
            # 检查退出条件
            if not message:
                print("📝 请输入消息")
                continue
            
            if message.lower() in ['quit', '退出', 'exit', 'q', 'bye', '再见']:
                print("👋 再见！感谢使用Hello World技能！")
                break
            
            # 处理消息并显示响应
            response = skill.handle_message(message)
            print(f"🤖 我: {response}")
            print("-" * 30)
            
        except KeyboardInterrupt:
            print("\n👋 再见！")
            break
        except Exception as e:
            print(f"❌ 发生错误: {e}")
            print("请重新输入...")
            continue


def run_test_cases():
    """运行测试用例
    
    自动运行一组预定义的测试用例，验证技能功能。
    """
    print("🧪 运行测试用例...")
    print("-" * 40)
    
    skill = HelloSkillBasic()
    
    # 定义测试用例
    test_cases = [
        ("hello", "问候测试"),
        ("你好", "中文问候测试"),
        ("time", "时间查询测试"),
        ("现在几点了？", "中文时间查询测试"),
        ("help", "帮助测试"),
        ("unknown", "未知消息测试"),
        ("", "空消息测试"),
    ]
    
    # 运行测试
    passed = 0
    total = len(test_cases)
    
    for message, description in test_cases:
        try:
            response = skill.handle_message(message)
            print(f"✅ {description}:")
            print(f"   输入: '{message}'")
            print(f"   输出: '{response}'")
            passed += 1
        except Exception as e:
            print(f"❌ {description} 失败: {e}")
        
        print("-" * 30)
    
    # 显示测试结果
    print(f"📊 测试结果: {passed}/{total} 通过")
    if passed == total:
        print("🎉 所有测试用例通过！")
    else:
        print("⚠️  部分测试用例失败，请检查代码。")


if __name__ == "__main__":
    """主函数
    
    根据命令行参数选择运行模式：
    - 无参数: 运行交互演示
    - --test: 运行测试用例
    - --help: 显示帮助信息
    """
    import sys
    
    if len(sys.argv) > 1:
        if sys.argv[1] == "--test":
            run_test_cases()
        elif sys.argv[1] == "--help":
            print("使用方法:")
            print("  python hello_skill_basic.py          # 交互演示")
            print("  python hello_skill_basic.py --test   # 运行测试")
            print("  python hello_skill_basic.py --help   # 显示帮助")
        else:
            # 直接处理单个消息
            skill = HelloSkillBasic()
            response = skill.handle_message(" ".join(sys.argv[1:]))
            print(response)
    else:
        # 默认运行交互演示
        run_interactive_demo()