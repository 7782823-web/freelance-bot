# AI 自由职业接单机器人

基于飞书 Webhook 的自动化接单系统

## 🚀 快速部署到 Railway

### 1. 创建 Railway 账号
访问 https://railway.app/signup 使用 GitHub 登录

### 2. 部署项目
1. 点击 "New Project"
2. 选择 "Deploy from GitHub repo"
3. 选择 freelance-bot 仓库
4. 添加环境变量 `WEBHOOK_URL`（见下方）
5. 点击 "Deploy"

### 3. 配置环境变量
```
WEBHOOK_URL=https://open.feishu.cn/open-apis/bot/v2/hook/oc_d6320885048ca26f33d2c51933257707
```

### 4. 获取 Bot URL
部署完成后，Railway 会分配一个 URL，如：
```
https://freelance-bot.onrailway.app
```

### 5. 在飞书中测试
在飞书群聊中发送：
```
接单：写一份商业计划书
```

---

## 💰 服务报价

| 服务类型 | 价格范围 | 交付时间 |
|---------|---------|---------|
| 简单文案 | ¥200-500 | 1-2 天 |
| 文章写作 | ¥500-1,000 | 2-3 天 |
| Logo 设计 | ¥800-2,000 | 2-3 天 |
| 商业计划书 | ¥2,000-5,000 | 3-5 天 |
| UI/UX 设计 | ¥1,500-5,000 | 3-5 天 |
| 网站开发 | ¥3,000-10,000 | 5-10 天 |
| APP 开发 | ¥5,000-20,000 | 7-15 天 |

---

## 🔧 其他云平台选项

### Render.com
- 免费套餐：每月 750 小时
- 部署步骤类似 Railway

### Fly.io
- 免费额度：每月 $5
- 需要使用 flyctl CLI

### Vercel
- 完全免费
- 适合 Serverless 部署

---

## 📞 技术支持

如有问题，请查看 Railway 文档或联系开发者。
