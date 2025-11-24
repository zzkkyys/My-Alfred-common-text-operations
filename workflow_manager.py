"""
Workflow管理器
统一管理所有文本处理器和Alfred Workflow操作
"""
import hashlib
import time
import os
import sys
from typing import Dict, List, Optional
from workflow import Workflow3
from text_processors import (
    CommonConverter,
    NumberFormatter,
    LatexProcessor,
    MarkdownProcessor,
    MermaidProcessor,
    TextDiffProcessor
)


class WorkflowManager:
    """Workflow管理器"""
    
    def __init__(self):
        self.wf = Workflow3()
        self.processors = self._init_processors()
        self.diff_processor = TextDiffProcessor()
    
    def _init_processors(self) -> Dict[str, object]:
        """初始化所有文本处理器"""
        return {
            'common_converter': CommonConverter(),
            'number_formatter': NumberFormatter(),
            'latex_processor': LatexProcessor(),
            'markdown_processor': MarkdownProcessor(),
            'mermaid_processor': MermaidProcessor()
        }
    
    def show_main_menu(self, text: str = ""):
        """显示主菜单"""
        
        if not os.path.exists('temp_html'):
            os.makedirs('temp_html')
        else:
            for html_file in os.listdir('temp_html'):
                os.remove(os.path.join('temp_html', html_file))
        
        
        # 添加所有处理器的菜单项
        for processor in self.processors.values():
            for item in processor.get_menu_items(text=text):
                self.wf.add_item(
                    title=item['title'],
                    subtitle=item.get('subtitle', ''),
                    arg=item['arg'],
                    valid=item.get('valid', True),
                    quicklookurl=self.generate_quicklookurl(text=text, process_result=item.get('quicklookurl', '')) 
                )
        
        self.wf.send_feedback()
        
    def generate_quicklookurl(self, text: str = "", process_result: str = ""):
        """生成quicklookurl"""
        html_content = self.diff_processor.process(text, process_result)
        html_path = f"temp_html/{time.time()}-{hashlib.md5(text.encode() + process_result.encode()).hexdigest()}.html"
        with open(html_path, 'w') as f:
            f.write(html_content)
        return html_path
        
        
    def handle_action(self, action: str, text: str = ""):
        for processor in self.processors.values():
            for item in processor.get_menu_items():
                if item['arg'] == action:
                    result = processor.process_with_arg(text, arg=item['arg'])
                    return result
                
        return None
    

        
        
