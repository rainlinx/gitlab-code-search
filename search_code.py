import gitlab
import gitlab.const


def init(url, token):
    return gitlab.Gitlab(url, token)


def search(gl, keyword):
    projects = gl.projects.list(iterator=True)
    for project in projects:
        for item in project.search(gitlab.const.SearchScope.BLOBS, keyword, iteraotr=True):
            print(item)
