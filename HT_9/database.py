import sqlite3
from pathlib import Path


def data_base_create():
	con = sqlite3.connect(Path(__file__).parent/ 'bankomat.db')
	cur = con.cursor()
	cur.execute('''
	CREATE TABLE IF NOT EXISTS users (
		id integer PRIMARY KEY AUTOINCREMENT,
		username text NOT NULL,
		password text NOT NULL,
		role text DEFAULT user
	);

	''')

	# ente data to users table
	cur.execute("""
	   	INSERT INTO users 
	    (username, password, role) 
	    VALUES (
	        'user1',
	        'user1',
	        'user'
	    )
	""")

	insert_user2 = """
	    INSERT INTO users 
	    (username, password, role) 
	    VALUES (
	        'user2',
	        'user2',
	        'user'
	    )
	"""
	insert_user3 = """
	    INSERT INTO users 
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
		user_id integer NOT NULL,
		amount integer NOT NULL DEFAULT 0,
		FOREIGN KEY (user_id) REFERENCES users (id)
	);
	''')

	insert_for_user1 = """
	    INSERT INTO balance 
	    (user_id, amount) 
	    VALUES (
	       	2,
	        400
	    )
	"""
	insert_for_user2 = """
	    INSERT INTO balance 
	    (user_id, amount) 
	    VALUES (
	        3,
	        600
	    )
	"""
	cur.execute(insert_for_user1)
	cur.execute(insert_for_user2)

	# creating cash table
	cur.execute('''
	CREATE TABLE IF NOT EXISTS cash (
		id integer NOT NULL,
		banknotes text NOT NULL
		
	);
	''')

	str_cash = str({"10": 3, "20": 0, "50": 0, "100": 1, "200": 1, "500": 2, "1000": 5})
	cur.execute("INSERT INTO cash (id,banknotes) VALUES (1,?)", [str_cash])


	# creating transactons table
	cur.execute('''
	CREATE TABLE IF NOT EXISTS transactions (
		user_id integer NOT NULL,
		text_transaction text NOT NULL,
		FOREIGN KEY (user_id) REFERENCES users (id)
	);
	''')

	con.commit()

