import main


def test_compute_1():
    assert main.computeNumbers("2665687") == ['bonjour']


def test_compute_2():
    assert main.computeNumbers("72588") == ['salut']


def test_compute_3():
    assert main.computeNumbers("2662273437") == ['bombardier']
