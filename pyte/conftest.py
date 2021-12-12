import pytest

@pytest.fixture()
def login():
    print("in login")
    yield
    print("in teardown")
