#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
class Employee:
   '所有学生的基类'
   empCount = 0
 
   def __init__(self, name, student_no,class_no,gender):
      self.name = name
      self.student_no = student_no
      self.class_no = class_no
      self.gender = gender
      Employee.empCount += 1
   def speakenglish(self):
       print  "can speak english!!"
   def singing(self):
       print "can sing"
   def displayCount(self):
     print "Total Employee %d" % Employee.empCount
 
   def displayEmployee(self):
      print "Name : ", self.name,  ", student_no: ", self.student_no,",class_no:",self.class_no,"gender:",self.gender     
 
