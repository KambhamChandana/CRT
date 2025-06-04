create database practice;
use practice
create table student(
    roll_no int primary key,
    name varchar(150) not null,
    course_name varchar(100) not null
    );
    create table details(
        roll_no int,
        address text,
        phone_no varchar(20) not null,
        foreign key (roll_no) references student(roll_no)
        );
        insert into student(rollno,sname,sname) values
        (1,"A","CSE"),
        (2,"B","ECE"),
        (3,"C","AI"),
        (4,"D","EEE"),
        (5,"E","CSE");
select * from student;
truncate table details 
insert into details(roll_no,address,phone_no) values(1,NULL,123);
insert into details(roll_no,address,phone_no) values(2,"HYD",456);
select * from details;
 
 select * 
 from student
 right join details
 on student.roll_no=details.roll_no;
 
 select* from student;
 select *
 from student s
  join details d
 on s.roll_no=d.roll_no
 
 
 select * from student;
 insert into details(roll_no,address,phone_no) values(10,"HELLO","ECE");
