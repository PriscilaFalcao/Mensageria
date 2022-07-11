import file_manager  
import sqlite3

con = None

def createSqliteDatabase(path, name):
    print("creating database")
    try:
        if file_manager.isFileOnDisck(path, name) == False:
            con = sqlite3.connect(name)
        else:
            print("not created cause already exists")
        return con
    except:
        print("Error on file " + path + name)

def insert(tableName, mapFields): 
    cur = con.cursor()
    columns = ""
    values = ""
    for field in mapFields:
        columns += field.name + ","
        values  += field.values + "," 
    insertString = "INSERT INTO " + tableName + "(" + columns[0:len(columns) - 1] +") VALUES(?,?,?)"
    insertValue = values[0:len(values) - 1]
    cur.execute("INSERT INTO " + tableName + "(" + columns[0:len(columns) - 1] +") VALUES(?,?,?)", (values[0:len(values) - 1],))
    print ("Insert left " + insertString)
    print ("Insert right " + insertValue)
    con.commit()


#def createTable(name, fields):
