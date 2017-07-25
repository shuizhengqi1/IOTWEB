#coding=utf-8
import sys
from logger import logger
import re
import json
from dbcontrol import db
sys.path.append('module')
db = db()

class moduleIMPORT:
    def run(self,list):
        importlist = []
        for moduleInfo in list:
            modulename = moduleInfo[0]
            moduleaction = moduleInfo[1]
            try:
                modulei = __import__(modulename)
                logger.log.info("import   "+modulename+ "    success")
            except Exception,e:
                    print '请检查是否模块填写错误'
                    logger.log.error("import"+modulename+"    error,please check")
            moduleimp = {'modulename':modulename,'moduleaction':moduleaction,'module':modulei}
            importlist.append(moduleimp)
        print '-----import success-----'
        return importlist
class moduleRUN:
    def run(self,list):
        print '-----start run-----'
        for moduleInfo in list:
            module = moduleInfo['module']
            modulename = moduleInfo['modulename']
            moduleaction = moduleInfo['moduleaction']
            try:
                rel = getattr(module, moduleaction)
                logger.log.info("execute  "+modulename+"    "+moduleaction+"  success")
                print rel()
            except Exception, e:
                print '请检查方法名是否错误'
                logger.log.error("execute   "+modulename+"     "+moduleaction+"    error,please check")
        print '-----end run-----'

if __name__ == '__main__':
    print "-----start-----"
    db.modulemod('test1','run','1')
    db.modulemod('test2','getresult','1')
    list = db.modulelist()
    importlist = moduleIMPORT().run(list)
    moduleRUN().run(importlist)
