#!/usr/bin/env python3
"""
测试文本对比功能
"""

import os
import tempfile
import webbrowser
from text_processors.text_diff import TextDiffProcessor


def test_text_diff():
    """测试文本对比功能"""
    
    # 示例文本
    original_text = """这是第一行
这是第二行 (test)
这是第三行
这是第四行
这是第五行 1234567"""

    processed_text = """这是第一行
这是第二行 （test）
这是第三行
这是第四行
这是第五行 1,234,567"""

    # 创建处理器
    processor = TextDiffProcessor()
    
    # 生成HTML对比
    print("正在生成HTML对比...")
    html_content = processor.generate_html_diff(
        original_text, 
        processed_text, 
        "文本处理对比示例"
    )
    
    # 保存到临时文件
    with tempfile.NamedTemporaryFile(mode='w', suffix='.html', delete=False, encoding='utf-8') as f:
        f.write(html_content)
        temp_file = f.name
    
    print(f"HTML文件已保存到: {temp_file}")
    
    # 在浏览器中打开
    webbrowser.open(f'file://{temp_file}')
    
    print("HTML文件已在浏览器中打开")
    print("按回车键删除临时文件...")
    input()
    
    # 清理临时文件
    os.unlink(temp_file)
    print("临时文件已删除")


def test_with_separator():
    """测试使用分隔符的格式"""
    
    # 使用 ||| 分隔符的格式
    combined_text = """这是第一行
这是第二行 (test)
这是第三行|||这是第一行
这是第二行 （test）
这是第三行"""
    
    processor = TextDiffProcessor()
    result = processor.process(combined_text)
    
    # 保存到临时文件
    with tempfile.NamedTemporaryFile(mode='w', suffix='.html', delete=False, encoding='utf-8') as f:
        f.write(result)
        temp_file = f.name
    
    print(f"HTML文件已保存到: {temp_file}")
    webbrowser.open(f'file://{temp_file}')


if __name__ == "__main__":
    print("选择测试模式:")
    print("1. 直接对比")
    print("2. 使用分隔符格式")
    
    choice = input("请输入选择 (1 或 2): ").strip()
    
    if choice == "1":
        test_text_diff()
    elif choice == "2":
        test_with_separator()
    else:
        print("无效选择") 