import aws_cdk as core
import aws_cdk.assertions as assertions

from nuevo.nuevo_stack import NuevoStack

# example tests. To run these tests, uncomment this file along with the example
# resource in nuevo/nuevo_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = NuevoStack(app, "nuevo")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
