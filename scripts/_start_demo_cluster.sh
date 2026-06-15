#!/bin/bash
# 在集群一键起 scrapy demo:30B llama-server(8080)→ Chainlit 问答(8001)→ mkdocs 文档站(8000)。
# 三个服务各自 setsid 脱离,ssh 断开后继续运行。内存安全:30B 进 VRAM,ctx 8192 单槽。
cd /home/sht7/api_doc || exit 1
rm -f /tmp/demo.started

# 1) 30B llama-server(进 VRAM,系统内存不受压)
export MODEL=/home/sht7/api_doc/models/Qwen3-Coder-30B-A3B-Instruct-Q4_K_M.gguf
export CTX=8192 SLOTS=1 PORT=8080
pkill -x llama-server 2>/dev/null; sleep 2
setsid nohup bash scripts/serve_llama_prebuilt_vulkan.sh >/tmp/demo.llama.log 2>&1 </dev/null &

# 等 server 健康(最多 ~180s)
ok=no
for i in $(seq 1 90); do
  if curl -s http://127.0.0.1:8080/health 2>/dev/null | grep -q '"status":"ok"'; then ok=yes; break; fi
  sleep 2
done
echo "llama_health=$ok" > /tmp/demo.started

# 2) Chainlit 问答(REPO=scrapy,绑 127.0.0.1 配合 SSH -L 隧道)
export LLAMA_BASE_URL=http://127.0.0.1:8080/v1
REPO=scrapy setsid nohup .venv/bin/chainlit run app.py --host 127.0.0.1 --port 8001 --headless >/tmp/demo.chainlit.log 2>&1 </dev/null &

# 3) mkdocs 文档站
setsid nohup .venv/bin/python -m mkdocs serve -f docs/scrapy/mkdocs.yml -a 127.0.0.1:8000 >/tmp/demo.mkdocs.log 2>&1 </dev/null &

sleep 4
echo "launched chainlit+mkdocs" >> /tmp/demo.started
