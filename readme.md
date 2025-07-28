# Alfred 通用文本处理 Workflow

一个功能丰富的Alfred workflow，用于处理各种文本转换和格式化操作。

## 功能特性

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

## 安装方法

1. 下载 `.alfredworkflow` 文件
2. 双击文件安装到Alfred
3. 确保已安装Python 3和相关依赖包

## 使用方法

### 方法一：Universal Action
1. 选择任意文本
2. 按 `⌘ + Space` 打开Alfred
3. 选择"通用文本处理"
4. 选择相应的处理选项

### 方法二：快捷键触发
1. 复制要处理的文本到剪贴板
2. 使用设置的快捷键（默认为 `⌘ + Space`）
3. 选择相应的处理选项

### 方法三：直接输入
1. 在Alfred中输入文本
2. 选择相应的处理选项

## 功能详解

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

## 技术实现

- **主要脚本**: `query.py` - 处理各种文本转换功能
- **菜单脚本**: `main.py` - 提供功能选择菜单
- **工具模块**: `utils/` - 包含各种专用处理模块
- **工作流框架**: 基于 `workflow3.py` 构建

## 依赖要求

- Python 3.6+
- Alfred 4+
- 相关Python包：
  - `pyperclip` - 剪贴板操作
  - `workflow3` - Alfred workflow框架

## 配置说明

workflow使用以下环境变量：
- `text`: 要处理的文本内容
- `action`: 要执行的操作类型

## 故障排除

1. **Python路径问题**: 确保Alfred能找到正确的Python解释器
2. **权限问题**: 确保workflow有访问剪贴板的权限
3. **依赖缺失**: 安装所需的Python包

## 更新日志

### v1.1
- 添加移除LaTeX粗体命令功能
- 优化正则表达式匹配
- 改进用户反馈机制

### v1.0
- 初始版本发布
- 支持基础文本处理功能
- 支持LaTeX、Mermaid、Markdown处理

## 贡献

欢迎提交Issue和Pull Request来改进这个workflow！

## 许可证

MIT License

---

**作者**: AY  
**创建时间**: 2022-10-17  
**最后更新**: 2024 