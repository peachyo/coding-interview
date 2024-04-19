# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        
        def get_hostname(url):
            return url.split('/')[2]
        
        start_hostname = get_hostname(startUrl)
        visited = set()
        def dfs(start, path):
            visited.add(start)
            urls = htmlParser.getUrls(start)
            for url in urls: 
                if get_hostname(url) == start_hostname and url not in visited:
                    dfs(url, visited)
        dfs(startUrl, visited)
        return visited