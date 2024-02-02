import logging

import gitlab
import gitlab.const
import concurrent.futures
import pandas as pd
from datetime import datetime

logging.basicConfig(level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
data = {'项目ID': [], '项目名': [], '项目路径': [], '文件': [], '路径': [], '行号': [], '分支': [], '内容': []}


# 初始化GitLab连接
def init(url, token):
    return gitlab.Gitlab(url, token, keep_base_url=True)


# 根据关键字查询所有仓库
def search(gl, keyword):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        projects = gl.projects.list(iterator=True)
        all_task = [executor.submit(search_in_project, project, keyword) for project in projects]
        concurrent.futures.wait(all_task)
    file_name = f'search_result_{datetime.now().strftime("%Y%m%d_%H_%M_%S")}.xlsx'
    pd.DataFrame(data, columns=['项目ID', '项目名', '项目路径', '文件', '路径', '行号', '分支', '内容']) \
        .to_excel(file_name, 'result')
    logger.info(f'搜索完毕，结果见{file_name}')


# 根据关键字查询单个仓库
def search_in_project(project, keyword):
    for item in project.search(gitlab.const.SearchScope.BLOBS, keyword, iterator=True):
        data['项目ID'].append(item['project_id'])
        data['项目名'].append(project.name)
        data['项目路径'].append(project.name_with_namespace)
        data['文件'].append(item['filename'])
        data['路径'].append(item['path'])
        data['行号'].append(item['startline'])
        data['分支'].append(item['ref'])
        data['内容'].append(item['data'])
