# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Optional, TYPE_CHECKING, Union

from azure.core.pipeline.transport._base import _format_url_section
from azure.purview.scanning.core.rest import HttpRequest
from msrest import Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any

_SERIALIZER = Serializer()


def build_run_scan_request(
    data_source_name: str,
    scan_name: str,
    run_id: str,
    *,
    scan_level: Optional[Union[str, "_models.ScanLevelType"]] = None,
    **kwargs: Any
) -> HttpRequest:
    """Runs the scan.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder into your code flow.

    :param data_source_name:
    :type data_source_name: str
    :param scan_name:
    :type scan_name: str
    :param run_id:
    :type run_id: str
    :keyword scan_level:
    :paramtype scan_level: str or ~azure.purview.scanning.models.ScanLevelType
    :return: Returns an :class:`~azure.purview.scanning.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this response into your code flow.
    :rtype: ~azure.purview.scanning.core.rest.HttpRequest

    Example:
        .. code-block:: python


            # response body for status code(s): 202
            response_body == {
                "endTime": "datetime (optional)",
                "error": {},
                "scanResultId": "str (optional)",
                "startTime": "datetime (optional)",
                "status": "str (optional)"
            }

    """
    api_version = "2018-12-01-preview"
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/datasources/{dataSourceName}/scans/{scanName}/runs/{runId}')
    path_format_arguments = {
        'dataSourceName': _SERIALIZER.url("data_source_name", data_source_name, 'str'),
        'scanName': _SERIALIZER.url("scan_name", scan_name, 'str'),
        'runId': _SERIALIZER.url("run_id", run_id, 'str'),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    if scan_level is not None:
        query_parameters['scanLevel'] = _SERIALIZER.query("scan_level", scan_level, 'str')
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_cancel_scan_request(
    data_source_name: str,
    scan_name: str,
    run_id: str,
    **kwargs: Any
) -> HttpRequest:
    """Cancels a scan.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder into your code flow.

    :param data_source_name:
    :type data_source_name: str
    :param scan_name:
    :type scan_name: str
    :param run_id:
    :type run_id: str
    :return: Returns an :class:`~azure.purview.scanning.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this response into your code flow.
    :rtype: ~azure.purview.scanning.core.rest.HttpRequest

    Example:
        .. code-block:: python


            # response body for status code(s): 202
            response_body == {
                "endTime": "datetime (optional)",
                "error": {},
                "scanResultId": "str (optional)",
                "startTime": "datetime (optional)",
                "status": "str (optional)"
            }

    """
    api_version = "2018-12-01-preview"
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/datasources/{dataSourceName}/scans/{scanName}/runs/{runId}/:cancel')
    path_format_arguments = {
        'dataSourceName': _SERIALIZER.url("data_source_name", data_source_name, 'str'),
        'scanName': _SERIALIZER.url("scan_name", scan_name, 'str'),
        'runId': _SERIALIZER.url("run_id", run_id, 'str'),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_list_scan_history_request(
    data_source_name: str,
    scan_name: str,
    **kwargs: Any
) -> HttpRequest:
    """Lists the scan history of a scan.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder into your code flow.

    :param data_source_name:
    :type data_source_name: str
    :param scan_name:
    :type scan_name: str
    :return: Returns an :class:`~azure.purview.scanning.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this response into your code flow.
    :rtype: ~azure.purview.scanning.core.rest.HttpRequest

    Example:
        .. code-block:: python


            # response body for status code(s): 200
            response_body == {
                "count": "long (optional)",
                "nextLink": "str (optional)",
                "value": [
                    {
                        "assetsClassified": "long (optional)",
                        "assetsDiscovered": "long (optional)",
                        "dataSourceType": "str (optional)",
                        "diagnostics": {},
                        "endTime": "datetime (optional)",
                        "error": {},
                        "errorMessage": "str (optional)",
                        "id": "str (optional)",
                        "parentId": "str (optional)",
                        "pipelineStartTime": "datetime (optional)",
                        "queuedTime": "datetime (optional)",
                        "resourceId": "str (optional)",
                        "runType": "str (optional)",
                        "scanLevelType": "str (optional)",
                        "scanRulesetType": "str (optional)",
                        "scanRulesetVersion": "int (optional)",
                        "startTime": "datetime (optional)",
                        "status": "str (optional)"
                    }
                ]
            }

    """
    api_version = "2018-12-01-preview"
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/datasources/{dataSourceName}/scans/{scanName}/runs')
    path_format_arguments = {
        'dataSourceName': _SERIALIZER.url("data_source_name", data_source_name, 'str'),
        'scanName': _SERIALIZER.url("scan_name", scan_name, 'str'),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )

