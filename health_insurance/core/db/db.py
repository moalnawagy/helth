from mysql.connector import connect, Error



def db(*sqlqueries):
    myhost = 'localhost'
    mydatabase = 'healthInsurance'
    myuser = 'root'
    mypass = 'Mayo@192771'

    con = connect(host = myhost,
                  database = mydatabase,
                  user = myuser,
                  password = mypass)
    cur = con.cursor()
    try:
        for query in sqlqueries:
            cur.execute(query)
    except Error as e:
        print("Eception", e)
        return 'failed'
    try:
        records = cur.fetchall()
    except:
        records = 0
    con.commit()
    con.close()
    return records