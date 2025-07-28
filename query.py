# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     custom_cell_magics: kql
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.11.2
#   kernelspec:
#     display_name: Python 3.9.16 ('torch')
#     language: python
#     name: python3
# ---

# %% tags=[]
import os
import sys
import argparse
import urllib.parse
import time
from datetime import datetime
import webbrowser
import pyperclip
from functools import partial

# %% tags=[]
# print("hello, this is argv:", os.environ["files"], file=sys.stderr)



# %% tags=[]
def convert_brackets(text):
    """将文本中的英文括号转换为中文括号"""
    # 定义括号映射关系
    bracket_mapping = {
        '(': '（',
        ')': '）'
    }
    
    # 替换所有英文括号为中文括号
    for eng_bracket, ch_bracket in bracket_mapping.items():
        text = text.replace(eng_bracket, ch_bracket)
    
    return text


def format_thousand_separator(text):
    """将数字按千位加逗号"""
    import re
    
    def add_commas(match):
        number = match.group(0)
        # 处理小数
        if '.' in number:
            integer_part, decimal_part = number.split('.')
            # 从右往左每三位加一个逗号
            formatted_integer = ''
            for i in range(len(integer_part)):
                if i > 0 and (len(integer_part) - i) % 3 == 0:
                    formatted_integer += ','
                formatted_integer += integer_part[i]
            return f"{formatted_integer}.{decimal_part}"
        else:
            # 从右往左每三位加一个逗号
            formatted_number = ''
            for i in range(len(number)):
                if i > 0 and (len(number) - i) % 3 == 0:
                    formatted_number += ','
                formatted_number += number[i]
            return formatted_number
    
    # 匹配数字（包括小数）
    pattern = r'\b\d+(?:\.\d+)?\b'
    return re.sub(pattern, add_commas, text)


def remove_textbf(text):
    """移除LaTeX中的\textbf{}命令，保留其中的内容"""
    import re
    
    # 匹配\textbf{...}模式，其中...是任意非大括号字符或嵌套的大括号
    pattern = r'\\textbf\{([^{}]*(?:\{[^{}]*\}[^{}]*)*)\}'
    
    def replace_textbf(match):
        # 返回\textbf{}中的内容
        return match.group(1)
    
    return re.sub(pattern, replace_textbf, text)


def dummy_text(wf, text, title, subtitle):
    wf.add_item(title=title, arg=text, subtitle=subtitle, valid=True)
    wf.send_feedback()



# %%
from workflow import Workflow3

# %% tags=[]
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--action", type=str)
    args = parser.parse_args()

    text = os.environ.get("text", "")

    print(text, args, file=sys.stderr)

    if args.action == "latex":

        def latex(wf):
            wf.add_item(
                title="去除引用",
                subtitle=r"~\cite{aa, bb, cc_dd}",
                arg="latex_rm_cite",
                valid=True,
            )
            wf.send_feedback()

        wf = Workflow3()
        sys.exit(wf.run(latex))
    elif args.action == "mermaid":

        def mermaid(wf):
            wf.add_item(
                title='使用""将cell里的文字括起来', arg="mermaid-quote", valid=True
            )
            wf.send_feedback()

        wf = Workflow3()
        sys.exit(wf.run(mermaid))
    elif args.action == "markdown":

        def markdown(wf):
            wf.add_item(
                title="替换数学公式中的indicator",
                subtitle="将\\[ \\]替换为$$",
                arg="markdown-replace-math-indicator",
                valid=True,
            )
            wf.send_feedback()

        wf = Workflow3()
        sys.exit(wf.run(markdown))
    elif args.action == "change_brackets(EN-CN)":
        # 直接转换文本中的括号并输出
        converted_text = convert_brackets(text)
        print(converted_text, file=sys.stderr)
        # 将转换后的文本复制到剪贴板
        pyperclip.copy(converted_text)

        wf = Workflow3()
        _dummy_text = partial(dummy_text, text=converted_text, title="已复制到剪贴板", subtitle=converted_text)
        sys.exit(wf.run(_dummy_text))
    elif args.action == "format_thousand_separator":
        # 直接转换文本中的数字并输出
        converted_text = format_thousand_separator(text)
        print(converted_text, file=sys.stderr)
        # 将转换后的文本复制到剪贴板
        pyperclip.copy(converted_text)

        wf = Workflow3()
        _dummy_text = partial(dummy_text, text=converted_text, title="已复制到剪贴板", subtitle=converted_text)
        sys.exit(wf.run(_dummy_text))
    elif args.action == "remove_textbf":
        # 移除LaTeX中的\textbf{}命令
        converted_text = remove_textbf(text)
        print(converted_text, file=sys.stderr)
        # 将转换后的文本复制到剪贴板
        pyperclip.copy(converted_text)

        wf = Workflow3()
        _dummy_text = partial(dummy_text, text=converted_text, title="已复制到剪贴板", subtitle=converted_text)
        sys.exit(wf.run(_dummy_text))
    
    

        
        

