# GitLab代码全文检索小工具
本工具是为了快速检索GitLab代码片段，原理是获取全部项目后循环查找包含`keyword`的文件，需自行准备拥有查询权限的private-token
## 运行方法
### 环境准备(基于python3.9)
```python
python -m venv venv
source venv/bin/active
```
### 安装依赖
```python
python -m pip install -r requirements.txt
```
### 执行命令
```python
python main.py $url $private-token $keyword
```
