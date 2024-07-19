import streamlit as st
import pandas as pd
import numpy as np
import random
import json

class main:       

    def main(self):
        st.title("Hello world")

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
        st.write("You selected : ",b)

        if b == "Other":
            b = random.choice(self.gender[0:2])
        print(self.gender.index(b))

        global submitteddata
        submitteddata = st.button(label='Submit',on_click=lambda: submitdata(self))
        # ,on_click= self.submitdata,args=(agesel,gensel,hstsel,artsel,stysel,stdsel,attsel,notsel,lissel,cgpsel)

        if submitteddata:
            st.write("Submitted dataset : ",submitteddata)
            
        def submitdata(self):
            self.dataset = {
                '1':f"{self.age.index(a)}",
                '2':f"{self.gender.index(b)}",
                '3':f"{self.hstype.index(c)}",
                '6':f"{self.artsport.index(d)}",
                '10':f"{self.stay.index(e)}",
                '17':f"{self.studyhrs.index(f)}",
                '22':f"{self.attend.index(g)}",
                '25':f"{self.notes.index(h)}",
                '26':f"{self.listen.index(i)}",
                '29':f"{self.cgpa.index(j)}"
            }
            
            print(self.dataset)
            
            with open('data.json','a') as file:

                with open('data.json') as readfile:

                    filelen = len(readfile.read())

                if filelen >= 106:
                    file.write(",")
                
                file.write(json.dumps(self.dataset))


                # if file.readline

                # print(json.loads(file))
            return self.dataset

        

if __name__ == "__main__":
    main().main()
    
