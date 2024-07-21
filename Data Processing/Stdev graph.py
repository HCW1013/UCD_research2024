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
counter = 0
high_eng = []
for i in range(0, int((len(eng_class) / 5) - 1)):
    if eng_class[counter + 2] == '3' and eng_class[counter + 4] == '0':
        high_eng.append(eng_class[counter])
    counter += 5

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





'''
def neutral_list_mod():
    plots = [angry_plot, happy_plot, disgust_plot, fear_plot, sad_plot, surprise_plot, neutral_plot]
    for i in plots:
        for j in range(0, len(i) - 1):
            i[j] = 100 * int(i[j]) / len(high_eng)
            
            Total: {sum([anger_prop, happy_prop, disgust_prop, fear_prop, sad_prop, surprise_prop, neutral_prop])}
            '''



def std():
    high_eng = []
    global total_frames
    global x
    global y
    x = []
    y = []
    for j in range(1,5):
        for k in range (0,4):
            for n in range(0, int((len(eng_class) / 5) - 1)):
                counter = 0
                high_eng = []
                if eng_class[counter + j] == str(k):
                    high_eng.append(eng_class[counter])
                counter += 5
            organize()
            
            
            x.append(sum(angry_plot))
            x.append(sum(sad_plot))
            x.append(sum(happy_plot))
            x.append(sum(neutral_plot))
            x.append(sum(fear_plot))
            x.append(sum(surprise_plot))
            
            y.append(stat.stdev(angry_plot))
            y.append(stat.stdev(sad_plot))
            y.append(stat.stdev(happy_plot))
            y.append(stat.stdev(neutral_plot))
            y.append(stat.stdev(fear_plot))
            y.append(stat.stdev(surprise_plot))


std()
plt.scatter(x,y)
a, b = np.polyfit(x, y, deg=1)
z = [i * a + b for i in x]
plt.plot(x, z)
print(z)
















