from sklearn import tree

X = [ [68,172,8.5], [72,225,12], [63,119,6], [70,162,10.5], [76,295,14], [60,102,5], [59,99,4.5], [71,187,10.5], [68,158,9], [68,142,7.5], [71,205,10.5]]
Y = ['male', 'male', 'female', 'female', 'male', 'female', 'female', 'male', 'male', 'female', 'male']

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X,Y)
prediction = clf.predict([[68,165,9]])

#print ("Prediction is: %s") %(prediction) 
for item in prediction:
	print (item)