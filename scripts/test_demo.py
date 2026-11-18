import pytest


@pytest.mark.aaa
def test_query_user(db):
    data = db.select_all("select * from login_user")
    print(data)
    assert data is not None
