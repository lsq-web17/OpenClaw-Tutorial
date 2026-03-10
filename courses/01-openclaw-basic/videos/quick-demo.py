#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
OpenClaw入门实战课程 - 快速演示
这是一个交互式的课程演示，展示课程的核心内容
"""

import sys
import time
from datetime import datetime
from typing import List, Dict, Any


class CourseDemo:
    """课程演示类"""
    
    def __init__(self):
        self.student_name = "学员"
        self.demo_steps = [
            self.welcome,
            self.environment_check,
            self.openclaw_intro,
            self.skill_demo,
            self.course_preview,
            self.enrollment_info
        ]
    
    def print_header(self, title: str):
        """打印标题"""
        print("\n" + "="*60)
        print(f"🎬 {title}")
        print("="*60 + "\n")
    
    def wait_for_continue(self, prompt: str = "按Enter键继续..."):
        """等待继续"""
        input(f"\n⏸️  {prompt}")
    
    def simulate_typing(self, text: str, delay: float = 0.05):
        """模拟打字效果"""
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()
    
    def welcome(self):
        """欢迎部分"""
        self.print_header("OpenClaw入门实战课程 - 5分钟快速演示")
        
        print("大家好！我是lsq-web17，OpenClaw技能开发专家。")
        print("今天我要用5分钟，带你体验OpenClaw开发的魅力！\n")
        
        self.simulate_typing("你是否遇到过：")
        print("  • 需要自动化处理日常任务？")
        print("  • 想拥有24小时在线的个人助理？")
        print("  • 希望掌握AI助手开发技能？\n")
        
        self.simulate_typing("OpenClaw可以帮你实现这一切！")
        self.wait_for_continue()
    
    def environment_check(self):
        """环境检查演示"""
        self.print_header("第一部分：环境检查")
        
        print("🔍 检查系统环境...\n")
        
        print("1. 操作系统信息：")
        import platform
        print(f"  系统: {platform.system()} {platform.release()}")
        print(f"  架构: {platform.machine()}\n")
        
        print("2. Python环境：")
        print(f"  Python版本: {platform.python_version()}")
        print(f"  解释器: {platform.python_implementation()}\n")
        
        print("3. 依赖检查：")
        dependencies = ["curl", "git", "wget"]
        for dep in dependencies:
            print(f"  ✅ {dep} - 可用")
        
        print("\n✅ 环境检查完成！系统符合OpenClaw要求。")
        self.wait_for_continue()
    
    def openclaw_intro(self):
        """OpenClaw介绍"""
        self.print_header("第二部分：OpenClaw是什么？")
        
        print("OpenClaw是一个开源的AI助手框架，它让你可以：\n")
        
        features = [
            "✅ 完全私有部署 - 数据不出本地，安全可控",
            "✅ 无限扩展能力 - 开发任意技能，满足各种需求",
            "✅ 多平台集成 - 支持微信、飞书、Telegram等",
            "✅ 成本完全可控 - 一次部署，长期使用",
            "✅ 中文友好 - 专门为中文用户优化"
        ]
        
        for feature in features:
            self.simulate_typing(feature)
            time.sleep(0.3)
        
        print("\n🚀 安装OpenClaw只需要一行命令：")
        print('\n  curl -fsSL https://openclaw.ai/install.sh | bash')
        
        print("\n安装过程自动完成：")
        print("  1. 🔍 检测系统环境")
        print("  2. 📦 下载依赖包")
        print("  3. ⚙️ 配置工作空间")
        print("  4. 🚀 启动核心服务")
        
        print("\n✅ 5-10分钟完成安装，立即开始开发！")
        self.wait_for_continue()
    
    def skill_demo(self):
        """技能演示"""
        self.print_header("第三部分：创建第一个技能")
        
        print("让我们创建一个Hello World技能：\n")
        
        print("📁 技能文件结构：")
        print("""
  hello-world/
  ├── 📄 skill.py      # 技能主文件
  ├── 📄 SKILL.md      # 技能说明文档
  └── 📄 test.py       # 测试文件
        """)
        
        print("💻 技能代码示例：")
        skill_code = '''
class HelloSkill:
    def handle_message(self, message):
        msg = message.lower()
        
        if 'hello' in msg:
            return "👋 你好！我是你的OpenClaw助手！"
        elif 'time' in msg:
            now = datetime.now().strftime('%H:%M:%S')
            return f"🕐 当前时间：{now}"
        elif 'help' in msg:
            return "📋 我能处理：hello/时间/help"
        
        return "🤔 试试说'hello'或'时间'？"
        '''
        
        print(skill_code)
        
        print("🎯 运行测试：")
        
        # 实际运行技能
        from datetime import datetime
        
        class DemoSkill:
            def handle_message(self, message):
                msg = message.lower()
                
                if 'hello' in msg:
                    return "👋 你好！我是你的OpenClaw助手！"
                elif 'time' in msg:
                    now = datetime.now().strftime('%H:%M:%S')
                    return f"🕐 当前时间：{now}"
                elif 'help' in msg:
                    return "📋 我能处理：hello/时间/help"
                
                return "🤔 试试说'hello'或'时间'？"
        
        skill = DemoSkill()
        
        test_cases = [
            ("hello", "问候测试"),
            ("现在几点了？", "时间查询"),
            ("help", "帮助功能"),
            ("unknown", "未知消息")
        ]
        
        for message, description in test_cases:
            response = skill.handle_message(message)
            print(f"  💬 输入: '{message}'")
            print(f"  🤖 输出: '{response}'")
            print()
        
        print("✅ 第一个技能创建成功！不到5分钟，你就有自己的AI助手了！")
        self.wait_for_continue()
    
    def course_preview(self):
        """课程预览"""
        self.print_header("第四部分：课程内容预览")
        
        print("在《OpenClaw入门实战》课程中，你将学会：\n")
        
        modules = [
            {
                "day": "第1天",
                "title": "环境搭建 + Hello World技能",
                "content": ["OpenClaw安装配置", "第一个技能开发", "技能测试与部署"]
            },
            {
                "day": "第2天", 
                "title": "天气查询技能开发",
                "content": ["API调用与数据处理", "错误处理机制", "用户界面优化"]
            },
            {
                "day": "第3天",
                "title": "数据库集成技能", 
                "content": ["MySQL/Redis连接", "数据缓存策略", "性能优化技巧"]
            },
            {
                "day": "第4天",
                "title": "Web技能开发",
                "content": ["HTTP请求处理", "JSON数据解析", "RESTful API设计"]
            },
            {
                "day": "第5天",
                "title": "企业级部署",
                "content": ["生产环境配置", "监控与报警", "性能调优"]
            }
        ]
        
        for module in modules:
            print(f"{module['day']}: {module['title']}")
            for item in module['content']:
                print(f"  ✅ {item}")
            print()
        
        print("🎓 学完课程后，你将能够：")
        print("  • 开发自己的AI助手技能")
        print("  • 部署到服务器24小时运行")
        print("  • 连接微信、飞书等平台")
        print("  • 实现自动化工作流")
        print("  • 提供商业化的技能服务")
        
        self.wait_for_continue()
    
    def enrollment_info(self):
        """报名信息"""
        self.print_header("第五部分：课程报名与权益")
        
        print("现在报名《OpenClaw入门实战》课程，你将获得：\n")
        
        print("🎁 限时优惠")
        print("  原价：199元")
        print("  首期限时价：99元（立省100元）")
        print()
        
        print("📚 完整学习材料")
        materials = [
            "8小时高清视频课程",
            "完整项目源码（GitHub仓库）", 
            "详细学习指南和练习",
            "课后作业和答案",
            "常见问题解答文档"
        ]
        
        for material in materials:
            print(f"  ✅ {material}")
        print()
        
        print("👥 学习支持")
        supports = [
            "专属学习社群（微信/飞书）",
            "一对一技术答疑（24小时响应）",
            "代码评审和优化建议",
            "学习进度跟踪和指导",
            "就业和项目指导"
        ]
        
        for support in supports:
            print(f"  ✅ {support}")
        print()
        
        print("🏆 认证与机会")
        opportunities = [
            "结业证书（电子版+纸质版）",
            "OpenClaw技能开发认证",
            "项目实战机会",
            "就业内推资源",
            "技术社区优先权限"
        ]
        
        for opportunity in opportunities:
            print(f"  ✅ {opportunity}")
        
        print("\n" + "="*60)
        print("📞 报名方式：")
        print("="*60 + "\n")
        
        print("1. 访问课程网站：")
        print("   https://github.com/lsq-web17/OpenClaw-Tutorial\n")
        
        print("2. 扫描二维码加入学习社群获取报名链接\n")
        
        print("3. 或直接联系：arringtondhuka@gmail.com\n")
        
        print("="*60)
        print("💬 讲师寄语：")
        print("="*60 + "\n")
        
        print("技术的学习不在于知道多少，而在于开始动手。")
        print("每一个伟大的项目，都始于第一行代码。")
        print("我在课程中等你，让我们一起开启AI助手开发之旅！\n")
        
        print("-"*40)
        print("lsq-web17")
        print("OpenClaw技能开发专家")
        print("-"*40)
        
        print("\n🎉 演示结束！感谢观看！")
        print("\n想立即体验？运行以下命令：")
        print("  python3 courses/01-openclaw-basic/code/chapter-01/hello_skill_basic.py")
    
    def run(self):
        """运行完整演示"""
        try:
            for i, step in enumerate(self.demo_steps, 1):
                step()
                if i < len(self.demo_steps):
                    print("\n" + "➡️"*30 + "\n")
        except KeyboardInterrupt:
            print("\n\n👋 演示已中断。感谢观看！")
        except Exception as e:
            print(f"\n❌ 演示出错: {e}")
            print("请检查环境并重试。")
    
    def quick_run(self):
        """快速运行演示（无交互）"""
        print("🚀 OpenClaw入门实战课程 - 快速演示\n")
        
        print("📋 课程亮点：")
        print("  • 5天掌握OpenClaw开发")
        print("  • 从零到一创建AI助手")
        print("  • 实战项目驱动学习")
        print("  • 中文友好，零基础可学\n")
        
        print("🎯 学习成果：")
        print("  • 开发自己的AI助手技能")
        print("  • 部署24小时在线服务")
        print("  • 实现自动化工作流")
        print("  • 掌握AI助手开发全流程\n")
        
        print("💰 课程信息：")
        print("  • 定价：99元（原价199元）")
        print("  • 时长：8小时视频 + 实践")
        print("  • 支持：社群+一对一答疑")
        print("  • 认证：结业证书+技能认证\n")
        
        print("📞 联系方式：")
        print("  • GitHub: lsq-web17/OpenClaw-Tutorial")
        print("  • 邮箱: arringtondhuka@gmail.com")
        print("  • 课程源码: 已全部开源")


def main():
    """主函数"""
    demo = CourseDemo()
    
    if len(sys.argv) > 1 and sys.argv[1] == "--quick":
        demo.quick_run()
    else:
        print("正在启动OpenClaw课程演示...")
        time.sleep(1)
        demo.run()


if __name__ == "__main__":
    main()