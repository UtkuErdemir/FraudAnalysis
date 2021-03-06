import seaborn as sns
import pandas as pandas
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
from consoleOperations import create_line_break
from fileOperations import get_csv
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from sklearn.metrics import roc_auc_score
import numpy as np
from sklearn.ensemble import RandomForestClassifier

normalTransactions = get_csv().loc[get_csv()['Class'] == 0]
fraudTransactions = get_csv().loc[get_csv()['Class'] == 1]
print('Veri setindeki sütunlar:', get_csv().shape[1], 'adet sütun bulunmaktadır. Bunlar isimleri ve veri tipleri ile beraber aşağıda listelenmiştir.')
create_line_break()
print(get_csv().info())
create_line_break()
print('Veri setindeki satır sayısı:', get_csv().shape[0])
create_line_break()
print('Veri setindeki dolandırıcılık işlemi olan veri sayısı:',len(fraudTransactions))
print('Veri setindeki dolandırıcılık işlemi olanların yüzdesi: %',100*len(fraudTransactions)/get_csv().shape[0])
create_line_break()
print('Veri setindeki normal işlemlerin veri sayısı:',len(normalTransactions))
print('Veri setindeki normal işlemlerin yüzdesi: %',100*len(normalTransactions)/get_csv().shape[0])
create_line_break()
print('Bu sonuçlardan veri setinin düzensiz şekilde dağıldığını söyleyebiliriz.')
create_line_break()
print('Veri setindeki ilk on veri:\n', get_csv().head(10))
create_line_break()
print('Veri setindeki bütün işlemlerin istatistiksel incelenmesi:\n',get_csv()[['Amount','Time']].describe())
create_line_break()
print('Veri setindeki normal işlemlerin istatistiksel incelenmesi:\n',normalTransactions[['Amount','Time']].describe())
create_line_break()
print('Veri setindeki dolandırıcılık işlemlerinin istatistiksel incelenmesi:\n',fraudTransactions[['Amount','Time']].describe())
create_line_break()
classTypes = [0, 1]
classNames = ["Normal", "Dolandırıclık"]
classResults = [len(normalTransactions), len(fraudTransactions)]

plt.bar(classTypes, classResults, color='purple')
plt.xlabel("Yapılan İşlemler")
plt.ylabel("İşlem Sayısı")
plt.title("Yapılan İşlemlerin Dağılımı")
plt.xticks(classTypes, [name + " (" + str(classResults[i]) + ")" for i, name in enumerate(classNames)])
plt.show()
plt.scatter(normalTransactions['V1'], normalTransactions['V2'], label="Normal İşlemler", alpha=1, linewidth=0.10,c='r')
plt.scatter(fraudTransactions['V1'], fraudTransactions['V2'], label="Dolandırıclık İşlemleri", alpha=0.3, linewidth=0.50,c='g')
plt.show()
figured, graph = plt.subplots(1, 2, figsize=(18,4))
sns.distplot(get_csv()['Time'].values/(60*60), ax=graph[0], color='#FC1C9C')
graph[0].set_title('İşlem Zamanlarının Dağılımı', fontsize=10)
graph[0].set_xlim([min(get_csv()['Time'].values/(60*60)), max(get_csv()['Time'].values/(60*60))])
sns.distplot(get_csv()['Amount'].values, ax=graph[1], color='#0CFC90')
graph[1].set_title('İşlem Tutarlarının Dağılımı', fontsize=10)
graph[1].set_xlim([min(get_csv()['Amount'].values), max(get_csv()['Amount'].values)])
plt.show()
plt.figure(figsize = (10,3))
plt.title('İşlemlerin Zaman Yoğunluğu Grafiği')
sns.distplot(normalTransactions['Time'],kde=True,bins=240)
sns.distplot(fraudTransactions['Time'],kde=True,bins=240)
plt.show()
create_line_break()
print('Veri setindeki eksik verilerin yüzdesi:\n'+str(get_csv().isnull().sum() / get_csv().count()))
print('Bu sonuçlara göre herhangi bir boş/kayıp veri bulunmamaktadır.')
create_line_break()
print('Veri setindeki dolandırıcılık işlemlerinin istatistiksel incelenmesi:\n', fraudTransactions.describe())
create_line_break()
print('Veri setindeki normal işlemlerin istatistiksel incelenmesi:\n', normalTransactions.describe())

figured, graph = plt.subplots(ncols=2, figsize=(12,6))
snsplot = sns.boxplot(ax = graph[0], x="Class", y="Amount", hue="Class",data=get_csv(), palette="Set3",showfliers=True)
snsplot = sns.boxplot(ax = graph[1], x="Class", y="Amount", hue="Class",data=get_csv(), palette="Set3",showfliers=False)

plt.show()
corr = get_csv().corr(method='pearson')
df_lt = corr.where(np.tril(np.ones(corr.shape)).astype(np.bool))
mask_ut=np.triu(np.ones(corr.shape)).astype(np.bool)
figured, graph= plt.subplots(1, 1, figsize=(24,20))
sns.heatmap(df_lt, mask=mask_ut,cmap='Spectral_r', annot_kws={'size':20})
graph.set_title("Korelasyon Sıcaklık Matrisi", fontsize=20)
plt.show()
snsplot = sns.lmplot(x='V20', y='Amount',data=get_csv(), hue='Class', fit_reg=True,scatter_kws={'s':2})
snsplot = sns.lmplot(x='V7', y='Amount',data=get_csv(), hue='Class', fit_reg=True,scatter_kws={'s':2})
plt.show()
snsplot = sns.lmplot(x='V2', y='Amount',data=get_csv(), hue='Class', fit_reg=True,scatter_kws={'s':2})
snsplot = sns.lmplot(x='V5', y='Amount',data=get_csv(), hue='Class', fit_reg=True,scatter_kws={'s':2})
plt.show()
sns.set_style('whitegrid')
plt.figure()
figured, graph = plt.subplots(8,4,figsize=(16,28))

for i, column in enumerate(get_csv().columns.values):
    plt.subplot(8,4,i+1)
    sns.kdeplot(normalTransactions[column],  color="yellow", bw=0.7,label="Normal İşlem")
    sns.kdeplot(fraudTransactions[column], bw=0.7, color="magenta",label="Dolandırıcılık İşlemi")
    plt.xlabel(column, fontsize=14)
    _, labels = plt.xticks()
    plt.tick_params(axis='both', which='major', labelsize=14)
plt.show()

predictors_names=['Time', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10',\
       'V11', 'V12', 'V13', 'V14', 'V15', 'V16', 'V17', 'V18', 'V19',\
       'V20', 'V21', 'V22', 'V23', 'V24', 'V25', 'V26', 'V27', 'V28',\
       'Amount']
target_name= 'Class'
predictors = get_csv()[predictors_names]
target = get_csv()[target_name]

x_train, x_test, y_train, y_test = train_test_split(predictors, target, test_size=0.40, random_state=0)
models = [  ('Naive Bayes', GaussianNB()),
            ('Decision Tree (CART)', DecisionTreeClassifier()), ('K-NN', KNeighborsClassifier()),
            ('RandomForestClassifier', RandomForestClassifier(n_jobs=8,
                             criterion='entropy',
                             verbose=False))]

for name, model in models:
    k = model.fit(x_train, y_train)
    y_pred = k.predict(x_test)
    print("%s -> Hassasiyet: %%%.2f" % (name, metrics.accuracy_score(y_test, y_pred) * 100))
    if name=='RandomForestClassifier':
        plt.figure(figsize=(7, 4))
        plt.title('Niteliklerin Onemi', fontsize=14)
        s = sns.barplot(x='nitelik', y='niteliklerinonemi', data=pandas.DataFrame({'nitelik': predictors_names, 'niteliklerinonemi': model.feature_importances_}))
        s.set_xticklabels(s.get_xticklabels(), rotation=90)
        plt.show()
