from special.spiral_matrix.algorytm import Analytical


def test_calculate_k():
    solver = Analytical(3)
    assert solver._calculate_k(7) == 0
    assert solver._calculate_k(8) == 1
    
    solver = Analytical(4)
    assert solver._calculate_k(0) == 0
    assert solver._calculate_k(11) == 0
    assert solver._calculate_k(12) == 1
    assert solver._calculate_k(15) == 1
    
    solver = Analytical(6)
    assert solver._calculate_k(0) == 0
    assert solver._calculate_k(19) == 0
    assert solver._calculate_k(20) == 1
    assert solver._calculate_k(31) == 1
    assert solver._calculate_k(32) == 2
    
    solver = Analytical(7)
    assert solver._calculate_k(0) == 0
    assert solver._calculate_k(23) == 0
    assert solver._calculate_k(24) == 1
    assert solver._calculate_k(39) == 1
    assert solver._calculate_k(40) == 2
    assert solver._calculate_k(47) == 2
    assert solver._calculate_k(48) == 3

