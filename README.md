# 🎮 方块吞噬者 (Block Eater)

一个**极易上手、极度上瘾、极其流畅**的网页端吞噬游戏。

## 🎯 游戏规则（3秒理解）

| 操作 | 说明 |
|------|------|
| 🎯 **目标** | 吞噬比你**小**的方块变大 |
| ⚠️ **警告** | 碰到比你**大**的方块 = 游戏结束 |
| 👆 **操作** | 鼠标 / 触摸移动方块 |

## 🚀 快速开始

**方式一：直接打开**
```bash
# 直接在浏览器打开
open index.html
# 或
xdg-open index.html
```

**方式二：本地服务器**
```bash
npx serve .
# 或
python -m http.server 8000
```

**方式三：部署到 GitHub Pages**
1. Fork 本仓库
2. 启用 GitHub Pages (来源: main branch)
3. 访问 `https://你的用户名.github.io/仓库名`

## 🎮 在线试玩

- **GitHub Pages**: `https://zhenvis.github.io/web-game-evolution`
- **CodePen**: (待添加)

## 🏆 游戏特性

### 上瘾机制 ✓
- **0.3秒重开** - 空格键 / 点击立刻重来
- **高频反馈** - 每吞噬一个方块都有粒子特效 + 分数动画
- **连击系统** - 连续吞噬触发连击，奖励翻倍
- **成长曲线** - 体型逐渐变大，速度保持灵敏
- **无等待** - 实时渲染，零加载时间
- **打击感** - 屏幕震动 + 音效反馈

### 视觉效果 ✓
- 流畅的60fps动画
- 粒子爆炸特效
- 分数弹出动画
- 瞳孔跟随系统
- 屏幕震动反馈
- 渐变配色方案

### 音效系统 ✓
- **Web Audio API** - 零依赖，无需加载音频文件
- **动态音调** - 连击数越高，音调越高
- **三种音效** - 吞噬 / 连击 / 死亡
- **可关闭** - 默认开启，可通过代码关闭

### 响应式设计 ✓
- PC 端：鼠标控制
- 移动端：触摸控制
- 完美适配各种屏幕尺寸

## 🛠️ 技术栈

| 技术 | 用途 |
|------|------|
| **HTML5 Canvas** | 核心游戏渲染 |
| **Vanilla JavaScript** | 游戏逻辑（零依赖） |
| **CSS3** | UI与动画 |
| **localStorage** | 最高分持久化 |

## 📁 项目结构

```
web-game-evolution/
├── index.html        # 完整的单文件游戏
├── README.md         # 本文档
├── CONTRIBUTING.md   # 贡献指南
└── docs/             # 文档目录
    ├── GAME_RULES.md      # 游戏规则
    ├── DEVELOPMENT.md     # 开发指南
    └── ADDICTION_MODEL.md # 上瘾模型分析
```

## 🎨 自定义修改

### 1. 修改颜色

```javascript
// 搜索 config 对象，修改颜色
const config = {
    playerColor: '#ff6b6b',  // 玩家颜色
    enemyHueMin: 30,          // 敌人最小色相
    enemyHueMax: 90,          // 敌人最大色相
    // ...
};
```

### 2. 调整难度

```javascript
const config = {
    growthRate: 0.5,      // 每次吞噬的成长量
    spawnInterval: 500,   // 生成间隔(ms)
    maxEnemies: 30,      // 最大敌人数
    enemySpeed: 2,       // 敌人基础速度
    // ...
};
```

### 3. 添加新方块类型

在 `Game.spawnEnemy()` 中添加：

```javascript
// 示例：添加特殊方块
if (Math.random() < 0.1) {  // 10%概率
    this.enemies.push({
        x: spawnX,
        y: spawnY,
        size: 40,
        color: '#ffd93d',  // 金色方块
        special: 'bonus',  // 特殊类型
        // ...
    });
}
```

## 🤝 贡献指南

欢迎 Fork 和贡献！

### 如何贡献
1. Fork 本项目
2. 创建特性分支 (`git checkout -b feature/amazing-feature`)
3. 提交更改 (`git commit -m 'Add amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 开启 Pull Request

### 贡献方向
- 🎮 新游戏模式
- 🎨 视觉效果优化
- 🌐 国际化支持
- 📱 移动端体验
- 🔊 音效系统
- 🐛 Bug 修复

## 📈 版本历史

### v1.0.0 (2026-02-11)
- ✅ 基础吞噬玩法
- ✅ 连击系统
- ✅ 粒子特效
- ✅ 分数动画
- ✅ 响应式设计
- ✅ 最高分保存

## 🎯 设计哲学

> **像 4399 一样上瘾，像独立游戏一样精致**

我们的目标：
1. **10秒上手** - 无需教程，看一眼就会玩
2. **停不下来** - 高频反馈，持续刺激
3. **一局接一局** - 极短重开路径
4. **百玩不腻** - 技巧深度与运气结合
5. **极易二创** - 代码清晰，模块化设计

## 📄 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE)

## 🙏 致谢

- [4399](https://www.4399.com) - 上瘾模型灵感来源
- [Hextris](https://hextris.io) - 节奏设计参考
- [Flappy Bird](https://flappybird.io) - 极简规则深度参考

---

**Made with ❤️ by [KINGSTON-115](https://github.com/zhenvis)**

*永不停歇的进化*
