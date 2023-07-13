import sqlite3

studname = 'martin'
findstudent = '%'+studname+'%'
connection = sqlite3.connect("database.db")
cursor = connection.cursor()
count = cursor.execute("SELECT COUNT(id) FROM students")
print(count.fetchall()[0][0])
result = cursor.execute("SELECT id FROM students WHERE name LIKE ?", (findstudent,))
        # for index, row_data in enumerate(result):
        #     self.table.insertRow(index)
        #     for column, data in enumerate(row_data):
        #         self.table.setItem(index, column, QTableWidgetItem(str(data)))

namelist = result.fetchall()
print(namelist)

#if namelist:
#    hits = mainwindow.table.findItems(self.search_student.text(), Qt.MatchFlag.MatchContains)
#    for hit in hits:
#        hit.setSelected(True)

cursor.close()
connection.close()
