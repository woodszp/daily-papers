# 📄 Daily LLM Quantization Papers

一个自动化的论文追踪和展示平台，专注于LLM量化、端侧部署和多模态研究。

![Vercel](https://vercel.com/button) ![GitHub](https://img.shields.io/github/stars/ZhipingWoods/daily-papers)

## 🌟 功能特点

- 📰 **每日自动更新** - 自动从arXiv获取最新论文
- 🎨 **卡片式展示** - 精美的Vercel风格UI
- 🔍 **多种浏览方式**
  - 按日期浏览（年/月/日）
  - 按类别浏览（LLM量化/端侧部署/无人机视觉）
- 📊 **论文深度分析** - 自动提取研究动机、方法、贡献等
- 🔄 **一键部署** - 支持Vercel自动部署

## 📱 在线演示

访问: https://daily-papers.vercel.app

## 🚀 快速部署

### 方法1: Vercel一键部署

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/import/project?template=https://github.com/ZhipingWoods/daily-papers)

### 方法2: 本地部署

```bash
# 克隆仓库
git clone https://github.com/ZhipingWoods/daily-papers.git
cd daily-papers

# 安装依赖
pip install -r requirements.txt

# 本地运行
python app.py

# 访问 http://localhost:5000
```

### 方法3: Docker部署

```bash
docker build -t daily-papers .
docker run -p 5000:5000 daily-papers
```

## 📂 项目结构

```
daily-papers/
├── app.py                 # Flask主应用
├── paper_analysis.py      # 论文分析模块
├── update_papers.py       # 自动更新脚本
├── requirements.txt       # Python依赖
├── vercel.json           # Vercel配置
├── templates/
│   └── index.html        # 前端模板
└── papers/
    ├── papers_latest.md  # 最新论文
    └── analysis_latest.md # 论文分析
```

## ⚙️ 自定义配置

### 1. 修改关键词

编辑 `skills/paper-pusher/scripts/fetch_papers.py` 中的关键词：

```python
RESEARCH_KEYWORDS = {
    'LLM Quantization': [
        'quantization', 'LLM', 'multimodal', 'VLM', 
        'PTQ', 'QAT', '4-bit', '8-bit', 'low-bit',
        # 添加你的关键词
    ],
    'Edge Deployment': [
        'edge deployment', 'on-device', 'TensorRT',
        'NCNN', 'ONNX', 'model compression',
        # 添加你的关键词
    ],
    'UAV Vision': [
        'drone', 'UAV', 'aerial', 'video tracking',
        'object detection', 'small object',
        # 添加你的关键词
    ]
}
```

### 2. 修改论文类别

在 `app.py` 中修改类别映射：

```python
CATEGORY_MAP = {
    'LLM Quantization': '🎯 LLM Quantization',
    'Edge Deployment': '📱 Edge Deployment', 
    'UAV Vision': '🚁 UAV Vision',
    # 添加新类别
}
```

### 3. 修改抓取时间

编辑crontab：

```bash
crontab -e
# 添加: 0 8 * * * python3 /path/to/update_papers.py
```

## 🔧 自动更新设置

### GitHub Actions (推荐)

在 `.github/workflows/update.yml`:

```yaml
name: Daily Update
on:
  schedule:
    - cron: '0 8 * * *'  # 每天8点
  workflow_dispatch:

jobs:
  update:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Run update
        run: python update_papers.py
      - name: Commit and push
        run: |
          git config --global user.name "Daily Papers Bot"
          git add .
          git commit -m "Update papers $(date +%Y-%m-%d)"
          git push
```

### 本地Cron

```bash
# 每天早上8点自动更新
0 8 * * * cd /path/to/daily-papers && python update_papers.py >> /tmp/paper_update.log 2>&1
```

## 📊 论文分析维度

每篇论文都包含以下分析：

| 维度 | 说明 |
|------|------|
| 研究动机 | 为什么要做这个研究 |
| 相关工作 | 现有方法有哪些 |
| 贡献点 | 本文的主要创新 |
| 方法论 | 具体做法和步骤 |
| 为什么更好 | 相比现有方法的优势 |
| 局限性 | 存在的不足 |
| 多模态支持 | 是否适合多模态大模型 |
| 实验设置 | 数据集和实验方法 |

## 🤝 贡献

欢迎提交Issue和PR！

1. Fork本仓库
2. 创建特性分支 (`git checkout -b feature/xxx`)
3. 提交更改 (`git commit -m 'Add xxx'`)
4. 推送到分支 (`git push origin feature/xxx`)
5. 创建Pull Request

## 📝 License

MIT License

## 🙏 致谢

- [Kai-Liu001/Awesome-Model-Quantization](https://github.com/Kai-Liu001/Awesome-Model-Quantization)
- [Efficient-ML/Awesome-Model-Quantization](https://github.com/Efficient-ML/Awesome-Model-Quantization)
- [arXiv](https://arxiv.org/) - 论文来源

---

Made with ❤️ by [ZhipingWoods](https://github.com/ZhipingWoods)