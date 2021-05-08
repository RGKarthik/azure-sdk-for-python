# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from typing import TYPE_CHECKING

from azure.core import PipelineClient
from azure.profiles import KnownProfiles, ProfileDefinition
from azure.profiles.multiapiclient import MultiApiClientMixin
from msrest import Deserializer, Serializer

from ._configuration import TextAnalyticsClientConfiguration
from ._operations_mixin import TextAnalyticsClientOperationsMixin

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Optional

    from azure.core.credentials import TokenCredential
    from azure.core.pipeline.transport import HttpRequest, HttpResponse

class _SDKClient(object):
    def __init__(self, *args, **kwargs):
        """This is a fake class to support current implemetation of MultiApiClientMixin."
        Will be removed in final version of multiapi azure-core based client
        """
        pass

class TextAnalyticsClient(TextAnalyticsClientOperationsMixin, MultiApiClientMixin, _SDKClient):
    """The Text Analytics API is a suite of text analytics web services built with best-in-class Microsoft machine learning algorithms. The API can be used to analyze unstructured text for tasks such as sentiment analysis, key phrase extraction and language detection. No training data is needed to use this API; just bring your text data. This API uses advanced natural language processing techniques to deliver best in class predictions. Further documentation can be found in https://docs.microsoft.com/en-us/azure/cognitive-services/text-analytics/overview.

    This ready contains multiple API versions, to help you deal with all of the Azure clouds
    (Azure Stack, Azure Government, Azure China, etc.).
    By default, it uses the latest API version available on public Azure.
    For production, you should stick to a particular api-version and/or profile.
    The profile sets a mapping between an operation group and its API version.
    The api-version parameter sets the default API version if the operation
    group is not described in the profile.

    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials.TokenCredential
    :param endpoint: Supported Cognitive Services endpoints (protocol and hostname, for example: https://westus.api.cognitive.microsoft.com).
    :type endpoint: str
    :param api_version: API version to use if no profile is provided, or if missing in profile.
    :type api_version: str
    :param profile: A profile definition, from KnownProfiles to dict.
    :type profile: azure.profiles.KnownProfiles
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    DEFAULT_API_VERSION = 'v3.0'
    _PROFILE_TAG = "azure.ai.textanalytics.TextAnalyticsClient"
    LATEST_PROFILE = ProfileDefinition({
        _PROFILE_TAG: {
            None: DEFAULT_API_VERSION,
        }},
        _PROFILE_TAG + " latest"
    )

    def __init__(
        self,
        credential,  # type: "TokenCredential"
        endpoint,  # type: str
        api_version=None, # type: Optional[str]
        profile=KnownProfiles.default, # type: KnownProfiles
        **kwargs  # type: Any
    ):
        if api_version == 'v3.0':
            base_url = '{Endpoint}/text/analytics/v3.0'
        elif api_version == 'v3.1-preview.5':
            base_url = '{Endpoint}/text/analytics/v3.1-preview.5'
        else:
            raise ValueError("API version {} is not available".format(api_version))
        self._config = TextAnalyticsClientConfiguration(credential, endpoint, **kwargs)
        self._client = PipelineClient(base_url=base_url, config=self._config, **kwargs)
        super(TextAnalyticsClient, self).__init__(
            api_version=api_version,
            profile=profile
        )

    @classmethod
    def _models_dict(cls, api_version):
        return {k: v for k, v in cls.models(api_version).__dict__.items() if isinstance(v, type)}

    @classmethod
    def models(cls, api_version=DEFAULT_API_VERSION):
        """Module depends on the API version:

           * v3.0: :mod:`v3_0.models<azure.ai.textanalytics.v3_0.models>`
           * v3.1-preview.5: :mod:`v3_1_preview_5.models<azure.ai.textanalytics.v3_1_preview_5.models>`
        """
        if api_version == 'v3.0':
            from .v3_0 import models
            return models
        elif api_version == 'v3.1-preview.5':
            from .v3_1_preview_5 import models
            return models
        raise ValueError("API version {} is not available".format(api_version))

    def close(self):
        self._client.close()
    def __enter__(self):
        self._client.__enter__()
        return self
    def __exit__(self, *exc_details):
        self._client.__exit__(*exc_details)
