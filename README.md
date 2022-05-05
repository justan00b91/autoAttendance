# Attendance
A selenium project to automate the process of marking attendance in my university.

## Description:
  This project is developed to record the attendance on the university website. My university uses the UNIX time stamp to check the date and has a unique ID
  for each course.
  Using this simple fact, the seleium toolkit logins the account and checks for open attendance links in each course.
  If it finds an open attendance, then it marks present.
  
  Otherwise, `Attendance is closed in <NAME>.` message is displayed.
  
## Requirements:
  The code requires Python 3.x+ version installed in the system.
  
  Apart from that, the code requires `selenium` package for web automation.

## Usage:
  Clone the repo using the following command and install the dependencies.
  ```bash
  $> git clone https://github.com/justan00b91/Attendance.git
  $> cd Attendance
  $> pip3 install selenium
  ```
  
  Open the code `main.py` in a text editor (vim or vi) and edit the username, password and link to the attendance page.
  Furthermore, add the course names and IDs in the dictionary and then execute the program.
  ```bash
  $> python3 main.py
  ```
  
  Now watch the magic happen.
