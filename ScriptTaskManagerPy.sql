CREATE DATABASE tasks_py;

USE tasks_py;

CREATE TABLE users(
	User_id int not null auto_increment,
    Account_name varchar(40),
    Email varchar (40),
    Password varchar (150),
		PRIMARY KEY (User_Id)
);

CREATE TABLE user_tasks (
	Task_id int not null auto_increment,
    User_id int not null,
    Task_name varchar (30),
    Due_date date not null,
    Due_time time not null,
    Priotity enum("Normal", "Medium", "High") not null,
    Status enum ("Pending", "In Progress", "Completed") not null,
    Comments text,
		PRIMARY KEY (Task_id),
        FOREIGN KEY (User_id) REFERENCES users (User_id)
);

select * from users;
select * from user_tasks;
