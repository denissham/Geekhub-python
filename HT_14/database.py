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

