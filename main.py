"""
重构后的主入口文件
使用WorkflowManager统一管理所有文本处理功能
"""

import os
import sys
import argparse
from workflow_manager import WorkflowManager
from workflow.notify import notify

def main(wf):
    """主函数 - 显示主菜单"""
    manager = WorkflowManager()
    manager.show_main_menu()


def handle_query():
    """处理查询 - 根据动作参数执行相应的处理"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--action", type=str, required=True)
    args = parser.parse_args()
    
    # 获取输入文本
    text = os.environ.get("text", "")
    
    # 创建Workflow管理器并处理动作
    manager = WorkflowManager()
    result = None
    try:
        result = manager.handle_action(args.action, text)
    except Exception as e:
        notify("处理失败", str(e))
        return
    
    print(result)
    notify("Processed successfully", result)


if __name__ == "__main__":
    # 检查是否有命令行参数
    if len(sys.argv) > 1:
        # 有参数时，执行查询处理
        handle_query()
    else:
        # 无参数时，显示主菜单
        from workflow import Workflow3
        wf = Workflow3()
        sys.exit(wf.run(main)) 
        
        