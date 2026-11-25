# HANDOFF — Dad Joke Showdown

比赛：u-mfnakmal-dad-joke-showdown-1d2ce3e5（$5，截止北京时间 2026-11-26 04:25）
比赛页：https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5

## 做了什么

全部文件均为工人亲手用写工具写出，未读任何现成代码、未复制粘贴、未用脚本生成文件内容：

- `main.py`：入口在仓库根目录。只做一件事——把文案一字不改地写到 `/output/entry.txt`，无换行符、无多余字符，不读外部文件、不联网。
- `LICENSE`：MIT，含 `SPDX-License-Identifier: MIT` 行。
- `README.md`：写明这是 Dad Joke Showdown 投稿，附比赛页链接和三枚官方徽章。
- `prompt.txt`：用户亲口原话两行照抄（文案 + `- 爸爸笑话对决`）。
- `.makefun/owner.json`：钱包 `6t8k8dD19c2zDMiZ1VNsbRDWaSNSedmQQB6A15hy3XFx`。
- `HANDOFF.md`：本文件。

## 文案

> The mechanic told me my car needed a new muffler. I said, “Keep it quiet.”

- 字符数：74（含弯引号 “ ”，未超 200 字符上限）
- UTF-8 字节数：78（两个弯引号各占 3 字节，其余 72 个 ASCII 字符各 1 字节）

## 输出校验（main.py 跑两次）

- 第 1 次 sha256：`4e06133b4b58495126f53b8b24762e34ef0f3a6d54e905ef395cf2c5be248b65`
- 第 2 次 sha256：`4e06133b4b58495126f53b8b24762e34ef0f3a6d54e905ef395cf2c5be248b65`
- `cmp` 对比：两次输出逐字节一致（IDENTICAL）
- 内容核对：与文案逐字一致，弯引号 “ ” 保留，无换行符、无多余字符

## 备注

- 本机 Python 为 3.12.3（任务写 Python 3.13；代码只用标准库，3.12/3.13 均可跑）。
- 未提交、未建 GitHub 仓、未碰 bundle。
