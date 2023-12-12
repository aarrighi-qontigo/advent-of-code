#!/usr/bin/env python3


from Trebuchet import process_line

def test_linea_1():
    result = process_line('1abc2')
    assert result == 12

def test_linea_2():
    result = process_line('pqr3stu8vwx')
    assert result == 38

def test_linea_3():
    result = process_line('a1b2c3d4e5f')
    assert result == 15


def test_linea_4():
    result = process_line('treb7uchet')
    assert result == 77

def test_linea_5():
    input = """ 
    1abc2
    pqr3stu8vwx
    a1b2c3d4e5f
    treb7uchet
    """
    result = process_text(input)
    assert result == 142