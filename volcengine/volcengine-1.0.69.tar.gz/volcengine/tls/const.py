# coding=utf-8

# HTTP request and response.
HTTP_GET = "GET"
HTTP_POST = "POST"
HTTP_DELETE = "DELETE"
HTTP_PUT = "PUT"

HTTP_PREFIX = "http://"
HTTPS_PREFIX = "https://"

CONTENT_TYPE = "Content-Type"
APPLICATION_JSON = "application/json"
APPLICATION_X_PROTOBUF = "application/x-protobuf"
CONTENT_MD5 = "Content-MD5"

X_SECURITY_TOKEN = "X-Security-Token"
X_TLS_REQUEST_ID = "X-Tls-Requestid"
X_TLS_HASHKEY = "x-tls-hashkey"
X_TLS_COMPRESSTYPE = "x-tls-compresstype"
X_TLS_BODYRAWSIZE = "x-tls-bodyrawsize"
X_TLS_CURSOR = "X-Tls-Cursor"
X_TLS_COUNT = "X-Tls-Count"

PARAMS = "Params"
BODY = "Body"
REQUEST_HEADERS = "RequestHeaders"

OK_STATUS = 200

# TLS APIs
CREATE_PROJECT = "/CreateProject"
DELETE_PROJECT = "/DeleteProject"
MODIFY_PROJECT = "/ModifyProject"
DESCRIBE_PROJECT = "/DescribeProject"
DESCRIBE_PROJECTS = "/DescribeProjects"

CREATE_TOPIC = "/CreateTopic"
DELETE_TOPIC = "/DeleteTopic"
MODIFY_TOPIC = "/ModifyTopic"
DESCRIBE_TOPIC = "/DescribeTopic"
DESCRIBE_TOPICS = "/DescribeTopics"

PUT_LOGS = "/PutLogs"
DESCRIBE_CURSOR = "/DescribeCursor"
CONSUME_LOGS = "/ConsumeLogs"
SEARCH_LOGS = "/SearchLogs"
DESCRIBE_LOG_CONTEXT = "/DescribeLogContext"
WEB_TRACKS = "/WebTracks"
DESCRIBE_HISTOGRAM = "/DescribeHistogram"
CREATE_DOWNLOAD_TASK = "/CreateDownloadTask"
DESCRIBE_DOWNLOAD_TASKS = "/DescribeDownloadTasks"
DESCRIBE_DOWNLOAD_URL = "/DescribeDownloadUrl"

CREATE_INDEX = "/CreateIndex"
DELETE_INDEX = "/DeleteIndex"
MODIFY_INDEX = "/ModifyIndex"
DESCRIBE_INDEX = "/DescribeIndex"

DESCRIBE_SHARDS = "/DescribeShards"

CREATE_HOST_GROUP = "/CreateHostGroup"
DELETE_HOST_GROUP = "/DeleteHostGroup"
MODIFY_HOST_GROUP = "/ModifyHostGroup"
DESCRIBE_HOST_GROUP = "/DescribeHostGroup"
DESCRIBE_HOST_GROUPS = "/DescribeHostGroups"
DESCRIBE_HOSTS = "/DescribeHosts"
DELETE_HOST = "/DeleteHost"
DESCRIBE_HOST_GROUP_RULES = "/DescribeHostGroupRules"
MODIFY_HOST_GROUPS_AUTO_UPDATE = "/ModifyHostGroupsAutoUpdate"

CREATE_RULE = "/CreateRule"
DELETE_RULE = "/DeleteRule"
MODIFY_RULE = "/ModifyRule"
DESCRIBE_RULE = "/DescribeRule"
DESCRIBE_RULES = "/DescribeRules"
APPLY_RULE_TO_HOST_GROUPS = "/ApplyRuleToHostGroups"
DELETE_RULE_FROM_HOST_GROUPS = "/DeleteRuleFromHostGroups"

CREATE_ALARM_NOTIFY_GROUP = "/CreateAlarmNotifyGroup"
DELETE_ALARM_NOTIFY_GROUP = "/DeleteAlarmNotifyGroup"
MODIFY_ALARM_NOTIFY_GROUP = "/ModifyAlarmNotifyGroup"
DESCRIBE_ALARM_NOTIFY_GROUPS = "/DescribeAlarmNotifyGroups"
CREATE_ALARM = "/CreateAlarm"
DELETE_ALARM = "/DeleteAlarm"
MODIFY_ALARM = "/ModifyAlarm"
DESCRIBE_ALARMS = "/DescribeAlarms"

OPEN_KAFKA_CONSUMER = "/OpenKafkaConsumer"
CLOSE_KAFKA_CONSUMER = "/CloseKafkaConsumer"
DESCRIBE_KAFKA_CONSUMER = "/DescribeKafkaConsumer"

# TLS API fields
DATA = "Data"

REQUEST_ID = "RequestId"
DESCRIPTION = "Description"
PAGE_NUMBER = "PageNumber"
PAGE_SIZE = "PageSize"
TOTAL = "Total"
CREATE_TIME = "CreateTime"
MODIFY_TIME = "ModifyTime"

PROJECT_ID = "ProjectId"
PROJECT_NAME = "ProjectName"
REGION = "Region"
IS_FULL_NAME = "IsFullName"
PROJECTS = "Projects"

TOPIC_ID = "TopicId"
TOPIC_NAME = "TopicName"
TTL = "Ttl"
SHARD_COUNT = "ShardCount"
TOPICS = "Topics"

FULL_TEXT = "FullText"
KEY_VALUE = "KeyValue"
KEY = "Key"
VALUE = "Value"
CASE_SENSITIVE = "CaseSensitive"
DELIMITER = "Delimiter"
INCLUDE_CHINESE = "IncludeChinese"
VALUE_TYPE = "ValueType"
SQL_FLAG = "SqlFlag"

SHARD_ID = "ShardId"
SHARDS = "Shards"
LZ4 = "lz4"
FROM = "From"
CURSOR = "Cursor"
END_CURSOR = "EndCursor"
LOG_GROUP_COUNT = "LogGroupCount"
COMPRESSION = "Compression"
START_TIME = "StartTime"
END_TIME = "EndTime"
QUERY = "Query"
LIMIT = "Limit"
CONTEXT = "Context"
SORT = "Sort"
DESC = "desc"
ASC = "asc"
SCHEMA = "Schema"
TYPE = "Type"
RESULT_STATUS = "ResultStatus"
HIT_COUNT = "HitCount"
LIST_OVER = "ListOver"
ANALYSIS = "Analysis"
COUNT = "Count"
LOGS = "Logs"
ANALYSIS_RESULT = "AnalysisResult"
LOG_CONTEXT_INFOS = "LogContextInfos"
PREV_OVER = "PrevOver"
NEXT_OVER = "NextOver"
SOURCE = "Source"
INTERVAL = "Interval"
TOTAL_COUNT = "TotalCount"
HISTOGRAM = "Histogram"
TASK_ID = "TaskId"
TASKS = "Tasks"
DOWNLOAD_URL = "DownloadUrl"

HOST_GROUP_ID = "HostGroupId"
HOST_GROUP_IDS = "HostGroupIds"
HOST_GROUP_NAME = "HostGroupName"
HOST_GROUP_TYPE = "HostGroupType"
IP = "Ip"
IP_TYPE = "IP"
LABEL = "Label"
HOST_IP_LIST = "HostIpList"
HOST_IDENTIFIER = "HostIdentifier"
HOST_GROUP_INFO = "HostGroupInfo"
HOST_GROUP_INFOS = "HostGroupInfos"
HOST_INFOS = "HostInfos"
HEARTBEAT_STATUS = "HeartbeatStatus"

RULE_ID = "RuleId"
RULE_NAME = "RuleName"
PATHS = "Paths"
LOG_TYPE = "LogType"
INPUT_TYPE = "InputType"
EXTRACT_RULE = "ExtractRule"
EXCLUDE_PATHS = "ExcludePaths"
USER_DEFINE_RULE = "UserDefineRule"
LOG_SAMPLE = "LogSample"
CONTAINER_RULE = "ContainerRule"
RULE_INFO = "RuleInfo"
RULE_INFOS = "RuleInfos"
HOST_GROUP_HOSTS_RULES_INFO = "HostGroupHostsRulesInfo"
HOST_GROUP_HOSTS_RULES_INFOS = "HostGroupHostsRulesInfos"
ENV_TAG = "EnvTag"
KUBERNETES_RULE = "KubernetesRule"
PARSE_PATH_RULE = "ParsePathRule"
PATH_SAMPLE = "PathSample"
BEGIN_REGEX = "BeginRegex"
LOG_REGEX = "LogRegex"
KEYS = "Keys"
TIME_KEY = "TimeKey"
TIME_FORMAT = "TimeFormat"
FILTER_KEY_REGEX = "FilterKeyRegex"
UN_MATCH_UP_LOAD_SWITCH = "UnMatchUpLoadSwitch"
UN_MATCH_LOG_KEY = "UnMatchLogKey"
REGEX = "Regex"
STREAM = "Stream"
CONTAINER_NAME_REGEX = "ContainerNameRegex"
INCLUDE_CONTAINER_LABEL_REGEX = "IncludeContainerLabelRegex"
EXCLUDE_CONTAINER_LABEL_REGEX = "ExcludeContainerLabelRegex"
INCLUDE_CONTAINER_ENV_REGEX = "IncludeContainerEnvRegex"
EXCLUDE_CONTAINER_ENV_REGEX = "ExcludeContainerEnvRegex"
LOG_TEMPLATE = "LogTemplate"
FORMAT = "Format"
HASH_KEY = "HashKey"
SHARD_HASH_KEY = "ShardHashKey"
ENABLE_RAW_LOG = "EnableRawLog"
FIELDS = "Fields"

ALARM_NOTIFY_GROUP_ID = "AlarmNotifyGroupId"
ALARM_NOTIFY_GROUP_NAME = "AlarmNotifyGroupName"
NOTIFY_TYPE = "NotifyType"
TRIGGER = "Trigger"
RECOVERY = "Recovery"
RECEIVERS = "Receivers"
RECEIVER_NAME = "ReceiverName"
ALARM_NOTIFY_GROUPS = "AlarmNotifyGroups"
ALARM_ID = "AlarmId"
ALARM_NAME = "AlarmName"
QUERY_REQUEST = "QueryRequest"
REQUEST_CYCLE = "RequestCycle"
CONDITION = "Condition"
ALARM_PERIOD = "AlarmPeriod"
ALARM_NOTIFY_GROUP = "AlarmNotifyGroup"
STATUS = "Status"
TRIGGER_PERIOD = "TriggerPeriod"
USER_DEFINE_MSG = "UserDefineMsg"
ALARMS = "Alarms"
TIME = "Time"
NUMBER = "Number"
START_TIME_OFFSET = "StartTimeOffset"
END_TIME_OFFSET = "EndTimeOffset"
RECEIVER_TYPE = "ReceiverType"
RECEIVER_NAMES = "ReceiverNames"
RECEIVER_CHANNELS = "ReceiverChannels"
WEBHOOK = "Webhook"

ALLOW_CONSUME = "AllowConsume"
CONSUME_TOPIC = "ConsumeTopic"
