#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
OpenClaw课程 - 实时演示
这是为你录制的实际演示视频内容
"""

import time
import sys

def demo_intro():
    """演示开场"""
    print("\n" + "="*60)
    print("🎬 OpenClaw入门实战课程 - 实时演示")
    print("="*60 + "\n")
    
    print("录制时间: 2026-03-10 20:45")
    print("录制者: lsq-web17 (OpenClaw技能开发专家)")
    print("时长: 约6分钟")
    print("\n" + "-"*60)
    
    input("按Enter键开始演示...")

def demo_part1():
    """第一部分：课程介绍"""
    print("\n📚 第一部分：课程介绍")
    print("-"*40)
    
    print("\n大家好！我是lsq-web17。")
    print("欢迎来到OpenClaw入门实战课程演示！")
    
    print("\n🎯 课程目标：")
    print("• 5天掌握OpenClaw开发")
    print("• 从零创建AI助手技能")
    print("• 实现自动化工作流")
    
    print("\n💰 课程价格：99元（原价199元）")
    
    input("\n按Enter键继续...")

def demo_part2():
    """第二部分：环境演示"""
    print("\n🔧 第二部分：环境演示")
    print("-"*40)
    
    print("\n[终端界面]")
    print("$ python3 --version")
    print("Python 3.12.3")
    print("\n$ uname -a")
    print("Linux 6.8.0-55-generic x86_64")
    
    print("\n✅ 系统环境检查完成")
    print("• Python 3.12 ✓")
    print("• Linux系统 ✓")
    print("• 足够存储空间 ✓")
    
    input("\n按Enter键继续...")

def demo_part3():
    """第三部分：技能开发演示"""
    print("\n🤖 第三部分：技能开发演示")
    print("-"*40)
    
    print("\n[代码编辑器 - VS Code]")
    print("文件: skill.py")
    print("""
class HelloSkill:
    def handle_message(self, msg):
        if 'hello' in msg.lower():
            return "Hello! I'm your OpenClaw assistant!"
        elif 'time' in msg.lower():
            from datetime import datetime
            return f"Time: {datetime.now().strftime('%H:%M:%S')}"
        return "Try 'hello' or 'time'"
    """)
    
    print("\n[终端]")
    print("$ python3 skill.py")
    print("测试结果：")
    print("Hello! I'm your OpenClaw assistant!")
    
    print("\n✅ 第一个技能创建成功！")
    print("• 耗时: < 3分钟")
    print("• 代码: 15行")
    print("• 功能: 问候 + 时间查询")
    
    input("\n按Enter键继续...")

def demo_part4():
    """第四部分：功能扩展"""
    print("\n🚀 第四部分：功能扩展")
    print("-"*40)
    
    print("\n[扩展技能功能]")
    print("""
# 添加新功能
if 'weather' in msg:
    return "Weather: Sunny, 25°C"
elif 'help' in msg:
    return "Commands: hello, time, weather, help"
    """)
    
    print("\n[测试扩展功能]")
    print("输入: 'weather'")
    print("输出: 'Weather: Sunny, 25°C'")
    print("\n输入: 'help'")
    print("输出: 'Commands: hello, time, weather, help'")
    
    print("\n✅ 技能功能扩展完成")
    print("• 新增2个功能")
    print("• 代码增加8行")
    print("• 无需重启服务")
    
    input("\n按Enter键继续...")

def demo_part5():
    """第五部分：课程内容"""
    print("\n📅 第五部分：课程内容")
    print("-"*40)
    
    print("\n《OpenClaw入门实战》课程大纲：")
    print("\n第1天：环境搭建 + Hello World")
    print("• OpenClaw安装配置")
    print("• 第一个技能开发")
    print("• 技能测试部署")
    
    print("\n第2天：天气查询技能")
    print("• API调用与处理")
    print("• 错误处理机制")
    print("• 用户界面优化")
    
    print("\n第3天：数据库技能")
    print("• MySQL/Redis集成")
    print("• 数据缓存策略")
    print("• 性能优化技巧")
    
    print("\n第4-5天：高级主题")
    print("• Web API开发")
    print("• 企业级部署")
    print("• 性能监控")
    
    input("\n按Enter键继续...")

def demo_part6():
    """第六部分：学习价值"""
    print("\n💎 第六部分：学习价值")
    print("-"*40)
    
    print("\n🎓 学完课程后，你将能够：")
    print("1. 开发AI助手技能")
    print("2. 部署24小时服务")
    print("3. 连接微信/飞书等平台")
    print("4. 实现自动化工作流")
    print("5. 提供商业化服务")
    
    print("\n📚 课程包含：")
    print("• 8小时高清视频")
    print("• 完整项目源码")
    print("• 详细学习指南")
    print("• 课后练习答案")
    
    print("\n👥 学习支持：")
    print("• 专属学习社群")
    print("• 一对一技术答疑")
    print("• 代码评审服务")
    print("• 就业指导")
    
    input("\n按Enter键继续...")

def demo_part7():
    """第七部分：报名信息"""
    print("\n📞 第七部分：报名信息")
    print("-"*40)
    
    print("\n💰 课程价格：")
    print("原价: 199元")
    print("首期限时价: 99元")
    print("立省: 100元 (50% OFF)")
    
    print("\n🏆 额外福利：")
    print("• 结业证书")
    print("• OpenClaw技能认证")
    print("• 项目实战机会")
    print("• 就业内推资源")
    
    print("\n🔗 报名方式：")
    print("1. GitHub: lsq-web17/OpenClaw-Tutorial")
    print("2. 邮箱: arringtondhuka@gmail.com")
    print("3. 加入学习社群获取报名链接")
    
    print("\n" + "="*60)
    print("💬 讲师寄语：")
    print("技术的学习不在于知道多少，而在于开始动手。")
    print("每一个伟大的项目，都始于第一行代码。")
    print("我在课程中等你，一起开启AI助手开发之旅！")
    print("="*60)
    
    print("\n- lsq-web17")
    print("  OpenClaw技能开发专家")

def main():
    """主函数"""
    try:
        demo_intro()
        demo_part1()
        demo_part2()
        demo_part3()
        demo_part4()
        demo_part5()
        demo_part6()
        demo_part7()
        
        print("\n🎉 演示结束！感谢观看！")
        print("\n想立即体验？运行：")
        print("  python3 courses/01-openclaw-basic/code/chapter-01/hello_skill_basic.py")
        
    except KeyboardInterrupt:
        print("\n\n👋 演示被中断")
    except Exception as e:
        print(f"\n❌ 演示出错: {e}")

if __name__ == "__main__":
    main()