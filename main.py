
import numpy as np

from consoleOperations import create_line_break
from fileOperations import get_csv

print('Veri setindeki sütunlar:',get_csv().columns)
create_line_break()
print('Veri setindeki sütun sayısı:', len(get_csv().columns))
create_line_break()
print('Veri setindeki ilk beş veri:\n', get_csv().head())
