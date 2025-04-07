import json
import os
from config.config import LLM_CONFIG

def switch_model():
    """切换主要使用的模型"""
    config_file = os.path.join(os.path.expanduser('~'), '.bili-hardcore', 'model_config.json')
    
    print("当前模型配置：")
    print(f"- 主模型: {LLM_CONFIG['primary_model']}")
    print(f"- 备用模型: {LLM_CONFIG['fallback_model']}")
    
    # 切换主模型和备用模型
    new_primary = LLM_CONFIG['fallback_model']
    new_fallback = LLM_CONFIG['primary_model']
    
    # 更新配置
    updated_config = {
        'primary_model': new_primary,
        'fallback_model': new_fallback,
        'max_retries': LLM_CONFIG['max_retries'],
        'retry_delay': LLM_CONFIG['retry_delay']
    }
    
    # 保存配置
    try:
        os.makedirs(os.path.dirname(config_file), exist_ok=True)
        with open(config_file, 'w') as f:
            json.dump(updated_config, f, indent=2)
        print(f"\n已切换模型配置:")
        print(f"- 主模型: {new_primary}")
        print(f"- 备用模型: {new_fallback}")
        print("\n重启程序后生效。")
    except Exception as e:
        print(f"保存配置失败: {str(e)}")

if __name__ == "__main__":
    switch_model() 