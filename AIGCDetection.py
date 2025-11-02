# aigc_detector.py
import os
import pickle

class AIGCDetector:
    """
    AIGC 文本检测器（仅推理）
    使用已训练的 One-Class SVM 模型判断文本是否为 AI 生成
    """
    
    def __init__(self, model_path='AIGCDetectModel.pkl'):
        self.model_path = model_path
        self.model = None
        self.load_model()

    def load_model(self):
        """加载已训练的模型"""
        if not os.path.exists(self.model_path):
            raise FileNotFoundError(f"模型文件未找到: {self.model_path}")
        
        with open(self.model_path, 'rb') as f:
            self.model = pickle.load(f)
        print(f"✅ 模型已从 '{self.model_path}' 加载")

    def isAIGC(self, text):
        """
        判断输入文本是否为 AIGC（AI生成内容）
        :param text: str, 输入文本
        :return: bool, True 表示是 AIGC，False 表示是人发言
        """
        if not isinstance(text, str) or not text.strip():
            raise ValueError("输入必须是非空字符串")
        
        text = text.strip()
        pred = self.model.predict([text])[0]  # 1: 人发言（正常），-1: AIGC（异常）
        print(f"预测结果: {pred}(1: 人类发言，-1: AIGC)")
        return pred == -1  # True if AIGC

    def predict(self, text):
        """
        输出详细结果
        """
        text = text.strip()
        is_aigc = self.isAIGC(text)
        score = self.model.decision_function([text])[0]
        label = "❌ AIGC文本" if is_aigc else "✅ 人类发言"
        print(f"文本: {text}")
        print(f"结果: {label}")
        print(f"决策分: {score:.3f} (越低越可能是AI生成)")

from sys import argv
def main():
    detector = AIGCDetector()
    for text in argv[1:]:
        detector.predict(text)
        

if __name__ == '__main__':
    main()