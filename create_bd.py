import sqlite3

#with open("BASE.db", "w+") as f:
    #pass

# Создания базы данных, чтобы в случае утраты базы данных, быстро восстановить шаблон


#cur.execute("ВАШ-SQL-ЗАПРОС-ЗДЕСЬ;")



if __name__ == '__main__':
    conn = sqlite3.connect('BASE.db', check_same_thread=False)
    cur = conn.cursor()
    if input("Удалить или создать? Del/Cre") == "Del":
        # созданию таблицу
        cur.execute("DELETE FROM users")

        conn.commit()
        conn.close()
    else:
        # созданию таблицу
        cur.execute("""CREATE TABLE IF NOT EXISTS users(
           userid INT PRIMARY KEY,
           level INT,
           task INT);
        """) #level&task - 3 уровень, 5 задание. Хранится кортеж

        conn.commit()
        conn.close()
