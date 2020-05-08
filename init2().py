class Students:
	def __init__(self,afname,alname,amono,aenrno,aemail):
		self.fname = afname
		self.lname = alname
		self.mono = amono
		self.enrno = aenrno
		self.email = aemail
	def header(self):
		print("FirstName","LastName","Mobile.No","Enr.No","Email")
	def display(self):
		print(self.fname,"",self.lname,"",self.mono,"",self.enrno,"",self.email)
	
s1 =  Students("Parth","Patel",9638613178,176230316084,"parthitadara@gmail.com")
s1.header()
s1.display()