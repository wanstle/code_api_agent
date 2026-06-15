#!/bin/bash
# 在集群 venv 安装 demo 依赖(chainlit + mkdocs-material),走清华镜像加速,脱离式跑
cd /home/sht7/api_doc || exit 1
export UV_DEFAULT_INDEX=https://pypi.tuna.tsinghua.edu.cn/simple
export UV_INDEX_URL=https://pypi.tuna.tsinghua.edu.cn/simple
rm -f /tmp/uvinstall.done /tmp/uvinstall.log
/home/sht7/.local/bin/uv pip install --python .venv/bin/python chainlit==2.11.1 mkdocs-material
echo "$?" > /tmp/uvinstall.done
