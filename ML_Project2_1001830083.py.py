#!/usr/bin/env python
# coding: utf-8

# In[37]:


import os
import random
import math


# In[ ]:


#Compute probability of a particular category
import math
def compute_category_probability(path, categories, files):
    value = {}
    highest = -1000
    hcategory = ''
    for category in categories:
        value[category] = 0
        path, direc, files = next(os.walk("20_newsgroups/" + category))
        for file in files:
            with open(path + '/' + file , 'r') as content:
                for line in content:
                    words = line.lower().split()
                    for word in words:
                        word = word.strip('()\",.?:-@!*^=></\\')
                        if word in feature_list:
                            #for category in categories:
                            value[category] += math.log(probability[category][word])
    
    
    for category in value:
        if(value[category] > highest):
            highest = value[category] 
            hcategory = category
    return hcategory
        
        


# In[38]:


#preprocess the data -- remove not important words and construct feature list
import os
def count_word():
    notimp_words = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't", '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
    category_count = {}
    category_total = 0
    categories = os.listdir("train_data/")
    for category in categories:
        path, direc, files = next(os.walk("train_data/" + category))
        for file in files:
            with open(path + '/' + file , 'r') as content:
                for line in content:
                    words = line.lower().split()
                    for word in words:
                        word = word.strip('()\",.?:-@!*^=></\\')
                        if word != '' and word not in notimp_words and len(word) > 5 :
                            if word in feature_list:
                                feature_list[word] += 1
                                category_count.setdefault(word,0)
                                category_count[word] += 1
                                category_total += 1
                            else:
                                feature_list[word] = 1
                                category_count[word] = 1
                                category_total += 1

    delete_words=[]
    for word in feature_list:
        if feature_list[word] < 4:
            delete_words.append(word)

    for word in delete_words:
        del feature_list[word]
        
    
    return category_count,category_total    


# In[ ]:


#create directory, split data using random library 
feature_list={}

def get_directory_list(main_directory):
    dirs = os.listdir(main_directory)
    categories = []

    for category in dirs:
        if category != '.DS_Store':
            categories.append(category)

    return categories

def create_directory(categories):
    os.system('mkdir train_data')
    for category in categories:
        #print(category)
        os.mkdir('train_data/' + category)

def partition_data(categories):
    for category in categories:
        pathDir = './20_newsgroups/' + category + '/'
       
        random_sample = random.sample(os.listdir(pathDir), 500)     
        for name in random_sample:
            #print(name)
            
            os.rename(pathDir + name, './train_data/' + category + '/' + name)


# In[39]:


#train the model, compute probability of a particular word in a particular category
probability = {}
total_words = {}

def train_model():
    categories = os.listdir("train_data/")
    for category in categories:
        path, direc, files = next(os.walk("train_data/" + category))
        probability[category], total_words[category] = count_word()
        print('We are training the category :', category)
        tcount = total_words[category] + len(feature_list)
        for word in feature_list:
            if word in probability[category]:
                count = probability[category][word]
            else:
                count = 1
            probability[category][word] = float(count+1)/tcount  
            #print('Probability of %s %s ',category, word)
            #print(probability[category][word])
    print('Training of all the categories is completed..\n')
        


# In[40]:


#compute probability of a particilar category
import math
def compute_category_probability(path, categories, files):
    value = {}
    highest = -1000
    hcategory = ''
    for category in categories:
        value[category] = 0
        path, direc, files = next(os.walk("20_newsgroups/" + category))
        for file in files:
            with open(path + '/' + file , 'r') as content:
                for line in content:
                    words = line.lower().split()
                    for word in words:
                        word = word.strip('()\",.?:-@!*^=></\\')
                        if word in feature_list:
                            #for category in categories:
                            value[category] += math.log(probability[category][word])
    
    
    for category in value:
        if(value[category] > highest):
            highest = value[category] 
            hcategory = category
    return hcategory
        
        


# In[42]:


#compute accuracy of a particular category and also the accuracy of the model
def test_model():
    categories = os.listdir("20_newsgroups/")
    t_accuracy = 0
    for category in categories:
        
        correct = 0
        total = 0
        print('We are currently testing category', category)
        path, direc, files = next(os.walk("20_newsgroups/" + category))
        for file in files:
            total += 1
            cat = compute_category_probability(path, categories, files)
            if cat == category:
                correct = correct + 1
        
        accuracy = float(correct/total*100)
        
        print('Accuracy is ',accuracy)
        t_accuracy += accuracy
    print('total accuracy of the model is', t_accuracy/20)
    


# In[ ]:


import time

main_directory = './20_newsgroups/'
categories = get_directory_list(main_directory)
print("main", main_directory)
create_directory(categories)
print("cat", categories)
partition_data(categories)
os.system('move 20_newsgroups/ test_data')
start_time = time.time()
train_model()
test_model()
print('time %s', (time.time()-start_time))


# In[ ]:





# In[ ]:




