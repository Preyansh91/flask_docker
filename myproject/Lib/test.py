from MySQL import SQL

conn = SQL()

out = conn.check_if_user_registered('preyansh.10607@gmail.com','pshah')
print out

