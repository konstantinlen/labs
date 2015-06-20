import psycopg2


flag = 1

conn1 = psycopg2.connect("dbname='D1' user='postgres' host='localhost' password='brut0303'")
conn2 = psycopg2.connect("dbname='D2' user='postgres' host='localhost' password='brut0303'")


cur1 = conn1.cursor()
cur2 = conn2.cursor()
conn1.commit()
conn2.commit()

try:
    cur1.execute("""BEGIN""")
    cur2.execute("""BEGIN""")

    cur1.execute("""INSERT INTO t1 VALUES (3,'Yegor')""")
    cur2.execute("""INSERT INTO t1 VALUES (3,'Yegor')""")
    
    cur1.execute("""PREPARE TRANSACTION 'trFirst'""")
    cur2.execute("""PREPARE TRANSACTION 'trSecond'""")
    
except:
    print "Error DataBase!"
    cur1.execute("""ROLLBACK PREPARED 'trFirst'""")
    cur2.execute("""ROLLBACK PREPARED 'trSecond'""")
    flag = 0
    
if flag == 0:
    print "FAIL, Transaction!"
    cur1.execute("""ROLLBACK PREPARED 'trFirst'""")
    cur2.execute("""ROLLBACK PREPARED 'trSecond'""")
else:
    print "Success, Transaction!"
    cur1.execute("""COMMIT PREPARED 'trFirst'""")
    conn1.commit()
    conn2.commit()
    cur2.execute("""COMMIT PREPARED 'trSecond'""")

conn1.close()
conn2.close()

   



#    cur2.execute("""INSERT INTO t1 VALUES (1,'Sasha')""")
#    conn2.commit()
#cur.execute("""INSERT INTO t1 VALUES (2,'Alex')""")
#conn.commit()


    
