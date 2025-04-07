# Bili-Hardcore

B 站硬核会员自动答题工具，利用 Gemini API 和 DeepSeek API 实现智能答题功能，支持模型故障切换。

## 使用说明

### 方式一：从 release 下载 exe 文件
1. 下载 exe 文件
2. 双击 exe 运行或在命令行中执行 `.\bili-hardcore.exe`

### 方式二：从源码运行
1. 克隆项目到本地

```bash
git clone [项目地址]
cd bili-hardcore
```

2. 安装依赖

```bash
pip install -r requirements.txt
```
3. 运行主程序

```bash
python bili-hardcore/main.py
```

## 使用流程
1. 输入自己的 Gemini API Key 和 DeepSeek API Key（两个都需要配置才能实现完全的故障切换）
2. 扫描二维码登录
3. 输入要进行答题的分类
4. 查看并输入图形验证码
5. 程序会自动开始答题流程

## 附加功能

### 切换模型
程序默认使用 Gemini 作为主模型，DeepSeek 作为备用模型。如需切换，请运行：

```bash
python bili-hardcore/main.py --switch-model
```

此命令会将当前的备用模型设置为主模型，原主模型设置为备用模型。修改后需要重启程序生效。

### 故障切换机制
程序内置了故障切换机制，当主模型调用失败时，会自动切换到备用模型。具体行为：

1. 当主模型调用失败时，会先尝试重试（默认最多3次）
2. 如果重试仍然失败，则切换到备用模型
3. 如果备用模型也失败，程序会报错并提示用户

## 注意事项
- 使用前请确保已配置正确的 API Key（Gemini 和 DeepSeek）
- 程序仅调用 B 站接口和相关 AI API，不会上传任何个人信息
- 首次输入 API Key 和登录后，会将信息保存到 `~/.bili-hardcore`，下次运行时会自动读取。如遇到奇怪问题，请先清空此文件夹重新运行软件
- 注意需要切换至相应 API 允许的地区运行，否则会被拦截
- 请合理使用，遵守 B 站相关规则