import ffmpeg
import os 




#copy list of file names
with open("Validation.txt") as f:
    names = f.read()



#Create 2 lists. Names are the clip file name, videos are the .avi file name
videos = names.split('\n')
str(names)
names = names.replace('.avi', '')
names = names.split('\n')

'''
f4 = open('Validation_Frames.txt', 'w')
file_names = []
for i in range(0, len(names) - 1):
    for j in range(1, 251):
        file_names.append(str(names[i]) + str(j))
for i in range(0, len(file_names) - 1):
    if not('.mp4' in file_names[i]):
        f4.write(f"{file_names[i]}\n")
'''


#create a list of the first 5 digits of file name for path builing
user = names
inst = []
for i in range(0, len(names) - 1):
    inst.append(names[i][0:6])
f2 = open('completed.txt', 'w')
with open("completed.txt", 'r') as f2:
    completion = str(f2.read())
    completion = completion.split('\n')

f2 = open('completed.txt', 'w')
f3 = open('errors.txt', 'w')


#builds file path from lists and extracts frames
complete = []
count = 0
progress = 0
for i in range(1600, len(names) - 1):
    progress += 1
    print(f'Progress: {100 * (progress / 300):.0f}%')
    if not(videos[i] in completion):
        file = "Validation" + "\\" + str(inst[i]) + "\\" + str(names[i]) + "\\" + str(videos[i])
        #file = "C:\\Users\\hcwha\\Desktop\\exttest\\110001\\1100011002\\1100011002.avi"
        print(os.path.isfile(file))
        print(file)
        if  os.path.isfile(file):
            f2.write(str(videos[i]) + '\n')
            (
            	ffmpeg.input(file)
            	.output(str(names[i]) + '%d.png', vframes=250)
            	.run()
            )
        else:
            f3.write(str(videos[i]) + '\n')
            count += 1
    else:
        continue
        
f.close()
f2.close()
print('Extraction Complete!')
print(f'Missed Files: {count}')

