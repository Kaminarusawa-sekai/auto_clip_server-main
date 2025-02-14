import sqlite3

VIDEO_DB="DataBase/DB/video.db"
def create_db_and_tables():
    # 连接到SQLite数据库（如果数据库不存在，则会自动创建）
    conn = sqlite3.connect(VIDEO_DB)
    
    # 创建一个游标对象
    cursor = conn.cursor()
    
    # 创建表id2name
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS id2name (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL
        )
    ''')
    
    # 创建表description
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS description (
            id INTEGER PRIMARY KEY,
            description TEXT NOT NULL
        )
    ''')
    
    # 创建表hotpot
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS hotpot (
            id INTEGER PRIMARY KEY,
            hotpot TEXT NOT NULL
        )
    ''')
    
    # 创建表hotstart
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS hotstart (
            id INTEGER PRIMARY KEY,
            hotstart TEXT NOT NULL
        )
    ''')

    # 提交操作
    conn.commit()
    
    # 关闭与数据库的连接
    conn.close()

def insert_id_name_data(id,name):
    # 重新连接到SQLite数据库
    conn = sqlite3.connect(VIDEO_DB)
    cursor = conn.cursor()
    
    # 向表id2name插入数据
    cursor.execute('''
        INSERT INTO id2name (id, name) VALUES
        (?, ?)
    ''',[id,name])
    
    # 提交操作
    conn.commit()
    
    # 关闭与数据库的连接
    conn.close()


def insert_id_description_data(id,description):
    # 重新连接到SQLite数据库
    conn = sqlite3.connect(VIDEO_DB)
    cursor = conn.cursor()
    

    # 向表description插入数据
    cursor.execute('''
        INSERT INTO description (id, description) VALUES
        (?, ?)
    ''',[id,description])
    
    # 提交操作
    conn.commit()
    
    # 关闭与数据库的连接
    conn.close()


def insert_hotpot_data(id,hotpot):
    # 重新连接到SQLite数据库
    conn = sqlite3.connect(VIDEO_DB)
    cursor = conn.cursor()
    

    # 向表description插入数据
    cursor.execute('''
        INSERT INTO hotpot (id, hotpot) VALUES
        (?, ?)
    ''',[id,hotpot])
    
    # 提交操作
    conn.commit()
    
    # 关闭与数据库的连接
    conn.close()


def insert_hotstart_data(id,hotstart):
    # 重新连接到SQLite数据库
    conn = sqlite3.connect(VIDEO_DB)
    cursor = conn.cursor()
    

    # 向表description插入数据
    cursor.execute('''
        INSERT INTO hotstart (id, hotstart) VALUES
        (?, ?)
    ''',[id,hotstart])
    
    # 提交操作
    conn.commit()
    
    # 关闭与数据库的连接
    conn.close()


def get_hotstarts():
    conn = sqlite3.connect(VIDEO_DB)
    cursor = conn.cursor()
    

    # 向表description插入数据
    cursor.execute('''SELECT * FROM hotstart''')
    
    rows = cursor.fetchall()
    
    # 关闭与数据库的连接
    conn.close()

    return rows

def get_hotpots():
    conn = sqlite3.connect(VIDEO_DB)
    cursor = conn.cursor()
    

    # 向表description插入数据
    cursor.execute('''SELECT * FROM hotpot''')
    
    rows = cursor.fetchall()
    
    # 关闭与数据库的连接
    conn.close()
    
    return rows

def get_video_names():
    conn = sqlite3.connect(VIDEO_DB)
    cursor = conn.cursor()
    

    # 向表description插入数据
    cursor.execute('''SELECT * FROM id2name''')
    
    rows = cursor.fetchall()
    
    # 关闭与数据库的连接
    conn.close()
    
    return rows

def get_video_descriptions():
    conn = sqlite3.connect(VIDEO_DB)
    cursor = conn.cursor()
    

    # 向表description插入数据
    cursor.execute('''SELECT * FROM description''')
    
    rows = cursor.fetchall()
    
    # 关闭与数据库的连接
    conn.close()
    
    return rows



if __name__ == '__main__':
    # 创建数据库和表格
    create_db_and_tables()
    
    # # 插入数据
    # insert_id_description_data
    # insert_id_description_data