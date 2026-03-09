# 📁 资源文件目录

本目录包含 OpenClaw-Tutorial 项目的各种资源文件。

## 📋 文件说明

### 1. 图标文件
- **logo.png** - 项目主图标（建议尺寸：512×512）
- **favicon.ico** - 网站图标（16×16, 32×32, 48×48）
- **banner.png** - 项目横幅（建议尺寸：1200×300）

### 2. 图片资源
- **tutorial-images/** - 教程配图目录
  - `/setup/` - 环境搭建相关图片
  - `/examples/` - 示例代码截图
  - `/projects/` - 实战项目展示

### 3. 文档资源
- **pdf/** - PDF文档版本
  - `完整教程.pdf` - 所有教程的PDF版本
  - `快速指南.pdf` - 快速入门PDF

### 4. 示例数据
- **sample-data/** - 示例数据文件
  - `stock_data.csv` - 股票数据示例
  - `weather_data.json` - 天气数据示例

## 🎨 设计规范

### 色彩方案
- **主色**：`#4CAF50`（绿色）- 代表成长、技术、开源
- **辅色**：`#2196F3`（蓝色）- 代表知识、信任、专业
- **强调色**：`#FF9800`（橙色）- 代表创新、活力、醒目
- **背景色**：`#F5F5F5`（浅灰）- 代表简洁、专业、易读

### 字体规范
- **主要字体**：`-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif`
- **代码字体**：`"SFMono-Regular", Consolas, "Liberation Mono", Menlo, Courier, monospace`

### 图片规范
- **格式**：PNG（透明背景）、JPG（照片类）
- **尺寸**：响应式设计，提供多种尺寸
- **质量**：压缩优化，保持清晰的同时减小文件大小

## 🔧 使用指南

### 添加新图标
1. 将图标文件放在相应目录
2. 更新相关文档中的引用
3. 确保图片符合设计规范

### 更新资源
1. 备份原有资源文件
2. 使用专业设计工具（如 Figma、Adobe XD）
3. 保持风格一致性
4. 更新版本号和说明

### 优化建议
1. 使用矢量图标（SVG）以获得更好的缩放效果
2. 压缩图片文件以减小仓库体积
3. 提供多种尺寸的图标以适应不同使用场景

## 📊 文件清单

```
assets/
├── icons/                    # 图标文件
│   ├── logo.png             # 主图标
│   ├── favicon.ico          # 网站图标
│   ├── app-icon.png         # 应用图标
│   └── social/              # 社交媒体图标
│       ├── github.png
│       ├── wechat.png
│       └── zhihu.png
├── images/                   # 图片资源
│   ├── tutorial-images/     # 教程配图
│   ├── screenshots/        # 项目截图
│   └── diagrams/           # 架构图
├── documents/               # 文档资源
│   ├── pdf/                # PDF文档
│   └── templates/          # 模板文件
└── sample-data/            # 示例数据
    ├── csv/               # CSV格式数据
    ├── json/              # JSON格式数据
    └── sql/               # SQL脚本
```

## 🚀 快速开始

### 获取图标
```html
<!-- 使用主图标 -->
<img src="./assets/icons/logo.png" alt="OpenClaw Tutorial Logo">

<!-- 使用网站图标 -->
<link rel="icon" href="./assets/icons/favicon.ico">
```

### 引用资源
```markdown
![环境准备示意图](./assets/images/tutorial-images/setup/01-installation.png)
```

## 📝 注意事项

1. **版权问题**：确保所有资源文件具有合法使用权
2. **文件大小**：控制单个文件大小，避免影响GitHub Pages加载速度
3. **格式兼容**：确保图片在多种浏览器和设备上正常显示
4. **更新维护**：定期检查资源文件，删除过时内容

## 🔗 相关链接

- [OpenClaw 官方网站](https://openclaw.ai)
- [GitHub Pages 文档](https://pages.github.com)
- [图片优化工具](https://squoosh.app)
- [图标设计指南](https://material.io/design/iconography)

---

**保持资源文件整洁有序，有助于提升项目的专业性和用户体验！** 🎯