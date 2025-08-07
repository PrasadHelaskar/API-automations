import pytest

@pytest.fixture(scope='session')
def base_attributes() -> list:
    url="https://www.shoppersstack.com/shopping"
    
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    
    return [url,headers]