import sqlite3

class db:
    con = sqlite3.connect('db/Module.db')
    checktablesql = 'CREATE TABLE IF NOT EXISTS MODULELIST(id INTEGER PRIMARY KEY AUTOINCREMENT,modulename VARCHAR(20) not NULL,moduleaction VARCHAR(20) not NULL,TIME int not NULL);'
    con.execute(checktablesql)
    def moduleadd(self,modulename,moduleaction,time):
        checkmodulesql = "select id from MODULELIST WHERE modulename = '"+modulename+"' "
        result = self.con.execute(checkmodulesql)
        print result.fetchall()
        print len(result.fetchall())
        print result.rowcount
        if result.rowcount == 0:
            addmodulesql = "INSERT INTO MODULELIST VALUES (NULL,'"+modulename+"','"+moduleaction+"','"+time+"')"
            print addmodulesql
            self.con.execute(addmodulesql)
            self.con.commit()
            self.con.close()
db().moduleadd('test12','rsun','1')