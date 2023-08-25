# 项目介绍
本项目把chatpgt接入QQ，实现在QQ中和通义千问群聊或私聊。

项目基于go-cqhttp和chatgpt 的 api，部署本项目前请先部署好go-cqhttp，并获得gpt的api-key。

go-cqhttp项目地址：[go-cqhttp](https://github.com/Mrs4s/go-cqhttp)，帮助文档：[docs.go-cqhttp](https://docs.go-cqhttp.org/)


# 项目使用
1. ``main.py``中第七行的botQQ改为自己的机器人QQ号
2. ``gpt.py``中第三行改为自己的api-key
3. 运行go-cqhttp
4. 运行main.py
