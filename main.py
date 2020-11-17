import seaborn as sns
import numpy as np

from consoleOperations import create_line_break
from fileOperations import get_csv
import matplotlib.pyplot as plt
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
print('Veri setindeki normal işlemlerin istatistiksel incelenmesi:\n',normalTransactions.describe())
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
plt.title('İşlemlerin Zaman Yoğunluğu Grafiği')
plt.figure(figsize = (10,3))
sns.distplot(normalTransactions['Time'],kde=True,bins=240)
sns.distplot(fraudTransactions['Time'],kde=True,bins=240)
plt.show()
create_line_break()
print('Veri setindeki eksik verilerin yüzdesi:\n'+str(get_csv().isnull().sum() / get_csv().count()))
print('Bu sonuçlara göre herhangi bir boş/kayıp veri bulunmamaktadır.')
create_line_break()
print('Veri setindeki dolandırıcılık işlemlerinin istatistiksel incelenmesi:\n', get_csv().loc[get_csv().Class==1].describe())