from os import path
from aws_cdk import (
    aws_lambda as _lambda,
    aws_iam as _iam,
    aws_ec2 as _ec2,
    aws_dynamodb as dynamodb,
    )

global_table = dynamodb.Table(self, "Table",
    partition_key=dynamodb.Attribute(name="id", type=dynamodb.AttributeType.STRING),
    replication_regions=["us-east-1"],
    billing_mode=dynamodb.BillingMode.PROVISIONED
)
global_table.auto_scale_write_capacity(
    min_capacity=1,
    max_capacity=1
).scale_on_utilization(target_utilization_percent=75)