#!/usr/bin/env python3
"""修复 index.html 中的 AudioContext 问题"""

file_path = "/home/KINGSTON/.openclaw/workspace/web-game-evolution/index.html"

with open(file_path, 'r') as f:
    content = f.read()

# 修复 click 事件
old1 = """document.getElementById('startBtn').addEventListener('click', () => this.start());"""
new1 = """document.getElementById('startBtn').addEventListener('click', () => {
                    AudioSys.init();
                    this.start();
                });"""

content = content.replace(old1, new1)

# 修复 touchend 事件
old2 = """document.getElementById('startBtn').addEventListener('touchend', (e) => {
                    e.preventDefault();
                    this.start();
                });"""
new2 = """document.getElementById('startBtn').addEventListener('touchend', (e) => {
                    e.preventDefault();
                    AudioSys.init();
                    this.start();
                });"""

content = content.replace(old2, new2)

with open(file_path, 'w') as f:
    f.write(content)

print("✅ 已修复 AudioContext 初始化问题")
