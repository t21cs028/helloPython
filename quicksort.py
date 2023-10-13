'''
Created on 2023/10/13

@author: t21cs028
'''
from unittest.mock import right

def quick_sort(data) : 
    
    #分割できなるなる（リスト要素が１以下）であれば、そのままデータを返す
    
    if len(data) <= 1: 
        return data
    
    pivot = data.pop(0) #リストの先頭をピボットとして取り出す
    
    #ピボットより小さいものでリストを作る
    left = [i for i in data if i<= pivot] 
    
    right = [i for i in data if i > pivot]
    
    left= quick_sort(left)
    right=quick_sort(right)
    
    return left + [pivot] + right
    
    
if __name__ == '__main__': 
    DATA = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]
    
    print(f"{DATA} -> {quick_sort(DATA)}")
    
    