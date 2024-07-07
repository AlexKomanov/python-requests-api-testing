import pytest

@pytest.mark.xfail(reason="Uknown bug  - currently under investigation")
def test_failed_assertion():
    assert 2 + 5 == 6