#!/bin/bash
# OpenClaw入门实战课程 - 交互式演示脚本
# 作者：lsq-web17
# 日期：2026-03-10

echo "================================================"
echo "🚀 OpenClaw入门实战课程 - 5分钟快速演示"
echo "================================================"
echo ""
echo "大家好！我是lsq-web17，OpenClaw技能开发专家。"
echo "今天我要用5分钟，带你体验OpenClaw开发的魅力！"
echo ""
read -p "按Enter键开始演示..." dummy

clear
echo "🎯 第一部分：环境检查"
echo "================================================"
echo ""
echo "🔍 检查系统环境..."
echo ""
echo "1. 操作系统信息："
uname -a
echo ""
echo "2. Python版本："
python3 --version
echo ""
echo "3. 磁盘空间："
df -h . | head -2
echo ""
echo "✅ 环境检查完成！"
echo ""
read -p "按Enter键继续..." dummy

clear
echo "🚀 第二部分：OpenClaw安装演示"
echo "================================================"
echo ""
echo "OpenClaw提供了一键安装脚本："
echo ""
echo "安装命令："
echo "  curl -fsSL https://openclaw.ai/install.sh | bash"
echo ""
echo "安装过程（模拟）："
echo "1. 🔍 检测系统环境..."
sleep 1
echo "2. 📦 下载依赖包..."
sleep 1
echo "3. ⚙️ 配置工作空间..."
sleep 1
echo "4. 🚀 启动核心服务..."
sleep 1
echo ""
echo "✅ OpenClaw安装完成！"
echo ""
echo "注意：实际安装需要5-10分钟，这里做了加速演示。"
echo ""
read -p "按Enter键继续..." dummy

clear
echo "🤖 第三部分：创建第一个技能"
echo "================================================"
echo ""
echo "让我们创建一个Hello World技能："
echo ""
echo "1. 创建技能目录："
echo "   mkdir -p ~/.openclaw/workspace/skills/hello-world"
echo "   cd ~/.openclaw/workspace/skills/hello-world"
echo ""
echo "2. 创建技能文件 skill.py："
cat << 'EOF'
#!/usr/bin/env python3
from datetime import datetime

class HelloSkill:
    def handle_message(self, msg):
        if 'hello' in msg.lower():
            return "👋 你好！我是你的OpenClaw助手！"
        elif 'time' in msg.lower():
            return f"🕐 当前时间：{datetime.now().strftime('%H:%M:%S')}"
        return "🤔 试试说'hello'或'time'？"

if __name__ == "__main__":
    skill = HelloSkill()
    print("🎯 技能测试：")
    print("1. 输入'hello'：", skill.handle_message("hello"))
    print("2. 输入'time'：", skill.handle_message("time"))
    print("3. 输入'其他'：", skill.handle_message("其他内容"))
EOF
echo ""
echo "3. 运行技能测试："
python3 -c "
from datetime import datetime

class HelloSkill:
    def handle_message(self, msg):
        if 'hello' in msg.lower():
            return '👋 你好！我是你的OpenClaw助手！'
        elif 'time' in msg.lower():
            return f'🕐 当前时间：{datetime.now().strftime(\"%H:%M:%S\")}'
        return '🤔 试试说\"hello\"或\"time\"？'

skill = HelloSkill()
print('🎯 技能测试结果：')
print('1. 输入\"hello\":', skill.handle_message('hello'))
print('2. 输入\"time\":', skill.handle_message('time'))
print('3. 输入\"其他\":', skill.handle_message('其他内容'))
"
echo ""
echo "✅ 第一个技能创建成功！"
echo ""
read -p "按Enter键继续..." dummy

clear
echo "🌟 第四部分：技能扩展演示"
echo "================================================"
echo ""
echo "这只是一个开始！OpenClaw可以做的还有很多："
echo ""
echo "1. 🌤️ 天气查询技能"
cat << 'EOF'
def get_weather(city):
    # 调用天气API
    import requests
    response = requests.get(f'https://api.weather.com/{city}')
    data = response.json()
    return f"🌤️ {city}天气：{data['temp']}°C，{data['condition']}"
EOF
echo ""
echo "2. 📰 新闻聚合技能"
cat << 'EOF'
def get_news(topic):
    # 抓取新闻网站
    import feedparser
    feed = feedparser.parse(f'https://news/rss/{topic}')
    return f"📰 最新{topic}新闻：{feed.entries[0].title}"
EOF
echo ""
echo "3. 💹 股票监控技能"
cat << 'EOF'
def get_stock_price(code):
    # 获取股票数据
    import yfinance as yf
    stock = yf.Ticker(code)
    price = stock.history(period='1d')['Close'][0]
    return f"💹 {code}股价：¥{price:.2f}"
EOF
echo ""
echo "✅ 每个功能都可以通过简单的Python代码实现！"
echo ""
read -p "按Enter键继续..." dummy

clear
echo "📚 第五部分：课程内容预览"
echo "================================================"
echo ""
echo "在《OpenClaw入门实战》课程中，你将学会："
echo ""
echo "📅 第1天：环境搭建 + Hello World技能"
echo "   ✅ OpenClaw安装与配置"
echo "   ✅ 第一个技能开发"
echo "   ✅ 技能测试与部署"
echo ""
echo "📅 第2天：天气查询技能开发"
echo "   ✅ API调用与数据处理"
echo "   ✅ 错误处理与重试机制"
echo "   ✅ 用户界面优化"
echo ""
echo "📅 第3天：数据库集成技能"
echo "   ✅ MySQL/Redis连接"
echo "   ✅ 数据缓存策略"
echo "   ✅ 性能优化技巧"
echo ""
echo "📅 第4天：Web技能开发"
echo "   ✅ HTTP请求处理"
echo "   ✅ JSON数据解析"
echo "   ✅ RESTful API设计"
echo ""
echo "📅 第5天：企业级部署"
echo "   ✅ 生产环境配置"
echo "   ✅ 监控与报警"
echo "   ✅ 性能调优"
echo ""
read -p "按Enter键继续..." dummy

clear
echo "🎁 第六部分：课程权益与报名"
echo "================================================"
echo ""
echo "现在报名《OpenClaw入门实战》课程，你将获得："
echo ""
echo "1. 🎁 限时优惠"
echo "   原价：199元"
echo "   首期限时价：99元"
echo ""
echo "2. 📚 完整学习材料"
echo "   ✅ 8小时高清视频课程"
echo "   ✅ 完整项目源码"
echo "   ✅ 详细学习指南"
echo "   ✅ 课后练习答案"
echo ""
echo "3. 👥 学习支持"
echo "   ✅ 专属学习社群"
echo "   ✅ 一对一技术答疑"
echo "   ✅ 代码评审服务"
echo "   ✅ 就业指导"
echo ""
echo "4. 🏆 认证与机会"
echo "   ✅ 结业证书"
echo "   ✅ OpenClaw技能认证"
echo "   ✅ 项目实战机会"
echo "   ✅ 就业内推资源"
echo ""
echo "================================================"
echo "📞 报名方式："
echo ""
echo "1. 访问课程网站："
echo "   https://github.com/lsq-web17/OpenClaw-Tutorial"
echo ""
echo "2. 加入学习社群获取报名链接"
echo ""
echo "3. 或联系：arringtondhuka@gmail.com"
echo ""
echo "================================================"
echo "💬 讲师寄语："
echo ""
echo "技术的学习不在于知道多少，而在于开始动手。"
echo "我在课程中等你，让我们一起开启AI助手开发之旅！"
echo ""
echo "- lsq-web17"
echo "  OpenClaw技能开发专家"
echo "================================================"

echo ""
echo "演示结束！感谢观看！"
echo "想了解更多？运行这个脚本查看详细课程内容："
echo "  python3 courses/01-openclaw-basic/code/chapter-01/hello_skill_basic.py"