#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Hello World技能测试
测试技能的各种功能
"""

import unittest
import sys
import os
from datetime import datetime

# 添加当前目录到Python路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from hello_skill import HelloSkill


class TestHelloSkill(unittest.TestCase):
    """测试Hello World技能"""
    
    def setUp(self):
        """测试前准备"""
        self.skill = HelloSkill()
    
    def test_greeting(self):
        """测试问候功能"""
        # 测试英文问候
        response = self.skill.handle_message("hello")
        self.assertIn("你好", response)
        self.assertIn("当前时间", response)
        
        # 测试中文问候
        response = self.skill.handle_message("你好")
        self.assertIn("你好", response)
        
        # 测试其他问候
        response = self.skill.handle_message("hi")
        self.assertIn("你好", response)
        
        response = self.skill.handle_message("嗨")
        self.assertIn("你好", response)
    
    def test_time_query(self):
        """测试时间查询功能"""
        # 测试英文时间查询
        response = self.skill.handle_message("time")
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M")
        # 检查是否包含当前时间（忽略秒）
        self.assertIn(current_time, response)
        
        # 测试中文时间查询
        response = self.skill.handle_message("时间")
        self.assertIn("当前时间", response)
        
        # 测试其他时间查询
        response = self.skill.handle_message("现在几点")
        self.assertIn("当前时间", response)
        
        response = self.skill.handle_message("当前时间")
        self.assertIn("当前时间", response)
    
    def test_help(self):
        """测试帮助功能"""
        response = self.skill.handle_message("help")
        self.assertIn("我能做", response)
        self.assertIn("问候回复", response)
        self.assertIn("时间查询", response)
        self.assertIn("历史记录", response)
        
        # 测试中文帮助
        response = self.skill.handle_message("帮助")
        self.assertIn("我能做", response)
        
        # 测试其他帮助查询
        response = self.skill.handle_message("功能")
        self.assertIn("我能做", response)
        
        response = self.skill.handle_message("你能做什么")
        self.assertIn("我能做", response)
    
    def test_history(self):
        """测试历史记录功能"""
        # 先进行一些对话
        self.skill.handle_message("hello")
        self.skill.handle_message("time")
        self.skill.handle_message("help")
        
        # 测试历史记录查询
        response = self.skill.handle_message("history")
        self.assertIn("最近5条对话记录", response)
        self.assertIn("hello", response)
        self.assertIn("time", response)
        self.assertIn("help", response)
        
        # 测试中文历史记录查询
        response = self.skill.handle_message("历史")
        self.assertIn("最近5条对话记录", response)
    
    def test_info(self):
        """测试技能信息功能"""
        response = self.skill.handle_message("info")
        self.assertIn("Hello World 技能", response)
        self.assertIn("版本", response)
        self.assertIn("作者", response)
        self.assertIn("功能", response)
        
        # 测试中文信息查询
        response = self.skill.handle_message("信息")
        self.assertIn("Hello World 技能", response)
        
        response = self.skill.handle_message("关于")
        self.assertIn("Hello World 技能", response)
    
    def test_ping(self):
        """测试Ping功能"""
        response = self.skill.handle_message("ping")
        self.assertEqual("🏓 pong! 服务正常运行", response)
        
        response = self.skill.handle_message("测试")
        self.assertEqual("🏓 pong! 服务正常运行", response)
        
        response = self.skill.handle_message("状态")
        self.assertEqual("🏓 pong! 服务正常运行", response)
    
    def test_thanks(self):
        """测试感谢功能"""
        response = self.skill.handle_message("谢谢")
        self.assertIn("不客气", response)
        
        response = self.skill.handle_message("感谢")
        self.assertIn("不客气", response)
        
        response = self.skill.handle_message("thanks")
        self.assertIn("不客气", response)
        
        response = self.skill.handle_message("thank you")
        self.assertIn("不客气", response)
    
    def test_goodbye(self):
        """测试告别功能"""
        response = self.skill.handle_message("bye")
        self.assertIn("再见", response)
        
        response = self.skill.handle_message("再见")
        self.assertIn("再见", response)
        
        response = self.skill.handle_message("拜拜")
        self.assertIn("再见", response)
        
        response = self.skill.handle_message("goodbye")
        self.assertIn("再见", response)
    
    def test_unknown_message(self):
        """测试未知消息处理"""
        response = self.skill.handle_message("随便说点什么")
        self.assertIn("抱歉", response)
        self.assertIn("不明白", response)
        
        response = self.skill.handle_message("abcdefg")
        self.assertIn("抱歉", response)
        
        response = self.skill.handle_message("123456")
        self.assertIn("抱歉", response)
    
    def test_config_loading(self):
        """测试配置加载"""
        # 创建测试配置文件
        test_config = {
            'greeting': '🎉 欢迎！',
            'time_format': '%H:%M',
            'enable_history': False
        }
        
        import tempfile
        import json
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            json.dump(test_config, f)
            config_file = f.name
        
        try:
            # 使用自定义配置创建技能
            skill = HelloSkill(config_file)
            
            # 测试配置生效
            response = skill.handle_message("hello")
            self.assertIn("🎉 欢迎！", response)
            
            # 测试时间格式
            response = skill.handle_message("time")
            current_time = datetime.now().strftime("%H:%M")
            self.assertIn(current_time, response)
            
            # 测试历史记录是否禁用
            skill.handle_message("test")
            self.assertEqual(len(skill.history), 0)
            
        finally:
            # 清理临时文件
            os.unlink(config_file)
    
    def test_history_management(self):
        """测试历史记录管理"""
        # 清空历史记录
        self.skill.history = []
        
        # 添加对话记录
        for i in range(15):
            self.skill.handle_message(f"test {i}")
        
        # 检查历史记录长度限制（默认10条）
        self.assertEqual(len(self.skill.history), 10)
        
        # 检查最近的消息存在
        recent_messages = [item['message'] for item in self.skill.history]
        self.assertIn("test 14", recent_messages)
        self.assertIn("test 5", recent_messages)
        # 早期的消息应该被移除
        self.assertNotIn("test 0", recent_messages)
        self.assertNotIn("test 4", recent_messages)
    
    def test_get_history_method(self):
        """测试获取历史记录方法"""
        # 清空历史记录
        self.skill.history = []
        
        # 添加一些对话
        for i in range(8):
            self.skill.handle_message(f"message {i}")
        
        # 测试获取全部历史记录
        all_history = self.skill.get_history()
        self.assertEqual(len(all_history), 8)
        
        # 测试获取部分历史记录
        limited_history = self.skill.get_history(3)
        self.assertEqual(len(limited_history), 3)
        
        # 检查获取的是最近的消息
        recent_messages = [item['message'] for item in limited_history]
        self.assertIn("message 7", recent_messages)
        self.assertIn("message 6", recent_messages)
        self.assertIn("message 5", recent_messages)
        self.assertNotIn("message 0", recent_messages)
    
    def test_random_responses(self):
        """测试随机回复功能"""
        # 测试多次问候，应该有不同的回复（因为有随机选择）
        responses = set()
        for _ in range(10):
            response = self.skill.handle_message("hello")
            responses.add(response)
        
        # 由于有随机性，可能会有不同的回复
        # 至少应该有一个回复
        self.assertGreater(len(responses), 0)
    
    def test_case_insensitive(self):
        """测试大小写不敏感"""
        # 测试大写
        response1 = self.skill.handle_message("HELLO")
        response2 = self.skill.handle_message("hello")
        self.assertIn("你好", response1)
        self.assertIn("你好", response2)
        
        # 测试混合大小写
        response3 = self.skill.handle_message("HeLlO")
        self.assertIn("你好", response3)
        
        # 测试中文（大小写不影响）
        response4 = self.skill.handle_message("你好")
        response5 = self.skill.handle_message("你 好")  # 有空格
        self.assertIn("你好", response4)
        self.assertIn("你好", response5)


class TestCommandLineInterface(unittest.TestCase):
    """测试命令行接口"""
    
    def test_direct_message(self):
        """测试直接传递消息"""
        import subprocess
        
        # 测试问候消息
        result = subprocess.run(
            [sys.executable, 'hello_skill.py', 'hello'],
            capture_output=True,
            text=True,
            cwd=os.path.dirname(os.path.abspath(__file__))
        )
        self.assertIn("你好", result.stdout)
        self.assertEqual(result.returncode, 0)
        
        # 测试时间查询
        result = subprocess.run(
            [sys.executable, 'hello_skill.py', 'time'],
            capture_output=True,
            text=True,
            cwd=os.path.dirname(os.path.abspath(__file__))
        )
        self.assertIn("当前时间", result.stdout)
        self.assertEqual(result.returncode, 0)
    
    def test_no_arguments(self):
        """测试无参数运行"""
        import subprocess
        
        result = subprocess.run(
            [sys.executable, 'hello_skill.py'],
            capture_output=True,
            text=True,
            cwd=os.path.dirname(os.path.abspath(__file__))
        )
        # 应该显示帮助信息
        self.assertIn("我能做", result.stdout)
        self.assertEqual(result.returncode, 0)
    
    def test_info_argument(self):
        """测试--info参数"""
        import subprocess
        
        result = subprocess.run(
            [sys.executable, 'hello_skill.py', '--info'],
            capture_output=True,
            text=True,
            cwd=os.path.dirname(os.path.abspath(__file__))
        )
        self.assertIn("Hello World 技能", result.stdout)
        self.assertEqual(result.returncode, 0)
    
    def test_history_argument(self):
        """测试--history参数"""
        import subprocess
        
        result = subprocess.run(
            [sys.executable, 'hello_skill.py', '--history'],
            capture_output=True,
            text=True,
            cwd=os.path.dirname(os.path.abspath(__file__))
        )
        # 可能显示"还没有对话记录"或历史记录
        self.assertIn("最近5条对话记录", result.stdout)
        self.assertEqual(result.returncode, 0)


def run_tests():
    """运行所有测试"""
    # 创建测试套件
    suite = unittest.TestSuite()
    
    # 添加测试类
    suite.addTest(unittest.makeSuite(TestHelloSkill))
    suite.addTest(unittest.makeSuite(TestCommandLineInterface))
    
    # 运行测试
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # 返回测试结果
    return result.wasSuccessful()


if __name__ == '__main__':
    # 运行测试
    success = run_tests()
    
    # 退出代码
    sys.exit(0 if success else 1)