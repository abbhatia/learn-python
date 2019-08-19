from sklearn import tree,svm
clf =  tree.DecisionTreeClassifier()

# [height, weight, shoe_size]

X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]
     
y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
     'female', 'male', 'male']

clf = clf.fit(X,y)
test_data = [[190, 70, 43]]
prediction = clf.predict(test_data)

print(prediction)

clf_svm = svm.SVC(gamma='scale')
clf_svm = clf_svm.fit(X,y)
prediction = clf_svm.predict(test_data)
print(prediction)
