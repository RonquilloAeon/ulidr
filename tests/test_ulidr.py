from ulidr import __version__, generate_ulid


def test_version():
    assert __version__ == "0.1.0"


def test_generate_ulid():
    assert len(generate_ulid().decode("utf-8")) == 26
