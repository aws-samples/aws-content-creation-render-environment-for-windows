from __future__ import print_function

import logging

import boto3
from crhelper import CfnResource

logger = logging.getLogger(__name__)
helper = CfnResource(json_logging=False, log_level='DEBUG', boto_level='CRITICAL', sleep_on_delete=120)
fsx = boto3.client('fsx')


@helper.create
def create(event, context):
    logger.info("Got Create")
    properties = event.get('ResourceProperties', {})
    fsx_id = properties.get('FSxFileSystemId')

    fsx_dns_name = _fsx_dns_name(fsx_id)

    helper.Data.update(
        {
            "FSxDNSName": fsx_dns_name
        }
    )
    return fsx_dns_name


@helper.update
def update(event, context):
    logger.info("Got Update")


@helper.delete
def delete(event, context):
    logger.info("Got Delete")


def handler(event, context):
    helper(event, context)


def _fsx_dns_name(fsx_id):
    response = fsx.describe_file_systems(
        FileSystemIds=[
            fsx_id,
        ]
    )
    return response['FileSystems'][0]['DNSName']
