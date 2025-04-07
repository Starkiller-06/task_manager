from PyQt5.QtWidgets import (QApplication, 
                             QWidget, 
                             QLabel, 
                             QPushButton,  
                             QLineEdit, 
                             QVBoxLayout,
                             QMessageBox,
                             QTimeEdit,
                             QHBoxLayout,
                             QListWidget,
                             QComboBox)
from PyQt5.QtChart import QChart, QPieSeries, QChartView
from PyQt5.QtCore import *
from PyQt5.uic import loadUi
import sys
import mysql.connector
from datetime import *

db_conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="SQLRuiz06X!",
        database="tasks_py",
        auth_plugin="mysql_native_password")

if db_conn.is_connected():
    cursor = db_conn.cursor(buffered=True)
    
class PopUp(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Add Task")
        self.setGeometry(520, 200, 300, 100) 
        self.setStyleSheet("""
            background-color: #FCFBEA
        """)
        
        layout = QVBoxLayout()
        
        self.task_name = QLineEdit()
        layout.addWidget(QLabel("Task Name:"))
        layout.addWidget(self.task_name)
        
        self.due_date = QLineEdit()
        layout.addWidget(QLabel("Due date: (yyyy-mm-dd)"))
        layout.addWidget(self.due_date)

        self.due_time = QTimeEdit()
        layout.addWidget(QLabel("Time"))
        layout.addWidget(self.due_time)
        
        self.priority = QComboBox()
        self.priority.addItems(["Normal", "Medium", "High"])
        layout.addWidget(QLabel("priority:"))
        layout.addWidget(self.priority)
        
        self.status = QComboBox()
        self.status.addItems(["Pending", "In Progress", "Completed"])
        layout.addWidget(QLabel("Status:"))
        layout.addWidget(self.status)
        
        self.setLayout(layout)
        
        self.comments = QLineEdit()
        layout.addWidget(QLabel("Comments:"))
        layout.addWidget(self.comments)
        
        self.confirm_button = QPushButton("Confirm")
        layout.addWidget(self.confirm_button)
        self.confirm_button.setStyleSheet("""
            background-color: #C6D4E7;
            border-style: outset;     
            border-color: blue;
            border-radius: 10px;    
            font: bold 11px;  
            padding: 5px                
        """)
        
    def confirm_msg(self):
        message = QMessageBox()
        message.setWindowTitle("Task Added")
        message.setText("Your task has been added")
        message.setIcon(QMessageBox.Information)
        m = message.exec_()

class UpdateTaskPopUp(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Edit Task")
        self.setGeometry(520, 200, 300, 100) 
        self.setStyleSheet("""
            background-color: #FCFBEA
        """)
        
        layout = QVBoxLayout()
        
        self.task_name = QLineEdit()
        layout.addWidget(QLabel("Task Name:"))
        layout.addWidget(self.task_name)
        
        self.due_date = QLineEdit()
        layout.addWidget(QLabel("Due date: (yyyy-mm-dd)"))
        layout.addWidget(self.due_date)

        self.due_time = QTimeEdit()
        layout.addWidget(QLabel("Time"))
        layout.addWidget(self.due_time)
        
        self.priority = QComboBox()
        self.priority.addItems(["Normal", "Medium", "High"])
        layout.addWidget(QLabel("priority:"))
        layout.addWidget(self.priority)
        
        self.status = QComboBox()
        self.status.addItems(["Pending", "In Progress", "Completed"])
        layout.addWidget(QLabel("Status:"))
        layout.addWidget(self.status)
        
        self.setLayout(layout)
        
        self.comments = QLineEdit()
        layout.addWidget(QLabel("Comments:"))
        layout.addWidget(self.comments)
        
        self.confirm_button = QPushButton("Save Changes")
        layout.addWidget(self.confirm_button)
        self.confirm_button.setStyleSheet("""
            background-color: #C6D4E7;
            border-style: outset;     
            border-color: blue;
            border-radius: 10px;    
            font: bold 11px;  
            padding: 5px                
        """)
    
    def confirm_msg(self):
        message = QMessageBox()
        message.setWindowTitle("Task Updated")
        message.setText("Your task has been updated")
        message.setIcon(QMessageBox.Information)
        m = message.exec_()

class WeekTaskListPopUp(QWidget):
    def __init__(self,data,dateSelected):
        super().__init__()
        
        self.setWindowTitle("Week Task List")
        self.setGeometry(520, 200, 300, 100) 
        self.setStyleSheet("""
            background-color: #FCFBEA
        """)

        self.main_layout = QHBoxLayout(self)
        
        self.days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        
        
        for day in self.days_of_week:
            day_layout = QVBoxLayout()
            day_label = QLabel(day)
            day_label.setAlignment(Qt.AlignCenter)
            day_list_widget = QListWidget()
            
            filtered_data = []
            
            for task_data in data:
                if task_data[3].strftime("%U") == dateSelected.strftime("%U"):
                    filtered_data.append(task_data)
            for task_data in filtered_data:
                if(task_data[3].strftime("%A")==day):
                    task_info = f"{task_data[2]} | {task_data[3]} | {task_data[4]} | {task_data[5]} | {task_data[6]} | {task_data[7]}"
                    day_list_widget.addItem(task_info)
            
            day_layout.addWidget(day_label)
            day_layout.addWidget(day_list_widget)
            self.main_layout.addLayout(day_layout)

        self.setLayout(self.main_layout)

class MonthTaskListPopUp(QWidget):
    def __init__(self,data,dateSelected):
        super().__init__()
        
        self.setWindowTitle("Month Task List")
        self.setGeometry(520, 200, 300, 100) 
        self.setStyleSheet("""
            background-color: #FCFBEA
        """)

        self.main_layout = QHBoxLayout(self)
        
        self.days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        
        for day in self.days_of_week:
            day_layout = QVBoxLayout()
            day_label = QLabel(day)
            day_label.setAlignment(Qt.AlignCenter)
            day_list_widget = QListWidget()
            
            filtered_data = []
                        
            for task_data in data:
                if task_data[3].strftime("%B") == dateSelected.strftime("%B"):
                    filtered_data.append(task_data)
            for task_data in filtered_data:
                if(task_data[3].strftime("%A")==day):
                    task_info = f"{task_data[2]} | {task_data[3]} | {task_data[4]} | {task_data[5]} | {task_data[6]} | {task_data[7]}"
                    day_list_widget.addItem(task_info)
            
            day_layout.addWidget(day_label)
            day_layout.addWidget(day_list_widget)
            self.main_layout.addLayout(day_layout)

        self.setLayout(self.main_layout)
        
class PieChartPopUp(QWidget):
    def __init__(self,data):
        super().__init__()
        
        self.setWindowTitle("Week Task List")
        self.setGeometry(520, 200, 500, 500) 
        self.setStyleSheet("""
            background-color: #FCFBEA
        """)
        self.setWindowTitle('Completion Chart')
        
        self.main_layout = QHBoxLayout(self)

        in_progress_count = sum(1 for task_data in data if task_data[6] == "In progress")
        completed_count = sum(1 for task_data in data if task_data[6] == "Completed")
        pending_count = sum(1 for task_data in data if task_data[6] == "Pending")
  
        series = QPieSeries()
        series.append("In progress", in_progress_count)
        series.append("Completed", completed_count)
        series.append("Pending", pending_count)
       
        chart = QChart()
        chart.addSeries(series)
        
        pie_chart = QChartView()
        pie_chart.setChart(chart)
        
        self.main_layout.addWidget(pie_chart)
        self.setLayout(self.main_layout)

class Task_manager(QWidget): 
    def __init__(self, user_id, user_name):
        super(Task_manager, self).__init__()
        loadUi("PyCalendarApp.ui", self)
        
        self.w = None
        self.updWindow = None
        self.user_id = user_id
        self.user_name = user_name
        self.year = None
        self.month = None
        self.time_frame = "Day"
                    
        self.dateEdit.hide()
        self.fil_criteria_cbox.hide()
        
        self.chart_btn.clicked.connect(self.show_chart)
        self.month_btn.clicked.connect(self.show_month_task_list)
        self.week_btn.clicked.connect(self.show_week_task_list)
        self.addTaskBtn.clicked.connect(self.show_new_window)
        self.calendar.clicked.connect(self.calendarDateChanged)
        self.UpdButton.clicked.connect(self.show_update_window)
        self.DelButton.clicked.connect(self.deleteTask)
        self.show_user_name.setText(f"Welcome {self.user_name}")
        self.calendar.currentPageChanged.connect(self.handleMonthChanged)
        self.filter_cbox.currentIndexChanged.connect(self.handleFilterChanged)
        self.filterBy_btn.clicked.connect(self.filterTask)
        self.sortBy_btn.clicked.connect(self.sortTasks)
        self.calendarDateChanged()
       
    def handleMonthChanged(self, year, month):
        self.year = year
        self.month = month
        
    def show_new_window(self): 
        self.w = None
        dateSelected = str(self.calendar.selectedDate().toPyDate())
        self.w = PopUp()
        self.w.due_date.setText(dateSelected)
        self.w.confirm_button.clicked.connect(self.AddTask)
        self.w.show()
        
    def AddTask(self, calendar_date):   
        
        u_task = self.w.task_name.text()
        u_due_date = self.w.due_date.text()
        u_due_time = self.w.due_time.time().toPyTime()
        u_priority = self.w.priority.currentText()
        u_status = self.w.status.currentText()
        u_comments = self.w.comments.text()
        
        if u_task == "":
            message = QMessageBox()
            message.setWindowTitle("Error")
            message.setText("All fields are required. Try again.")
            message.setIcon(QMessageBox.Warning)
            message.exec_()
        
        else: 
            query = f"INSERT INTO user_tasks (User_Id, Task_name, Due_date, Due_time, priotity, Status, Comments) VALUES ({self.user_id}, '{u_task}', '{u_due_date}', '{u_due_time}', '{u_priority}', '{u_status}', '{u_comments}')"
            cursor.execute(query)
            db_conn.commit()
            
            self.show_tasks(u_due_date)
            
            self.w.confirm_msg()
            self.w.close()
            self.w = None
   
    def calendarDateChanged(self):
        dateSelected = self.calendar.selectedDate().toPyDate() 
        self.show_tasks(dateSelected)
        
    def show_tasks (self, date):
        self.day_task_list.clear()
        
        query = f"SELECT CONCAT(Task_name,' | ', Due_date,' | ', Due_time, ' | ', Priotity, ' | ', Status, ' | ', Comments) FROM user_tasks WHERE User_Id = {self.user_id} AND due_date = '{date}'"
        cursor.execute(query)
        returned_rows = cursor.fetchall()

        for task_data in returned_rows:
            task_info = ' | '.join(str(item) for item in task_data)
            self.day_task_list.addItem(task_info)
        
    def settingData(self, TaskName):
        query = f"SELECT * FROM user_tasks WHERE User_Id = {self.user_id} AND task_name = '{TaskName}'"
        cursor.execute(query)
        returned_row = cursor.fetchone()
        
        self.task_Id= returned_row[0]
        
        self.updWindow.task_name.setText(returned_row[2]) 
        self.updWindow.due_date.setText(str(returned_row[3]))
        due_time = datetime.strptime(str(returned_row[4]), '%H:%M:%S').time()
        due_datetime = datetime.combine(datetime.today(), due_time)
        self.updWindow.due_time.setTime(due_datetime.time())
        self.updWindow.priority.setCurrentText(returned_row[5]) 
        self.updWindow.status.setCurrentText(returned_row[6]) 
        self.updWindow.comments.setText(returned_row[7])
        self.updWindow.confirm_button.clicked.connect(self.editedTask)
        
    def editedTask(self):
        dateSelected = self.calendar.selectedDate().toPyDate()
        
        n_name = self.updWindow.task_name.text()
        n_due_date = self.updWindow.due_date.text()
        n_due_time = self.updWindow.due_time.time().toPyTime()
        n_priority = self.updWindow.priority.currentText()
        n_status = self.updWindow.status.currentText()
        n_comments = self.updWindow.comments.text()
        
        if n_name == "":
            message = QMessageBox()
            message.setWindowTitle("Error")
            message.setText("All fields are required. Try again.")
            message.setIcon(QMessageBox.Warning)
            message.exec_()
        
        else: 
            query = f"UPDATE user_tasks SET Task_name = '{n_name}', Due_date = '{n_due_date}', Due_time = '{n_due_time}', Priotity = '{n_priority}', Status = '{n_status}', Comments = '{n_comments}' WHERE task_id = '{self.task_Id}' "
            cursor.execute(query)
            db_conn.commit()
            
            self.show_tasks(dateSelected)
            self.updWindow.confirm_msg()
            self.updWindow.close()
            self.updWindow = None
       
    def get_taskName(self, task):
        task_strip = task.strip()
        task_split = task_strip.split("|")
        
        return task_split[0].strip()
    
    def show_chart(self):
        query = f"SELECT * FROM user_tasks WHERE User_Id = {self.user_id}"
        cursor.execute(query)
        returned_rows = cursor.fetchall()
        self.weekTaskList = PieChartPopUp(returned_rows)
        self.weekTaskList.show()
    
    def show_month_task_list(self):
        query = f"SELECT * FROM user_tasks WHERE User_Id = {self.user_id}"
        cursor.execute(query)
        returned_rows = cursor.fetchall()
        dateSelected = self.calendar.selectedDate().toPyDate() 
        self.monthTaskList = MonthTaskListPopUp(returned_rows,dateSelected)
        self.monthTaskList.show()
    
    def show_week_task_list(self):    
        query = f"SELECT * FROM user_tasks WHERE User_Id = {self.user_id}"
        cursor.execute(query)
        returned_rows = cursor.fetchall()
        dateSelected = self.calendar.selectedDate().toPyDate() 
        self.weekTaskList = WeekTaskListPopUp(returned_rows,dateSelected)
        self.weekTaskList.show()
    
    def show_update_window(self):
        try:
            self.updWindow = UpdateTaskPopUp()
            selected_task = self.day_task_list.currentItem().text()
            task_nameSer = self.get_taskName(selected_task)
            self.settingData(task_nameSer)
            self.updWindow.show()
            
        except:
            message = QMessageBox()
            message.setWindowTitle("Update error")
            message.setText("Task not selected.")
            message.setIcon(QMessageBox.Warning)
            message.exec_()
            
    def deleteTask(self):
        try:
            selected_task = self.day_task_list.currentItem().text()
            task_nameSer = self.get_taskName(selected_task)
            query = f"DELETE FROM user_tasks WHERE task_name = '{task_nameSer}' AND user_id = '{self.user_id}'"
            cursor.execute(query)
            db_conn.commit()
            
            dateSelected = self.calendar.selectedDate().toPyDate() 
            self.show_tasks(dateSelected)
            
        except:
            message = QMessageBox()
            message.setWindowTitle("Deletion error")
            message.setText("Task not selected.")
            message.setIcon(QMessageBox.Warning)
            message.exec_()
    
    
    def handleFilterChanged(self):
        filter_map = {
            "-": [],
            "Status": ["Pending", "In Progress", "Completed"],
            "Time": ["Morning", "Afternoon", "Night"],
            "Priority" : ["Normal", "Medium", "High"]
        }
        
        self.fil_criteria_cbox.clear()
        filter_option = self.filter_cbox.currentText()
        
        if filter_option == "Date":
            self.fil_criteria_cbox.hide()
            self.text_search.hide()
            self.dateEdit.show()
        
        elif filter_option == "Text":
            self.fil_criteria_cbox.hide()
            self.dateEdit.hide()
            self.text_search.show()

        else:
            self.dateEdit.hide()
            self.text_search.hide()
            self.fil_criteria_cbox.show()
            self.fil_criteria_cbox.addItems(filter_map[filter_option])

    def filterTask(self):
        t_filter = self.filter_cbox.currentText()
        filt_criteria = self.fil_criteria_cbox.currentText()
          
        if t_filter == "-":
            return
        
        elif t_filter == "Status":
            query = f"SELECT CONCAT(Task_name,' | ', Due_date,' | ', Due_time, ' | ', Priotity, ' | ', Status, ' | ', Comments) FROM user_tasks WHERE User_Id = {self.user_id} AND status = '{filt_criteria}'"
       
        elif t_filter == "Priority":    
            query = f"SELECT CONCAT(Task_name,' | ', Due_date,' | ', Due_time, ' | ', Priotity, ' | ', Status, ' | ', Comments) FROM user_tasks WHERE User_Id = {self.user_id} AND priotity = '{filt_criteria}'"
       
        elif t_filter == "Time":
            date = self.calendar.selectedDate().toPyDate() 
            if filt_criteria == "Morning":
                query = f"SELECT CONCAT(Task_name,' | ', Due_date,' | ', Due_time, ' | ', Priotity, ' | ', Status, ' | ', Comments) FROM user_tasks WHERE User_Id = {self.user_id} AND due_time BETWEEN '00:00:00' AND '11:59:59' AND due_date = '{date}'"
            elif filt_criteria == "Afternoon":
                query = f"SELECT CONCAT(Task_name,' | ', Due_date,' | ', Due_time, ' | ', Priotity, ' | ', Status, ' | ', Comments) FROM user_tasks WHERE User_Id = {self.user_id} AND due_time BETWEEN '12:00:00' AND '17:59:59' AND due_date = '{date}'" 
            else:
                query = f"SELECT CONCAT(Task_name,' | ', Due_date,' | ', Due_time, ' | ', Priotity, ' | ', Status, ' | ', Comments) FROM user_tasks WHERE User_Id = {self.user_id} AND due_time BETWEEN '18:00:00' AND '23:59:59' AND due_date = '{date}'"
        
        elif t_filter == "Text":
            search = self.text_search.text()
            query = f"SELECT CONCAT(Task_name,' | ', Due_date,' | ', Due_time, ' | ', Priotity, ' | ', Status, ' | ', Comments) FROM user_tasks WHERE User_Id = {self.user_id} AND (LOWER(Task_name) LIKE LOWER('%{search}%') OR LOWER(Comments) LIKE LOWER('%{search}%'))"

        else:
            date_selected = self.dateEdit.date().toPyDate()
            query = f"SELECT CONCAT(Task_name,' | ', Due_date,' | ', Due_time, ' | ', Priotity, ' | ', Status, ' | ', Comments) FROM user_tasks WHERE User_Id = {self.user_id} AND due_date = '{date_selected}'"
            
        cursor.execute(query)
        filtered_tasks = cursor.fetchall()
        self.day_task_list.clear()
        
        for task_data in filtered_tasks:
            task_info = ' | '.join(str(item) for item in task_data)
            self.day_task_list.addItem(task_info)
       
    def sortTasks(self):
        order_by = self.sort_cbox.currentText()
        tasks = [self.day_task_list.item(i).text() 
                 for i in range (self.day_task_list.count())
                 ]
    
        if order_by == "-":
            return
        
        elif order_by == "Ascending":
            tasks.sort()

        else:
            tasks.sort(reverse= True)

        self.day_task_list.clear()
        
        for task_info in tasks:
            self.day_task_list.addItem(task_info)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window= Task_manager()
    window.show()
    sys.exit(app.exec())
    