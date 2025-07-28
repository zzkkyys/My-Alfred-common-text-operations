import re, argparse, sys, os

def convert_math_delimiters(text):
    """
    将 LaTeX 风格的数学公式界定符替换为美元符号风格。

    参数:
    text (str): 包含 LaTeX 公式的输入字符串。

    返回:
    str: 界定符被替换后的字符串。
    """
    # 替换行内公式 \( ... \) 为 $ ... $
    # 使用非贪婪匹配 (.*?) 来确保只匹配到最近的 \)
    text = re.sub(r'\\\((.*?)\\\)', r'$\1$', text)

    # 替换行间公式 \[ ... \] 为 $$ ... $$
    # 使用非贪婪匹配 (.*?) 来确保只匹配到最近的 \]
    # 需要转义方括号，因为它们在正则表达式中有特殊含义
    text = re.sub(r'\\\[(.*?)\\\]', r'$$\1$$', text)

    return text

if __name__ == u"__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('--action', type=str)
    args = parser.parse_args()

    text = os.environ["text"]
    
    print(args, file=sys.stderr)
    
    if args.action == "markdown-replace-math-indicator":
        # 转换数学公式分隔符
        converted_text = convert_math_delimiters(text)
        print(converted_text, file=sys.stdout)