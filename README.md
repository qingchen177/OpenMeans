# OpenMeans
OpenMeans 是一个开源项目，致力于通过整合多样化的开源工具、库和框架，提升 openManus 的创造力和功能。

> 此分支在first_hackathon分支基础上添加了[Marp-CLI](https://github.com/marp-team/marp-cli)，可以进行HTML、PDF、PPT的生成。

## 安装
> 前置环境：
> - Git
> - Conda(推荐)
> - Node.js(必须)
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
# 工具安装

# ++++ Marp-CLI - 必须 ++++
conda install -c conda-forge nodejs
npm install --save-dev @marp-team/marp-cli

# ++++ 浏览器自动化工具 - 推荐 ++++
playwright install
```

## 开源协议

本项目采用MIT开源协议，详情请参阅[LICENSE](LICENSE)文件。 

项目中使用的第三方工具、库和框架可能使用不同的开源协议，请查阅其官方文档。