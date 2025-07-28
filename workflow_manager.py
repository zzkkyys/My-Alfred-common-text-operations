"""
Workflow管理器
统一管理所有文本处理器和Alfred Workflow操作
"""

import os
import sys
from typing import Dict, List, Optional
from workflow import Workflow3
from text_processors import (
    BracketConverter,
    NumberFormatter,
    LatexProcessor,
    MarkdownProcessor,
    MermaidProcessor
)


class WorkflowManager:
    """Workflow管理器"""
    
    def __init__(self):
        self.wf = Workflow3()
        self.processors = self._init_processors()
        # self.action_handlers = self._init_action_handlers()
    
    def _init_processors(self) -> Dict[str, object]:
        """初始化所有文本处理器"""
        return {
            'bracket_converter': BracketConverter(),
            'number_formatter': NumberFormatter(),
            'latex_processor': LatexProcessor(),
            'markdown_processor': MarkdownProcessor(),
            'mermaid_processor': MermaidProcessor()
        }
    
    def show_main_menu(self):
        """显示主菜单"""
        # 添加所有处理器的菜单项
        for processor in self.processors.values():
            for item in processor.get_menu_items():
                self.wf.add_item(
                    title=item['title'],
                    subtitle=item.get('subtitle', ''),
                    arg=item['arg'],
                    valid=item.get('valid', True)
                )
        
        self.wf.send_feedback()
        
    def handle_action(self, action: str, text: str = ""):
        for processor in self.processors.values():
            for item in processor.get_menu_items():
                if item['arg'] == action:
                    result = processor.process(text)
                    return result
                
        return None
    

        
        
