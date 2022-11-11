from app.src.cal import Calculator

calu = Calculator()

def test_summ():
    assert calu.summ(1,1) == 2
    assert calu.summ(1,3) == 4
