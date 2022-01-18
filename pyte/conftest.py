import pytest

@pytest.fixture()
def login():
    print("in login")
    yield
    print("in teardown")

def pytest_configure(config):
    marker_list = ["weibo","hongmi"]
    for markers in marker_list:
        config.addinivalue_line("markers", markers)

