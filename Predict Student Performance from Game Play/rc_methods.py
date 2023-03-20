# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 11:47:45 2023

@author: RITARTHA CHAKI
"""
import os
import pandas as pd
def load_data(path):
    train = pd.read_csv(path['train'])
    test = pd.read_csv(path['test'])
    column_list = list(train.columns)
    temp = []
    print('Column list =',column_list,'\n\n')
    print('Index','=>','name:')
    for i in range(len(column_list)):
        print(i,'=>',column_list[i])

    print('Specify index which one is target:')
    
    target = int(input())
    temp.append(column_list[target])
    print('Specify the indexes separated by commas of the names that will be discarded from feature list')
    redundant = input().split(',')
    for i in redundant:
        try:
            temp.append(column_list[int(i)])
        except:
            temp = temp
    print(temp)
    for i in temp:
        column_list.remove(i)
        
    #print('print test0',temp[0])    
    data = {
        'train':train,
        'test':test,
        'target_name':temp[0],
        'target':train[temp[0]],
        'features':column_list,
    }
    return data
def Missing_value(data,treat_by_num,treat_by_cat):
    '''
    drop,
    missing category,
    replace by median,mean
    '''
    temp = data
    data = data['train']
    if treat_by_num == 'mean':
        for col in data.columns:
            if data[col].dtype == float or data[col].dtype == float:
                data[col] = data[col].fillna(data[col].mean())
            else:
                pass
            
    elif treat_by_num == 'median':
        for col in data.columns:
            if data[col].dtype == float or data[col].dtype == float:
                data[col] = data[col].fillna(data[col].mean())
            else:
                pass
            
    if treat_by_cat == 'mode':
        for col in data.columns:
            if data[col].dtype == object:
                val = data[col].mode()
                data[col] = data[col].fillna(val[0])
               
            else:
                pass
    elif treat_by_cat == 'missing':        
        for col in data.columns:
            if data[col].dtype == object:
                data[col] = data[col].fillna('Missing')
            else:
                pass
    temp['train'] = data        
    return temp

from sklearn.utils import resample
def upsample(data):
    df_train = data['train']
    target = data['target_name']
    count = df_train[target].value_counts()
    count_class_0, count_class_1 = count.values
    keys = count.keys()
    print('1')
    # Divide by class



    df_class_0 = df_train[df_train[target] == keys[0]]
    df_class_1 = df_train[df_train[target] == keys[1]]
    df_class_1_over = df_class_1.sample(count_class_0, replace=True)
    df_test_over = pd.concat([df_class_0, df_class_1_over], axis=0)

    print('Random over-sampling:')
    print(df_test_over[target].value_counts())
    df_test_over[target].value_counts().plot(kind='bar', title='Count (target)');
    
    data['train'] = df_test_over 
    data['target'] = df_test_over[target]
    return data