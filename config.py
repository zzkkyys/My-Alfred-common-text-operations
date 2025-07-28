"""
配置文件
集中管理Workflow的设置和常量
"""

# Workflow基本信息
WORKFLOW_INFO = {
    "name": "Alfred Common Text Operations",
    "version": "2.0.0",
    "description": "常用文本处理工具集合"
}

# 文本处理器配置
PROCESSOR_CONFIG = {
    "bracket_converter": {
        "name": "括号转换(EN-CN)",
        "description": "将英文括号转换为中文括号",
        "enabled": True
    },
    "number_formatter": {
        "name": "格式化千分数字",
        "description": "将数字按千位加逗号分隔符",
        "enabled": True
    },
    "latex_processor": {
        "name": "LaTeX文本处理",
        "description": "处理LaTeX相关的文本转换",
        "enabled": True
    },
    "markdown_processor": {
        "name": "Markdown文本处理",
        "description": "处理Markdown相关的文本转换",
        "enabled": True
    },
    "mermaid_processor": {
        "name": "Mermaid代码处理",
        "description": "处理Mermaid图表相关的文本转换",
        "enabled": True
    }
}

# 动作映射配置
ACTION_MAPPING = {
    # 直接处理动作
    "change_brackets(EN-CN)": {
        "processor": "bracket_converter",
        "method": "process",
        "copy_to_clipboard": True
    },
    "format_thousand_separator": {
        "processor": "number_formatter",
        "method": "process",
        "copy_to_clipboard": True
    },
    "remove_textbf": {
        "processor": "latex_processor",
        "method": "remove_textbf",
        "copy_to_clipboard": True
    },
    
    # 菜单动作
    "latex": {
        "type": "menu",
        "processor": "latex_processor"
    },
    "mermaid": {
        "type": "menu",
        "processor": "mermaid_processor"
    },
    "markdown": {
        "type": "menu",
        "processor": "markdown_processor"
    },
    
    # 输出到stdout的动作
    "latex_rm_cite": {
        "processor": "latex_processor",
        "method": "remove_cite",
        "output": "stdout"
    },
    "markdown-replace-math-indicator": {
        "processor": "markdown_processor",
        "method": "convert_math_delimiters",
        "output": "stdout"
    },
    "mermaid-quote": {
        "processor": "mermaid_processor",
        "method": "add_quotes_to_nodes",
        "output": "stdout"
    }
}

# 日志配置
LOGGING_CONFIG = {
    "level": "INFO",
    "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    "file": None  # 设置为None表示不输出到文件
}

# 缓存配置
CACHE_CONFIG = {
    "enabled": True,
    "max_age": 3600,  # 1小时
    "session_cache": True
} 