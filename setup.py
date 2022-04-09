from setuptools import setup
from setuptools_rust import Binding, RustExtension

setup(
    name="ulidr",
    version="1.0",  # TODO: get version from src
    packages=["ulidr"],
    package_data={'watchfiles': ['py.typed', '*.pyi']},
    rust_extensions=[RustExtension("ulidr._rust_ulid", binding=Binding.PyO3)],
    zip_safe=False,
)
