# autotuwen

小红书本地教师 IP 图文笔记全流程 skill：数据驱动选题 → 正文 → 封面/附图 → 审图 → 存草稿 → 发布后迭代。

## 适用
个人老师 IP（教培/本地服务类账号通用）的持续图文运营。每一步都停下来等用户确认。

## 安装
```bash
npx -y skills add laofang522/xiaohongshu -g --all
```

## 使用
对 agent 说「做一篇小红书笔记」，按 SKILL.md 七步执行；首次使用需配置照片目录、工作台目录、账号定位。

## 依赖
- 封面脚本需要 Pillow：`pip install pillow`
- 存草稿步骤需 ego-browser + 已登录的小红书创作者后台（或改用 MCP 直发）
- 搜对标需小红书搜索入口（MCP 或创作者后台搜索）
