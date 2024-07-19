import streamlit as st
import pandas as pd
import numpy as np
import random
import json
import subprocess

class main:       

    def main(self):
        st.title("Student Grade Predictor")

        # 1,2,3,6,10,17,22,25,26,29
        self.age = ["18-21","22-25",">26"]#a
        self.gender = ["Male","Female","Other"]#b
        self.hstype = ["Private","State","Other"]#c
        self.artsport = ["Yes","No"]#d
        self.stay = ["PG","Hostel","Day-Scholar","Other"]#e
        self.studyhrs = ["None", "<5 hours", "6-10 hours", "11-20 hours", "more than 20 hours"]#f
        self.attend = ["Most of the time","Sometimes","Never"]#g
        self.notes = ["Never","Sometimes","Always"]#h
        self.listen = ["Never","Sometimes","Always"]#i
        self.cgpa = ["<5.00", "5.00-6.24", "6.25-7.49", "7.5-8.74", "above 8.74"]#j

        a = st.selectbox('Select age grp',self.age)
        b = st.selectbox('Select gender',self.gender)
        c = st.selectbox('Select PU college type',self.hstype)
        d = st.selectbox('Select any co-ciricular activities',self.artsport)
        e = st.selectbox('Select stay type',self.stay)
        f = st.selectbox('Select study hours',self.studyhrs)
        g = st.selectbox('Select attendance criteria',self.attend)
        h = st.selectbox('Select frequency of taking notes',self.notes)
        i = st.selectbox('Select frequency of listening in class',self.listen)
        j = st.selectbox('Select prev sem cgpa',self.cgpa)
        # st.write("You selected : ",b)

        if b == "Other":
            b = random.choice(self.gender[0:2])
        # print(self.gender.index(b))

        submitteddata = st.button(label='Submit',on_click=lambda: submitdata(self))
        # ,on_click= self.submitdata,args=(agesel,gensel,hstsel,artsel,stysel,stdsel,attsel,notsel,lissel,cgpsel)

        if submitteddata:
            st.write("Submitted dataset : ",submitteddata)
            result = subprocess.check_output(["python","mlmodel.py"])
        
            lis = list(result.decode().split("\t"))

            print(result.decode())
            st.write(lis[0])
            st.write(lis[2])
            
            
        def submitdata(self):
            self.dataset = f"""1,2,3,6,10,17,22,25,26,29\n{self.gender.index(b)},{self.age.index(a)},{self.hstype.index(c)},{self.artsport.index(d)},{self.stay.index(e)},{self.studyhrs.index(f)},{self.attend.index(g)},{self.notes.index(h)},{self.listen.index(i)},{self.cgpa.index(j)}"""
            
            # print(self.dataset)
            
            with open('out.csv','a') as file:
                print(file.write(f"{self.age.index(a)+1},{self.gender.index(b)+1},{self.hstype.index(c)+1},{self.artsport.index(d)+1},{self.stay.index(e)+1},{self.studyhrs.index(f)+1},{self.attend.index(g)+1},{self.notes.index(h)+1},{self.listen.index(i)+1},{self.cgpa.index(j)+1}\n"))
        
            return self.dataset

        

if __name__ == "__main__":
    main().main()
    
