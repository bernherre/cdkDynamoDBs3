
from os import device_encoding
import aws_cdk as core

from dynamocdk import AwsDynamodbStack

dev = core.Environment(account='611426951697', region='us-east-1')

app = core.App()
#IntranalyticsLambdasStack(app, "intranalytics-api-test", stage='test')
#IntranalyticsLambdasStack(app, "intranalytics-api", stage='prod')

# StudentMetricsStack(app, "student-metrics-dev", stage='dev')

AwsDynamodbStack(app, "dynamo-free", env=core.Environment(
    account="611426951697",
    region='us-east-1'), stage='dev')


#IntranalyticsLambdasStack(app, "intranalytics-api-main", stage='main')

app.synth()
