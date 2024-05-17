from sklearn import datasets
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.svm import SVC
import numpy as np


trail = 10

C = [2 ** (-5 + 2 * i) for i in range(trail)]
gamma = [2 ** (-15 + 2 * i) for i in range(trail)]

iris = datasets.load_iris()
acc_list = []
for i in range(trail):

    x = iris["data"]
    y = iris["target"]
    x_trainset, x_, y_trainset, y_ = train_test_split(x, y, test_size=0.4)
    x_testset, x_validset, y_testset, y_validset = train_test_split(
        x_, y_, test_size=0.5
    )
    svm_val = SVC(kernel="rbf")
    grid_srch = GridSearchCV(svm_val, {"C": C, "gamma": gamma}, cv=3)
    grid_srch.fit(x_validset, y_validset)
    print("Best parameter =", grid_srch.best_params_)

    svm_train = SVC(
        kernel="rbf",
        C=grid_srch.best_params_["C"],
        gamma=grid_srch.best_params_["gamma"],
    )
    svm_train.fit(x_trainset, y_trainset)
    acc = svm_train.score(x_testset, y_testset)
    acc_list.append(acc)
    print("Trail {} accuracy ={}".format(i, acc))
print("Avg. accuracy=", np.mean(acc_list))
