import sqlite3

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
        print count
        if count == 0:
            modulesql = "INSERT INTO MODULELIST VALUES (NULL,'"+modulename+"','"+moduleaction+"','"+time+"')"
        else:
            modulesql = "UPDATE MODULELIST SET moduleaction = '"+moduleaction+"', TIME = '"+time+"' where modulename = '"+modulename+"'"
        print modulesql
        cursor.execute(modulesql)
        self.con.commit()
        cursor.close()
        self.con.close()
db().modulemod('tessst12','rsu2n','12')