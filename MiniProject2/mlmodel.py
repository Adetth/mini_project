import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.metrics import accuracy_score,confusion_matrix

data = pd.read_csv('StudentData.csv')

X = data[['1','2','3','6','10','17','22','25','26','29']]
y = data.iloc[:,-3]

# print(X)
Xtrain, Xtest, ytrain, ytest = train_test_split(X,y,train_size=0.8,random_state=41)

lda = LinearDiscriminantAnalysis(solver='svd')
model = lda.fit_transform(Xtrain,ytrain)

ypred = lda.predict(Xtest)

print("The current accuracy of the model:",accuracy_score(ytest,ypred).round(3)*100,"%\t")
# print(confusion_matrix(ytest,ypred))

# print(Xtest)
# print(pd.DataFrame([ytest,ypred]))

xcustom = pd.read_csv('out.csv')
xcustom.columns = ["1","2","3","6","10","17","22","25","26","29"]

# print(xcustom)

custompredict = lda.predict(xcustom)
print("Custom prediction : ",custompredict[-5:],"\t")
custompredict = custompredict[-1]

if custompredict == 0:
    print("Your predicted grade by the time of your graduation will be less than 5 CGPA")

elif custompredict == 1:
    print("Your predicted grade by the time of your graduation will be around 5 to 6.24 CGPA")

elif custompredict == 2:
    print("Your predicted grade by the time of your graduation will be around 6.25 to 7.49 CGPA")

elif custompredict == 3:
    print("Your predicted grade by the time of your graduation will be around 7.5 to 8.74 CGPA")

elif custompredict == 4:
    print("Your predicted grade by the time of your graduation will be more than 8.75 CGPA")


