
from sklearn import tree
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt
from sklearn import datasets
import  warnings
warnings.filterwarnings("ignore")
databases =[datasets.load_iris(),datasets.load_wine(),datasets.load_digits()]
for database in databases:#import the databases, iris, wine and digits.
    print("Depth\t","Accuarcy\t","Precision\t","F1-Score\t","Recall")# print the title of the table.
    accuracy_list=[]#list of the accuracy for the depths(1-10).
    precision_list=[]#list of the precision for the depths(1-10).
    f1_list=[]#list of the f1-score for the depths(1-10).
    recall_list=[]#list of the recall for the depths(1-10).
    for i in range(1,11):#loop for the depths(1-10).
        clf = tree.DecisionTreeClassifier()
        clf.max_depth = i
        clf.criterion = 'entropy'
        clf = clf.fit(database.data, database.target)
        accuracy = cross_val_score(clf, database.data, database.target, scoring='accuracy', cv=10)#calculate the accuracy.
        precision = cross_val_score(clf, database.data, database.target, scoring='precision_weighted',cv=10)#calculate the precision.
        f1 = cross_val_score(clf, database.data, database.target, scoring='f1_weighted',cv=10)#calculate the f1-score.
        recall = cross_val_score(clf, database.data, database.target, scoring='recall_weighted',cv=10)#calculate the recall.
        print(i,"\t\t",round(accuracy.mean(),3),"\t\t",round(precision.mean(),3),"\t\t",round(f1.mean(),3),"\t\t", round(recall.mean(),3),"\n")#print the accuracy, precision, f1-score and recall for each depth.
        accuracy_list.append(accuracy.mean())#add the accuracy to the list.
        precision_list.append(precision.mean())#add the precision to the list.
        f1_list.append(f1.mean())#add the f1-score to the list.
        recall_list.append(recall.mean())#add the recall to the list.
    print("The depth with the best accuracy is: ",(accuracy_list.index(max(accuracy_list))+1),"\n")#Prints the depth with the best accuracy.
    depth_list=range(1,11)
    plt.plot(depth_list, accuracy_list, label = "accuracy")
    plt.plot(depth_list,precision_list, label = "precision")
    plt.plot(depth_list,f1_list, label = "f1_score")
    plt.plot(depth_list,recall_list, label = "recall")
    plt.title('Accuracy, Precision, F1-Score And Recall')
    plt.xlabel("Depth")
    plt.legend()
    plt.show()



'''
Answers to the exercise:

1)
 a: Depth=5
 b: Accuracy=0.96
    Precision= 0.959
 c: F1-score= 0.96
    Recall=0.96

2) 
Depth	 Accuarcy	 Precision	 F1-Score	 Recall
1 		 0.667 		 0.5 		 0.556 		 0.667 

2 		 0.953 		 0.955 		 0.946 		 0.953 

3 		 0.96 		 0.967 		 0.96 		 0.96 

4 		 0.953 		 0.964 		 0.953 		 0.953 

5 		 0.96 		 0.959 		 0.96 		 0.96 

6 		 0.953 		 0.959 		 0.953 		 0.953 

7 		 0.953 		 0.959 		 0.953 		 0.953 

8 		 0.953 		 0.964 		 0.96 		 0.953 

9 		 0.953 		 0.959 		 0.96 		 0.953 

10 		 0.953 		 0.964 		 0.96 		 0.953 

3) Can be seen by running the code.

4) Can be seen by running the code.

5) Can be seen by running the code.

6) Can be seen by running the code.

'''
