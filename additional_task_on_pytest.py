"""list"""
list_one = [1,3,5,6]

"""dict"""
dict_one = {
        "name" : "Whale",
        "location": "Ocean",
        "size": "huge",
    }

dict_two = {
        "name" : "Whale",
        "location": "Ocean",
        "size": "huge",
    }

def test_list_in():
    assert 5 in list_one

def test_list_any():
    assert any(list_one)

def test_list_all():
    assert all(list_one)

def test_dict_any():
    assert any(dict_one)

def test_dict_all():
    assert all(dict_one)

def test_dict_compare():
    assert dict_one == dict_two