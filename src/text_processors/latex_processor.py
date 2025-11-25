"""
LaTeX文本处理器
处理LaTeX相关的文本转换
"""

import re
from .base import TextProcessor


class LatexProcessor(TextProcessor):
    """LaTeX文本处理器"""
    
    def __init__(self):
        super().__init__(
            name="LaTeX文本处理",
            description="处理LaTeX相关的文本转换"
        )
    
    def remove_textbf(self, text: str) -> str:
        """
        移除LaTeX中的\textbf{}命令，保留其中的内容
        
        Args:
            text: 输入的文本
            
        Returns:
            处理后的文本
        """
        # 匹配\textbf{...}模式，其中...是任意非大括号字符或嵌套的大括号
        pattern = r'\\textbf\{([^{}]*(?:\{[^{}]*\}[^{}]*)*)\}'
        
        def replace_textbf(match):
            # 返回\textbf{}中的内容
            return match.group(1)
        
        return re.sub(pattern, replace_textbf, text)
    
    def remove_cite(self, text: str) -> str:
        """
        移除LaTeX中的引用命令
        
        Args:
            text: 输入的文本
            
        Returns:
            处理后的文本
        """
        # 移除 ~\cite{...} 模式
        pattern = r'~\\cite\{[^{}]+\}'
        return re.sub(pattern, "", text)
    
    def escape_percent(self, text: str) -> str:
        r"""
        将数字后面的%转换为\%
        
        Args:
            text: 输入的文本
            
        Returns:
            处理后的文本
        """
        # 匹配数字后面的%，但不匹配已经转义的\%
        pattern = r'(\d)%(?!\\)'
        return re.sub(pattern, r'\1\\%', text)
    
    def process(self, text: str) -> str:
        """
        处理LaTeX文本（默认移除\textbf{}）
        
        Args:
            text: 输入的文本
            
        Returns:
            处理后的文本
        """
        return self.remove_textbf(text)
    
    def process_with_arg(self, text: str, arg: str) -> str:
        """
        根据参数处理文本
        """
        if arg == "remove_textbf":
            return self.process(text)
        elif arg == "remove_cite":
            return self.remove_cite(text)
        elif arg == "escape_percent":
            return self.escape_percent(text)
        return text
    
    def get_menu_items(self, text: str = "") -> list:
        """获取菜单项"""
        return [
            {
                "title": "移除LaTeX粗体命令",
                "subtitle": "将\\textbf{text}转换为text",
                "arg": "remove_textbf",
                "valid": True,
                "quicklookurl": self.process(text),
                "icon": "imgs/texstudio.svg"
            },
            {
                "title": "移除LaTeX引用命令",
                "subtitle": "将~\\cite{...}转换为空",
                "arg": "remove_cite",
                "valid": True,
                "quicklookurl": self.remove_cite(text),
                "icon": "imgs/texstudio.svg"
            },
            {
                "title": "转义百分号",
                "subtitle": "将数字后的%转换为\\%",
                "arg": "escape_percent",
                "valid": True,
                "quicklookurl": self.escape_percent(text),
                "icon": "imgs/texstudio.svg"
            }
        ] 