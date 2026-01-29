from db.connection import connect

def main():
    db = connect('projects')
    cursor = db.cursor()
    cursor.execute("SELECT * FROM projects")
    result = cursor.fetchall()
    print(result)
    db.close()

if __name__ == "__main__":
    main()