# TTS 文本净化工具 

一个文本净化(Text Purification)工具，专为文本转语音(TTS)应用设计，能够智能净化AI生成的文本，去除可能导致朗读不自然的元素，同时保留数学公式等重要内容。

## 功能特点

- **移除Markdown格式**：去除标题、粗体、斜体、代码块、链接等Markdown标记
- **清理颜文字和表情符号**：智能识别并移除由特殊字符组成的颜文字
- **保留数学公式**：特别保留数学符号（如 ≌√∈²³ 等）使其能被正确朗读
- **优化文本流**：处理多余的空白字符，使文本更加流畅

## 安装

这个工具是纯Python实现，无需额外依赖，直接下载即可使用。

```bash
# 克隆或下载本仓库
git clone https://github.com/SRInternet/TTS_Sanitizer.git
cd TTS_Sanitizer
```

## 使用方法

### 基本使用

```python
from tts_sanitizer import sanitize_for_tts

# 待净化的文本
text = "你好呀😊，这是一个**粗体**和*斜体*的测试，数学公式：a² + b² = c²。"

# 净化文本
cleaned_text = sanitize_for_tts(text)

print(cleaned_text)  # 输出: 你好呀，这是一个粗体和斜体的测试，数学公式：a² + b² = c²。
```

### 作为类使用

```python
from tts_sanitizer import TTSSanitizer

# 创建净化器实例
sanitizer = TTSSanitizer()

# 待净化的文本
text = "# 标题\n这是包含`代码`的正文，还有数学公式：x ∈ R。颜文字测试：(๑•̀ㅂ•́)و✧"

# 净化文本
cleaned_text = sanitizer.sanitize(text)

print(cleaned_text)  # 输出: 这是包含代码的正文，还有数学公式：x ∈ R。颜文字测试：
```

## 技术原理

### 1. Markdown处理

使用正则表达式识别并移除各种Markdown格式标记：
- 标题标记 (`#`, `##`, etc.)
- 强调标记 (`**`, `*`, `__`, `_`)
- 代码块和行内代码
- 链接和图片引用
- 列表、引用和分割线

### 2. 颜文字检测与移除

通过以下方式识别颜文字：
- 检查字符的Unicode类别（符号、其他等）
- 维护常见颜文字组成字符列表
- 使用启发式算法检测连续的特殊字符序列

### 3. 数学符号保留

特别保留以下数学符号：
- Unicode数学符号类别（Sm）中的字符
- 常见数学符号，如：`≌√∈²³⁴⁵⁶⁷⁸⁹₀₁₂₃₄₅₆₇₈₉±×÷≤≥≠≈≡∫∑∏√∞∂∆πφθ`

## 测试示例

运行以下命令可以查看工具的测试结果：

```bash
python tts_sanitizer.py
```

工具包含多个测试用例，覆盖了Markdown格式、数学公式和颜文字等各种情况。

## 应用场景

- AI对话系统的语音输出优化
- 聊天机器人的TTS文本预处理
- 文档朗读应用
- 任何需要将AI生成内容转换为自然语音的场景

## 自定义扩展

如果需要调整净化规则，可以修改`TTSSanitizer`类中的相关方法：
- 修改`_init_patterns()`方法调整Markdown识别规则
- 更新`is_math_symbol()`方法添加新的数学符号
- 调整`is_emoji_or_emoticon()`方法修改颜文字识别策略

## 许可证

本项目采用MIT许可证 - 详情请查看LICENSE文件

## 更新日志

### v1.0.0
- 初始版本发布
- 支持Markdown格式移除
- 支持颜文字清理
- 支持数学符号保留
