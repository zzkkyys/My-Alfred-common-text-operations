# %%
import os
import sys
from workflow import Workflow3

# %%
def main(wf):

    wf.add_item(title="括号转换(EN-CN)", arg="change_brackets(EN-CN)", valid=True)
    wf.add_item(title="格式化千分数字", subtitle="convert 1932131 to 1,932,131", arg="format_thousand_separator", valid=True)
    wf.add_item(title="移除LaTeX粗体命令", subtitle="将\\textbf{text}转换为text", arg="remove_textbf", valid=True)
    wf.add_item(title="latex文本处理", arg="latex", valid=True)
    wf.add_item(title="mermaid代码处理", arg="mermaid", valid=True)
    wf.add_item(title="markdown文本处理", arg="markdown", valid=True)
    wf.send_feedback()



if __name__ == u"__main__":

    # inputs = sys.argv
    # print("hello, this is argv:", inputs, file=sys.stderr)

    wf = Workflow3()
    sys.exit(wf.run(main))
    


