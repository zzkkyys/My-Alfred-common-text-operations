# Alfred 通用文本处理 Workflow

一个功能丰富的Alfred workflow，用于处理各种文本转换和格式化操作。

## 1. 功能特性

### 🔤 基础文本处理
- **括号转换 (EN-CN)**: 将英文括号 `()` 转换为中文括号 `（）`
- **格式化千分数字**: 为数字添加千位分隔符，如 `1932131` → `1,932,131`

### 📝 LaTeX 相关
- **移除LaTeX粗体命令**: 将 `\textbf{text}` 转换为 `text`
- **去除引用**: 处理LaTeX中的引用命令

### 📊 Mermaid 相关
- **为节点加引号**: 在Mermaid图表中为节点文字添加引号

### 📄 Markdown 相关
- **替换数学公式指示符**: 将 `\[ \]` 替换为 `$$`

## 2. 安装方法

1. 下载 `.alfredworkflow` 文件
2. 双击文件安装到Alfred
3. 确保`Environment Variables`中设置了正确的`PYTHON_PATHS`，多种python路径可以使用冒号`:`连接。



## 3. 功能详解

### 括号转换 (EN-CN)
将文本中的英文括号转换为中文括号，适用于中文文档排版。

**示例:**
```
输入: This is a (test) example
输出: This is a （test） example
```

### 格式化千分数字
为数字添加千位分隔符，提高大数字的可读性。

**示例:**
```
输入: 1932131
输出: 1,932,131

输入: 1234567.89
输出: 1,234,567.89
```

### 移除LaTeX粗体命令
移除LaTeX文档中的 `\textbf{}` 命令，保留其中的文本内容。

**示例:**
```
输入: \textbf{hello world}
输出: hello world

输入: This is \textbf{bold text} in a sentence.
输出: This is bold text in a sentence.

输入: \textbf{text with {nested} braces}
输出: text with {nested} braces
```

### Mermaid节点加引号
为Mermaid图表中的节点文字添加引号，提高可读性。

**示例:**
```
输入: [节点名称]
输出: ["节点名称"]
```

### Markdown数学公式处理
替换Markdown中的数学公式指示符。

**示例:**
```
输入: \[ E = mc^2 \]
输出: $$ E = mc^2 $$
```


## 贡献

欢迎提交Issue和Pull Request来改进这个workflow！

## 许可证

MIT License
