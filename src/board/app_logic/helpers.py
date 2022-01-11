def check_access_by_age(age):

    if age < 15:
        return False
    else:
        return True
        
        
def test_if_age_is_14():        
    
    if not check_access_by_age(14):
        return True
    else:
        return False
        
        
def test_if_age_less_than_18():

    for i in range(17):
        result = check_access_by_age(i)
        #print(i, result)
        if result:
            return False
        else:
            return True
            
            
def test_if_age_equal_18():

    result = check_access_by_age(18)
    if not result:
        return False
    else:
        return True
        
        
def test_if_age_greater_than_18():

    for i in range(18, 130):
        result = check_access_by_age(i)
        if not result:
            return False
        else:
            return True