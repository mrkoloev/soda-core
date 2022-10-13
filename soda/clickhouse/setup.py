#!/usr/bin/env python
import sys

from setuptools import find_namespace_packages, setup

if sys.version_info < (3, 7):
    print("Error: Soda SQL requires at least Python 3.7")
    print("Error: Please upgrade your Python version to 3.7 or later")
    sys.exit(1)

package_name = "soda-core-clickhouse"
package_version = "3.0.10"
description = "Soda Core ClickHouse Package"

requires = [
    f"soda-core=={package_version}",
    "clickhouse-driver==0.2.2",
    "clickhouse-sqlalchemy==0.1.7",
    "sqlalchemy-clickhouse==0.1.5.post0"

]
# TODO Fix the params
setup(
    name=package_name,
    version=package_version,
    install_requires=requires,
    packages=find_namespace_packages(include=["soda*"]),
)
