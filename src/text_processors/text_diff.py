"""
文本对比处理器
生成原始文本和处理后文本的行级和字符级HTML对比
"""

import difflib
import html



class TextDiffProcessor:
    """文本对比处理器"""
    
    def _highlight_char_diff(self, old_line: str, new_line: str) -> tuple:
        """
        高亮显示两行之间的字符级差异
        
        Args:
            old_line: 原始行
            new_line: 新行
            
        Returns:
            (highlighted_old, highlighted_new) 元组
        """
        s = difflib.SequenceMatcher(None, old_line, new_line)
        
        old_parts = []
        new_parts = []
        
        for tag, i1, i2, j1, j2 in s.get_opcodes():
            old_text = html.escape(old_line[i1:i2])
            new_text = html.escape(new_line[j1:j2])
            
            if tag == 'equal':
                old_parts.append(old_text)
                new_parts.append(new_text)
            elif tag == 'replace':
                old_parts.append(f'<span class="char-removed">{old_text}</span>')
                new_parts.append(f'<span class="char-added">{new_text}</span>')
            elif tag == 'delete':
                old_parts.append(f'<span class="char-removed">{old_text}</span>')
            elif tag == 'insert':
                new_parts.append(f'<span class="char-added">{new_text}</span>')
        
        return ''.join(old_parts), ''.join(new_parts)
    
    def generate_html_diff_for_small_window(self, original_text: str, processed_text: str, title: str = "文本对比") -> str:
        original_lines = original_text.splitlines()
        processed_lines = processed_text.splitlines()
        
        # 使用 SequenceMatcher 来配对行
        s = difflib.SequenceMatcher(None, original_lines, processed_lines)
        
        formatted_lines = []
        for tag, i1, i2, j1, j2 in s.get_opcodes():
            if tag == 'equal':
                # 未改变的行
                for line in original_lines[i1:i2]:
                    content = html.escape(line)
                    line_html = f'<div class="line unchanged">  {content}</div>'
                    formatted_lines.append(line_html)
            elif tag == 'replace':
                # 修改的行 - 显示字符级差异
                for old_line, new_line in zip(original_lines[i1:i2], processed_lines[j1:j2]):
                    old_highlighted, new_highlighted = self._highlight_char_diff(old_line, new_line)
                    formatted_lines.append(f'<div class="line removed">- {old_highlighted}</div>')
                    formatted_lines.append(f'<div class="line added">+ {new_highlighted}</div>')
                
                # 处理行数不匹配的情况
                if i2 - i1 > j2 - j1:
                    for line in original_lines[i1 + (j2 - j1):i2]:
                        content = html.escape(line)
                        formatted_lines.append(f'<div class="line removed">- {content}</div>')
                elif j2 - j1 > i2 - i1:
                    for line in processed_lines[j1 + (i2 - i1):j2]:
                        content = html.escape(line)
                        formatted_lines.append(f'<div class="line added">+ {content}</div>')
            elif tag == 'delete':
                # 删除的行
                for line in original_lines[i1:i2]:
                    content = html.escape(line)
                    formatted_lines.append(f'<div class="line removed">- {content}</div>')
            elif tag == 'insert':
                # 新增的行
                for line in processed_lines[j1:j2]:
                    content = html.escape(line)
                    formatted_lines.append(f'<div class="line added">+ {content}</div>')

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
            .char-added {{
                background: #acf2bd;
                font-weight: bold;
            }}
            .char-removed {{
                background: #fdb8c0;
                font-weight: bold;
                text-decoration: line-through;
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
