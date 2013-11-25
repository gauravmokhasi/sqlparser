"""
database project - sql parser
submitted to dr.ravindranath c
by gaurav srikant mokhasi, 11co37
29th october 2013
"""
import ast

class student:    

	def select_all(self):

		dicquery[3]=dicquery[3]+".txt"
		fob = open(dicquery[3],'r')
		a=fob.readlines()
		self.dicty4=ast.literal_eval(a[0])
		self.string=""
		for k in self.dicty4.keys():
			self.string=self.string+k+","
		temp=list(self.string)
		temp1=temp[:len(temp)-1]
		self.string=''.join(temp1)
		#print self.string
		dicquery[1]=dicquery[1].replace("*",self.string)
		fields = dicquery[1].split(',')
		for i in a:
			self.dicty=ast.literal_eval(i)
			for j in fields:
				print str(self.dicty[j])+"\t",
			print
		fob.close()



	def project_field(self):
		dicquery[3]=dicquery[3]+".txt"
		fob = open(dicquery[3],'r')
		a=fob.readlines()
		fields = dicquery[1].split(',')
		for i in a:
			self.dicty=ast.literal_eval(i)
			for j in fields:
				print str(self.dicty[j])+"\t",
			print
		fob.close()

	def select_condition(self,cond):
		dicquery[3]=dicquery[3]+".txt"
		fob = open(dicquery[3],'r')
		a=fob.readlines()
		self.dicty4=ast.literal_eval(a[0])
		for k in self.dicty4.keys():
			#print k
			cond=cond.replace(k,"self.dicty['%s']"%k)
		#print cond
		if dicquery[1]=="*":
			self.string=""
			for k in self.dicty4.keys():
				self.string=self.string+k+","
			temp=list(self.string)
			temp1=temp[:len(temp)-1]
			self.string=''.join(temp1)
			#print self.string
			dicquery[1]=dicquery[1].replace("*",self.string)
		fields = dicquery[1].split(',')
		for i in a:
                        self.dicty=ast.literal_eval(i)
                        if eval(cond):
                                for j in fields:
                                        print str(self.dicty[j])+"\t",
                                print
		fob.close()
							             
	def project_condition(self):
		dicquery[3]=dicquery[3]+".txt"
		fob = open(dicquery[3],'r')
		a=fob.readlines()
		fob.close()

	def join(self,t1,t2,t3,cond):
		t3=t3+".txt"
		t2=t2+".txt"
		t1=t1+".txt"
		fob3 = open("temp.txt",'w')
		fob1 = open(t1,'r')
		fob2 = open(t2,'r')
		a=fob1.readlines()
		b=fob2.readlines()
		for i in a:
			for j in b:
				i=i.rstrip()
				j=j.rstrip()
				line=i+j
				line=line.rstrip()
				line=line.replace('}{',', ')	
				#print "Line" + line							
				#self.dicty=ast.literal_eval(line)
				fob3.write(line+"\n")
		fob3.close()
		fob1.close()
		fob2.close()								
		fob3 = open("temp.txt",'r')
		fob4 = open(t3,'w')
		a=fob3.readlines()
		self.dicty4=ast.literal_eval(a[0])
		for k in self.dicty4.keys():
			#print k
			cond=cond.replace(k,"self.dicty['%s']"%k)
		for i in a:
                        self.dicty=ast.literal_eval(i)
                        if eval(cond):
                                fob4.write(str(self.dicty)+"\n")
		fob3.close()
		fob4.close()

				

stu=student()
query = raw_input("Enter your query: ")
listquery = query.split()
dicquery = {}
count=0

for word in listquery:
        dicquery[count]=word
        count+=1

if dicquery[0]== 'select':
        if len(dicquery)<5: # no condition has been mentioned
                if dicquery[1]=='*':
                        stu.select_all() # select * from...
                else:
                        stu.project_field() # select a,b,c.. from table without condition
                        # select val1,val2,val3,val4 from tablename
        elif len(dicquery)>4: #where clause has been mentioned
                if dicquery[4]=="where":
                        cond=query[query.find("where")+6:] # parsing the query to store everything after where into variable cond
                        stu.select_condition(cond)
			

if dicquery[0]== 'join':
	cond="1"
	if len(dicquery)>4:
		if dicquery[4]=="where":
			cond=query[query.find("where")+6:]
	stu.join(dicquery[1],dicquery[2],dicquery[3],cond)

