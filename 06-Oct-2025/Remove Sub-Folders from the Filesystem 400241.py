# Problem: Remove Sub-Folders from the Filesystem - https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        res = []
        prev = ""
        
        for f in folder:
            if not prev or not f.startswith(prev + "/"):
                res.append(f)
                prev = f  
        
        return res