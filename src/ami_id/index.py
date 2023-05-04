import json
import logging

import boto3
from crhelper import CfnResource

logger = logging.getLogger(__name__)
helper = CfnResource(json_logging=False, log_level="DEBUG", boto_level="CRITICAL")


@helper.create
def create(event, context):
    logger.info("Got Create")

    properties = event.get("ResourceProperties", {})
    owner_id = properties.get("OWNER_ID")
    filters_string = properties.get("FILTERS")
    filters = json.loads(filters_string)

    ec2_client = boto3.client("ec2")
    response = ec2_client.describe_images(Filters=filters, Owners=[owner_id])
    images = sorted(response["Images"], key=lambda x: x["CreationDate"], reverse=True)
    latest_ami_id = images[0]["ImageId"]

    return latest_ami_id


@helper.update
def update(event, context):
    logger.info("Got Update")
    pass


@helper.delete
def delete(event, context):
    logger.info("Got Delete")
    pass


def handler(event, context):
    helper(event, context)
