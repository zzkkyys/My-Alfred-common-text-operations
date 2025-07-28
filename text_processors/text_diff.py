"""
文本对比处理器
生成原始文本和处理后文本的行级HTML对比
"""

import difflib
import html



class TextDiffProcessor:
    """文本对比处理器"""
    
    
    def generate_html_diff_for_small_window(self, original_text: str, processed_text: str, title: str = "文本对比") -> str:
        original_lines = original_text.splitlines()
        processed_lines = processed_text.splitlines()
        diff_lines = list(difflib.ndiff(original_lines, processed_lines))

        formatted_lines = []
        for line in diff_lines:
            prefix = line[0]
            content = html.escape(line[2:])
            if prefix == '+':
                line_html = f'<div class="line added">+ {content}</div>'
            elif prefix == '-':
                line_html = f'<div class="line removed">- {content}</div>'
            elif prefix == '?':
                continue  # 忽略 ? 行，或你也可以突出显示
            else:
                line_html = f'<div class="line unchanged">  {content}</div>'
            formatted_lines.append(line_html)

        return f"""<!DOCTYPE html>
    <html lang="zh-CN">
    <head>
        <meta charset="UTF-8">
        <style>
            body {{
                font-family: monospace;
                font-size: 12px;
                margin: 0;
                padding: 8px;
                background: #ffffff;
                color: #333;
            }}
            .line {{
                white-space: pre-wrap;
                word-break: break-word;
                padding: 1px 2px;
            }}
            .added {{
                background: #e6ffed;
                color: #22863a;
            }}
            .removed {{
                background: #ffeef0;
                color: #b31d28;
            }}
            .unchanged {{
                color: #586069;
            }}
            .title {{
                font-weight: bold;
                margin-bottom: 6px;
                font-size: 14px;
            }}
        </style>
    </head>
    <body>
        <div class="title">{html.escape(title)}</div>
        {''.join(formatted_lines)}
    </body>
    </html>"""
    
    def _format_lines(self, lines: list, section_type: str) -> str:
        """格式化行显示"""
        formatted_lines = []
        for i, line in enumerate(lines, 1):
            line_class = "unchanged"
            if section_type == "original" and not line.strip():
                line_class = "removed"
            elif section_type == "processed" and not line.strip():
                line_class = "added"
            
            formatted_lines.append(f'<div class="line {line_class}">{i:4d}: {line}</div>')
        
        return '\n'.join(formatted_lines)
    
    def _generate_stats(self, original_lines: list, processed_lines: list, diff_lines: list) -> str:
        """生成统计信息"""
        original_count = len(original_lines)
        processed_count = len(processed_lines)
        added_count = sum(1 for line in diff_lines if line.startswith('+ '))
        removed_count = sum(1 for line in diff_lines if line.startswith('- '))
        changed_count = sum(1 for line in diff_lines if line.startswith('? '))
        
        return f"""
            <span>原始行数: {original_count}</span>
            <span>处理后行数: {processed_count}</span>
            <span>新增行数: {added_count}</span>
            <span>删除行数: {removed_count}</span>
            <span>修改行数: {changed_count}</span>
        """
    
    def process(self, original_text: str, processed_text: str) -> str:
        """
        处理文本（这里需要原始文本和处理后文本）
        
        Args:
            text: 输入的文本（格式：原始文本|||处理后文本）
            
        Returns:
            HTML格式的对比结果
        """
        
        return self.generate_html_diff_for_small_window(original_text, processed_text)
