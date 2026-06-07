"""F. Q&A Agent:在仓库上用工具循环回答问题,带 file:line 引用。

预检索(D2)给种子上下文,agent 再用 read_file/grep/list_dir 按需补充(混合式)。
"""
