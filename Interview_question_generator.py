#!/usr/bin/env python
# coding: utf-8

# __Import the modules__

# In[69]:


import PyPDF2
import re
import random
from random import randint
from datetime import datetime
import string


# In[4]:


from tkinter import *


# ## Read and clean the question pool

# In[5]:


pdf_file = open('64interviewquestions1.pdf', 'rb')
read_pdf = PyPDF2.PdfFileReader(pdf_file)


# In[6]:


# the pages that contain index of questions
page_content3 = read_pdf.getPage(3).extractText()
page_content4 = read_pdf.getPage(4).extractText()
index_page = page_content3 + page_content4


# In[94]:


def clean_text(text):
    '''
    Used to clean the texts
    ARG: raw text extracted by PdfFileReader
    '''
    text1 = re.sub(r'[.]+[0-9]*', ' ', ' '.join(text.split()))
    text2 = re.sub(r'™',"'", text1)
    text3 = re.sub(r'ﬂ', '"', text2)
    text4 = re.sub(r'Œ', '-', text3)
    text5 = re.sub(r'–', '...', text4)
    text6 = re.sub(r'  64 Toughest Questions Page 2', '', text5)
    text7 = re.sub(r'ﬁ', '"', text6)
    return text7


# In[95]:


clean_index1 = [*map(clean_text, (re.split(r'Q(?=[0-9])', index_page)))]
clean_index2 = clean_index1[1:]
clean_index2[51] = '52 What do you look for when you hire people?'


# In[96]:


clean_index2


# ## Build the Generator

# In[9]:


def get_random_question():
    randidx = random.randint(0,64)
    return (clean_index2[randidx])


# In[10]:


get_random_question()


# In[90]:


def Take_input(): 
    '''
    Take user's input from the Text Block
    '''
    INPUT = entry.get("1.0",END) 
    with open(file_name + '.txt', 'a') as the_file:
        the_file.write('\n' + str(today) + ':\n\n' + INPUT + '\n========================\n')


# In[86]:


def refresh_with_new_question():
    '''
    Get another random question
    Warning: will update the value of random_q, q_no, today, file_name
    '''
    
    global random_q, q_no, today, file_name
    
    random_q = get_random_question()
    q_no = re.sub(r'(^[0-9]*).*', r'\1', random_q)
    today = datetime.today().strftime('%Y-%m-%d %H-%M')
    file_name = 'Q' + re.sub('[!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~]', '', random_q)
    
    label2.config(text = random_q + '\n', borderwidth=20, wraplength = 350)
    
    entry.delete("1.0", END)


# __Build the Window__

# In[99]:


master = Tk()

master.geometry("400x400")
# master.configure(background='white')

  
random_q = get_random_question()
q_no = re.sub(r'(^[0-9]*).*', r'\1', random_q)
today = datetime.today().strftime('%Y-%m-%d %H-%M')
file_name = 'Q' + re.sub('[!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~]', '', random_q)

label1 = Label(master, text = '\nYOUR QUESTION:\n', borderwidth=2,).pack()
label2 = Label(master, text = random_q + '\n', borderwidth=20, wraplength = 350)
label2.pack()

entry = Text(master, height = 15, width = 50)
entry.pack()

buttonCommit=Button(master, height=1, width=10, text="Commit", 
                    command = lambda: Take_input())
buttonCommit.pack()

buttonRefresh=Button(master, height=1, width=10, text="Refresh", 
                    command = lambda: refresh_with_new_question())
buttonRefresh.pack()
# display_everything()

mainloop()

