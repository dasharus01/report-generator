import pytest
import gener_report
import erroscach
from docxtpl import DocxTemplate
import io
# для года
import datetime
# для получения данных из консоли
import sys
from docx import Document
from docx.shared import Inches
import filecmp
import pathlib
import hashlib
from inputd import d 

def test_1():
    
    k = erroscach.main(d)
    if k == 1:
        assert False, "Проверьте заголовок"
def test_2():
    
    k = erroscach.main(d)
    if k == 4:
        assert False, "Статус преподавателя" 
def test_3():
    
    k = erroscach.main(d)
    if k == 5:
        assert False, "ФИО преподавателя"

def test_4():
    
    k = erroscach.main(d)
    if k == 6 or k == 7 or k == 8:
        assert False, "Данные о предмете"  
def test_5():
    
    k = erroscach.main(d)
    if k == 9:
        assert False, "Группа студента"    
def test_6():
    
    k = erroscach.main(d)
    if k == 10:
        assert False, "ФИО студента"         

