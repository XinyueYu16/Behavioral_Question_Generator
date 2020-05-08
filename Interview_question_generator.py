#!/usr/bin/env python
# coding: utf-8

# In[133]:


import PyPDF2
import re
import random
from random import randint
from datetime import datetime


# In[59]:


from tkinter import *


# In[4]:


pdf_file = open('64interviewquestions1.pdf', 'rb')
read_pdf = PyPDF2.PdfFileReader(pdf_file)


# In[12]:


page_content3 = read_pdf.getPage(3).extractText()
page_content4 = read_pdf.getPage(4).extractText()


# In[17]:


index_page = page_content3 + page_content4


# In[52]:


clean_index1 = [*map(lambda x: re.sub(r'[.]+[0-9]', ' ', ' '.join(x.split())), (re.split(r'Q(?=[0-9])', index_page)))]
clean_index2 = clean_index1[1:]


# In[56]:


def get_random_question():
    randidx = random.randint(0,64)
    return (clean_index2[randidx])


# In[55]:


get_random_question()


# In[173]:


def Take_input(): 
#     global INPUT
    INPUT = entry.get("1.0",END) 
    with open(file_name + '.txt', 'a') as the_file:
        the_file.write(INPUT)


# In[174]:


master = Tk()

master.geometry("400x400")
# master.configure(background='white')


random_q = get_random_question()
q_no = re.sub(r'(^[0-9]*).*', r'\1', random_q)
today = datetime.today().strftime('%Y-%m-%d %H-%M')
file_name = 'Q' + q_no + ' ' + str(today)

label1 = Label(master, text = '\nYOUR QUESTION:\n', borderwidth=2,).pack()
label2 = Label(master, text = random_q + '\n', borderwidth=20, wraplength = 350).pack()




entry = Text(master, height = 15, width = 50)
entry.pack()

buttonCommit=Button(master, height=1, width=10, text="Commit", 
                    command=lambda: Take_input())
#command=lambda: retrieve_input() >>> just means do this when i press the button
buttonCommit.pack()


mainloop()

