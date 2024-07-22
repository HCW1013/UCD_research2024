import matplotlib.pyplot as plt

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
list_mod()
#%%

#graphing
def line_chart():
    plt.plot(angry_plot, color = 'r')
    plt.plot(disgust_plot, color = 'g')
    plt.plot(fear_plot, color = 'm')
    plt.plot(happy_plot, color = 'y')
    plt.plot(neutral_plot, color = 'gray')
    plt.plot(sad_plot, color = 'b')
    plt.plot(surprise_plot, color = 'pink')
    plt.title("3/3 Frustration Emotional Estimation\nSampled at 25FPS")
    plt.xticks([0, 50, 100, 150, 200, 250],[0,2,4,6,8,10])
    plt.xlabel("Time(s)")
    plt.ylabel("Proportion of frames for given emotion(%)")
    return None

def bar_chart_neutral():
    sum_list = [sum(angry_plot)/ 250, sum(happy_plot)/ 250, 
                sum(neutral_plot) / 250, sum(disgust_plot)/250, 
                sum(fear_plot)/250, sum(sad_plot)/250, 
                sum(surprise_plot)/250]
    plt.bar([1,2,3,4,5,6,7],sum_list, color=['r','y','gray','g','m','b','pink'])
    plt.title("3/3 Frustration Emotional Estimation\nSampled at 25FPS\nSummarization")
    plt.xlabel("Emotion")
    plt.xticks([1,2,3,4,5,6,7],['Angry', 'Happy', 'Neutral', 'Disgust', 'Fear', 'Sad', 'Surprise'])
    plt.ylabel("Proportion of frames for given emotion(%)")
    return None

def bar_chart():
    sum_list = [100 * sum(angry_plot)/total_frames, 100 * sum(happy_plot)/total_frames,
                100 * sum(disgust_plot)/total_frames, 100 * sum(fear_plot)/total_frames, 
                100 * sum(sad_plot)/total_frames, 100 * sum(surprise_plot)/total_frames]
    plt.bar([1,2,3,4,5,6],sum_list, color=['r','y','g','m','b','pink'])
    plt.title("2/3 Frustration Continuous Emotional Estimation\nSampled at 25FPS\nSummarization")
    plt.xlabel("Emotion")
    plt.xticks([1,2,3,4,5,6],['Angry', 'Happy', 'Disgust', 'Fear', 'Sad', 'Surprise'])
    plt.ylabel("Proportion of frames for given emotion(%)")
    return None

def stats():
    anger_prop = sum(angry_plot) / 250
    happy_prop = sum(happy_plot) / 250
    disgust_prop = sum(disgust_plot) / 250
    fear_prop = sum(fear_plot) / 250
    sad_prop = sum(sad_plot) / 250
    surprise_prop = sum(surprise_plot) / 250
    neutral_prop = sum(neutral_plot) / 250
    overall_prop = 100 * total_frames / len(frames)

    print(f'''
Anger Proportion: {anger_prop:.2f}%
Happy Proportion: {happy_prop:.2f}%
Disgust Proportion: {disgust_prop:.2f}%
Fear Proportion: {fear_prop:.2f}%
Sad Proportion: {sad_prop:.2f}%
Surprise Proportion: {surprise_prop:.2f}%
Neutral Proportion: {neutral_prop:.2f}%
Overall Share of Videos: {overall_prop:.2f}%

{anger_prop:.2f}%
{happy_prop:.2f}%
{disgust_prop:.2f}%
{fear_prop:.2f}%
{sad_prop:.2f}%
{surprise_prop:.2f}%
{neutral_prop:.2f}%
{overall_prop:.2f}%
          ''')




'''
def neutral_list_mod():
    plots = [angry_plot, happy_plot, disgust_plot, fear_plot, sad_plot, surprise_plot, neutral_plot]
    for i in plots:
        for j in range(0, len(i) - 1):
            i[j] = 100 * int(i[j]) / len(high_eng)
            
            Total: {sum([anger_prop, happy_prop, disgust_prop, fear_prop, sad_prop, surprise_prop, neutral_prop])}
            '''

bar_chart_neutral()
#line_chart()

stats()
























