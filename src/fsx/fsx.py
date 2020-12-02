from __future__ import print_function

import logging

import boto3
from crhelper import CfnResource

logger = logging.getLogger(__name__)
helper = CfnResource(
    json_logging=False, log_level="DEBUG", boto_level="CRITICAL", sleep_on_delete=120
)
fsx = boto3.client("fsx")


@helper.create
def create(event, context):
    logger.info("Got Create")
    properties = event.get("ResourceProperties", {})
    fsx_id = properties.get("FSxFileSystemId")

    dns_name, private_ip = _fsx_describe_file_systems(fsx_id)

    helper.Data.update({"FSxDNSName": dns_name, "FSxPrivateIP": private_ip})


@helper.update
def update(event, context):
    logger.info("Got Update")


@helper.delete
def delete(event, context):
    logger.info("Got Delete")


def handler(event, context):
    helper(event, context)


def _fsx_describe_file_systems(fsx_id):
    response = fsx.describe_file_systems(
        FileSystemIds=[
            fsx_id,
        ]
    )
    dns_name = response["FileSystems"][0]["DNSName"]
    private_ip = response["FileSystems"][0]["WindowsConfiguration"][
        "PreferredFileServerIp"
    ]
    return dns_name, private_ip
