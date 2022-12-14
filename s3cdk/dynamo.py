import { Stack, StackProps } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as dynamodb from 'aws-cdk-lib/aws-dynamodb';
export class AwsDynamodbStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);
    new dynamodb.Table(this, "SimpleDynamoDB", {
      partitionKey: {
        name: "id",
        type: dynamodb.AttributeType.STRING
      },
    })
  }
}