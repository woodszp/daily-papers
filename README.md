# 📄 Daily LLM Quantization Papers

[![Vercel](https://vercel.com/button)](https://vercel.com)
[![GitHub stars](https://img.shields.io/github/stars/ZhipingWoods/daily-papers)](https://github.com/ZhipingWoods/daily-papers)
[![License](https://img.shields.io/github/license/ZhipingWoods/daily-papers)](LICENSE)

An automated paper tracking and display platform focused on LLM Quantization, Edge Deployment, and Multimodal Research.

**[🇨🇳 中文版](./README_ZH.md)**

---

## 🌟 Features

- 📰 **Daily Auto-Update** - Automatically fetch latest papers from arXiv
- 🎨 **Card-Style Display** - Beautiful Vercel-style UI
- 🔍 **Multiple View Modes**
  - Browse by Date (Year/Month/Day)
  - Browse by Category (LLM Quantization/Edge Deployment/UAV Vision)
- 📊 **Deep Paper Analysis** - Auto-extract research motivation, methods, contributions
- 🔄 **One-Click Deploy** - Support Vercel auto-deployment

## 📱 Live Demo

Visit: https://daily-papers.vercel.app

## 🚀 Quick Deploy

### Method 1: Vercel One-Click Deploy

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/import/project?template=https://github.com/ZhipingWoods/daily-papers)

### Method 2: Local Development

```bash
# Clone repository
git clone https://github.com/ZhipingWoods/daily-papers.git
cd daily-papers

# Install dependencies
pip install -r requirements.txt

# Run locally
python app.py

# Visit http://localhost:5000
```

### Method 3: Docker

```bash
docker build -t daily-papers .
docker run -p 5000:5000 daily-papers
```

## 📂 Project Structure

```
daily-papers/
├── app.py                 # Flask main application
├── paper_analysis.py      # Paper analysis module
├── update_papers.py       # Auto-update script
├── requirements.txt       # Python dependencies
├── vercel.json           # Vercel configuration
├── README.md             # English version (this file)
├── README_ZH.md          # Chinese version
├── templates/
│   └── index.html        # Frontend template
└── papers/
    ├── papers_latest.md  # Latest papers
    └── analysis_latest.md # Paper analysis
```

## ⚙️ Customization

### 1. Modify Keywords

Edit keywords in `skills/paper-pusher/scripts/fetch_papers.py`:

```python
RESEARCH_KEYWORDS = {
    'LLM Quantization': [
        'quantization', 'LLM', 'multimodal', 'VLM', 
        'PTQ', 'QAT', '4-bit', '8-bit', 'low-bit',
    ],
    'Edge Deployment': [
        'edge deployment', 'on-device', 'TensorRT',
        'NCNN', 'ONNX', 'model compression',
    ],
    'UAV Vision': [
        'drone', 'UAV', 'aerial', 'video tracking',
        'object detection', 'small object',
    ]
}
```

### 2. Modify Categories

Edit category mapping in `app.py`:

```python
CATEGORY_MAP = {
    'LLM Quantization': '🎯 LLM Quantization',
    'Edge Deployment': '📱 Edge Deployment', 
    'UAV Vision': '🚁 UAV Vision',
}
```

### 3. Set Auto-Update Schedule

```bash
crontab -e
# Add: 0 8 * * * python3 /path/to/update_papers.py
```

## 📊 Paper Analysis Dimensions

Each paper includes:

| Dimension | Description |
|-----------|-------------|
| Research Motivation | Why this research |
| Related Work | Existing methods |
| Contributions | Main innovations |
| Methodology | Approach and steps |
| Why Better | Advantages over SOTA |
| Limitations | Current shortcomings |
| Multimodal Support | Suitable for multimodal LLMs |
| Experiments | Datasets and methods |

## 🤝 Contributing

Welcome to submit Issues and PRs!

1. Fork this repository
2. Create feature branch (`git checkout -b feature/xxx`)
3. Commit changes (`git commit -m 'Add xxx'`)
4. Push to branch (`git push origin feature/xxx`)
5. Create Pull Request

## 📝 License

MIT License

## 🙏 Acknowledgments

- [Kai-Liu001/Awesome-Model-Quantization](https://github.com/Kai-Liu001/Awesome-Model-Quantization)
- [Efficient-ML/Awesome-Model-Quantization](https://github.com/Efficient-ML/Awesome-Model-Quantization)
- [arXiv](https://arxiv.org/) - Paper source

---

Made with ❤️ by [ZhipingWoods](https://github.com/ZhipingWoods)# Trigger rebuild
