# 588. Design In-Memory File System

from collections import defaultdict


class FileNode:
    def __init__(self):                        
        self.isfile = False
        self.content = ''
        self.children = defaultdict(FileNode)  

class FileSystem:
    def __init__(self):
        self.root = FileNode()        
        
    def ls(self, path: str) -> List[str]:
        curr = self.root
        for p in path.split('/'):
            if not p:
                continue
            curr = curr.children[p]
        if curr.isfile:
            return [p]
        return sorted(curr.children.keys())        
        
    def mkdir(self, path: str) -> None:
        curr = self.root
        for p in path.split('/'):
            if not p:
                continue
            curr = curr.children[p]

    def addContentToFile(self, filePath: str, content: str) -> None:
        curr = self.root
        for p in filePath.split('/'):
            if not p:
                continue
            curr = curr.children[p]
        curr.isfile = True
        curr.content += content

    def readContentFromFile(self, filePath: str) -> str:
        curr = self.root
        for p in filePath.split('/'):
            if not p:
                continue
            curr = curr.children[p]
        return curr.content
        