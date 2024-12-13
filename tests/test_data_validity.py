import array_xpl
import pytest
import pathlib

csv_data_21x3 = pathlib.Path(__file__).parent / "sample_data" / "data_21x3.csv"


@pytest.fixture
def csv_data_1():
    return array_xpl.load_csv_data(csv_data_21x3)
    
def test_data_loading(csv_data_1):
    assert len(csv_data_1) == 21
    assert csv_data_1.shape == (21, 3)
    assert csv_data_1.dtype == "float64"
    assert csv_data_1[:, 0].tolist() == [
        0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0
    ]
    assert csv_data_1[:, 1].tolist() == [
        0.0, 1.0, 4.0, 9.0, 16.0, 25.0, 36.0, 49.0, 64.0, 81.0, 100.0, 121.0, 144.0, 169.0, 196.0, 225.0, 256.0, 289.0, 324.0, 361.0, 400.0
    ]
    assert csv_data_1[:, 2].tolist() == [
        0.0, 1.0, 8.0, 27.0, 64.0, 125.0, 216.0, 343.0, 512.0, 729.0, 1000.0, 1331.0, 1728.0, 2197.0, 2744.0, 3375.0, 4096.0, 4913.0, 5832.0, 6859.0, 8000.0
    ]