# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, TYPE_CHECKING

from azure.core import AsyncPipelineClient
from azure.purview.scanning.core.rest import AsyncHttpResponse, HttpRequest, _AsyncStreamContextManager
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Dict

    from azure.core.credentials_async import AsyncTokenCredential

from ._configuration import PurviewScanningClientConfiguration


class PurviewScanningClient(object):
    """Creates a Microsoft.Scanning management client.

    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param endpoint: The scanning endpoint of your purview account. Example: https://{accountName}.scan.purview.azure.com.
    :type endpoint: str
    """

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        endpoint: str,
        **kwargs: Any
    ) -> None:
        base_url = '{Endpoint}'
        self._config = PurviewScanningClientConfiguration(credential, endpoint, **kwargs)
        self._client = AsyncPipelineClient(base_url=base_url, config=self._config, **kwargs)

        self._serialize = Serializer()
        self._deserialize = Deserializer()
        self._serialize.client_side_validation = False

    async def send_request(self, http_request: HttpRequest, **kwargs: Any) -> AsyncHttpResponse:
        """Runs the network request through the client's chained policies.

        We have helper methods to create requests specific to this service in `azure.purview.scanning.rest`.
        Use these helper methods to create the request you pass to this method. See our example below:

        >>> from azure.purview.scanning.rest import build_get_request
        >>> request = build_get_request(key_vault_name)
        <HttpRequest [GET], url: '/azureKeyVaults/{keyVaultName}'>
        >>> response = await client.send_request(request)
        <AsyncHttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/python/protocol/quickstart

        For advanced cases, you can also create your own :class:`~azure.purview.scanning.core.rest.HttpRequest`
        and pass it in.

        :param http_request: The network request you want to make. Required.
        :type http_request: ~azure.purview.scanning.core.rest.HttpRequest
        :keyword bool stream_response: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.purview.scanning.core.rest.AsyncHttpResponse
        """
        request_copy = deepcopy(http_request)
        path_format_arguments = {
            'Endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }
        request_copy.url = self._client.format_url(request_copy.url, **path_format_arguments)
        if kwargs.pop("stream_response", False):
            return _AsyncStreamContextManager(
                client=self._client._pipeline,
                request=request_copy,
            )
        pipeline_response = await self._client._pipeline.run(request_copy._internal_request, **kwargs)
        response = AsyncHttpResponse(
            status_code=pipeline_response.http_response.status_code,
            request=request_copy,
            _internal_response=pipeline_response.http_response
        )
        await response.read()
        return response

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "PurviewScanningClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
