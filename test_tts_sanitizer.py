import unittest
from tts_sanitizer import sanitize_for_tts, TTSSanitizer

class TestTTSSanitizer(unittest.TestCase):
    
    def setUp(self):
        # 创建净化器实例
        self.sanitizer = TTSSanitizer()
    
    def test_remove_markdown(self):
        """测试Markdown格式移除功能"""
        test_cases = [
            ("# 标题", "标题"),
            ("## 二级标题", "二级标题"),
            ("**粗体文本**", "粗体文本"),
            ("*斜体文本*", "斜体文本"),
            ("__下划线文本__", "下划线文本"),
            ("`行内代码`", "行内代码"),
            ("[链接文本](https://example.com)", "链接文本"),
            ("![图片](image.jpg)", "图片"),
            ("- 列表项1\n- 列表项2", "列表项1 列表项2"),
            ("1. 第一项\n2. 第二项", "第一项 第二项"),
            ("> 引用文本", "引用文本"),
            ("---", ""),
        ]
        
        for input_text, expected in test_cases:
            result = self.sanitizer.remove_markdown(input_text)
            # 清理多余空格进行比较
            result = ' '.join(result.split())
            self.assertEqual(result, expected)
    
    def test_clean_emoticons(self):
        """测试颜文字清理功能"""
        test_cases = [
            ("你好(๑•̀ㅂ•́)و✧世界", "你好世界"),
            ("测试~(≧▽≦)/~表情", "测试表情"),
            ("简单符号!@#$%", "简单符号"),
            ("单个符号: 这里有一个冒号", "单个符号 这里有一个冒号"),
        ]
        
        for input_text, expected in test_cases:
            result = self.sanitizer.clean_emoticons(input_text)
            # 清理多余空格进行比较
            result = ' '.join(result.split())
            self.assertEqual(result, expected)
    
    def test_math_symbols_preserved(self):
        """测试数学符号保留功能"""
        test_cases = [
            "a² + b² = c²",
            "√2 ≈ 1.414",
            "∑(i=1到n)i = n(n+1)/2",
            "x ∈ R",
            "α + β = γ",
            "f(x) = ∫ₐᵇ g(t)dt",
            "P(A ∩ B) = P(A) × P(B|A)",
        ]
        
        for input_text in test_cases:
            result = self.sanitizer.sanitize(input_text)
            # 确保所有数学符号都被保留
            for char in input_text:
                if self.sanitizer.is_math_symbol(char):
                    self.assertIn(char, result)
    
    def test_combined_functionality(self):
        """测试综合功能"""
        test_cases = [
            (
                "# 数学公式说明\n这是一个**重要**的公式：a² + b² = c²，也称为勾股定理。(๑•̀ㅂ•́)و✧", 
                "数学公式说明 这是一个重要的公式：a² + b² = c²，也称为勾股定理。"
            ),
            (
                "## 物理公式\n爱因斯坦的质能方程：E = mc²，其中c是光速。~(≧▽≦)/~", 
                "物理公式 爱因斯坦的质能方程：E = mc²，其中c是光速。"
            ),
            (
                "### 化学方程式\n水的电解：2H₂O → 2H₂ + O₂。反应条件是通电。٩(๑>◡<๑)۶", 
                "化学方程式 水的电解：2H₂O → 2H₂ + O₂。反应条件是通电。"
            ),
        ]
        
        for input_text, expected in test_cases:
            result = sanitize_for_tts(input_text)
            self.assertEqual(result, expected)
    
    def test_empty_and_special_cases(self):
        """测试边界情况"""
        test_cases = [
            ("", ""),  # 空字符串
            ("   ", ""),  # 只有空格
            ("!@#$%^&*()", ""),  # 只有特殊字符
            ("纯文本测试", "纯文本测试"),  # 没有需要净化的内容
        ]
        
        for input_text, expected in test_cases:
            result = sanitize_for_tts(input_text)
            self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()