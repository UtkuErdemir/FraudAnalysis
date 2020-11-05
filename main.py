
import numpy as np

from consoleOperations import create_line_break
from fileOperations import get_csv

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
print('Veri setindeki ilk beş veri:\n', get_csv().head())
create_line_break()
print('Veri setindeki normal işlemlerin istatistiksel incelenmesi:\n', get_csv().loc[get_csv().Class==0].describe())
create_line_break()
print('Veri setindeki dolandırıcılık işlemlerinin istatistiksel incelenmesi:\n', get_csv().loc[get_csv().Class==1].describe())