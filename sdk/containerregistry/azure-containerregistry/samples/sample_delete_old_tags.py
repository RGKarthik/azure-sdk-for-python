# coding: utf-8

# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

"""
FILE: sample_delete_old_tags.py

DESCRIPTION:
    These samples demonstrates deleting the three oldest tags for each repository

USAGE:
    python sample_delete_old_tags.py

    Set the environment variables with your own values before running the sample:
    1) CONTAINERREGISTRY_ENDPOINT - The URL of you Container Registry account
"""

from dotenv import find_dotenv, load_dotenv
import os


class DeleteOperations(object):
    def __init__(self):
        load_dotenv(find_dotenv())
        self.account_url = os.environ["CONTAINERREGISTRY_ENDPOINT"]

    def delete_old_tags(self):
        from azure.containerregistry import (
            ContainerRegistryClient,
            ContainerRepositoryClient,
            TagOrder
        )
        from azure.identity import DefaultAzureCredential

        # [START list_repository_names]
        account_url = os.environ["CONTAINERREGISTRY_ENDPOINT"]
        credential = DefaultAzureCredential()
        client = ContainerRegistryClient(account_url, credential)

        for repository in client.list_repository_names():
            repository_client = ContainerRepositoryClient(account_url, repository, credential)
            # [END list_repository_names]

            # [START list_tags]
            tag_count = 0
            for tag in repository_client.list_tags(order_by=TagOrder.LAST_UPDATE_TIME_DESCENDING):
                tag_count += 1
                if tag_count > 3:
                    repository_client.delete_tag(tag.name)
            # [END list_tags]

        client.close()
