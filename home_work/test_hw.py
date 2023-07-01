def test_home_work():
    assert ('home', 'work') == ('home', 'work')


def test_QAQC():
    assert 'QA' != 'QC'

def test_not1235():
    assert not (1, 1, 2, 3, 5) == (2, 3, 5)
