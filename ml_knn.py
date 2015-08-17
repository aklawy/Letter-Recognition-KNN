import numpy as np
import time
import math
from collections import Counter

start = time.time()
f = open("letter-recognition.data","r")
linelist = f.readlines()
data = []
for line in linelist:
    data.append(line.split(','))
training_data = data[0:16000]
test_data = data[16000:20000]
small_data = test_data[0:20]
prediction_data = [item[1:17] for item in test_data]
correct_classes = [item[0] for item in test_data]
small_pred_data = [item[1:17] for item in small_data]
small_classes = [item[0] for item in small_data]
correct = []
wrong = []
for k in range(1,22,2):
    letters = [None]*k
    distance = []
    predicted_classes = []
    correct_classified = 0
    wrong_classified = 0
    step = 0
    for pred in prediction_data:
        pred = list(map(int, pred))
        j = 0
        distance = []
        for train in training_data:
            train = list(map(int,train[1:17]))
            diff = [(a-b)**2 for a,b in zip(pred,train)]
            distance.append(math.sqrt(sum(diff)))
        distance_sorted = sorted(distance)
        for count in range(k):
            dist = distance_sorted[count]
            index = distance.index(dist)
            letters[count] = training_data[index][0]
        l = Counter(letters)
        mc = l.most_common()
        predicted_classes.append(mc[0][0])
        step = step+1
    for i,j in zip(predicted_classes,correct_classes):
        if i==j:
            correct_classified += 1
        else:
            wrong_classified   += 1
    correct.append(correct_classified)
    wrong.append(wrong_classified)
    print (k)
end = time.time()
print (end-start)
