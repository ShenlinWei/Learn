import re
from urllib import request


class Spider():
    url="https://www.huya.com/g/xingxiu"
    root_pattern = '<span class="txt">([\s\S]*?)</li>'
    name_pattern = '<i class="nick" title="([\s\S]*?)">'
    num_pattern = '<i class="js-num">([\s\S]*?)</i>'
    def __fetch_content(self):
        r = request.urlopen(Spider.url)
        htmls = r.read()
        htmls = str(htmls,encoding='utf-8')
        return htmls
    
    def __analysis(self,htmls):
        acnhors = []
        root_html = re.findall(Spider.root_pattern,htmls)
        for html in root_html:
            name = re.findall(Spider.name_pattern,html)
            num = re.findall(Spider.num_pattern,html)
            a=1
            anchor = {'name':name,'number':num}
            acnhors.append(anchor)
        # print(acnhors)
        return acnhors

    def __refine(self,acnhors):
        l = lambda anchor: {
            'name':anchor['name'][0].strip(),
            'number':anchor['number'][0]
        }
        return map(l,acnhors)

    def __sort(self,acnhors):
        acnhors = sorted(acnhors,key=self.__sort_seed,reverse=True)
        return acnhors
    
    def __sort_seed(self,anchor):
        r=re.findall('\d*', anchor['number'])
        number = float(r[0])
        if '万' in anchor['number']:
            number *= 10000
        return number

    def __show(self,acnhors):
        for rank in range(0,len(acnhors)):
            print('rank ' + str(rank+1)
            +'  :  '+acnhors[rank]['name']
            +'  :  '+acnhors[rank]['number'])

    def go(self):
        htmls = self.__fetch_content()
        acnhors = self.__analysis(htmls)
        acnhors = list(self.__refine(acnhors))
        acnhors = self.__sort(acnhors)
        self.__show(acnhors)


spider = Spider()
spider.go()