import os
from setuptools import setup


extra = {}
if not os.getenv("SKIP_RUST_EXTENSION"):
    from setuptools_rust import Binding, RustExtension

    extra["rust_extensions"] = [
        RustExtension("ulidr._rust_ulid", binding=Binding.PyO3)
    ]

setup(
    name="ulidr",
    version="1.0",  # TODO: get version from src
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Intended Audience :: Developers",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS",
        "Environment :: MacOS X",
    ],
    packages=["ulidr"],
    package_data={"ulidr": ["py.typed", "*.pyi"]},
    url="https://github.com/RonquilloAeon/ulidr",
    zip_safe=False,
    **extra,
)
