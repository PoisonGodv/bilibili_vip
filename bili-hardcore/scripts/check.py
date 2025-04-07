from config.config import API_KEY_GEMINI, API_KEY_DEEPSEEK, LLM_CONFIG
from tools.logger import logger

def check():
    """检查配置是否正确"""
    primary_model = LLM_CONFIG.get('primary_model')
    fallback_model = LLM_CONFIG.get('fallback_model')
    
    # 检查主模型API密钥
    if primary_model == 'gemini' and not API_KEY_GEMINI:
        logger.error("程序终止: 主模型为Gemini，但未配置Gemini API密钥")
        exit()
    elif primary_model == 'deepseek' and not API_KEY_DEEPSEEK:
        logger.error("程序终止: 主模型为DeepSeek，但未配置DeepSeek API密钥")
        exit()
    
    # 检查备用模型API密钥
    if fallback_model == 'gemini' and not API_KEY_GEMINI:
        logger.warning("警告: 备用模型为Gemini，但未配置Gemini API密钥，故障切换可能不可用")
    elif fallback_model == 'deepseek' and not API_KEY_DEEPSEEK:
        logger.warning("警告: 备用模型为DeepSeek，但未配置DeepSeek API密钥，故障切换可能不可用")
    
    logger.info(f"当前使用的模型: 主模型 - {primary_model}, 备用模型 - {fallback_model}")