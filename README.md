# GitLab代码全文检索小工具
本工具是为了快速检索GitLab代码片段，原理是获取全部项目后循环查找包含`keyword`的文件，需自行准备拥有查询权限的private-token
## 运行方法
```python
python main.py $url $private-token $keyword
```