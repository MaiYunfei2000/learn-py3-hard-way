# ex47 自动化测试 的子文件

# 有点不熟悉了请复习ex44e的「组合」
class Room(object):
    
    def __init__(self, name, description):
        self.name = name
        self.description = description
        # set self.paths to an instance of class dict
        self.paths = {}
    
    def go(self, direction):
        # get(direction, None): ???
        return self.paths.get(direction, None)
    
    def add_paths(self, paths):
        # update(): ???
        self.paths.update(paths)