#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

def remove_textbf(text):
    """移除LaTeX中的\textbf{}命令，保留其中的内容"""
    # 匹配\textbf{...}模式，其中...是任意非大括号字符或嵌套的大括号
    pattern = r'\\textbf\{([^{}]*(?:\{[^{}]*\}[^{}]*)*)\}'
    
    def replace_textbf(match):
        # 返回\textbf{}中的内容
        return match.group(1)
    
    return re.sub(pattern, replace_textbf, text)

# 测试用例
test_cases = [
    r"\textbf{hello world}",
    r"This is \textbf{bold text} in a sentence.",
    r"Multiple \textbf{first} and \textbf{second} bold words.",
    r"\textbf{text with {nested} braces}",
    r"Normal text without \textbf{}",
    r"\textbf{text} \textbf{more text} \textbf{even more}",
]

print("测试 remove_textbf 函数:")
print("=" * 50)

for i, test_case in enumerate(test_cases, 1):
    result = remove_textbf(test_case)
    print(f"测试 {i}:")
    print(f"  输入: {test_case}")
    print(f"  输出: {result}")
    print() 