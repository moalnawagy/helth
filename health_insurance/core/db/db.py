from mysql.connector import connect, Error


def db(sqlquery):
    myhost = 'sql4.freemysqlhosting.net'
    mydatabase = 'sql4462324'
    myuser = 'sql4462324'
    mypass = 'wrGVCKBsfH'

    con = connect(host = myhost,
                  database = mydatabase,
                  user = myuser,
                  password = mypass)
    cur = con.cursor()
    try:
        cur.execute(sqlquery)
    except Error as e:
        print("Eception", e)
    try:
        records = cur.fetchall()
    except:
        records = 0
    con.commit()
    con.close()
    return records