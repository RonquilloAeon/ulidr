from ulidr import __version__, generate_ulid


def test_version():
    assert __version__ == "0.1.0"


def test_generate_ulid():
    ulid1 = generate_ulid()
    ulid2 = generate_ulid()

    assert ulid1 != ulid2

    assert len(ulid1) == 26
    assert len(ulid2) == 26
