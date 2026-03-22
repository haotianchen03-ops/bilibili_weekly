## 📁 项目结构

### 📦 数据与结果

- `bilibili_weekly_top10.html`  
  每周热门视频 Top10 展示页面（可视化结果）

- `dashboard.png`  
  简单数据看板截图，用于展示分析结果

- `热门视频流量监控.twb`  
  Tableau 数据分析文件，用于可视化趋势分析

- `bilibili.json`  
  抓取后的原始数据示例（JSON格式） :contentReference[oaicite:0]{index=0}  

---

### 🕷️ 爬虫核心

- `bili.py`  
  爬虫主逻辑，负责请求接口并解析每周热门视频数据 :contentReference[oaicite:1]{index=1}  

- `items.py`  
  定义数据结构（视频期数、标题、作者、播放/点赞等指标） :contentReference[oaicite:2]{index=2}  

---

### 🧱 数据处理

- `pipelines.py`  
  数据入库逻辑，使用 MongoDB 存储数据（支持去重更新） :contentReference[oaicite:3]{index=3}  

---

### ⚙️ 配置文件

- `settings.py`  
  Scrapy 配置，包括请求频率、并发、MongoDB连接等 :contentReference[oaicite:4]{index=4}  

---

## 🚀 功能说明

- 抓取视频网站每周热门视频列表
- 提取核心指标：
  - 播放量
  - 点赞
  - 投币
  - 收藏
  - 分享
  - 评论 / 弹幕
- 数据自动存入 MongoDB
- 支持后续数据分析与可视化

---

## 🛠️ 使用方式

```bash
scrapy crawl bili
