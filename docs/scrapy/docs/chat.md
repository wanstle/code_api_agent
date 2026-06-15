# LLM Chat

<div class="llm-chat-shell">
  <iframe src="http://127.0.0.1:8001" title="RepoAgent LLM Chat" loading="lazy"></iframe>
</div>

!!! note "Local service required"
    Start the QA UI before using this page:

    ```bash
    REPO=scrapy .venv/bin/chainlit run app.py --host 127.0.0.1 --port 8001
    ```

    The generated documentation can run on `http://127.0.0.1:8000`, while this embedded chat connects to Chainlit on `8001`.
