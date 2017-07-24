#coding=utf-8
import sys
import re
import json
sys.path.append('module')
class moduleLIST:
  def getlist(self):
    list = []
    modulelist = open('config/modules').readlines()
    for line in modulelist:
        modulename = line.replace('\n', '').split(' ')[0]
        try:
            moduleaction = line.replace('\n', '').split(' ')[1]
        except:
            moduleaction = 'run'
        moduleInfo = {'modulename':modulename,'moduleaction':moduleaction}
        list.append(moduleInfo)
    return list

class moduleIMPORT:
    def run(self,list):
        importlist = []
        for moduleInfo in list:
            modulename = moduleInfo['modulename']
            moduleaction = moduleInfo['moduleaction']
            try:
                modulei = __import__(modulename)
            except Exception,e:
                    print '请检查是否方法填写错误'
            moduleimp = {'modulename':modulei,'moduleaction':moduleaction}
            importlist.append(moduleimp)
        print '-----import success-----'
        return importlist
class moduleADD:
    def run(self):
        nameadd = sys.argv[1]
        if len(sys.argv) == 3:
            actionadd = sys.argv[2]
        else:
            actionadd = ''
        contentadd = nameadd+' '+actionadd
        module = open('config/modules','a')
        module.write(contentadd)
class moduleRUN:
    def run(self,list):
        print '-----start run-----'
        for moduleInfo in list:
            modulename = moduleInfo['modulename']
            moduleaction = moduleInfo['moduleaction']
            try:
                rel = getattr(modulename, moduleaction)
                print rel()
            except Exception, e:
                print '请检查模块名是否错误'
if __name__ == '__main__':
    print "-----start-----"
    if len(sys.argv) > 1:
        moduleADD().run()
    list = moduleLIST().getlist()
    importlist = moduleIMPORT().run(list)
    moduleRUN().run(importlist)
