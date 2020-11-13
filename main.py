
import numpy as np

from consoleOperations import create_line_break
from fileOperations import get_csv
import matplotlib.pyplot as plt
print('Veri setindeki sütunlar:', get_csv().shape[1], 'adet sütun bulunmaktadır. Bunlar isimleri ve veri tipleri ile beraber aşağıda listelenmiştir.')
create_line_break()
print(get_csv().info())
create_line_break()
print('Veri setindeki satır sayısı:', get_csv().shape[0])
create_line_break()
print('Veri setindeki dolandırıcılık işlemi olan veri sayısı:',len(get_csv().loc[get_csv().Class==1]))
print('Veri setindeki dolandırıcılık işlemi olanların yüzdesi: %',100*len(get_csv().loc[get_csv().Class==1])/get_csv().shape[0])
create_line_break()
print('Veri setindeki normal işlemlerin veri sayısı:',len(get_csv().loc[get_csv().Class==0]))
print('Veri setindeki normal işlemlerin yüzdesi: %',100*len(get_csv().loc[get_csv().Class==0])/get_csv().shape[0])
create_line_break()
print('Bu sonuçlardan veri setinin düzensiz şekilde dağıldığını söyleyebiliriz.')
create_line_break()
print('Veri setindeki ilk on veri:\n', get_csv().head(10))
create_line_break()
print('Veri setindeki normal işlemlerin istatistiksel incelenmesi:\n', get_csv().loc[get_csv().Class==0].describe())
create_line_break()
classTypes = [0, 1]
classNames = ["Normal", "Dolandırıclık"]
classResults = [len(get_csv().loc[get_csv().Class==0]), len(get_csv().loc[get_csv().Class == 1])]
plt.bar(classTypes, classResults, color='purple')
plt.xlabel("Yapılan İşlemler")
plt.ylabel("İşlem Sayısı")
plt.title("Yapılan İşlemlerin Dağılımı")
plt.xticks(classTypes, [name + " (" + str(classResults[i]) + ")" for i, name in enumerate(classNames)])
plt.show()
plt.scatter(get_csv().loc[get_csv()['Class'] == 0]['V1'], get_csv().loc[get_csv()['Class'] == 0]['V2'], label="Class #0", alpha=0.5, linewidth=0.15)
plt.scatter(get_csv().loc[get_csv()['Class'] == 1]['V1'], get_csv().loc[get_csv()['Class'] == 1]['V2'], label="Class #1", alpha=0.5, linewidth=0.15,c='r')
plt.show()
create_line_break()
print('Veri setindeki eksik verilerin yüzdesi:\n'+str(get_csv().isnull().sum() / get_csv().count()))
print('Bu sonuçlara göre herhangi bir boş/kayıp veri bulunmamaktadır.')
create_line_break()
print('Veri setindeki dolandırıcılık işlemlerinin istatistiksel incelenmesi:\n', get_csv().loc[get_csv().Class==1].describe())