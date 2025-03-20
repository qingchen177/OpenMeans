# OpenMeans
OpenMeans是一个开源项目，旨在通过整合开源工具、库和框架的多样化生态系统来增强openManus的创造力。

## 安装
> 前置条件：
> - Conda(可选)
> - Git
> - Node.js/npm
>

### 步骤

#### OpenMeans

```bash
# 新建Conda环境并激活
conda create -n open_means python=3.12
conda activate open_means
# 克隆本项目代码
git clone  https://github.com/qingchen177/OpenMeans.git
cd  OpenMeans
# 安装依赖
pip install -r requirements.txt
```
#### 工具安装

```bash
# 工具安装（可选）

# ++++ 浏览器自动化工具 - 推荐 ++++
playwright install

# ++++ 安装PPTist - 推荐 ++++
cd utils
git clone https://github.com/pipipi-pikachu/PPTist.git
cd PPTist/PPTist
npm install
# 运行
nohup npm run dev > pptist.log 2>&1 &
# 能访问 http://127.0.0.1:5173/ 表示成功运行
```

## 开源协议

本项目采用MIT开源协议，详情请参阅[LICENSE](LICENSE)文件。 

不过项目中使用的第三方工具、库和框架可能使用不同的开源协议，请查阅其官方文档。

下方列出了本项目中一些使用的第三方工具、库和框架的开源协议：

- [PPTist](https://github.com/pipipi-pikachu/PPTist)：[AGPL-3.0 License](https://github.com/pipipi-pikachu/PPTist/blob/master/LICENSE)