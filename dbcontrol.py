import sqlite3
from logger import logger
class db:

    con = sqlite3.connect('db/Module.db')
    cur = con.cursor()
    checktablesql = 'CREATE TABLE IF NOT EXISTS MODULELIST(id INTEGER PRIMARY KEY AUTOINCREMENT,modulename VARCHAR(20) not NULL UNIQUE,moduleaction VARCHAR(20) not NULL,TIME int not NULL);'
    cur.execute(checktablesql)
    cur.close()
    def modulemod(self,modulename,moduleaction,time):
        checkmodulesql = "select id from MODULELIST WHERE modulename = '"+modulename+"' "
        cursor = self.con.cursor()
        cursor.execute(checkmodulesql)
        count = len(cursor.fetchall())

        if count == 0:
            modulesql = "INSERT INTO MODULELIST VALUES (NULL,'"+modulename+"','"+moduleaction+"','"+time+"')"
        else:
            modulesql = "UPDATE MODULELIST SET moduleaction = '"+moduleaction+"', TIME = '"+time+"' where modulename = '"+modulename+"'"
        logger.log.info(modulesql)
        print modulesql
        cursor.execute(modulesql)
        self.con.commit()
        cursor.close()

    def modulelist(self):
        cursor = self.con.cursor()
        listsql ='select modulename,moduleaction,time from MODULElist '
        cursor.execute(listsql)
        return cursor.fetchall()
        cursor.close()
