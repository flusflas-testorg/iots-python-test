# generated by datamodel-codegen:
#   filename:  anythingdb.yaml
#   timestamp: 2023-01-12T10:42:13+00:00

from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from pydantic import Field, constr

from models.basemodel import IterBaseModel


class Error(IterBaseModel):
    status: int = Field(..., example=400)
    message: str = Field(..., example='invalid id')
    details: Optional[Dict[str, Any]] = Field(
        None, description='Key/value object with extra information about the error.'
    )


class ErrorResponse(IterBaseModel):
    error: Optional[Error] = None


class Link(IterBaseModel):
    href_pattern: Optional[str] = Field(
        None, example='/spaces/myspace/categories/cpus/things/+'
    )
    rel_pattern: Optional[str] = Field(None, example='*')
    multiple: Optional[bool] = Field(None, example=False)
    optional: Optional[bool] = Field(None, example=False)


class Validators(IterBaseModel):
    links: Optional[List[Link]] = None


class Paging(IterBaseModel):
    next_cursor: Optional[str] = Field(None, example='')
    previous_cursor: Optional[str] = Field(None, example='')


class ModelBase(IterBaseModel):
    name: constr(regex=r'^[a-zA-Z0-9_:-]{1,26}$') = Field(
        ...,
        description='Name of the Model that will be used as a unique identifier.',
        example='RaspberryPiModel',
    )
    description: Optional[str] = Field(None, example='My Raspberry Pi Model')


class ModelCreate(ModelBase):
    pass


class ModelUpdate(ModelBase):
    pass


class Model(ModelBase):
    id: Optional[str] = Field(None, example='01FPT3MJBRBMA5462PEE57FRKB')
    created: Optional[datetime] = Field(None, example='2021-11-17T10:08:31Z')
    modified: Optional[datetime] = Field(None, example='2021-11-17T10:08:31Z')


class Paging1(IterBaseModel):
    next_cursor: Optional[str] = Field(None, example='')
    previous_cursor: Optional[str] = Field(None, example='')


class ModelList(IterBaseModel):
    data: Optional[List[Model]] = None
    paging: Optional[Paging1] = None


class LinkValidator(IterBaseModel):
    href_pattern: Optional[str] = Field(
        None,
        description="A URL expression to be checked against each `href` in Thing's links. URL expressions allow `+` (single level) and `#` (multi level) wildcards.",
    )
    rel_pattern: Optional[str] = Field(
        None, description="A regex to be checked against each `rel` in Thing's links."
    )
    multiple: Optional[bool] = Field(
        True,
        description="If `true`, more than one Thing's link in a Category can meet the criteria of this link validator.",
    )
    optional: Optional[bool] = Field(
        True,
        description='If `true`, a Thing will not need to have a link meeting the `href` and `rel` criteria of this link validator.',
    )


class Template(IterBaseModel):
    title: Optional[str] = Field(None, example='SmartWorks Device')
    description: Optional[str] = Field(None, example='My connected SmartWorks device')
    properties: Optional[Dict[str, Any]] = Field(
        None,
        example={
            'cpu': {
                'title': 'CPU %',
                'description': 'Device CPU usage in percent',
                'type': 'number',
                'unit': 'percent',
                'readOnly': False,
            }
        },
    )
    actions: Optional[Dict[str, Any]] = Field(
        None,
        example={
            'delay': {
                'title': 'Delay',
                'description': 'Change sending frequency',
                'input': {
                    'properties': {
                        'input': {'maximum': 100, 'minimum': 3, 'type': 'number'}
                    }
                },
            }
        },
    )
    events: Optional[Dict[str, Any]] = Field(
        None,
        example={
            'highCPU': {
                'title': 'High CPU',
                'description': 'The CPU usage is over 50%',
                'data': {'type': 'number', 'unit': 'percent'},
            }
        },
    )
    links: Optional[List[Dict[str, Any]]] = None


class ModelVersionBase(IterBaseModel):
    title: Optional[str] = Field(None, example='Version 1')
    description: Optional[str] = Field(None, example='Version 1 of RaspberryPiModel')
    template: Optional[Template] = None


class ModelVersionCreate(ModelVersionBase):
    pass


class ModelVersion(ModelVersionBase):
    version: Optional[int] = Field(None, example=1)
    created: Optional[datetime] = Field(None, example='2021-11-23T21:11:37Z')


class Paging2(IterBaseModel):
    next_cursor: Optional[str] = Field(None, example='')
    previous_cursor: Optional[str] = Field(None, example='')


class ModelVersionList(IterBaseModel):
    data: Optional[List[ModelVersion]] = None
    paging: Optional[Paging2] = None


class ModelDescription(IterBaseModel):
    name: Optional[str] = Field(
        None, description='Model name.', example='RaspberryPiModel'
    )
    version: Optional[int] = Field(None, description='Version number.', example=1)


class ModelDescriptionCategory(IterBaseModel):
    name: str = Field(..., description='Model name.', example='RaspberryPiModel')
    version: Optional[int] = Field(None, description='Version number.', example=1)


class ThingBase(IterBaseModel):
    title: Optional[str] = Field(None, example='SmartWorks Device')
    description: Optional[str] = Field(None, example='My connected SmartWorks device')
    field_type: Optional[Union[str, List[str]]] = Field(
        None, alias='@type', example=['Light', 'OnOffSwitch']
    )
    model: Optional[ModelDescription] = None
    properties: Optional[Dict[str, Any]] = Field(
        None,
        example={
            'cpu': {
                'title': 'CPU %',
                'description': 'Device CPU usage in percent',
                'type': 'number',
                'unit': 'percent',
                'readOnly': False,
            },
            'disk': {
                'title': 'Disk %',
                'description': 'Device Disk usage in percent',
                'type': 'number',
                'unit': 'percent',
                'readOnly': False,
            },
            'memory': {
                'title': 'Memory %',
                'description': 'Device Memory usage in percent',
                'type': 'number',
                'unit': 'percent',
                'readOnly': False,
            },
        },
    )
    actions: Optional[Dict[str, Any]] = Field(
        None,
        example={
            'delay': {
                'title': 'Delay',
                'description': 'Change sending frequency',
                'input': {
                    'properties': {
                        'input': {'maximum': 100, 'minimum': 3, 'type': 'number'}
                    }
                },
            },
            'reboot': {'title': 'Reboot', 'description': 'Reboot device'},
        },
    )
    events: Optional[Dict[str, Any]] = Field(
        None,
        example={
            'highCPU': {
                'title': 'High CPU',
                'description': 'The CPU usage is over 50%',
                'data': {'type': 'number', 'unit': 'percent'},
            }
        },
    )


class ThingCreate(ThingBase):
    categories: Optional[List[str]] = Field(None, example=['category1', 'category2'])


class ThingCategoryCreate(ThingBase):
    pass


class ThingUpdate(ThingBase):
    uid: Optional[str] = Field(None, example='01FPSXTMN4CEGX09HF5RQ4RMY6')
    id: Optional[str] = Field(
        None,
        example='https://api.swx.altairone.com/beta/spaces/space01/things/01FPSXTMN4CEGX09HF5RQ4RMY6',
    )
    categories: Optional[List[str]] = Field(None, example=['category1', 'category2'])


class ThingCategoryUpdate(ThingBase):
    uid: Optional[str] = Field(None, example='01FPSXTMN4CEGX09HF5RQ4RMY6')
    id: Optional[str] = Field(
        None,
        example='https://api.swx.altairone.com/beta/spaces/space01/categories/category1/things/01FPSXTMN4CEGX09HF5RQ4RMY6',
    )


class Thing(ThingBase):
    uid: Optional[str] = Field(None, example='01FPSXTMN4CEGX09HF5RQ4RMY6')
    id: Optional[str] = Field(
        None,
        example='https://api.swx.altairone.com/beta/spaces/space01/things/01FPSXTMN4CEGX09HF5RQ4RMY6',
    )
    categories: Optional[List[str]] = Field(None, example=['category1', 'category2'])
    created: Optional[datetime] = Field(None, example='2021-12-13T09:38:11Z')
    modified: Optional[datetime] = Field(None, example='2021-12-13T09:38:11Z')


class ThingCategory(ThingBase):
    uid: Optional[str] = Field(None, example='01FPSXTMN4CEGX09HF5RQ4RMY6')
    id: Optional[str] = Field(
        None,
        example='https://api.swx.altairone.com/beta/spaces/space01/categories/category1/things/01FPSXTMN4CEGX09HF5RQ4RMY6',
    )
    created: Optional[datetime] = Field(None, example='2021-12-13T09:38:11Z')
    modified: Optional[datetime] = Field(None, example='2021-12-13T09:38:11Z')


class Paging3(IterBaseModel):
    next_cursor: Optional[str] = Field(None, example='')
    previous_cursor: Optional[str] = Field(None, example='')


class ThingList(IterBaseModel):
    data: Optional[List[Thing]] = None
    paging: Optional[Paging3] = None


class Paging4(IterBaseModel):
    next_cursor: Optional[str] = Field(None, example='')
    previous_cursor: Optional[str] = Field(None, example='')


class ThingCategoryList(IterBaseModel):
    data: Optional[List[ThingCategory]] = None
    paging: Optional[Paging4] = None


class ThingsDeleted(IterBaseModel):
    __root__: List[str] = Field(
        ...,
        description='List of IDs of the deleted Things.',
        example=['01GM38SSQC0X32YQSXZYFJPGGC', '01GM38T332KMGEXJZNB6VYTRBM'],
        title='Things Deleted',
    )


class ThingOAuth2Credentials(IterBaseModel):
    client_id: Optional[str] = Field(
        None,
        description="The Client ID of the Thing's OAuth2 client.",
        example='altair::01GJCPZPVCZKD9GDV4A51NT27H',
    )
    client_secret: Optional[str] = Field(
        None,
        description="The Client secret of the Thing's OAuth2 client.",
        example='MSivCvI71kHEAo0tXY6edIhTsQl12n',
    )


class ActionRequest(IterBaseModel):
    __root__: Optional[Dict[str, Any]] = None


class ActionResponse(IterBaseModel):
    __root__: Optional[Dict[str, Any]] = None


class ActionWithCategoryResponse(IterBaseModel):
    __root__: Optional[Dict[str, Any]] = None


class Paging5(IterBaseModel):
    next_cursor: Optional[str] = Field(None, example='')
    previous_cursor: Optional[str] = Field(None, example='')


class ActionDelayListResponse(IterBaseModel):
    data: Optional[List[ActionResponse]] = Field(
        None,
        example=[
            {
                'delay': {
                    'input': {'delay': 5},
                    'status': 'pending',
                    'timeRequested': '2022-06-02 15:37:46+0000',
                    'href': '/beta/spaces/altair/things/01FPSXTMN4CEGX09HF5RQ4RMY6/actions/delay/01EDCAQE78A7CP6REXV5J8BAKR',
                }
            },
            {
                'delay': {
                    'input': {'delay': 7},
                    'status': 'pending',
                    'timeRequested': '2022-06-02 15:39:54+0000',
                    'href': '/beta/spaces/altair/things/01FPSXTMN4CEGX09HF5RQ4RMY6/actions/delay/01EDCB9FMD0Q3QR0YV4TWY4S3E',
                }
            },
        ],
    )
    paging: Optional[Paging5] = None


class Paging6(IterBaseModel):
    next_cursor: Optional[str] = Field(None, example='')
    previous_cursor: Optional[str] = Field(None, example='')


class ActionDelayListWithCategoryResponse(IterBaseModel):
    data: Optional[List[ActionWithCategoryResponse]] = Field(
        None,
        example=[
            {
                'delay': {
                    'input': {'delay': 5},
                    'status': 'pending',
                    'timeRequested': '2022-06-02 15:37:46+0000',
                    'href': '/spaces/altair/categories/ElectronicBoards/things/01FPSXTMN4CEGX09HF5RQ4RMY6/actions/delay/01EDCAQE78A7CP6REXV5J8BAKR',
                }
            },
            {
                'delay': {
                    'input': {'delay': 7},
                    'status': 'pending',
                    'timeRequested': '2022-06-02 15:39:54+0000',
                    'href': '/spaces/altair/things/categories/ElectronicBoards/01FPSXTMN4CEGX09HF5RQ4RMY6/actions/delay/01EDCB9FMD0Q3QR0YV4TWY4S3E',
                }
            },
        ],
    )
    paging: Optional[Paging6] = None


class Paging7(IterBaseModel):
    next_cursor: Optional[str] = Field(None, example='')
    previous_cursor: Optional[str] = Field(None, example='')


class ActionListResponse(IterBaseModel):
    data: Optional[List[ActionResponse]] = Field(
        None,
        example=[
            {
                'delay': {
                    'input': {'delay': 5},
                    'status': 'pending',
                    'timeRequested': '2022-06-02 15:37:46+0000',
                    'href': '/beta/spaces/altair/things/01FPSXTMN4CEGX09HF5RQ4RMY6/actions/delay/01EDCAQE78A7CP6REXV5J8BAKR',
                }
            },
            {
                'delay': {
                    'input': {'delay': 7},
                    'status': 'pending',
                    'timeRequested': '2022-06-02 15:39:54+0000',
                    'href': '/beta/spaces/altair/things/01FPSXTMN4CEGX09HF5RQ4RMY6/actions/delay/01EDCB9FMD0Q3QR0YV4TWY4S3E',
                }
            },
            {
                'reboot': {
                    'status': 'pending',
                    'timeRequested': '2022-06-02 15:56:12+0000',
                    'href': '/beta/spaces/altair/things/01FPSXTMN4CEGX09HF5RQ4RMY6/actions/delay/01EDCCZYATJW1Z3D4T4BA4S2QH',
                }
            },
        ],
    )
    paging: Optional[Paging7] = None


class Paging8(IterBaseModel):
    next_cursor: Optional[str] = Field(None, example='')
    previous_cursor: Optional[str] = Field(None, example='')


class ActionListWithCategoryResponse(IterBaseModel):
    data: Optional[List[ActionWithCategoryResponse]] = Field(
        None,
        example=[
            {
                'delay': {
                    'input': {'delay': 5},
                    'status': 'pending',
                    'timeRequested': '2022-06-02 15:37:46+0000',
                    'href': '/spaces/altair/categories/ElectronicBoards/things/01FPSXTMN4CEGX09HF5RQ4RMY6/actions/delay/01EDCAQE78A7CP6REXV5J8BAKR',
                }
            },
            {
                'delay': {
                    'input': {'delay': 7},
                    'status': 'pending',
                    'timeRequested': '2022-06-02 15:39:54+0000',
                    'href': '/spaces/altair/categories/ElectronicBoards/things/01FPSXTMN4CEGX09HF5RQ4RMY6/actions/delay/01EDCB9FMD0Q3QR0YV4TWY4S3E',
                }
            },
            {
                'reboot': {
                    'status': 'pending',
                    'timeRequested': '2022-06-02 15:56:12+0000',
                    'href': '/spaces/altair/categories/ElectronicBoards/things/01FPSXTMN4CEGX09HF5RQ4RMY6/actions/delay/01EDCCZYATJW1Z3D4T4BA4S2QH',
                }
            },
        ],
    )
    paging: Optional[Paging8] = None


class ActionUpdateRequest(IterBaseModel):
    __root__: Optional[Dict[str, Any]] = None


class ActionUpdateResponse(IterBaseModel):
    __root__: Optional[Dict[str, Any]] = None


class ActionUpdateWithCategoryResponse(IterBaseModel):
    __root__: Optional[Dict[str, Any]] = None


class EventRequest(IterBaseModel):
    __root__: Optional[Dict[str, Any]] = None


class EventResponse(IterBaseModel):
    __root__: Optional[Dict[str, Any]] = None


class EventWithCategoryResponse(IterBaseModel):
    __root__: Optional[Dict[str, Any]] = None


class Paging9(IterBaseModel):
    next_cursor: Optional[str] = Field(None, example='')
    previous_cursor: Optional[str] = Field(None, example='')


class EventListResponse(IterBaseModel):
    data: Optional[List[EventResponse]] = Field(
        None,
        example=[
            {
                'highCPU': {
                    'data': 61,
                    'timestamp': '2020-04-02 15:22:37+0000',
                    'href': '/beta/spaces/altair/things/01FPSXTMN4CEGX09HF5RQ4RMY6/events/highCPU/01EDCEZDTJX50SQTCJST5EW5NX',
                }
            },
            {
                'highCPU': {
                    'data': 85,
                    'timestamp': '2020-04-02 15:26:42+0000',
                    'href': '/beta/spaces/altair/things/01FPSXTMN4CEGX09HF5RQ4RMY6/events/highCPU/01EDCGYKV4YQ1CY3QHHSX8J843',
                }
            },
        ],
    )
    paging: Optional[Paging9] = None


class Paging10(IterBaseModel):
    next_cursor: Optional[str] = Field(None, example='')
    previous_cursor: Optional[str] = Field(None, example='')


class EventListWithCategoryResponse(IterBaseModel):
    data: Optional[List[EventWithCategoryResponse]] = Field(
        None,
        example=[
            {
                'highCPU': {
                    'data': 61,
                    'timestamp': '2020-04-02 15:22:37+0000',
                    'href': '/spaces/altair/categories/ElectronicBoards/things/01FPSXTMN4CEGX09HF5RQ4RMY6/events/highCPU/01EDCEZDTJX50SQTCJST5EW5NX',
                }
            },
            {
                'highCPU': {
                    'data': 85,
                    'timestamp': '2020-04-02 15:26:42+0000',
                    'href': '/spaces/altair/categories/ElectronicBoards/things/01FPSXTMN4CEGX09HF5RQ4RMY6/events/highCPU/01EDCGYKV4YQ1CY3QHHSX8J843',
                }
            },
        ],
    )
    paging: Optional[Paging10] = None


class Properties(IterBaseModel):
    __root__: Optional[Dict[str, Any]] = None


class Property(IterBaseModel):
    __root__: Optional[Dict[str, Any]] = None


class PropertyValues(IterBaseModel):
    __root__: Optional[Dict[str, Any]] = None


class PropertyHistoryValue(IterBaseModel):
    at: datetime = Field(
        ...,
        description='Date and time the values were recorded.',
        example='2022-08-22T13:10:00Z',
    )
    properties: PropertyValues


class PropertyHistoryValues(IterBaseModel):
    __root__: List[PropertyHistoryValue] = Field(
        ...,
        description='List of historical Property values.',
        example=[
            {
                'at': '2022-08-22T13:10:00Z',
                'properties': {'cpu': 43, 'memory': 27, 'disk': 19},
            },
            {'at': '2022-08-22T13:09:00Z', 'properties': {'cpu': 87, 'memory': 69}},
            {'at': '2022-08-22T13:08:30Z', 'properties': {'disk': 17}},
        ],
        title='Property History Values',
    )


class Paging11(IterBaseModel):
    next_cursor: Optional[str] = Field(None, example='')
    previous_cursor: Optional[str] = Field(None, example='')


class PropertyHistoryValueList(IterBaseModel):
    data: Optional[List[PropertyHistoryValue]] = None
    paging: Optional[Paging11] = None


class ThingStatusBase(IterBaseModel):
    title: Optional[str] = Field(None, example='SmartWorks Device')
    description: Optional[str] = Field(None, example='My connected SmartWorks device')
    field_type: Optional[Union[str, List[str]]] = Field(
        None, alias='@type', example=['Light', 'OnOffSwitch']
    )
    model: Optional[ModelDescription] = None
    properties: Optional[PropertyValues] = None


class ThingStatusCreate(ThingStatusBase):
    categories: Optional[List[str]] = Field(None, example=['category1', 'category2'])


class ThingStatusCategoryCreate(ThingStatusBase):
    pass


class ThingStatusUpdate(ThingStatusBase):
    uid: Optional[str] = Field(None, example='01FPSXTMN4CEGX09HF5RQ4RMY6')
    id: Optional[str] = Field(
        None,
        example='https://api.swx.altairone.com/beta/spaces/space01/things/01FPSXTMN4CEGX09HF5RQ4RMY6',
    )
    categories: Optional[List[str]] = Field(None, example=['category1', 'category2'])


class ThingStatusCategoryUpdate(ThingStatusBase):
    uid: Optional[str] = Field(None, example='01FPSXTMN4CEGX09HF5RQ4RMY6')
    id: Optional[str] = Field(
        None,
        example='https://api.swx.altairone.com/beta/spaces/space01/categories/category1/things/01FPSXTMN4CEGX09HF5RQ4RMY6',
    )


class ThingStatus(ThingStatusBase):
    uid: Optional[str] = Field(None, example='01FPSXTMN4CEGX09HF5RQ4RMY6')
    id: Optional[str] = Field(
        None,
        example='https://api.swx.altairone.com/beta/spaces/space01/things/01FPSXTMN4CEGX09HF5RQ4RMY6',
    )
    categories: Optional[List[str]] = Field(None, example=['category1', 'category2'])
    created: Optional[datetime] = Field(None, example='2021-12-13T09:38:11Z')
    modified: Optional[datetime] = Field(None, example='2021-12-13T09:38:11Z')


class ThingStatusCategory(ThingStatusBase):
    uid: Optional[str] = Field(None, example='01FPSXTMN4CEGX09HF5RQ4RMY6')
    id: Optional[str] = Field(
        None,
        example='https://api.swx.altairone.com/beta/spaces/space01/categories/category1/things/01FPSXTMN4CEGX09HF5RQ4RMY6',
    )
    created: Optional[datetime] = Field(None, example='2021-12-13T09:38:11Z')
    modified: Optional[datetime] = Field(None, example='2021-12-13T09:38:11Z')


class Paging12(IterBaseModel):
    next_cursor: Optional[str] = Field(None, example='')
    previous_cursor: Optional[str] = Field(None, example='')


class ThingStatusList(IterBaseModel):
    data: Optional[List[ThingStatus]] = None
    paging: Optional[Paging12] = None


class Paging13(IterBaseModel):
    next_cursor: Optional[str] = Field(None, example='')
    previous_cursor: Optional[str] = Field(None, example='')


class ThingStatusCategoryList(IterBaseModel):
    data: Optional[List[ThingStatusCategory]] = None
    paging: Optional[Paging13] = None


class PostAPICursor(IterBaseModel):
    query: str = Field(..., description='Contains the query string to be executed\n')
    count: Optional[bool] = Field(
        None,
        description='Indicates whether the number of documents in the result set should be returned in\nthe "count" attribute of the result.\nCalculating the "count" attribute might have a performance impact for some queries\nin the future so this option is turned off by default, and "count"\nis only returned when requested.\n',
    )
    batchSize: Optional[int] = Field(
        None,
        description='Maximum number of result documents to be transferred from\nthe server to the client in one roundtrip. If this attribute is\nnot set, a server-controlled default value will be used. A *batchSize* value of\n*0* is disallowed.\n',
    )
    ttl: Optional[int] = Field(
        None,
        description='The time-to-live for the cursor (in seconds). If the result set is small enough\n(less than or equal to `batchSize`) then results are returned right away.\nOtherwise they are stored in memory and will be accessible via the cursor with\nrespect to the `ttl`. The cursor will be removed on the server automatically\nafter the specified amount of time. This is useful to ensure garbage collection\nof cursors that are not fully fetched by clients. If not set, a server-defined\nvalue will be used (default: 30 seconds).\n',
    )
    cache: Optional[bool] = Field(
        None,
        description='Flag to determine whether the AQL query results cache\nshall be used. If set to *false*, then any query cache lookup will be skipped\nfor the query. If set to *true*, it will lead to the query cache being checked\nfor the query if the query cache mode is either *on* or *demand*.\n',
    )
    memoryLimit: Optional[int] = Field(
        None,
        description='The maximum number of memory (measured in bytes) that the query is allowed to\nuse. If set, then the query will fail with error "resource limit exceeded" in\ncase it allocates too much memory. A value of *0* indicates that there is no\nmemory limit.\n',
    )
    bindVars: Optional[List[Dict[str, Any]]] = Field(
        None, description='Key/value pairs representing the bind parameters.\n'
    )
    options: Optional[Dict[str, Any]] = Field(
        None, description='This attribute is currently ignored.\n'
    )


class PostAPICursorResponse(IterBaseModel):
    error: bool = Field(
        ...,
        description='A flag to indicate that an error occurred (*false* in this case)\n\n',
    )
    code: Optional[int] = Field(None, description='the HTTP status code\n\n')
    result: Optional[List] = Field(
        None,
        description='an array of result documents (might be empty if query has no results)\n\n',
    )
    hasMore: Optional[bool] = Field(
        None,
        description='A boolean indicator whether there are more results\navailable for the cursor on the server\n\n',
    )
    count: Optional[int] = Field(
        None,
        description='the total number of result documents available (only\navailable if the query was executed with the *count* attribute set)\n\n',
    )
    id: Optional[str] = Field(
        None,
        description='id of temporary cursor created on the server (optional, see above)\n\n',
    )
    extra: Optional[Dict[str, Any]] = Field(
        None,
        description='an optional JSON object with extra information about the query result\ncontained in its *stats* sub-attribute. For data-modification queries, the\n*extra.stats* sub-attribute will contain the number of modified documents and\nthe number of documents that could not be modified\ndue to an error (if *ignoreErrors* query option is specified)\n\n',
    )
    cached: Optional[bool] = Field(
        None,
        description='a boolean flag indicating whether the query result was served\nfrom the query cache or not. If the query result is served from the query\ncache, the *extra* return attribute will not contain any *stats* sub-attribute\nand no *profile* sub-attribute.\n\n',
    )


class ID(IterBaseModel):
    __root__: str = Field(..., example='01FPJGR4TWXHH23EHEKT4HEN6F')


class MQTTForm(IterBaseModel):
    enabled: Optional[bool] = Field(None, example=True)
    username: Optional[str] = Field(None, example='myusername')
    password: Optional[str] = Field(None, example='MyPa$$word123')
    description: Optional[str] = Field(None, example='MyCredential')


class MQTTThingForm(MQTTForm):
    pass


class MQTTCategoryForm(MQTTForm):
    collection_name: Optional[str] = Field(None, example='MyCollection')


class PublishItem(IterBaseModel):
    pattern: Optional[str] = Field(
        None,
        example='altair/collections/my_collection/things/01FWDZKSRZFGDACF4N7E3VSBBZ/data',
    )


class SubscribeItem(IterBaseModel):
    pattern: Optional[str] = Field(
        None,
        example='altair/collections/my_collection/things/01FWDZKSRZFGDACF4N7E3VSBBZ/data',
    )


class Acl(IterBaseModel):
    publish: Optional[List[PublishItem]] = None
    subscribe: Optional[List[SubscribeItem]] = None


class MQTTThingDocumentACL(IterBaseModel):
    acl: Optional[Acl] = None


class MQTTThingsDocument(MQTTThingForm):
    id: Optional[ID] = None
    created: Optional[str] = Field(None, example='2022-02-08T14:41:49.270946386+01:00,')


class MQTTCategoryDocument(MQTTCategoryForm):
    id: Optional[ID] = None
    created: Optional[str] = Field(None, example='2022-02-08T14:41:49.270946386+01:00,')


class MQTTThingsDocumentShow(MQTTThingForm):
    id: Optional[ID] = None
    created: Optional[str] = Field(None, example='2022-02-08T14:41:49.270946386+01:00,')
    topics: Optional[MQTTThingDocumentACL] = None


class Paging14(IterBaseModel):
    next_cursor: Optional[str] = Field(None, example='')
    previous_cursor: Optional[str] = Field(None, example='')


class MQTTThingsDocumentList(IterBaseModel):
    data: Optional[List[MQTTThingsDocumentShow]] = None
    paging: Optional[Paging14] = None


class CategoryBase(IterBaseModel):
    name: Optional[constr(regex=r'^[a-zA-Z0-9_:-]{1,26}$')] = Field(
        None,
        description='Name of the Category that will be used as a unique identifier.',
        example='ElectronicBoards',
    )
    description: Optional[str] = Field(None, example='My category')
    model: Optional[ModelDescriptionCategory] = None
    validators: Optional[Validators] = None


class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(CategoryBase):
    pass


class Category(CategoryBase):
    created: Optional[datetime] = Field(None, example='2021-11-17T03:15:40Z')
    modified: Optional[datetime] = Field(None, example='2021-11-17T03:15:40Z')


class CategoryList(IterBaseModel):
    data: Optional[List[Category]] = None
    paging: Optional[Paging] = None