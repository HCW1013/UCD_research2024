# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 23:10:00 2024

@author: hcwha
"""
import matplotlib.pyplot as plt
import statistics as stat
import numpy as np

emotions = []
frames = []

#separates file into emotions and frame names
with open("C:/Users/hcwha/Desktop/Data Processing/emotionrec.txt") as f:
    elements = f.read()
    elements = elements.replace('\n',';')
    elements = elements.split(';')


#separates into two lists
for i in range(0, len(elements) - 1):
    if i % 2 == 0:
        frames.append(elements[i])
    else:
        emotions.append(elements[i])


#create lists to sort frames into detected emotions
angry = []
disgust = []
fear = []
happy = []
neutral = []
sad = []
surprise = []

#sort frames into respective lists
for k in range(0, len(frames) - 1):
    if emotions[k] == 'angry':
        angry.append(frames[k])
    elif emotions[k] == 'disgust':
        disgust.append(frames[k])
    elif emotions[k] == 'fear':
        fear.append(frames[k])
    elif emotions[k] == 'happy':
        happy.append(frames[k])
    elif emotions[k] == 'neutral':
        neutral.append(frames[k])
    elif emotions[k] == 'sad':
        sad.append(frames[k])
    elif emotions[k] == 'surprise':
        surprise.append(frames[k])

global angry_plot
global disgust_plot
global fear_plot
global happy_plot
global neutral_plot 
global sad_plot
global surprise_plot
angry_plot = []
disgust_plot = []
fear_plot = []
happy_plot = []
neutral_plot = []
sad_plot = []
surprise_plot = []

with open("C:/Users/hcwha/Desktop/Data Processing/ValidationLabels.csv") as f:
    eng_class = f.read()
eng_class = eng_class.replace('.avi','')
eng_class = eng_class.replace('\n',',')
eng_class = eng_class.split(',')



def organize():
    global total_frames
    total_frames = 0
    for i in range(1, 251):
        
        angry_plot.append(0)
        disgust_plot.append(0)
        fear_plot.append(0)
        happy_plot.append(0)
        neutral_plot.append(0)
        sad_plot.append(0)
        surprise_plot.append(0)
        for j in range(0, len(frames)):
            test_frame = frames[j][10:]
            try:
                int(test_frame)
            except ValueError:
                continue
            if int(test_frame) == i and (frames[j][:10] in high_eng):
                total_frames += 1
                if emotions[j] == 'angry':
                    angry_plot[i - 1] += 1
                elif emotions[j] == 'disgust':
                    disgust_plot[i - 1] += 1
                elif emotions[j] == 'fear':
                    fear_plot[i - 1] += 1
                elif emotions[j] == 'happy':
                    happy_plot[i - 1] += 1
                elif emotions[j] == 'neutral':
                    neutral_plot[i - 1] += 1
                elif emotions[j] == 'sad':
                    sad_plot[i - 1] += 1
                elif emotions[j] == 'surprise':
                    surprise_plot[i - 1] += 1



def list_mod():
    plots = [angry_plot, happy_plot, disgust_plot, fear_plot, sad_plot, surprise_plot, neutral_plot]
    for i in plots:
        for j in range(0, 250):
            i[j] = (100 * int(i[j])) / len(high_eng)





def std():
    global high_eng
    global angry_plot
    global disgust_plot
    global fear_plot
    global happy_plot
    global neutral_plot 
    global sad_plot
    global surprise_plot
    high_eng = []
    global total_frames
    global x
    global y
    x = []
    y = []
    for p in range(1,5):
        for q in range(0,4):
            angry_plot = []
            disgust_plot = []
            fear_plot = []
            happy_plot = []
            neutral_plot = []
            sad_plot = []
            surprise_plot = []
            high_eng = []
            counter = 0
            for n in range(0, int((len(eng_class) / 5) - 1)):  
                if eng_class[counter + p] == str(q):
                    high_eng.append(eng_class[counter])
                counter += 5
            organize()
            x.append(sum(angry_plot) / len(frames))
            x.append(sum(sad_plot) / len(frames))
            x.append(sum(happy_plot) / len(frames))
            x.append(sum(neutral_plot) / len(frames))
            x.append(sum(fear_plot) / len(frames))
            x.append(sum(surprise_plot) / len(frames))
            list_mod()
            y.append(stat.stdev(angry_plot))
            y.append(stat.stdev(sad_plot))
            y.append(stat.stdev(happy_plot))
            y.append(stat.stdev(neutral_plot))
            y.append(stat.stdev(fear_plot))
            y.append(stat.stdev(surprise_plot))
            
            
            
            


std()
#%%
y_a = [y[i * 6] for i in range(0, (len(y) // 6) - 1)]
y_sad = [y[i * 6 + 1] for i in range(0, (len(y) // 6) - 1)]
y_h = [y[i * 6 + 2] for i in range(0, (len(y) // 6) - 1)]
y_n = [y[i * 6 + 3] for i in range(0, (len(y) // 6) - 1)]
y_f = [y[i * 6+ 4] for i in range(0, (len(y) // 6) - 1)]
y_sur = [y[i * 6 + 5] for i in range(0, (len(y) // 6) - 1)]

x_a = [x[i * 6] for i in range(0, (len(y) // 6) - 1)]
x_sad = [x[i * 6 + 1] for i in range(0, (len(y) // 6) - 1)]
x_h = [x[i * 6 + 2] for i in range(0, (len(y) // 6) - 1)]
x_n = [x[i * 6 + 3] for i in range(0, (len(y) // 6) - 1)]
x_f = [x[i * 6+ 4] for i in range(0, (len(y) // 6) - 1)]
x_sur = [x[i * 6 + 5] for i in range(0, (len(y) // 6) - 1)]
plt.scatter(x_a, y_a, color='r')
plt.scatter(x_sad, y_sad, color='b')
plt.scatter(x_h, y_h, color='y')
plt.scatter(x_n, y_n, color='gray')
plt.scatter(x_f, y_f, color='m')
plt.scatter(x_sur, y_sur, color='pink')
#plt.scatter(x,y)
a, b = np.polyfit(x, y, deg=1)
z = [i * a + b for i in x]
plt.plot(x, z)


#r = np.corrcoef(x,y)
#r2 = r ** 2














