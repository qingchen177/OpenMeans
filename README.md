# OpenMeans
OpenMeans 是一个开源项目，致力于通过整合多样化的开源工具、库和框架，提升 openManus 的创造力和功能。

## 快速开始
选择一个稳定分支或者标签，按照分支中的README.md安装环境和依赖。

然后配置使用的 LLM API

```bash
cp config/config.example.toml config/config.toml
```

示例：

```toml
# 全局 LLM 配置
[llm]
model = "gpt-4o"
base_url = "https://api.openai.com/v1"
api_key = "sk-..."  # 替换为真实 API 密钥
max_tokens = 4096
temperature = 0.0

# 可选特定 LLM 模型配置
[llm.vision]
model = "gpt-4o"
base_url = "https://api.openai.com/v1"
api_key = "sk-..."  # 替换为真实 API 密钥
```

最后运行命令即可体验！

```bash
python main.py
```

### 分支

- main: 主要开发分支，不建议直接使用此分支
- first_hackathon: 黑客松分支，有OpenManus的基础功能
- first_hackathon_marp: 增加了Marp生态圈，可以渲染markdown，生成ppt、pdf等格式的演示文稿

### 标签

- first_hackathon_v1：黑客松分支的稳定版本

## 项目计划

### PPT

目前计划实现AI全自动生成PPT的功能，达到生成的PPT经过少量调整就可以直接用于演示的效果。

#### 方案1：PPTist

开源项目[PPTist](https://github.com/pipipi-pikachu/PPTist)
由于是纯前端项目，没有API接口，不能通过Function Call的方式让模型调用

方式1：要么跑在本地，通过浏览器自动化工具（如playwright）调用PPTist生成PPT
方式2：对PPTist进行二次开发，增加API接口，让模型调用


#### 方案2：Marp

目前已经实现了Marp的基本功能，可以通过markdown文件生成PPT、PDF等格式的演示文稿。
