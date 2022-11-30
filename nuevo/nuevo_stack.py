import aws_cdk as cdk
from aws_cdk import (
    # Duration,
    aws_s3 as s3,
    aws_dynamodb as dynamodb
    # aws_sqs as sqs,
)
from constructs import Construct

class s3Folder(cdk.Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        bucket_output = s3.Bucket(self, "Output",bucket_name="outputs3freeac", versioned=True)
        
        demo_table = dynamodb.Table(self, "demo_table",table_name="data_inversion", partition_key=dynamodb.Attribute(name="id",type=dynamodb.AttributeType.STRING  )
        )
        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "NuevoQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
