#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Hello World 技能示例
最简单的OpenClaw技能，展示基本功能
"""

from datetime import datetime
import sys
import json
import os


class HelloSkill:
    """Hello World技能类"""
    
    def __init__(self, config_file=None):
        """初始化技能"""
        self.config = self._load_config(config_file)
        self.history = []
        
    def _load_config(self, config_file):
        """加载配置文件"""
        default_config = {
            'greeting': '👋 你好！',
            'time_format': '%Y-%m-%d %H:%M:%S',
            'enable_history': True,
            'max_history': 10,
            'responses': {
                'greeting': [
                    "你好！很高兴见到你！",
                    "嗨！今天过得怎么样？",
                    "Hello！有什么可以帮你的吗？"
                ],
                'time': [
                    "现在是 {time}",
                    "当前时间：{time}",
                    "🕐 {time}"
                ],
                'unknown': [
                    "🤔 抱歉，我不太明白。",
                    "😅 这个我还不会回答。",
                    "💡 试试说'hello'或'时间'？"
                ]
            }
        }
        
        if config_file and os.path.exists(config_file):
            try:
                with open(config_file, 'r', encoding='utf-8') as f:
                    user_config = json.load(f)
                    # 合并配置
                    default_config.update(user_config)
            except Exception as e:
                print(f"⚠️  配置文件加载失败: {e}")
        
        return default_config
    
    def get_current_time(self):
        """获取当前时间"""
        return datetime.now().strftime(self.config['time_format'])
    
    def get_random_response(self, response_type):
        """获取随机回复"""
        import random
        responses = self.config['responses'].get(response_type, [])
        if responses:
            return random.choice(responses)
        return ""
    
    def add_to_history(self, message, response):
        """添加到历史记录"""
        if self.config['enable_history']:
            self.history.append({
                'timestamp': self.get_current_time(),
                'message': message,
                'response': response
            })
            # 限制历史记录长度
            if len(self.history) > self.config['max_history']:
                self.history = self.history[-self.config['max_history']:]
    
    def get_history(self, limit=5):
        """获取历史记录"""
        return self.history[-limit:] if self.history else []
    
    def handle_message(self, message):
        """处理消息的核心函数"""
        # 转换为小写方便匹配
        msg = message.lower().strip()
        
        # 问候类消息
        if any(word in msg for word in ['hello', '你好', 'hi', '嗨', '哈喽']):
            current_time = self.get_current_time()
            greeting = self.get_random_response('greeting') or self.config['greeting']
            response = f"{greeting} 当前时间是 {current_time}"
            self.add_to_history(message, response)
            return response
        
        # 时间类消息
        if any(word in msg for word in ['time', '时间', '几点', '现在', '当前时间']):
            current_time = self.get_current_time()
            time_response = self.get_random_response('time') or "当前时间：{time}"
            response = time_response.format(time=current_time)
            self.add_to_history(message, response)
            return response
        
        # 帮助类消息
        if any(word in msg for word in ['help', '帮助', '功能', '你能做什么', '使用方法']):
            response = '''📋 我能做：
• 问候回复 - 说"hello"或"你好"
• 时间查询 - 说"time"或"时间"
• 历史记录 - 说"history"或"历史"
• 技能信息 - 说"info"或"信息"
• 简单对话 - 说"ping"或"测试"
输入"hello"或"时间"试试看！'''
            self.add_to_history(message, response)
            return response
        
        # 历史记录查询
        if any(word in msg for word in ['history', '历史', '记录', '对话历史']):
            history = self.get_history(5)
            if history:
                response = "📜 最近5条对话记录：\n"
                for i, item in enumerate(history, 1):
                    response += f"{i}. [{item['timestamp']}] {item['message']} → {item['response'][:30]}...\n"
            else:
                response = "📭 还没有对话记录"
            self.add_to_history(message, response)
            return response
        
        # 技能信息
        if any(word in msg for word in ['info', '信息', '关于', 'about', '版本']):
            response = f"""🤖 Hello World 技能
版本: 1.0.0
作者: OpenClaw Tutorial
功能: 基础对话、时间查询、历史记录
配置: {len(json.dumps(self.config, ensure_ascii=False))} 字符
历史记录: {len(self.history)} 条"""
            self.add_to_history(message, response)
            return response
        
        # Ping测试
        if any(word in msg for word in ['ping', '测试', 'echo', 'pong', '状态']):
            response = "🏓 pong! 服务正常运行"
            self.add_to_history(message, response)
            return response
        
        # 感谢类消息
        if any(word in msg for word in ['谢谢', '感谢', 'thanks', 'thank you']):
            response = "😊 不客气！很高兴能帮到你！"
            self.add_to_history(message, response)
            return response
        
        # 再见类消息
        if any(word in msg for word in ['bye', '再见', '拜拜', 'goodbye', '退出']):
            response = "👋 再见！期待下次聊天！"
            self.add_to_history(message, response)
            return response
        
        # 默认回复
        unknown_response = self.get_random_response('unknown') or "🤔 抱歉，我不明白您的意思。输入'help'查看我能做什么。"
        response = unknown_response
        self.add_to_history(message, response)
        return response
    
    def run_interactive(self):
        """运行交互模式"""
        print("=" * 50)
        print("🤖 Hello World 技能 - 交互模式")
        print("=" * 50)
        print("输入消息与我聊天（输入'quit'或'退出'结束）")
        print("提示：试试说'hello'、'时间'、'help'、'history'")
        print("-" * 50)
        
        while True:
            try:
                message = input("💬 你: ").strip()
                
                if not message:
                    print("📝 请输入消息")
                    continue
                
                if message.lower() in ['quit', '退出', 'exit', 'q', 'bye', '再见']:
                    print("👋 再见！")
                    break
                
                # 处理消息
                response = self.handle_message(message)
                print(f"🤖 我: {response}")
                print("-" * 30)
                
            except KeyboardInterrupt:
                print("\n👋 再见！")
                break
            except EOFError:
                print("\n👋 再见！")
                break
            except Exception as e:
                print(f"❌ 错误: {e}")
                continue


def main():
    """主函数"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Hello World OpenClaw技能')
    parser.add_argument('message', nargs='*', help='要处理的消息')
    parser.add_argument('--config', '-c', help='配置文件路径')
    parser.add_argument('--interactive', '-i', action='store_true', help='交互模式')
    parser.add_argument('--history', action='store_true', help='显示历史记录')
    parser.add_argument('--info', action='store_true', help='显示技能信息')
    
    args = parser.parse_args()
    
    # 创建技能实例
    skill = HelloSkill(args.config)
    
    # 处理参数
    if args.info:
        print(skill.handle_message("info"))
        return
    
    if args.history:
        print(skill.handle_message("history"))
        return
    
    if args.interactive:
        skill.run_interactive()
        return
    
    # 处理消息
    if args.message:
        message = ' '.join(args.message)
        response = skill.handle_message(message)
        print(response)
    else:
        # 默认显示帮助
        print(skill.handle_message("help"))


if __name__ == "__main__":
    main()