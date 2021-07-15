import boto3
import os
# import botocore
# from boto3.dynamodb.conditions import Key, Attr

from support.exceptions import UndefinedExampleException

dynamodb = boto3.resource('dynamodb')

EXAMPLE_TABLE = dynamodb.Table(os.environ["EXAMPLE_TABLE"])


def get_examples():
    examples = EXAMPLE_TABLE.scan()
    return examples["Items"]


def get_example(example_id):
    example = EXAMPLE_TABLE.get_item(Key={"id": example_id}).get("Item")

    if example is not None:
        return example
    else:
        raise UndefinedExampleException()
