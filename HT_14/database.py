import sqlite3
from pathlib import Path

class Database(object):

	def data_base_create(self):
		con = sqlite3.connect(Path(__file__).parent/ 'bankomat.db')
		cur = con.cursor()
		cur.execute('''
		CREATE TABLE IF NOT EXISTS users (
			id integer PRIMARY KEY AUTOINCREMENT,
			username text NOT NULL,
			password text NOT NULL,
			role text DEFAULT user,
			UNIQUE(username,password)
		);
		''')

		# ente data to users table
		cur.execute("""
		   	INSERT OR IGNORE INTO users 
		    (username, password, role) 
		    VALUES (
		        'user1',
		        'user1',
		        'user'
		    )
		""")

		insert_user2 = """
		    INSERT OR IGNORE INTO users 
		    (username, password, role) 
		    VALUES (
		        'user2',
		        'user2',
		        'user'
		    )
		"""
		insert_user3 = """
		    INSERT OR IGNORE INTO users 
		    (username, password, role) 
		    VALUES (
		        'admin',
		        'admin',
		        'incasator'
		    )
		"""

		cur.execute(insert_user2)
		cur.execute(insert_user3)

		# create balance table
		cur.execute('''
		CREATE TABLE IF NOT EXISTS balance (
			user_id integer,
			amount integer NOT NULL DEFAULT 0,
			UNIQUE(user_id)
			FOREIGN KEY (user_id) REFERENCES users (id)
		);
		''')

		insert_for_user1 = """
		    INSERT OR IGNORE INTO balance 
		    (user_id, amount) 
		    VALUES (
		       	1,
		        400
		    )
		"""
		insert_for_user2 = """
		    INSERT OR IGNORE INTO balance 
		    (user_id, amount) 
		    VALUES (
		        2,
		        600
		    )
		"""
		cur.execute(insert_for_user1)
		cur.execute(insert_for_user2)

		# creating cash table
		cur.execute('''
		CREATE TABLE IF NOT EXISTS cash (
			banknote text NOT NULL,
			value integer NOT NULL,
			UNIQUE(banknote)	
		);
		''')
		
		cur.execute("INSERT OR IGNORE INTO cash (banknote, value) VALUES ('10',99)")
		cur.execute("INSERT OR IGNORE INTO cash (banknote, value) VALUES ('20',99)")
		cur.execute("INSERT OR IGNORE INTO cash (banknote, value) VALUES ('50',99)")
		cur.execute("INSERT OR IGNORE INTO cash (banknote, value) VALUES ('100',99)")
		cur.execute("INSERT OR IGNORE INTO cash (banknote, value) VALUES ('200',99)")
		cur.execute("INSERT OR IGNORE INTO cash (banknote, value) VALUES ('500',99)")
		cur.execute("INSERT OR IGNORE INTO cash (banknote, value) VALUES ('1000',99)")

		# creating transactons table
		cur.execute('''
		CREATE TABLE IF NOT EXISTS transactions (
			user_id integer NOT NULL,
			text_transaction text NOT NULL,
			FOREIGN KEY (user_id) REFERENCES users (id)
		);
		''')

		con.commit()

	def get_cash(self):

		con = sqlite3.connect("bankomat.db")
		cursor = con.cursor()
		cursor.execute("SELECT * FROM cash")
		cash_from_db = cursor.fetchall()
		con.close()

		return cash_from_db

	def get_user_id(self, username):

		con = sqlite3.connect("bankomat.db")
		cursor = con.cursor()
		cursor.execute(f"SELECT id FROM users WHERE username LIKE \"%{username}%\";")
		id_db = cursor.fetchall()[0][0]
		con.close()

		return id_db

	def get_user_balance(self, id_db):

		con = sqlite3.connect("bankomat.db")
		cursor = con.cursor()
		cursor.execute(f"SELECT amount FROM balance WHERE user_id LIKE \"%{id_db}%\";")
		balance = cursor.fetchall()[0][0]
		con.close()

		return balance

	def update_cash(self, i, j):
		con = sqlite3.connect("bankomat.db")
		cursor = con.cursor()
		cursor.execute(f"UPDATE cash SET value = \"{j}\" WHERE banknote == \"{i}\"")
		con.commit()
		con.close()

	def update_balance(self, result, id_db):
		con = sqlite3.connect("bankomat.db")
		cursor = con.cursor()
		cursor.execute(f"UPDATE balance SET amount = \"{result}\" WHERE user_id == \"{id_db}\"")
		con.commit()
		con.close()

	def write_transaction(self, id_db, transaction_value):
		con = sqlite3.connect("bankomat.db")
		cursor = con.cursor()
		cursor.execute("INSERT INTO transactions (user_id,text_transaction) VALUES (?,?)", (id_db,transaction_value))
		con.commit()
		con.close()

	def add_new_user(self, new_username, new_password, new_role):
		con = sqlite3.connect("bankomat.db")
		cursor = con.cursor()
		cursor.execute("INSERT OR IGNORE INTO users (username, password, role) VALUES (?, ?, ?)", (new_username, new_password, new_role))
		con.commit()
		cursor.execute(f"SELECT id FROM users WHERE username LIKE \"%{new_username}%\";")
		id_db = cursor.fetchall()[0][0]
		insert_for_user = f"""
		    INSERT OR IGNORE INTO balance 
		    (user_id, amount) 
		    VALUES (
		        {id_db},
		        0
		    )
		"""
		cursor.execute(insert_for_user)
		con.commit()
		con.close()

	def get_username(self, username):
		con = sqlite3.connect("bankomat.db")
		cursor = con.cursor()
		cursor.execute(f"SELECT username FROM users WHERE username LIKE \"%{username}%\";")
		username_db = cursor.fetchall()[0][0]
		con.close()
		return username_db


	def get_password(self, username):
		con = sqlite3.connect("bankomat.db")
		cursor = con.cursor()
		cursor.execute(f"SELECT password FROM users WHERE username LIKE \"%{username}%\";")
		password_db = cursor.fetchall()[0][0]
		con.close()
		return password_db

	def get_role(self, username):
		con = sqlite3.connect("bankomat.db")
		cursor = con.cursor()
		cursor.execute(f"SELECT role FROM users WHERE username LIKE \"%{username}%\";")
		role_db = cursor.fetchall()[0][0]
		con.close()

		return role_db


