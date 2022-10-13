from __future__ import annotations

import logging
import os

from helpers.data_source_fixture import DataSourceFixture

logger = logging.getLogger(__name__)


class ClickHouseDataSourceFixture(DataSourceFixture):
    def _build_configuration_dict(self, schema_name: str | None = None) -> dict:
        return {
            "data_source clickhouse": {
                "type": "clickhouse",
                "host": os.getenv("CLICKHOUSE_HOST", "localhost"),
                "username": os.getenv("CLICKHOUSE_USERNAME", "sodacore"),
                "password": os.getenv("CLICKHOUSE_PASSWORD", "sodacore"),
                "database": schema_name if schema_name else os.getenv("CLICKHOUSE_DATABASE", "sodacore"),
            }
        }

    def _drop_schema_if_exists(self):
        super()._drop_schema_if_exists()

    def _create_schema_if_not_exists_sql(self):
        return f"CREATE DATABASE IF NOT EXISTS {self.schema_name}"

    def _drop_schema_if_exists_sql(self):
        return f"DROP DATABASE IF EXISTS {self.schema_name}"
