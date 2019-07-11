import easygui as g
import sys
import calendar
import datetime

while 1:

  s = g.enterbox("请输入目标时间（年月日，如20190706）： ")
  d = g.enterbox("请输入开始时间（年月日，如20190706）： ")

  a = str(s)
  b = str(d)



  year1 = int((a[0:4]))
  month1 = int(a[4:6])
  day1 = int(a[6:8])
 # print(year1,month1,day1)


  year2 = int((b[0:4]))
  month2 = int(b[4:6])
  day2 = int(b[6:8])
#print(year2,month2,day2)

  cal = calendar.month(year1,month1)
#print("本月日历为： ")
#print(cal)

  l = g.msgbox("目标月月历为： " +cal)





  def days(data1,data2):
      date1 = datetime.date(year1,month1,day1)
      date2 = datetime.date(year2,month2,day2)
      num = ((date1-date2).days+1)
      return num


  c = days(b, a)
#print("已经上班天数为：")
#print(c)

  g.msgbox("已经上班天数为："+ str(c))

  if c % 2 == 0:
      g.msgbox("你那天休息！")
      #print("你那天休息！")
  else:
      g.msgbox("你那天上班！")
      #print("你那天上班！")

  if g.ccbox("你希望重新开始计算吗？"):
      pass
  else:
      sys.exit(0)

