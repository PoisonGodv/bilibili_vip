from typing import Dict, Any, Optional
import time
from config.config import LLM_CONFIG
from tools.logger import logger
from tools.LLM.gemini import GeminiAPI
from tools.LLM.deepseek import DeepSeekAPI

class ModelManager:
    """模型管理器，处理不同模型的调用和故障切换"""
    
    def __init__(self):
        self.models = {
            'gemini': GeminiAPI,
            'deepseek': DeepSeekAPI
        }
        self.primary_model_name = LLM_CONFIG['primary_model']
        self.fallback_model_name = LLM_CONFIG['fallback_model']
        self.max_retries = LLM_CONFIG['max_retries']
        self.retry_delay = LLM_CONFIG['retry_delay']
        
        # 检查配置的模型是否存在
        if self.primary_model_name not in self.models:
            raise ValueError(f"主模型 '{self.primary_model_name}' 不存在")
        if self.fallback_model_name not in self.models:
            raise ValueError(f"备用模型 '{self.fallback_model_name}' 不存在")
    
    def ask(self, question: str, timeout: Optional[int] = 30) -> str:
        """使用配置的模型回答问题，如果失败则切换到备用模型
        
        Args:
            question: 要问的问题
            timeout: 请求超时时间（秒）
            
        Returns:
            str: 模型回答
        """
        # 首先尝试主模型
        current_model_name = self.primary_model_name
        retries = 0
        
        while retries <= self.max_retries:
            try:
                model_class = self.models[current_model_name]
                model = model_class()
                logger.info(f"使用 {current_model_name} 模型回答问题")
                return model.ask(question, timeout)
            except Exception as e:
                logger.warning(f"{current_model_name} 模型调用失败: {str(e)}")
                retries += 1
                
                # 如果已经达到最大重试次数或者当前使用的是备用模型，则切换模型
                if retries > self.max_retries or current_model_name == self.fallback_model_name:
                    if current_model_name == self.primary_model_name:
                        logger.info(f"切换到备用模型 {self.fallback_model_name}")
                        current_model_name = self.fallback_model_name
                        retries = 0  # 切换模型后重置重试计数
                    else:
                        # 如果备用模型也失败，则抛出异常
                        raise Exception(f"所有模型调用失败，无法获取回答")
                else:
                    # 等待一段时间后重试
                    logger.info(f"等待 {self.retry_delay} 秒后重试...")
                    time.sleep(self.retry_delay) 