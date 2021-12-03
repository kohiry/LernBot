import sqlite3
#* Это файл с основной логикой бота.
#* Здесь мы будем обрабатывать все запросы от нашего клиента
#* Наш клиент будет ООП объектом, с которым мы будем общаться через методы его класса



class client:
    #инициализация класса
    def __init__(self):
        #cur.execute("SELECT * FROM users;")
        #one_result = cur.fetchone()
        #инициализирую базу данных
        self.id = 0
        self.conn = sqlite3.connect('BASE.db', check_same_thread=False)
        self.cur = self.conn.cursor()

    def add_id(self, id):
        self.id = id

    def add_into_base(self, sqlite_insert_query, test=False):
        # ** sql шаблон
        #sqlite_insert_query = """INSERT INTO users
        #                      (userid, budget)
        #                      VALUES
        #                      (1234324234, 1);"""
        self.cur.execute(sqlite_insert_query)
        if not test:
            self.conn.commit()

    def registration(self, test=False): # test используется выше чтобы не коммитить пользователя
        # проверка есть ли userid в таблице users
        info = self.cur.execute('SELECT userid FROM users WHERE userid=?', (int(self.id),))
        if info.fetchone() is None:
            # если человека нету в бд
            self.add_into_base(f"INSERT INTO users(userid, level, task) VALUES({int(self.id)}, 1, 1);")
            return "Added"
        else:
            # если человек есть в бд
            return "Been"




    #далее тут будет находиться вспомогательная информация по классу
    def __str__(self):
        return """
        * Это файл с основной логикой бота.
        * Здесь мы будем обрабатывать все запросы от нашего клиента
        * Наш клиент будет ООП объектом, с которым мы будем общаться через методы его класса
        """


if __name__ == "__main__":
    print(
    """
    * Это файл с основной логикой бота.
    * Здесь мы будем обрабатывать все запросы от нашего клиента
    * Наш клиент будет ООП объектом, с которым мы будем общаться через методы его класса
    **__str__ - выводит string информацию по классу
    """
    )
