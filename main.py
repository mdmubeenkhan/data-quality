
import json
import great_expectations as gx


def data_quality(event, context):
    gx_context = gx.get_context()
    data_source = gx_context.sources.pandas_default.read_csv("/Users/mubeenkhan/aws/dq/data/data.csv")

    result = data_source.expect_column_values_to_not_be_null(column="name")
    print(f"result = {result}")


