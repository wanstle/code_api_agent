"""A 对比:同样几个模块,固定 prompt vs lens 增强,各出一份文档并存盘。

用法: .venv/bin/python -m scripts.compare_lens_doc [repo] [mod1,mod2,...]
两次都走现有 summarize 管线,唯一差别 = 是否注入该模块的 lens(增强不替换),
故差异完全归因于 lens。跳过 reduce 以省调用。
"""

from __future__ import annotations

import sys
from pathlib import Path

from docgen.summarize import generate

name = sys.argv[1] if len(sys.argv) > 1 else "click"
mods = (sys.argv[2].split(",") if len(sys.argv) > 2
        else ["src/click", "examples/aliases", "examples/imagepipe"])

print(f"对比仓库={name} · 模块={mods}\n")
print("跑 FIXED(固定 prompt)…")
fixed = generate(name, progress=lambda m: None, use_lens=False, only=mods, skip_reduce=True)
print("跑 LENS(注入 lens)…")
lensed = generate(name, progress=lambda m: None, use_lens=True, only=mods, skip_reduce=True)

out = Path(".cache/lens_compare")
out.mkdir(parents=True, exist_ok=True)
for m in mods:
    safe = m.replace("/", "_")
    f_txt = fixed.modules.get(m, "(无)")
    l_txt = lensed.modules.get(m, "(无)")
    (out / f"{safe}.FIXED.md").write_text(f_txt, "utf-8")
    (out / f"{safe}.LENS.md").write_text(l_txt, "utf-8")
    print("=" * 78)
    print(f"模块 {m}: FIXED {len(f_txt)} 字符 / LENS {len(l_txt)} 字符")
print(f"\n两份产出已写入 {out}/  (各模块 .FIXED.md 与 .LENS.md,可 diff)")
