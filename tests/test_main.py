from app.main import health_check, get_version


def test_health_check():
    assert health_check() == {"status": "ok"}


def test_get_version():
    assert get_version() == {"version": "1.0.0"}