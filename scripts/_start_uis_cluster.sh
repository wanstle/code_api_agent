#!/bin/bash
# 仅起 Chainlit(8001)+ mkdocs(8000);假设 30B llama-server 已在 8080 运行。
cd /home/sht7/api_doc || exit 1
export LLAMA_BASE_URL=http://127.0.0.1:8080/v1
pkill -f "chainlit run app.py" 2>/dev/null
pkill -f "mkdocs serve -f docs/scrapy" 2>/dev/null
sleep 1
REPO=scrapy setsid nohup .venv/bin/chainlit run app.py --host 127.0.0.1 --port 8001 --headless >/tmp/demo.chainlit.log 2>&1 </dev/null &
setsid nohup .venv/bin/python -m mkdocs serve -f docs/scrapy/mkdocs.yml -a 127.0.0.1:8000 >/tmp/demo.mkdocs.log 2>&1 </dev/null &
sleep 3
echo "UIs launched" > /tmp/demo.uis.started
