"""
测试重构后的Workflow功能
"""

import sys
import os
from text_processors import (
    BracketConverter,
    NumberFormatter,
    LatexProcessor,
    MarkdownProcessor,
    MermaidProcessor
)


def test_bracket_converter():
    """测试括号转换器"""
    print("测试括号转换器...")
    converter = BracketConverter()
    
    test_cases = [
        ("Hello (world)", "Hello （world）"),
        ("Test (123) and (456)", "Test （123） and （456）"),
        ("No brackets here", "No brackets here")
    ]
    
    for input_text, expected in test_cases:
        result = converter.process(input_text)
        status = "✓" if result == expected else "✗"
        print(f"  {status} '{input_text}' -> '{result}' (期望: '{expected}')")


def test_number_formatter():
    """测试数字格式化器"""
    print("\n测试数字格式化器...")
    formatter = NumberFormatter()
    
    test_cases = [
        ("1234567", "1,234,567"),
        ("1234567.89", "1,234,567.89"),
        ("123", "123"),
        ("1234", "1,234"),
        ("Text with 1234567 numbers", "Text with 1,234,567 numbers")
    ]
    
    for input_text, expected in test_cases:
        result = formatter.process(input_text)
        status = "✓" if result == expected else "✗"
        print(f"  {status} '{input_text}' -> '{result}' (期望: '{expected}')")


def test_latex_processor():
    """测试LaTeX处理器"""
    print("\n测试LaTeX处理器...")
    processor = LatexProcessor()
    
    # 测试\textbf移除
    test_cases = [
        (r"\textbf{Hello}", "Hello"),
        (r"\textbf{Hello World}", "Hello World"),
        (r"Normal text \textbf{bold} here", "Normal text bold here"),
        (r"No \textbf here", r"No \textbf here")
    ]
    
    for input_text, expected in test_cases:
        result = processor.remove_textbf(input_text)
        status = "✓" if result == expected else "✗"
        print(f"  {status} '{input_text}' -> '{result}' (期望: '{expected}')")
    
    # 测试引用移除
    cite_test_cases = [
        (r"~\cite{abc, def}", ""),
        (r"Text ~\cite{abc} here", "Text  here"),
        (r"No cite here", "No cite here")
    ]
    
    for input_text, expected in cite_test_cases:
        result = processor.remove_cite(input_text)
        status = "✓" if result == expected else "✗"
        print(f"  {status} '{input_text}' -> '{result}' (期望: '{expected}')")


def test_markdown_processor():
    """测试Markdown处理器"""
    print("\n测试Markdown处理器...")
    processor = MarkdownProcessor()
    
    test_cases = [
        (r"\(x + y\)", "$x + y$"),
        (r"\[x^2 + y^2 = z^2\]", "$$x^2 + y^2 = z^2$$"),
        (r"Normal \(inline\) and \[block\] math", "Normal $inline$ and $$block$$ math")
    ]
    
    for input_text, expected in test_cases:
        result = processor.convert_math_delimiters(input_text)
        status = "✓" if result == expected else "✗"
        print(f"  {status} '{input_text}' -> '{result}' (期望: '{expected}')")


def test_mermaid_processor():
    """测试Mermaid处理器"""
    print("\n测试Mermaid处理器...")
    processor = MermaidProcessor()
    
    test_cases = [
        ("[Start]", '["Start"]'),
        ("[Process]", '["Process"]'),
        ("[End]", '["End"]'),
        ("No brackets", "No brackets")
    ]
    
    for input_text, expected in test_cases:
        result = processor.add_quotes_to_nodes(input_text)
        status = "✓" if result == expected else "✗"
        print(f"  {status} '{input_text}' -> '{result}' (期望: '{expected}')")


def main():
    """运行所有测试"""
    print("开始测试重构后的Workflow功能...\n")
    
    test_bracket_converter()
    test_number_formatter()
    test_latex_processor()
    test_markdown_processor()
    test_mermaid_processor()
    
    print("\n所有测试完成！")


if __name__ == "__main__":
    main() 