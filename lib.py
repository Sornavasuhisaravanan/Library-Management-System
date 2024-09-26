import pymysql
con=pymysql.connect(host="localhost",user="root",password="",database="library")
l=con.cursor()

def addbook():
          bookid=int(input("Enter the book id:"))
          bookname=input("Enter the book name:")
          authorname=input("Enter the author name:")
          l.execute("insert into book values(%s,%s,%s)",(bookid,bookname,authorname))
          con.commit()
          print("inserted successfully.....")

def display():
          l.execute("select * from book ")
          r=l.fetchall()
          print("Bookid\tBookname\tAuthorname")
          print("-------------------------------------------------------------------")
          for i in r:
                    print(i[0],"\t",i[1],"\t",i[2])

def author():
          k=input("enter your author name:")
          l.execute("select * from book where authorname=%s ",(k))
          r=l.fetchall()
          for i in r:
                    print(i[0],"    ",i[1],"   ",i[2])

def countbook():
          print("Number of books in library")
          l.execute("select count(*) from book ")
          r=l.fetchall()
          print(r[0][0])
                    

print("\t\t\tLibrary management system")
print("\t\t\t========================")
print("1.Add book information")
print("2.Display book information")
print("3.Listing of all books of a given author")
print("4.Listing of count of books in library")
print("5.Exit")
 



while True:
          c=int(input("Enter your choice:"))
          match c:
                    case 1:
                              addbook() 
                    case 2:
                               display()
                    case 3:
                                author()
                    case 4:
                                 countbook()
                    case 5:
                                 break
                                 
                                 
          
