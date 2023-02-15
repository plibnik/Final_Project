import mysql.connector

powerdb = mysql.connector.connect(
  host="localhost",
  user="daemon_user", # REPLACE this later with SCM-pulled credentials!
  password="yourpassword", # REPLACE this too with SCM-pulled credentials!
  database="ENERGY_MONITORING"
)

print(mydb) 

# change string to test push to GitHub 
