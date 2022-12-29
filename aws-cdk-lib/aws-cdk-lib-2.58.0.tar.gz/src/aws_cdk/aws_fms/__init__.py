'''
# AWS::FMS Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_fms as fms
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for FMS construct libraries](https://constructs.dev/search?q=fms)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::FMS resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_FMS.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::FMS](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_FMS.html).

(Read the [CDK Contributing Guide](https://github.com/aws/aws-cdk/blob/main/CONTRIBUTING.md) and submit an RFC if you are interested in contributing to this construct library.)

<!--END CFNONLY DISCLAIMER-->
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from .._jsii import *

import constructs as _constructs_77d1e7e8
from .. import (
    CfnResource as _CfnResource_9df397a6,
    IInspectable as _IInspectable_c2943556,
    IResolvable as _IResolvable_da3f097b,
    TreeInspector as _TreeInspector_488e0dd5,
)


@jsii.implements(_IInspectable_c2943556)
class CfnNotificationChannel(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_fms.CfnNotificationChannel",
):
    '''A CloudFormation ``AWS::FMS::NotificationChannel``.

    Designates the IAM role and Amazon Simple Notification Service (SNS) topic to use to record SNS logs.

    To perform this action outside of the console, you must configure the SNS topic to allow the role ``AWSServiceRoleForFMS`` to publish SNS logs. For more information, see `Firewall Manager required permissions for API actions <https://docs.aws.amazon.com/waf/latest/developerguide/fms-api-permissions-ref.html>`_ in the *AWS Firewall Manager Developer Guide* .

    :cloudformationResource: AWS::FMS::NotificationChannel
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-notificationchannel.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_fms as fms
        
        cfn_notification_channel = fms.CfnNotificationChannel(self, "MyCfnNotificationChannel",
            sns_role_name="snsRoleName",
            sns_topic_arn="snsTopicArn"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        sns_role_name: builtins.str,
        sns_topic_arn: builtins.str,
    ) -> None:
        '''Create a new ``AWS::FMS::NotificationChannel``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param sns_role_name: The Amazon Resource Name (ARN) of the IAM role that allows Amazon SNS to record AWS Firewall Manager activity.
        :param sns_topic_arn: The Amazon Resource Name (ARN) of the SNS topic that collects notifications from AWS Firewall Manager .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a03e25c676e3f843e7365938075353612a65a3a2bd2538074f016448b29053c)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnNotificationChannelProps(
            sns_role_name=sns_role_name, sns_topic_arn=sns_topic_arn
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eae25dcbfb8d4710a66ea0f6804d609f2c8fbb762e291caa42156e2d5e0a5ccd)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__27e0110b31984037127ddfc8639de3754907e90f7485cfd5b43a5fbe4ad39717)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="snsRoleName")
    def sns_role_name(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the IAM role that allows Amazon SNS to record AWS Firewall Manager activity.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-notificationchannel.html#cfn-fms-notificationchannel-snsrolename
        '''
        return typing.cast(builtins.str, jsii.get(self, "snsRoleName"))

    @sns_role_name.setter
    def sns_role_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__00bd3c5f6e0b7d08ecc3e9d3f09ce0486f75f4e24649a6e59140bdaa48e6e9ed)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "snsRoleName", value)

    @builtins.property
    @jsii.member(jsii_name="snsTopicArn")
    def sns_topic_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the SNS topic that collects notifications from AWS Firewall Manager .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-notificationchannel.html#cfn-fms-notificationchannel-snstopicarn
        '''
        return typing.cast(builtins.str, jsii.get(self, "snsTopicArn"))

    @sns_topic_arn.setter
    def sns_topic_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d5dd2548355a1129e0085759bb293de343519fe581ead5c659ceff8ec36b346)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "snsTopicArn", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_fms.CfnNotificationChannelProps",
    jsii_struct_bases=[],
    name_mapping={"sns_role_name": "snsRoleName", "sns_topic_arn": "snsTopicArn"},
)
class CfnNotificationChannelProps:
    def __init__(
        self,
        *,
        sns_role_name: builtins.str,
        sns_topic_arn: builtins.str,
    ) -> None:
        '''Properties for defining a ``CfnNotificationChannel``.

        :param sns_role_name: The Amazon Resource Name (ARN) of the IAM role that allows Amazon SNS to record AWS Firewall Manager activity.
        :param sns_topic_arn: The Amazon Resource Name (ARN) of the SNS topic that collects notifications from AWS Firewall Manager .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-notificationchannel.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_fms as fms
            
            cfn_notification_channel_props = fms.CfnNotificationChannelProps(
                sns_role_name="snsRoleName",
                sns_topic_arn="snsTopicArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5624e06a5ce62823c414e320e35e25799cfeb05a7db7fa7dc3f5353d1e0fe469)
            check_type(argname="argument sns_role_name", value=sns_role_name, expected_type=type_hints["sns_role_name"])
            check_type(argname="argument sns_topic_arn", value=sns_topic_arn, expected_type=type_hints["sns_topic_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "sns_role_name": sns_role_name,
            "sns_topic_arn": sns_topic_arn,
        }

    @builtins.property
    def sns_role_name(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the IAM role that allows Amazon SNS to record AWS Firewall Manager activity.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-notificationchannel.html#cfn-fms-notificationchannel-snsrolename
        '''
        result = self._values.get("sns_role_name")
        assert result is not None, "Required property 'sns_role_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sns_topic_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the SNS topic that collects notifications from AWS Firewall Manager .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-notificationchannel.html#cfn-fms-notificationchannel-snstopicarn
        '''
        result = self._values.get("sns_topic_arn")
        assert result is not None, "Required property 'sns_topic_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnNotificationChannelProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnPolicy(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_fms.CfnPolicy",
):
    '''A CloudFormation ``AWS::FMS::Policy``.

    An AWS Firewall Manager policy.

    Firewall Manager provides the following types of policies:

    - An AWS Shield Advanced policy, which applies Shield Advanced protection to specified accounts and resources.
    - An AWS WAF policy (type WAFV2), which defines rule groups to run first in the corresponding AWS WAF web ACL and rule groups to run last in the web ACL.
    - An AWS WAF Classic policy, which defines a rule group. AWS WAF Classic doesn't support rule groups in Amazon CloudFront , so, to create AWS WAF Classic policies through CloudFront , you first need to create your rule groups outside of CloudFront .
    - A security group policy, which manages VPC security groups across your AWS organization.
    - An AWS Network Firewall policy, which provides firewall rules to filter network traffic in specified Amazon VPCs.
    - A DNS Firewall policy, which provides Amazon Route 53 Resolver DNS Firewall rules to filter DNS queries for specified Amazon VPCs.

    Each policy is specific to one of the types. If you want to enforce more than one policy type across accounts, create multiple policies. You can create multiple policies for each type.

    These policies require some setup to use. For more information, see the sections on prerequisites and getting started under `AWS Firewall Manager <https://docs.aws.amazon.com/waf/latest/developerguide/fms-prereq.html>`_ .

    :cloudformationResource: AWS::FMS::Policy
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_fms as fms
        
        cfn_policy = fms.CfnPolicy(self, "MyCfnPolicy",
            exclude_resource_tags=False,
            policy_name="policyName",
            remediation_enabled=False,
            resource_type="resourceType",
            security_service_policy_data=fms.CfnPolicy.SecurityServicePolicyDataProperty(
                type="type",
        
                # the properties below are optional
                managed_service_data="managedServiceData",
                policy_option=fms.CfnPolicy.PolicyOptionProperty(
                    network_firewall_policy=fms.CfnPolicy.NetworkFirewallPolicyProperty(
                        firewall_deployment_model="firewallDeploymentModel"
                    ),
                    third_party_firewall_policy=fms.CfnPolicy.ThirdPartyFirewallPolicyProperty(
                        firewall_deployment_model="firewallDeploymentModel"
                    )
                )
            ),
        
            # the properties below are optional
            delete_all_policy_resources=False,
            exclude_map={
                "account": ["account"],
                "orgunit": ["orgunit"]
            },
            include_map={
                "account": ["account"],
                "orgunit": ["orgunit"]
            },
            resources_clean_up=False,
            resource_tags=[fms.CfnPolicy.ResourceTagProperty(
                key="key",
        
                # the properties below are optional
                value="value"
            )],
            resource_type_list=["resourceTypeList"],
            tags=[fms.CfnPolicy.PolicyTagProperty(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        exclude_resource_tags: typing.Union[builtins.bool, _IResolvable_da3f097b],
        policy_name: builtins.str,
        remediation_enabled: typing.Union[builtins.bool, _IResolvable_da3f097b],
        resource_type: builtins.str,
        security_service_policy_data: typing.Union[typing.Union["CfnPolicy.SecurityServicePolicyDataProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b],
        delete_all_policy_resources: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        exclude_map: typing.Optional[typing.Union[typing.Union["CfnPolicy.IEMapProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
        include_map: typing.Optional[typing.Union[typing.Union["CfnPolicy.IEMapProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
        resources_clean_up: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        resource_tags: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union["CfnPolicy.ResourceTagProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]]]] = None,
        resource_type_list: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["CfnPolicy.PolicyTagProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::FMS::Policy``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param exclude_resource_tags: Used only when tags are specified in the ``ResourceTags`` property. If this property is ``True`` , resources with the specified tags are not in scope of the policy. If it's ``False`` , only resources with the specified tags are in scope of the policy.
        :param policy_name: The name of the AWS Firewall Manager policy.
        :param remediation_enabled: Indicates if the policy should be automatically applied to new resources.
        :param resource_type: The type of resource protected by or in scope of the policy. This is in the format shown in the `AWS Resource Types Reference <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html>`_ . To apply this policy to multiple resource types, specify a resource type of ``ResourceTypeList`` and then specify the resource types in a ``ResourceTypeList`` . For AWS WAF and Shield Advanced, example resource types include ``AWS::ElasticLoadBalancingV2::LoadBalancer`` and ``AWS::CloudFront::Distribution`` . For a security group common policy, valid values are ``AWS::EC2::NetworkInterface`` and ``AWS::EC2::Instance`` . For a security group content audit policy, valid values are ``AWS::EC2::SecurityGroup`` , ``AWS::EC2::NetworkInterface`` , and ``AWS::EC2::Instance`` . For a security group usage audit policy, the value is ``AWS::EC2::SecurityGroup`` . For an AWS Network Firewall policy or DNS Firewall policy, the value is ``AWS::EC2::VPC`` .
        :param security_service_policy_data: Details about the security service that is being used to protect the resources. This contains the following settings: - Type - Indicates the service type that the policy uses to protect the resource. For security group policies, Firewall Manager supports one security group for each common policy and for each content audit policy. This is an adjustable limit that you can increase by contacting AWS Support . Valid values: ``DNS_FIREWALL`` | ``NETWORK_FIREWALL`` | ``SECURITY_GROUPS_COMMON`` | ``SECURITY_GROUPS_CONTENT_AUDIT`` | ``SECURITY_GROUPS_USAGE_AUDIT`` | ``SHIELD_ADVANCED`` | ``WAFV2`` | ``WAF`` - ManagedServiceData - Details about the service that are specific to the service type, in JSON format. - Example: ``DNS_FIREWALL`` ``"ManagedServiceData": "{ \\"type\\": \\"DNS_FIREWALL\\", \\"preProcessRuleGroups\\": [{\\"ruleGroupId\\": \\"rslvr-frg-123456\\", \\"priority\\": 11}], \\"postProcessRuleGroups\\": [{\\"ruleGroupId\\": \\"rslvr-frg-123456\\", \\"priority\\": 9902}]}"`` - Example: ``NETWORK_FIREWALL`` ``"ManagedServiceData":"{\\"type\\":\\"NETWORK_FIREWALL\\",\\"networkFirewallStatelessRuleGroupReferences\\":[{\\"resourceARN\\":\\"arn:aws:network-firewall:us-east-1:000000000000:stateless-rulegroup\\/example\\",\\"priority\\":1}],\\"networkFirewallStatelessDefaultActions\\":[\\"aws:drop\\",\\"example\\"],\\"networkFirewallStatelessFragmentDefaultActions\\":[\\"aws:drop\\",\\"example\\"],\\"networkFirewallStatelessCustomActions\\":[{\\"actionName\\":\\"example\\",\\"actionDefinition\\":{\\"publishMetricAction\\":{\\"dimensions\\":[{\\"value\\":\\"example\\"}]}}}],\\"networkFirewallStatefulRuleGroupReferences\\":[{\\"resourceARN\\":\\"arn:aws:network-firewall:us-east-1:000000000000:stateful-rulegroup\\/example\\"}],\\"networkFirewallOrchestrationConfig\\":{\\"singleFirewallEndpointPerVPC\\":false,\\"allowedIPV4CidrList\\":[]}}"`` - Example: ``SECURITY_GROUPS_COMMON`` ``"SecurityServicePolicyData":{"Type":"SECURITY_GROUPS_COMMON","ManagedServiceData":"{\\"type\\":\\"SECURITY_GROUPS_COMMON\\",\\"revertManualSecurityGroupChanges\\":false,\\"exclusiveResourceSecurityGroupManagement\\":false,\\"securityGroups\\":[{\\"id\\":\\" sg-000e55995d61a06bd\\"}]}"},"RemediationEnabled":false,"ResourceType":"AWS::EC2::NetworkInterface"}`` - Example: ``SECURITY_GROUPS_CONTENT_AUDIT`` ``"SecurityServicePolicyData":{"Type":"SECURITY_GROUPS_CONTENT_AUDIT","ManagedServiceData":"{\\"type\\":\\"SECURITY_GROUPS_CONTENT_AUDIT\\",\\"securityGroups\\":[{\\"id\\":\\" sg-000e55995d61a06bd \\"}],\\"securityGroupAction\\":{\\"type\\":\\"ALLOW\\"}}"},"RemediationEnabled":false,"ResourceType":"AWS::EC2::NetworkInterface"}`` The security group action for content audit can be ``ALLOW`` or ``DENY`` . For ``ALLOW`` , all in-scope security group rules must be within the allowed range of the policy's security group rules. For ``DENY`` , all in-scope security group rules must not contain a value or a range that matches a rule value or range in the policy security group. - Example: ``SECURITY_GROUPS_USAGE_AUDIT`` ``"SecurityServicePolicyData":{"Type":"SECURITY_GROUPS_USAGE_AUDIT","ManagedServiceData":"{\\"type\\":\\"SECURITY_GROUPS_USAGE_AUDIT\\",\\"deleteUnusedSecurityGroups\\":true,\\"coalesceRedundantSecurityGroups\\":true}"},"RemediationEnabled":false,"Resou rceType":"AWS::EC2::SecurityGroup"}`` - Specification for ``SHIELD_ADVANCED`` for Amazon CloudFront distributions ``"ManagedServiceData": "{\\"type\\": \\"SHIELD_ADVANCED\\", \\"automaticResponseConfiguration\\": {\\"automaticResponseStatus\\":\\"ENABLED|IGNORED|DISABLED\\", \\"automaticResponseAction\\":\\"BLOCK|COUNT\\"}, \\"overrideCustomerWebaclClassic\\":true|false}"`` For example: ``"ManagedServiceData": "{\\"type\\":\\"SHIELD_ADVANCED\\",\\"automaticResponseConfiguration\\": {\\"automaticResponseStatus\\":\\"ENABLED\\", \\"automaticResponseAction\\":\\"COUNT\\"}}"`` The default value for ``automaticResponseStatus`` is ``IGNORED`` . The value for ``automaticResponseAction`` is only required when ``automaticResponseStatus`` is set to ``ENABLED`` . The default value for ``overrideCustomerWebaclClassic`` is ``false`` . For other resource types that you can protect with a Shield Advanced policy, this ``ManagedServiceData`` configuration is an empty string. - Example: ``WAFV2`` ``"ManagedServiceData": "{\\"type\\":\\"WAFV2\\",\\"preProcessRuleGroups\\":[{\\"ruleGroupArn\\":null,\\"overrideAction\\":{\\"type\\":\\"NONE\\"},\\"managedRuleGroupIdentifier\\":{\\"version\\":null,\\"vendorName\\":\\"AWS\\",\\"managedRuleGroupName\\":\\"AWSManagedRulesAmazonIpReputationList\\"},\\"ruleGroupType\\":\\"ManagedRuleGroup\\",\\"excludeRules\\":[]}],\\"postProcessRuleGroups\\":[],\\"defaultAction\\":{\\"type\\":\\"ALLOW\\"},\\"overrideCustomerWebACLAssociation\\":false,\\"loggingConfiguration\\":{\\"logDestinationConfigs\\":[\\"arn:aws:firehose:us-west-2:12345678912:deliverystream/aws-waf-logs-fms-admin-destination\\"],\\"redactedFields\\":[{\\"redactedFieldType\\":\\"SingleHeader\\",\\"redactedFieldValue\\":\\"Cookies\\"},{\\"redactedFieldType\\":\\"Method\\"}]}}"`` In the ``loggingConfiguration`` , you can specify one ``logDestinationConfigs`` , you can optionally provide up to 20 ``redactedFields`` , and the ``RedactedFieldType`` must be one of ``URI`` , ``QUERY_STRING`` , ``HEADER`` , or ``METHOD`` . - Example: ``WAF Classic`` ``"ManagedServiceData": "{\\"type\\": \\"WAF\\", \\"ruleGroups\\": [{\\"id\\":\\"12345678-1bcd-9012-efga-0987654321ab\\", \\"overrideAction\\" : {\\"type\\": \\"COUNT\\"}}],\\"defaultAction\\": {\\"type\\": \\"BLOCK\\"}}`` AWS WAF Classic doesn't support rule groups in CloudFront . To create a WAF Classic policy through CloudFormation, create your rule groups outside of CloudFront , then provide the rule group IDs in the WAF managed service data specification.
        :param delete_all_policy_resources: Used when deleting a policy. If ``true`` , Firewall Manager performs cleanup according to the policy type. For AWS WAF and Shield Advanced policies, Firewall Manager does the following: - Deletes rule groups created by Firewall Manager - Removes web ACLs from in-scope resources - Deletes web ACLs that contain no rules or rule groups For security group policies, Firewall Manager does the following for each security group in the policy: - Disassociates the security group from in-scope resources - Deletes the security group if it was created through Firewall Manager and if it's no longer associated with any resources through another policy After the cleanup, in-scope resources are no longer protected by web ACLs in this policy. Protection of out-of-scope resources remains unchanged. Scope is determined by tags that you create and accounts that you associate with the policy. When creating the policy, if you specify that only resources in specific accounts or with specific tags are in scope of the policy, those accounts and resources are handled by the policy. All others are out of scope. If you don't specify tags or accounts, all resources are in scope.
        :param exclude_map: Specifies the AWS account IDs and AWS Organizations organizational units (OUs) to exclude from the policy. Specifying an OU is the equivalent of specifying all accounts in the OU and in any of its child OUs, including any child OUs and accounts that are added at a later time. You can specify inclusions or exclusions, but not both. If you specify an ``IncludeMap`` , AWS Firewall Manager applies the policy to all accounts specified by the ``IncludeMap`` , and does not evaluate any ``ExcludeMap`` specifications. If you do not specify an ``IncludeMap`` , then Firewall Manager applies the policy to all accounts except for those specified by the ``ExcludeMap`` . You can specify account IDs, OUs, or a combination: - Specify account IDs by setting the key to ``ACCOUNT`` . For example, the following is a valid map: ``{“ACCOUNT” : [“accountID1”, “accountID2”]}`` . - Specify OUs by setting the key to ``ORGUNIT`` . For example, the following is a valid map: ``{“ORGUNIT” : [“ouid111”, “ouid112”]}`` . - Specify accounts and OUs together in a single map, separated with a comma. For example, the following is a valid map: ``{“ACCOUNT” : [“accountID1”, “accountID2”], “ORGUNIT” : [“ouid111”, “ouid112”]}`` .
        :param include_map: Specifies the AWS account IDs and AWS Organizations organizational units (OUs) to include in the policy. Specifying an OU is the equivalent of specifying all accounts in the OU and in any of its child OUs, including any child OUs and accounts that are added at a later time. You can specify inclusions or exclusions, but not both. If you specify an ``IncludeMap`` , AWS Firewall Manager applies the policy to all accounts specified by the ``IncludeMap`` , and does not evaluate any ``ExcludeMap`` specifications. If you do not specify an ``IncludeMap`` , then Firewall Manager applies the policy to all accounts except for those specified by the ``ExcludeMap`` . You can specify account IDs, OUs, or a combination: - Specify account IDs by setting the key to ``ACCOUNT`` . For example, the following is a valid map: ``{“ACCOUNT” : [“accountID1”, “accountID2”]}`` . - Specify OUs by setting the key to ``ORGUNIT`` . For example, the following is a valid map: ``{“ORGUNIT” : [“ouid111”, “ouid112”]}`` . - Specify accounts and OUs together in a single map, separated with a comma. For example, the following is a valid map: ``{“ACCOUNT” : [“accountID1”, “accountID2”], “ORGUNIT” : [“ouid111”, “ouid112”]}`` .
        :param resources_clean_up: Indicates whether AWS Firewall Manager should automatically remove protections from resources that leave the policy scope and clean up resources that Firewall Manager is managing for accounts when those accounts leave policy scope. For example, Firewall Manager will disassociate a Firewall Manager managed web ACL from a protected customer resource when the customer resource leaves policy scope. By default, Firewall Manager doesn't remove protections or delete Firewall Manager managed resources. This option is not available for Shield Advanced or AWS WAF Classic policies.
        :param resource_tags: An array of ``ResourceTag`` objects, used to explicitly include resources in the policy scope or explicitly exclude them. If this isn't set, then tags aren't used to modify policy scope. See also ``ExcludeResourceTags`` .
        :param resource_type_list: An array of ``ResourceType`` objects. Use this only to specify multiple resource types. To specify a single resource type, use ``ResourceType`` .
        :param tags: A collection of key:value pairs associated with an AWS resource. The key:value pair can be anything you define. Typically, the tag key represents a category (such as "environment") and the tag value represents a specific value within that category (such as "test," "development," or "production"). You can add up to 50 tags to each AWS resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a29b3b13041b0ccbd18a0c29ff5cff0adbc0e2aedc87591f1c54ec7a1fc830b4)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnPolicyProps(
            exclude_resource_tags=exclude_resource_tags,
            policy_name=policy_name,
            remediation_enabled=remediation_enabled,
            resource_type=resource_type,
            security_service_policy_data=security_service_policy_data,
            delete_all_policy_resources=delete_all_policy_resources,
            exclude_map=exclude_map,
            include_map=include_map,
            resources_clean_up=resources_clean_up,
            resource_tags=resource_tags,
            resource_type_list=resource_type_list,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4bd3d819ff879695091ea1782c6d44919a2d5d60ac904eb958a4baa5a9b7b105)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b5336d629941f59b9bc57ae2f0f9086302ff307956a981d17c0c74f56e281a98)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the policy.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The ID of the policy.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="excludeResourceTags")
    def exclude_resource_tags(
        self,
    ) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
        '''Used only when tags are specified in the ``ResourceTags`` property.

        If this property is ``True`` , resources with the specified tags are not in scope of the policy. If it's ``False`` , only resources with the specified tags are in scope of the policy.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-excluderesourcetags
        '''
        return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], jsii.get(self, "excludeResourceTags"))

    @exclude_resource_tags.setter
    def exclude_resource_tags(
        self,
        value: typing.Union[builtins.bool, _IResolvable_da3f097b],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__20a6c43cec956bc22ae07e19e1af4001c23e93faad6ca1043a917bf0f5dcfc1d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "excludeResourceTags", value)

    @builtins.property
    @jsii.member(jsii_name="policyName")
    def policy_name(self) -> builtins.str:
        '''The name of the AWS Firewall Manager policy.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-policyname
        '''
        return typing.cast(builtins.str, jsii.get(self, "policyName"))

    @policy_name.setter
    def policy_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__62ed5a312383f144ece33d5d7f925fd2a4d83062b6024f0b02b573273b2f360d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policyName", value)

    @builtins.property
    @jsii.member(jsii_name="remediationEnabled")
    def remediation_enabled(self) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
        '''Indicates if the policy should be automatically applied to new resources.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-remediationenabled
        '''
        return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], jsii.get(self, "remediationEnabled"))

    @remediation_enabled.setter
    def remediation_enabled(
        self,
        value: typing.Union[builtins.bool, _IResolvable_da3f097b],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ce24f414c17fee1c6464201d3595af0f5eddf30ec4dc5532e27f42a5a60bfba0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "remediationEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="resourceType")
    def resource_type(self) -> builtins.str:
        '''The type of resource protected by or in scope of the policy.

        This is in the format shown in the `AWS Resource Types Reference <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html>`_ . To apply this policy to multiple resource types, specify a resource type of ``ResourceTypeList`` and then specify the resource types in a ``ResourceTypeList`` .

        For AWS WAF and Shield Advanced, example resource types include ``AWS::ElasticLoadBalancingV2::LoadBalancer`` and ``AWS::CloudFront::Distribution`` . For a security group common policy, valid values are ``AWS::EC2::NetworkInterface`` and ``AWS::EC2::Instance`` . For a security group content audit policy, valid values are ``AWS::EC2::SecurityGroup`` , ``AWS::EC2::NetworkInterface`` , and ``AWS::EC2::Instance`` . For a security group usage audit policy, the value is ``AWS::EC2::SecurityGroup`` . For an AWS Network Firewall policy or DNS Firewall policy, the value is ``AWS::EC2::VPC`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-resourcetype
        '''
        return typing.cast(builtins.str, jsii.get(self, "resourceType"))

    @resource_type.setter
    def resource_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__45fbd20db788e5f26784bca772c0c150d7f583f3b21916156a9f85bdbbbd064d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceType", value)

    @builtins.property
    @jsii.member(jsii_name="securityServicePolicyData")
    def security_service_policy_data(
        self,
    ) -> typing.Union["CfnPolicy.SecurityServicePolicyDataProperty", _IResolvable_da3f097b]:
        '''Details about the security service that is being used to protect the resources.

        This contains the following settings:

        - Type - Indicates the service type that the policy uses to protect the resource. For security group policies, Firewall Manager supports one security group for each common policy and for each content audit policy. This is an adjustable limit that you can increase by contacting AWS Support .

        Valid values: ``DNS_FIREWALL`` | ``NETWORK_FIREWALL`` | ``SECURITY_GROUPS_COMMON`` | ``SECURITY_GROUPS_CONTENT_AUDIT`` | ``SECURITY_GROUPS_USAGE_AUDIT`` | ``SHIELD_ADVANCED`` | ``WAFV2`` | ``WAF``

        - ManagedServiceData - Details about the service that are specific to the service type, in JSON format.
        - Example: ``DNS_FIREWALL``

        ``"ManagedServiceData": "{ \\"type\\": \\"DNS_FIREWALL\\", \\"preProcessRuleGroups\\": [{\\"ruleGroupId\\": \\"rslvr-frg-123456\\", \\"priority\\": 11}], \\"postProcessRuleGroups\\": [{\\"ruleGroupId\\": \\"rslvr-frg-123456\\", \\"priority\\": 9902}]}"``

        - Example: ``NETWORK_FIREWALL``

        ``"ManagedServiceData":"{\\"type\\":\\"NETWORK_FIREWALL\\",\\"networkFirewallStatelessRuleGroupReferences\\":[{\\"resourceARN\\":\\"arn:aws:network-firewall:us-east-1:000000000000:stateless-rulegroup\\/example\\",\\"priority\\":1}],\\"networkFirewallStatelessDefaultActions\\":[\\"aws:drop\\",\\"example\\"],\\"networkFirewallStatelessFragmentDefaultActions\\":[\\"aws:drop\\",\\"example\\"],\\"networkFirewallStatelessCustomActions\\":[{\\"actionName\\":\\"example\\",\\"actionDefinition\\":{\\"publishMetricAction\\":{\\"dimensions\\":[{\\"value\\":\\"example\\"}]}}}],\\"networkFirewallStatefulRuleGroupReferences\\":[{\\"resourceARN\\":\\"arn:aws:network-firewall:us-east-1:000000000000:stateful-rulegroup\\/example\\"}],\\"networkFirewallOrchestrationConfig\\":{\\"singleFirewallEndpointPerVPC\\":false,\\"allowedIPV4CidrList\\":[]}}"``

        - Example: ``SECURITY_GROUPS_COMMON``

        ``"SecurityServicePolicyData":{"Type":"SECURITY_GROUPS_COMMON","ManagedServiceData":"{\\"type\\":\\"SECURITY_GROUPS_COMMON\\",\\"revertManualSecurityGroupChanges\\":false,\\"exclusiveResourceSecurityGroupManagement\\":false,\\"securityGroups\\":[{\\"id\\":\\" sg-000e55995d61a06bd\\"}]}"},"RemediationEnabled":false,"ResourceType":"AWS::EC2::NetworkInterface"}``

        - Example: ``SECURITY_GROUPS_CONTENT_AUDIT``

        ``"SecurityServicePolicyData":{"Type":"SECURITY_GROUPS_CONTENT_AUDIT","ManagedServiceData":"{\\"type\\":\\"SECURITY_GROUPS_CONTENT_AUDIT\\",\\"securityGroups\\":[{\\"id\\":\\" sg-000e55995d61a06bd \\"}],\\"securityGroupAction\\":{\\"type\\":\\"ALLOW\\"}}"},"RemediationEnabled":false,"ResourceType":"AWS::EC2::NetworkInterface"}``

        The security group action for content audit can be ``ALLOW`` or ``DENY`` . For ``ALLOW`` , all in-scope security group rules must be within the allowed range of the policy's security group rules. For ``DENY`` , all in-scope security group rules must not contain a value or a range that matches a rule value or range in the policy security group.

        - Example: ``SECURITY_GROUPS_USAGE_AUDIT``

        ``"SecurityServicePolicyData":{"Type":"SECURITY_GROUPS_USAGE_AUDIT","ManagedServiceData":"{\\"type\\":\\"SECURITY_GROUPS_USAGE_AUDIT\\",\\"deleteUnusedSecurityGroups\\":true,\\"coalesceRedundantSecurityGroups\\":true}"},"RemediationEnabled":false,"Resou rceType":"AWS::EC2::SecurityGroup"}``

        - Specification for ``SHIELD_ADVANCED`` for Amazon CloudFront distributions

        ``"ManagedServiceData": "{\\"type\\": \\"SHIELD_ADVANCED\\", \\"automaticResponseConfiguration\\": {\\"automaticResponseStatus\\":\\"ENABLED|IGNORED|DISABLED\\", \\"automaticResponseAction\\":\\"BLOCK|COUNT\\"}, \\"overrideCustomerWebaclClassic\\":true|false}"``

        For example: ``"ManagedServiceData": "{\\"type\\":\\"SHIELD_ADVANCED\\",\\"automaticResponseConfiguration\\": {\\"automaticResponseStatus\\":\\"ENABLED\\", \\"automaticResponseAction\\":\\"COUNT\\"}}"``

        The default value for ``automaticResponseStatus`` is ``IGNORED`` . The value for ``automaticResponseAction`` is only required when ``automaticResponseStatus`` is set to ``ENABLED`` . The default value for ``overrideCustomerWebaclClassic`` is ``false`` .

        For other resource types that you can protect with a Shield Advanced policy, this ``ManagedServiceData`` configuration is an empty string.

        - Example: ``WAFV2``

        ``"ManagedServiceData": "{\\"type\\":\\"WAFV2\\",\\"preProcessRuleGroups\\":[{\\"ruleGroupArn\\":null,\\"overrideAction\\":{\\"type\\":\\"NONE\\"},\\"managedRuleGroupIdentifier\\":{\\"version\\":null,\\"vendorName\\":\\"AWS\\",\\"managedRuleGroupName\\":\\"AWSManagedRulesAmazonIpReputationList\\"},\\"ruleGroupType\\":\\"ManagedRuleGroup\\",\\"excludeRules\\":[]}],\\"postProcessRuleGroups\\":[],\\"defaultAction\\":{\\"type\\":\\"ALLOW\\"},\\"overrideCustomerWebACLAssociation\\":false,\\"loggingConfiguration\\":{\\"logDestinationConfigs\\":[\\"arn:aws:firehose:us-west-2:12345678912:deliverystream/aws-waf-logs-fms-admin-destination\\"],\\"redactedFields\\":[{\\"redactedFieldType\\":\\"SingleHeader\\",\\"redactedFieldValue\\":\\"Cookies\\"},{\\"redactedFieldType\\":\\"Method\\"}]}}"``

        In the ``loggingConfiguration`` , you can specify one ``logDestinationConfigs`` , you can optionally provide up to 20 ``redactedFields`` , and the ``RedactedFieldType`` must be one of ``URI`` , ``QUERY_STRING`` , ``HEADER`` , or ``METHOD`` .

        - Example: ``WAF Classic``

        ``"ManagedServiceData": "{\\"type\\": \\"WAF\\", \\"ruleGroups\\": [{\\"id\\":\\"12345678-1bcd-9012-efga-0987654321ab\\", \\"overrideAction\\" : {\\"type\\": \\"COUNT\\"}}],\\"defaultAction\\": {\\"type\\": \\"BLOCK\\"}}``

        AWS WAF Classic doesn't support rule groups in CloudFront . To create a WAF Classic policy through CloudFormation, create your rule groups outside of CloudFront , then provide the rule group IDs in the WAF managed service data specification.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-securityservicepolicydata
        '''
        return typing.cast(typing.Union["CfnPolicy.SecurityServicePolicyDataProperty", _IResolvable_da3f097b], jsii.get(self, "securityServicePolicyData"))

    @security_service_policy_data.setter
    def security_service_policy_data(
        self,
        value: typing.Union["CfnPolicy.SecurityServicePolicyDataProperty", _IResolvable_da3f097b],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c28ba46bb386f4176af9e17ecbe45582b554c7807d38f2929fb3fd7a81f3976)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityServicePolicyData", value)

    @builtins.property
    @jsii.member(jsii_name="deleteAllPolicyResources")
    def delete_all_policy_resources(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Used when deleting a policy. If ``true`` , Firewall Manager performs cleanup according to the policy type.

        For AWS WAF and Shield Advanced policies, Firewall Manager does the following:

        - Deletes rule groups created by Firewall Manager
        - Removes web ACLs from in-scope resources
        - Deletes web ACLs that contain no rules or rule groups

        For security group policies, Firewall Manager does the following for each security group in the policy:

        - Disassociates the security group from in-scope resources
        - Deletes the security group if it was created through Firewall Manager and if it's no longer associated with any resources through another policy

        After the cleanup, in-scope resources are no longer protected by web ACLs in this policy. Protection of out-of-scope resources remains unchanged. Scope is determined by tags that you create and accounts that you associate with the policy. When creating the policy, if you specify that only resources in specific accounts or with specific tags are in scope of the policy, those accounts and resources are handled by the policy. All others are out of scope. If you don't specify tags or accounts, all resources are in scope.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-deleteallpolicyresources
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "deleteAllPolicyResources"))

    @delete_all_policy_resources.setter
    def delete_all_policy_resources(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9fe798b33151903c0017cb9d94013617a6afcad058e7ae0fe54c9cfd6dd679c2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deleteAllPolicyResources", value)

    @builtins.property
    @jsii.member(jsii_name="excludeMap")
    def exclude_map(
        self,
    ) -> typing.Optional[typing.Union["CfnPolicy.IEMapProperty", _IResolvable_da3f097b]]:
        '''Specifies the AWS account IDs and AWS Organizations organizational units (OUs) to exclude from the policy.

        Specifying an OU is the equivalent of specifying all accounts in the OU and in any of its child OUs, including any child OUs and accounts that are added at a later time.

        You can specify inclusions or exclusions, but not both. If you specify an ``IncludeMap`` , AWS Firewall Manager applies the policy to all accounts specified by the ``IncludeMap`` , and does not evaluate any ``ExcludeMap`` specifications. If you do not specify an ``IncludeMap`` , then Firewall Manager applies the policy to all accounts except for those specified by the ``ExcludeMap`` .

        You can specify account IDs, OUs, or a combination:

        - Specify account IDs by setting the key to ``ACCOUNT`` . For example, the following is a valid map: ``{“ACCOUNT” : [“accountID1”, “accountID2”]}`` .
        - Specify OUs by setting the key to ``ORGUNIT`` . For example, the following is a valid map: ``{“ORGUNIT” : [“ouid111”, “ouid112”]}`` .
        - Specify accounts and OUs together in a single map, separated with a comma. For example, the following is a valid map: ``{“ACCOUNT” : [“accountID1”, “accountID2”], “ORGUNIT” : [“ouid111”, “ouid112”]}`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-excludemap
        '''
        return typing.cast(typing.Optional[typing.Union["CfnPolicy.IEMapProperty", _IResolvable_da3f097b]], jsii.get(self, "excludeMap"))

    @exclude_map.setter
    def exclude_map(
        self,
        value: typing.Optional[typing.Union["CfnPolicy.IEMapProperty", _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b8f8c8d7be71d632f5fd707992c674dd52c74761a09f147830413fcfba30c273)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "excludeMap", value)

    @builtins.property
    @jsii.member(jsii_name="includeMap")
    def include_map(
        self,
    ) -> typing.Optional[typing.Union["CfnPolicy.IEMapProperty", _IResolvable_da3f097b]]:
        '''Specifies the AWS account IDs and AWS Organizations organizational units (OUs) to include in the policy.

        Specifying an OU is the equivalent of specifying all accounts in the OU and in any of its child OUs, including any child OUs and accounts that are added at a later time.

        You can specify inclusions or exclusions, but not both. If you specify an ``IncludeMap`` , AWS Firewall Manager applies the policy to all accounts specified by the ``IncludeMap`` , and does not evaluate any ``ExcludeMap`` specifications. If you do not specify an ``IncludeMap`` , then Firewall Manager applies the policy to all accounts except for those specified by the ``ExcludeMap`` .

        You can specify account IDs, OUs, or a combination:

        - Specify account IDs by setting the key to ``ACCOUNT`` . For example, the following is a valid map: ``{“ACCOUNT” : [“accountID1”, “accountID2”]}`` .
        - Specify OUs by setting the key to ``ORGUNIT`` . For example, the following is a valid map: ``{“ORGUNIT” : [“ouid111”, “ouid112”]}`` .
        - Specify accounts and OUs together in a single map, separated with a comma. For example, the following is a valid map: ``{“ACCOUNT” : [“accountID1”, “accountID2”], “ORGUNIT” : [“ouid111”, “ouid112”]}`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-includemap
        '''
        return typing.cast(typing.Optional[typing.Union["CfnPolicy.IEMapProperty", _IResolvable_da3f097b]], jsii.get(self, "includeMap"))

    @include_map.setter
    def include_map(
        self,
        value: typing.Optional[typing.Union["CfnPolicy.IEMapProperty", _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__94290c92cb339b7d588eedc5f7e4693403e89224115f954743aa8b94e5920b0f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "includeMap", value)

    @builtins.property
    @jsii.member(jsii_name="resourcesCleanUp")
    def resources_clean_up(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Indicates whether AWS Firewall Manager should automatically remove protections from resources that leave the policy scope and clean up resources that Firewall Manager is managing for accounts when those accounts leave policy scope.

        For example, Firewall Manager will disassociate a Firewall Manager managed web ACL from a protected customer resource when the customer resource leaves policy scope.

        By default, Firewall Manager doesn't remove protections or delete Firewall Manager managed resources.

        This option is not available for Shield Advanced or AWS WAF Classic policies.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-resourcescleanup
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "resourcesCleanUp"))

    @resources_clean_up.setter
    def resources_clean_up(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__12534b322db922dabec65a01e84b63ba7b3a489d9d25d5870fef80727d31a5c3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourcesCleanUp", value)

    @builtins.property
    @jsii.member(jsii_name="resourceTags")
    def resource_tags(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnPolicy.ResourceTagProperty", _IResolvable_da3f097b]]]]:
        '''An array of ``ResourceTag`` objects, used to explicitly include resources in the policy scope or explicitly exclude them.

        If this isn't set, then tags aren't used to modify policy scope. See also ``ExcludeResourceTags`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-resourcetags
        '''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnPolicy.ResourceTagProperty", _IResolvable_da3f097b]]]], jsii.get(self, "resourceTags"))

    @resource_tags.setter
    def resource_tags(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnPolicy.ResourceTagProperty", _IResolvable_da3f097b]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c77d40603d6f4c051dd3f9b5d662e1b2f8b3690fcfa612876de86b1cfb05ac0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceTags", value)

    @builtins.property
    @jsii.member(jsii_name="resourceTypeList")
    def resource_type_list(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An array of ``ResourceType`` objects.

        Use this only to specify multiple resource types. To specify a single resource type, use ``ResourceType`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-resourcetypelist
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "resourceTypeList"))

    @resource_type_list.setter
    def resource_type_list(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__defb2e92d0f62de49ea900ef5497c0bb92b81e991fe094bca77e0bc3225a174e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceTypeList", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["CfnPolicy.PolicyTagProperty"]]:
        '''A collection of key:value pairs associated with an AWS resource.

        The key:value pair can be anything you define. Typically, the tag key represents a category (such as "environment") and the tag value represents a specific value within that category (such as "test," "development," or "production"). You can add up to 50 tags to each AWS resource.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-tags
        '''
        return typing.cast(typing.Optional[typing.List["CfnPolicy.PolicyTagProperty"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.List["CfnPolicy.PolicyTagProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e61b60deb504fb101d8b3c5d4d91824672d7a44fdd9537dec8f729c7d34256be)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_fms.CfnPolicy.IEMapProperty",
        jsii_struct_bases=[],
        name_mapping={"account": "account", "orgunit": "orgunit"},
    )
    class IEMapProperty:
        def __init__(
            self,
            *,
            account: typing.Optional[typing.Sequence[builtins.str]] = None,
            orgunit: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''Specifies the AWS account IDs and AWS Organizations organizational units (OUs) to include in or exclude from the policy.

            Specifying an OU is the equivalent of specifying all accounts in the OU and in any of its child OUs, including any child OUs and accounts that are added at a later time.

            This is used for the policy's ``IncludeMap`` and ``ExcludeMap`` .

            You can specify account IDs, OUs, or a combination:

            - Specify account IDs by setting the key to ``ACCOUNT`` . For example, the following is a valid map: ``{“ACCOUNT” : [“accountID1”, “accountID2”]}`` .
            - Specify OUs by setting the key to ``ORGUNIT`` . For example, the following is a valid map: ``{“ORGUNIT” : [“ouid111”, “ouid112”]}`` .
            - Specify accounts and OUs together in a single map, separated with a comma. For example, the following is a valid map: ``{“ACCOUNT” : [“accountID1”, “accountID2”], “ORGUNIT” : [“ouid111”, “ouid112”]}`` .

            :param account: The account list for the map.
            :param orgunit: The organizational unit list for the map.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-iemap.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_fms as fms
                
                i_eMap_property = {
                    "account": ["account"],
                    "orgunit": ["orgunit"]
                }
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6bcb551e43b08ef4828de279b99e59a3954c4cdc19c8adfe6bf93e810ce36917)
                check_type(argname="argument account", value=account, expected_type=type_hints["account"])
                check_type(argname="argument orgunit", value=orgunit, expected_type=type_hints["orgunit"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if account is not None:
                self._values["account"] = account
            if orgunit is not None:
                self._values["orgunit"] = orgunit

        @builtins.property
        def account(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The account list for the map.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-iemap.html#cfn-fms-policy-iemap-account
            '''
            result = self._values.get("account")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def orgunit(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The organizational unit list for the map.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-iemap.html#cfn-fms-policy-iemap-orgunit
            '''
            result = self._values.get("orgunit")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IEMapProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_fms.CfnPolicy.NetworkFirewallPolicyProperty",
        jsii_struct_bases=[],
        name_mapping={"firewall_deployment_model": "firewallDeploymentModel"},
    )
    class NetworkFirewallPolicyProperty:
        def __init__(self, *, firewall_deployment_model: builtins.str) -> None:
            '''
            :param firewall_deployment_model: ``CfnPolicy.NetworkFirewallPolicyProperty.FirewallDeploymentModel``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-networkfirewallpolicy.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_fms as fms
                
                network_firewall_policy_property = fms.CfnPolicy.NetworkFirewallPolicyProperty(
                    firewall_deployment_model="firewallDeploymentModel"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1dee79c6872a0421399375d5fc2757431881011031a81ccd6674040de21bac13)
                check_type(argname="argument firewall_deployment_model", value=firewall_deployment_model, expected_type=type_hints["firewall_deployment_model"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "firewall_deployment_model": firewall_deployment_model,
            }

        @builtins.property
        def firewall_deployment_model(self) -> builtins.str:
            '''``CfnPolicy.NetworkFirewallPolicyProperty.FirewallDeploymentModel``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-networkfirewallpolicy.html#cfn-fms-policy-networkfirewallpolicy-firewalldeploymentmodel
            '''
            result = self._values.get("firewall_deployment_model")
            assert result is not None, "Required property 'firewall_deployment_model' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NetworkFirewallPolicyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_fms.CfnPolicy.PolicyOptionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "network_firewall_policy": "networkFirewallPolicy",
            "third_party_firewall_policy": "thirdPartyFirewallPolicy",
        },
    )
    class PolicyOptionProperty:
        def __init__(
            self,
            *,
            network_firewall_policy: typing.Optional[typing.Union[typing.Union["CfnPolicy.NetworkFirewallPolicyProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
            third_party_firewall_policy: typing.Optional[typing.Union[typing.Union["CfnPolicy.ThirdPartyFirewallPolicyProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
        ) -> None:
            '''
            :param network_firewall_policy: ``CfnPolicy.PolicyOptionProperty.NetworkFirewallPolicy``.
            :param third_party_firewall_policy: ``CfnPolicy.PolicyOptionProperty.ThirdPartyFirewallPolicy``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-policyoption.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_fms as fms
                
                policy_option_property = fms.CfnPolicy.PolicyOptionProperty(
                    network_firewall_policy=fms.CfnPolicy.NetworkFirewallPolicyProperty(
                        firewall_deployment_model="firewallDeploymentModel"
                    ),
                    third_party_firewall_policy=fms.CfnPolicy.ThirdPartyFirewallPolicyProperty(
                        firewall_deployment_model="firewallDeploymentModel"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5979520d8e95acd573ee171b00e0dcba3be3872b80af53615d64bc000f703299)
                check_type(argname="argument network_firewall_policy", value=network_firewall_policy, expected_type=type_hints["network_firewall_policy"])
                check_type(argname="argument third_party_firewall_policy", value=third_party_firewall_policy, expected_type=type_hints["third_party_firewall_policy"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if network_firewall_policy is not None:
                self._values["network_firewall_policy"] = network_firewall_policy
            if third_party_firewall_policy is not None:
                self._values["third_party_firewall_policy"] = third_party_firewall_policy

        @builtins.property
        def network_firewall_policy(
            self,
        ) -> typing.Optional[typing.Union["CfnPolicy.NetworkFirewallPolicyProperty", _IResolvable_da3f097b]]:
            '''``CfnPolicy.PolicyOptionProperty.NetworkFirewallPolicy``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-policyoption.html#cfn-fms-policy-policyoption-networkfirewallpolicy
            '''
            result = self._values.get("network_firewall_policy")
            return typing.cast(typing.Optional[typing.Union["CfnPolicy.NetworkFirewallPolicyProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def third_party_firewall_policy(
            self,
        ) -> typing.Optional[typing.Union["CfnPolicy.ThirdPartyFirewallPolicyProperty", _IResolvable_da3f097b]]:
            '''``CfnPolicy.PolicyOptionProperty.ThirdPartyFirewallPolicy``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-policyoption.html#cfn-fms-policy-policyoption-thirdpartyfirewallpolicy
            '''
            result = self._values.get("third_party_firewall_policy")
            return typing.cast(typing.Optional[typing.Union["CfnPolicy.ThirdPartyFirewallPolicyProperty", _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PolicyOptionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_fms.CfnPolicy.PolicyTagProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "value": "value"},
    )
    class PolicyTagProperty:
        def __init__(self, *, key: builtins.str, value: builtins.str) -> None:
            '''A collection of key:value pairs associated with an AWS resource.

            The key:value pair can be anything you define. Typically, the tag key represents a category (such as "environment") and the tag value represents a specific value within that category (such as "test," "development," or "production"). You can add up to 50 tags to each AWS resource.

            :param key: Part of the key:value pair that defines a tag. You can use a tag key to describe a category of information, such as "customer." Tag keys are case-sensitive.
            :param value: Part of the key:value pair that defines a tag. You can use a tag value to describe a specific value within a category, such as "companyA" or "companyB." Tag values are case-sensitive.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-policytag.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_fms as fms
                
                policy_tag_property = fms.CfnPolicy.PolicyTagProperty(
                    key="key",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4d5ee16e00771d59c6939cbdec3cdf3c57cdb9a09a7e914e3faf7baaa7416d62)
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "key": key,
                "value": value,
            }

        @builtins.property
        def key(self) -> builtins.str:
            '''Part of the key:value pair that defines a tag.

            You can use a tag key to describe a category of information, such as "customer." Tag keys are case-sensitive.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-policytag.html#cfn-fms-policy-policytag-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''Part of the key:value pair that defines a tag.

            You can use a tag value to describe a specific value within a category, such as "companyA" or "companyB." Tag values are case-sensitive.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-policytag.html#cfn-fms-policy-policytag-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PolicyTagProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_fms.CfnPolicy.ResourceTagProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "value": "value"},
    )
    class ResourceTagProperty:
        def __init__(
            self,
            *,
            key: builtins.str,
            value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The resource tags that AWS Firewall Manager uses to determine if a particular resource should be included or excluded from the AWS Firewall Manager policy.

            Tags enable you to categorize your AWS resources in different ways, for example, by purpose, owner, or environment. Each tag consists of a key and an optional value. Firewall Manager combines the tags with "AND" so that, if you add more than one tag to a policy scope, a resource must have all the specified tags to be included or excluded. For more information, see `Working with Tag Editor <https://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/tag-editor.html>`_ .

            :param key: The resource tag key.
            :param value: The resource tag value.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-resourcetag.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_fms as fms
                
                resource_tag_property = fms.CfnPolicy.ResourceTagProperty(
                    key="key",
                
                    # the properties below are optional
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1533af324aea7be8b3e806a7d4a851c48bea2139cd3bb0ce1cc81ff86e976487)
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "key": key,
            }
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def key(self) -> builtins.str:
            '''The resource tag key.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-resourcetag.html#cfn-fms-policy-resourcetag-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> typing.Optional[builtins.str]:
            '''The resource tag value.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-resourcetag.html#cfn-fms-policy-resourcetag-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ResourceTagProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_fms.CfnPolicy.SecurityServicePolicyDataProperty",
        jsii_struct_bases=[],
        name_mapping={
            "type": "type",
            "managed_service_data": "managedServiceData",
            "policy_option": "policyOption",
        },
    )
    class SecurityServicePolicyDataProperty:
        def __init__(
            self,
            *,
            type: builtins.str,
            managed_service_data: typing.Optional[builtins.str] = None,
            policy_option: typing.Optional[typing.Union[typing.Union["CfnPolicy.PolicyOptionProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
        ) -> None:
            '''
            :param type: ``CfnPolicy.SecurityServicePolicyDataProperty.Type``.
            :param managed_service_data: ``CfnPolicy.SecurityServicePolicyDataProperty.ManagedServiceData``.
            :param policy_option: ``CfnPolicy.SecurityServicePolicyDataProperty.PolicyOption``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-securityservicepolicydata.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_fms as fms
                
                security_service_policy_data_property = fms.CfnPolicy.SecurityServicePolicyDataProperty(
                    type="type",
                
                    # the properties below are optional
                    managed_service_data="managedServiceData",
                    policy_option=fms.CfnPolicy.PolicyOptionProperty(
                        network_firewall_policy=fms.CfnPolicy.NetworkFirewallPolicyProperty(
                            firewall_deployment_model="firewallDeploymentModel"
                        ),
                        third_party_firewall_policy=fms.CfnPolicy.ThirdPartyFirewallPolicyProperty(
                            firewall_deployment_model="firewallDeploymentModel"
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c049eeb7140522ded2ec5e8c352001a90a84400f6f8d601bcb6b17805b0a150e)
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument managed_service_data", value=managed_service_data, expected_type=type_hints["managed_service_data"])
                check_type(argname="argument policy_option", value=policy_option, expected_type=type_hints["policy_option"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "type": type,
            }
            if managed_service_data is not None:
                self._values["managed_service_data"] = managed_service_data
            if policy_option is not None:
                self._values["policy_option"] = policy_option

        @builtins.property
        def type(self) -> builtins.str:
            '''``CfnPolicy.SecurityServicePolicyDataProperty.Type``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-securityservicepolicydata.html#cfn-fms-policy-securityservicepolicydata-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def managed_service_data(self) -> typing.Optional[builtins.str]:
            '''``CfnPolicy.SecurityServicePolicyDataProperty.ManagedServiceData``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-securityservicepolicydata.html#cfn-fms-policy-securityservicepolicydata-managedservicedata
            '''
            result = self._values.get("managed_service_data")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def policy_option(
            self,
        ) -> typing.Optional[typing.Union["CfnPolicy.PolicyOptionProperty", _IResolvable_da3f097b]]:
            '''``CfnPolicy.SecurityServicePolicyDataProperty.PolicyOption``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-securityservicepolicydata.html#cfn-fms-policy-securityservicepolicydata-policyoption
            '''
            result = self._values.get("policy_option")
            return typing.cast(typing.Optional[typing.Union["CfnPolicy.PolicyOptionProperty", _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SecurityServicePolicyDataProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_fms.CfnPolicy.ThirdPartyFirewallPolicyProperty",
        jsii_struct_bases=[],
        name_mapping={"firewall_deployment_model": "firewallDeploymentModel"},
    )
    class ThirdPartyFirewallPolicyProperty:
        def __init__(self, *, firewall_deployment_model: builtins.str) -> None:
            '''
            :param firewall_deployment_model: ``CfnPolicy.ThirdPartyFirewallPolicyProperty.FirewallDeploymentModel``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-thirdpartyfirewallpolicy.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_fms as fms
                
                third_party_firewall_policy_property = fms.CfnPolicy.ThirdPartyFirewallPolicyProperty(
                    firewall_deployment_model="firewallDeploymentModel"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7f4a7c7a12ee187727472c21f2a6147ca000c43ae4d50b0ab60025dea29d98eb)
                check_type(argname="argument firewall_deployment_model", value=firewall_deployment_model, expected_type=type_hints["firewall_deployment_model"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "firewall_deployment_model": firewall_deployment_model,
            }

        @builtins.property
        def firewall_deployment_model(self) -> builtins.str:
            '''``CfnPolicy.ThirdPartyFirewallPolicyProperty.FirewallDeploymentModel``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-thirdpartyfirewallpolicy.html#cfn-fms-policy-thirdpartyfirewallpolicy-firewalldeploymentmodel
            '''
            result = self._values.get("firewall_deployment_model")
            assert result is not None, "Required property 'firewall_deployment_model' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ThirdPartyFirewallPolicyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_fms.CfnPolicyProps",
    jsii_struct_bases=[],
    name_mapping={
        "exclude_resource_tags": "excludeResourceTags",
        "policy_name": "policyName",
        "remediation_enabled": "remediationEnabled",
        "resource_type": "resourceType",
        "security_service_policy_data": "securityServicePolicyData",
        "delete_all_policy_resources": "deleteAllPolicyResources",
        "exclude_map": "excludeMap",
        "include_map": "includeMap",
        "resources_clean_up": "resourcesCleanUp",
        "resource_tags": "resourceTags",
        "resource_type_list": "resourceTypeList",
        "tags": "tags",
    },
)
class CfnPolicyProps:
    def __init__(
        self,
        *,
        exclude_resource_tags: typing.Union[builtins.bool, _IResolvable_da3f097b],
        policy_name: builtins.str,
        remediation_enabled: typing.Union[builtins.bool, _IResolvable_da3f097b],
        resource_type: builtins.str,
        security_service_policy_data: typing.Union[typing.Union[CfnPolicy.SecurityServicePolicyDataProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b],
        delete_all_policy_resources: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        exclude_map: typing.Optional[typing.Union[typing.Union[CfnPolicy.IEMapProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
        include_map: typing.Optional[typing.Union[typing.Union[CfnPolicy.IEMapProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
        resources_clean_up: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        resource_tags: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union[CfnPolicy.ResourceTagProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]]]] = None,
        resource_type_list: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[CfnPolicy.PolicyTagProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnPolicy``.

        :param exclude_resource_tags: Used only when tags are specified in the ``ResourceTags`` property. If this property is ``True`` , resources with the specified tags are not in scope of the policy. If it's ``False`` , only resources with the specified tags are in scope of the policy.
        :param policy_name: The name of the AWS Firewall Manager policy.
        :param remediation_enabled: Indicates if the policy should be automatically applied to new resources.
        :param resource_type: The type of resource protected by or in scope of the policy. This is in the format shown in the `AWS Resource Types Reference <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html>`_ . To apply this policy to multiple resource types, specify a resource type of ``ResourceTypeList`` and then specify the resource types in a ``ResourceTypeList`` . For AWS WAF and Shield Advanced, example resource types include ``AWS::ElasticLoadBalancingV2::LoadBalancer`` and ``AWS::CloudFront::Distribution`` . For a security group common policy, valid values are ``AWS::EC2::NetworkInterface`` and ``AWS::EC2::Instance`` . For a security group content audit policy, valid values are ``AWS::EC2::SecurityGroup`` , ``AWS::EC2::NetworkInterface`` , and ``AWS::EC2::Instance`` . For a security group usage audit policy, the value is ``AWS::EC2::SecurityGroup`` . For an AWS Network Firewall policy or DNS Firewall policy, the value is ``AWS::EC2::VPC`` .
        :param security_service_policy_data: Details about the security service that is being used to protect the resources. This contains the following settings: - Type - Indicates the service type that the policy uses to protect the resource. For security group policies, Firewall Manager supports one security group for each common policy and for each content audit policy. This is an adjustable limit that you can increase by contacting AWS Support . Valid values: ``DNS_FIREWALL`` | ``NETWORK_FIREWALL`` | ``SECURITY_GROUPS_COMMON`` | ``SECURITY_GROUPS_CONTENT_AUDIT`` | ``SECURITY_GROUPS_USAGE_AUDIT`` | ``SHIELD_ADVANCED`` | ``WAFV2`` | ``WAF`` - ManagedServiceData - Details about the service that are specific to the service type, in JSON format. - Example: ``DNS_FIREWALL`` ``"ManagedServiceData": "{ \\"type\\": \\"DNS_FIREWALL\\", \\"preProcessRuleGroups\\": [{\\"ruleGroupId\\": \\"rslvr-frg-123456\\", \\"priority\\": 11}], \\"postProcessRuleGroups\\": [{\\"ruleGroupId\\": \\"rslvr-frg-123456\\", \\"priority\\": 9902}]}"`` - Example: ``NETWORK_FIREWALL`` ``"ManagedServiceData":"{\\"type\\":\\"NETWORK_FIREWALL\\",\\"networkFirewallStatelessRuleGroupReferences\\":[{\\"resourceARN\\":\\"arn:aws:network-firewall:us-east-1:000000000000:stateless-rulegroup\\/example\\",\\"priority\\":1}],\\"networkFirewallStatelessDefaultActions\\":[\\"aws:drop\\",\\"example\\"],\\"networkFirewallStatelessFragmentDefaultActions\\":[\\"aws:drop\\",\\"example\\"],\\"networkFirewallStatelessCustomActions\\":[{\\"actionName\\":\\"example\\",\\"actionDefinition\\":{\\"publishMetricAction\\":{\\"dimensions\\":[{\\"value\\":\\"example\\"}]}}}],\\"networkFirewallStatefulRuleGroupReferences\\":[{\\"resourceARN\\":\\"arn:aws:network-firewall:us-east-1:000000000000:stateful-rulegroup\\/example\\"}],\\"networkFirewallOrchestrationConfig\\":{\\"singleFirewallEndpointPerVPC\\":false,\\"allowedIPV4CidrList\\":[]}}"`` - Example: ``SECURITY_GROUPS_COMMON`` ``"SecurityServicePolicyData":{"Type":"SECURITY_GROUPS_COMMON","ManagedServiceData":"{\\"type\\":\\"SECURITY_GROUPS_COMMON\\",\\"revertManualSecurityGroupChanges\\":false,\\"exclusiveResourceSecurityGroupManagement\\":false,\\"securityGroups\\":[{\\"id\\":\\" sg-000e55995d61a06bd\\"}]}"},"RemediationEnabled":false,"ResourceType":"AWS::EC2::NetworkInterface"}`` - Example: ``SECURITY_GROUPS_CONTENT_AUDIT`` ``"SecurityServicePolicyData":{"Type":"SECURITY_GROUPS_CONTENT_AUDIT","ManagedServiceData":"{\\"type\\":\\"SECURITY_GROUPS_CONTENT_AUDIT\\",\\"securityGroups\\":[{\\"id\\":\\" sg-000e55995d61a06bd \\"}],\\"securityGroupAction\\":{\\"type\\":\\"ALLOW\\"}}"},"RemediationEnabled":false,"ResourceType":"AWS::EC2::NetworkInterface"}`` The security group action for content audit can be ``ALLOW`` or ``DENY`` . For ``ALLOW`` , all in-scope security group rules must be within the allowed range of the policy's security group rules. For ``DENY`` , all in-scope security group rules must not contain a value or a range that matches a rule value or range in the policy security group. - Example: ``SECURITY_GROUPS_USAGE_AUDIT`` ``"SecurityServicePolicyData":{"Type":"SECURITY_GROUPS_USAGE_AUDIT","ManagedServiceData":"{\\"type\\":\\"SECURITY_GROUPS_USAGE_AUDIT\\",\\"deleteUnusedSecurityGroups\\":true,\\"coalesceRedundantSecurityGroups\\":true}"},"RemediationEnabled":false,"Resou rceType":"AWS::EC2::SecurityGroup"}`` - Specification for ``SHIELD_ADVANCED`` for Amazon CloudFront distributions ``"ManagedServiceData": "{\\"type\\": \\"SHIELD_ADVANCED\\", \\"automaticResponseConfiguration\\": {\\"automaticResponseStatus\\":\\"ENABLED|IGNORED|DISABLED\\", \\"automaticResponseAction\\":\\"BLOCK|COUNT\\"}, \\"overrideCustomerWebaclClassic\\":true|false}"`` For example: ``"ManagedServiceData": "{\\"type\\":\\"SHIELD_ADVANCED\\",\\"automaticResponseConfiguration\\": {\\"automaticResponseStatus\\":\\"ENABLED\\", \\"automaticResponseAction\\":\\"COUNT\\"}}"`` The default value for ``automaticResponseStatus`` is ``IGNORED`` . The value for ``automaticResponseAction`` is only required when ``automaticResponseStatus`` is set to ``ENABLED`` . The default value for ``overrideCustomerWebaclClassic`` is ``false`` . For other resource types that you can protect with a Shield Advanced policy, this ``ManagedServiceData`` configuration is an empty string. - Example: ``WAFV2`` ``"ManagedServiceData": "{\\"type\\":\\"WAFV2\\",\\"preProcessRuleGroups\\":[{\\"ruleGroupArn\\":null,\\"overrideAction\\":{\\"type\\":\\"NONE\\"},\\"managedRuleGroupIdentifier\\":{\\"version\\":null,\\"vendorName\\":\\"AWS\\",\\"managedRuleGroupName\\":\\"AWSManagedRulesAmazonIpReputationList\\"},\\"ruleGroupType\\":\\"ManagedRuleGroup\\",\\"excludeRules\\":[]}],\\"postProcessRuleGroups\\":[],\\"defaultAction\\":{\\"type\\":\\"ALLOW\\"},\\"overrideCustomerWebACLAssociation\\":false,\\"loggingConfiguration\\":{\\"logDestinationConfigs\\":[\\"arn:aws:firehose:us-west-2:12345678912:deliverystream/aws-waf-logs-fms-admin-destination\\"],\\"redactedFields\\":[{\\"redactedFieldType\\":\\"SingleHeader\\",\\"redactedFieldValue\\":\\"Cookies\\"},{\\"redactedFieldType\\":\\"Method\\"}]}}"`` In the ``loggingConfiguration`` , you can specify one ``logDestinationConfigs`` , you can optionally provide up to 20 ``redactedFields`` , and the ``RedactedFieldType`` must be one of ``URI`` , ``QUERY_STRING`` , ``HEADER`` , or ``METHOD`` . - Example: ``WAF Classic`` ``"ManagedServiceData": "{\\"type\\": \\"WAF\\", \\"ruleGroups\\": [{\\"id\\":\\"12345678-1bcd-9012-efga-0987654321ab\\", \\"overrideAction\\" : {\\"type\\": \\"COUNT\\"}}],\\"defaultAction\\": {\\"type\\": \\"BLOCK\\"}}`` AWS WAF Classic doesn't support rule groups in CloudFront . To create a WAF Classic policy through CloudFormation, create your rule groups outside of CloudFront , then provide the rule group IDs in the WAF managed service data specification.
        :param delete_all_policy_resources: Used when deleting a policy. If ``true`` , Firewall Manager performs cleanup according to the policy type. For AWS WAF and Shield Advanced policies, Firewall Manager does the following: - Deletes rule groups created by Firewall Manager - Removes web ACLs from in-scope resources - Deletes web ACLs that contain no rules or rule groups For security group policies, Firewall Manager does the following for each security group in the policy: - Disassociates the security group from in-scope resources - Deletes the security group if it was created through Firewall Manager and if it's no longer associated with any resources through another policy After the cleanup, in-scope resources are no longer protected by web ACLs in this policy. Protection of out-of-scope resources remains unchanged. Scope is determined by tags that you create and accounts that you associate with the policy. When creating the policy, if you specify that only resources in specific accounts or with specific tags are in scope of the policy, those accounts and resources are handled by the policy. All others are out of scope. If you don't specify tags or accounts, all resources are in scope.
        :param exclude_map: Specifies the AWS account IDs and AWS Organizations organizational units (OUs) to exclude from the policy. Specifying an OU is the equivalent of specifying all accounts in the OU and in any of its child OUs, including any child OUs and accounts that are added at a later time. You can specify inclusions or exclusions, but not both. If you specify an ``IncludeMap`` , AWS Firewall Manager applies the policy to all accounts specified by the ``IncludeMap`` , and does not evaluate any ``ExcludeMap`` specifications. If you do not specify an ``IncludeMap`` , then Firewall Manager applies the policy to all accounts except for those specified by the ``ExcludeMap`` . You can specify account IDs, OUs, or a combination: - Specify account IDs by setting the key to ``ACCOUNT`` . For example, the following is a valid map: ``{“ACCOUNT” : [“accountID1”, “accountID2”]}`` . - Specify OUs by setting the key to ``ORGUNIT`` . For example, the following is a valid map: ``{“ORGUNIT” : [“ouid111”, “ouid112”]}`` . - Specify accounts and OUs together in a single map, separated with a comma. For example, the following is a valid map: ``{“ACCOUNT” : [“accountID1”, “accountID2”], “ORGUNIT” : [“ouid111”, “ouid112”]}`` .
        :param include_map: Specifies the AWS account IDs and AWS Organizations organizational units (OUs) to include in the policy. Specifying an OU is the equivalent of specifying all accounts in the OU and in any of its child OUs, including any child OUs and accounts that are added at a later time. You can specify inclusions or exclusions, but not both. If you specify an ``IncludeMap`` , AWS Firewall Manager applies the policy to all accounts specified by the ``IncludeMap`` , and does not evaluate any ``ExcludeMap`` specifications. If you do not specify an ``IncludeMap`` , then Firewall Manager applies the policy to all accounts except for those specified by the ``ExcludeMap`` . You can specify account IDs, OUs, or a combination: - Specify account IDs by setting the key to ``ACCOUNT`` . For example, the following is a valid map: ``{“ACCOUNT” : [“accountID1”, “accountID2”]}`` . - Specify OUs by setting the key to ``ORGUNIT`` . For example, the following is a valid map: ``{“ORGUNIT” : [“ouid111”, “ouid112”]}`` . - Specify accounts and OUs together in a single map, separated with a comma. For example, the following is a valid map: ``{“ACCOUNT” : [“accountID1”, “accountID2”], “ORGUNIT” : [“ouid111”, “ouid112”]}`` .
        :param resources_clean_up: Indicates whether AWS Firewall Manager should automatically remove protections from resources that leave the policy scope and clean up resources that Firewall Manager is managing for accounts when those accounts leave policy scope. For example, Firewall Manager will disassociate a Firewall Manager managed web ACL from a protected customer resource when the customer resource leaves policy scope. By default, Firewall Manager doesn't remove protections or delete Firewall Manager managed resources. This option is not available for Shield Advanced or AWS WAF Classic policies.
        :param resource_tags: An array of ``ResourceTag`` objects, used to explicitly include resources in the policy scope or explicitly exclude them. If this isn't set, then tags aren't used to modify policy scope. See also ``ExcludeResourceTags`` .
        :param resource_type_list: An array of ``ResourceType`` objects. Use this only to specify multiple resource types. To specify a single resource type, use ``ResourceType`` .
        :param tags: A collection of key:value pairs associated with an AWS resource. The key:value pair can be anything you define. Typically, the tag key represents a category (such as "environment") and the tag value represents a specific value within that category (such as "test," "development," or "production"). You can add up to 50 tags to each AWS resource.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_fms as fms
            
            cfn_policy_props = fms.CfnPolicyProps(
                exclude_resource_tags=False,
                policy_name="policyName",
                remediation_enabled=False,
                resource_type="resourceType",
                security_service_policy_data=fms.CfnPolicy.SecurityServicePolicyDataProperty(
                    type="type",
            
                    # the properties below are optional
                    managed_service_data="managedServiceData",
                    policy_option=fms.CfnPolicy.PolicyOptionProperty(
                        network_firewall_policy=fms.CfnPolicy.NetworkFirewallPolicyProperty(
                            firewall_deployment_model="firewallDeploymentModel"
                        ),
                        third_party_firewall_policy=fms.CfnPolicy.ThirdPartyFirewallPolicyProperty(
                            firewall_deployment_model="firewallDeploymentModel"
                        )
                    )
                ),
            
                # the properties below are optional
                delete_all_policy_resources=False,
                exclude_map={
                    "account": ["account"],
                    "orgunit": ["orgunit"]
                },
                include_map={
                    "account": ["account"],
                    "orgunit": ["orgunit"]
                },
                resources_clean_up=False,
                resource_tags=[fms.CfnPolicy.ResourceTagProperty(
                    key="key",
            
                    # the properties below are optional
                    value="value"
                )],
                resource_type_list=["resourceTypeList"],
                tags=[fms.CfnPolicy.PolicyTagProperty(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8455eef74a6daf8d86ebd4c14f18184bf9c938d95a07a9902bf05c79f9b2b322)
            check_type(argname="argument exclude_resource_tags", value=exclude_resource_tags, expected_type=type_hints["exclude_resource_tags"])
            check_type(argname="argument policy_name", value=policy_name, expected_type=type_hints["policy_name"])
            check_type(argname="argument remediation_enabled", value=remediation_enabled, expected_type=type_hints["remediation_enabled"])
            check_type(argname="argument resource_type", value=resource_type, expected_type=type_hints["resource_type"])
            check_type(argname="argument security_service_policy_data", value=security_service_policy_data, expected_type=type_hints["security_service_policy_data"])
            check_type(argname="argument delete_all_policy_resources", value=delete_all_policy_resources, expected_type=type_hints["delete_all_policy_resources"])
            check_type(argname="argument exclude_map", value=exclude_map, expected_type=type_hints["exclude_map"])
            check_type(argname="argument include_map", value=include_map, expected_type=type_hints["include_map"])
            check_type(argname="argument resources_clean_up", value=resources_clean_up, expected_type=type_hints["resources_clean_up"])
            check_type(argname="argument resource_tags", value=resource_tags, expected_type=type_hints["resource_tags"])
            check_type(argname="argument resource_type_list", value=resource_type_list, expected_type=type_hints["resource_type_list"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "exclude_resource_tags": exclude_resource_tags,
            "policy_name": policy_name,
            "remediation_enabled": remediation_enabled,
            "resource_type": resource_type,
            "security_service_policy_data": security_service_policy_data,
        }
        if delete_all_policy_resources is not None:
            self._values["delete_all_policy_resources"] = delete_all_policy_resources
        if exclude_map is not None:
            self._values["exclude_map"] = exclude_map
        if include_map is not None:
            self._values["include_map"] = include_map
        if resources_clean_up is not None:
            self._values["resources_clean_up"] = resources_clean_up
        if resource_tags is not None:
            self._values["resource_tags"] = resource_tags
        if resource_type_list is not None:
            self._values["resource_type_list"] = resource_type_list
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def exclude_resource_tags(
        self,
    ) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
        '''Used only when tags are specified in the ``ResourceTags`` property.

        If this property is ``True`` , resources with the specified tags are not in scope of the policy. If it's ``False`` , only resources with the specified tags are in scope of the policy.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-excluderesourcetags
        '''
        result = self._values.get("exclude_resource_tags")
        assert result is not None, "Required property 'exclude_resource_tags' is missing"
        return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

    @builtins.property
    def policy_name(self) -> builtins.str:
        '''The name of the AWS Firewall Manager policy.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-policyname
        '''
        result = self._values.get("policy_name")
        assert result is not None, "Required property 'policy_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def remediation_enabled(self) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
        '''Indicates if the policy should be automatically applied to new resources.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-remediationenabled
        '''
        result = self._values.get("remediation_enabled")
        assert result is not None, "Required property 'remediation_enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

    @builtins.property
    def resource_type(self) -> builtins.str:
        '''The type of resource protected by or in scope of the policy.

        This is in the format shown in the `AWS Resource Types Reference <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html>`_ . To apply this policy to multiple resource types, specify a resource type of ``ResourceTypeList`` and then specify the resource types in a ``ResourceTypeList`` .

        For AWS WAF and Shield Advanced, example resource types include ``AWS::ElasticLoadBalancingV2::LoadBalancer`` and ``AWS::CloudFront::Distribution`` . For a security group common policy, valid values are ``AWS::EC2::NetworkInterface`` and ``AWS::EC2::Instance`` . For a security group content audit policy, valid values are ``AWS::EC2::SecurityGroup`` , ``AWS::EC2::NetworkInterface`` , and ``AWS::EC2::Instance`` . For a security group usage audit policy, the value is ``AWS::EC2::SecurityGroup`` . For an AWS Network Firewall policy or DNS Firewall policy, the value is ``AWS::EC2::VPC`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-resourcetype
        '''
        result = self._values.get("resource_type")
        assert result is not None, "Required property 'resource_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def security_service_policy_data(
        self,
    ) -> typing.Union[CfnPolicy.SecurityServicePolicyDataProperty, _IResolvable_da3f097b]:
        '''Details about the security service that is being used to protect the resources.

        This contains the following settings:

        - Type - Indicates the service type that the policy uses to protect the resource. For security group policies, Firewall Manager supports one security group for each common policy and for each content audit policy. This is an adjustable limit that you can increase by contacting AWS Support .

        Valid values: ``DNS_FIREWALL`` | ``NETWORK_FIREWALL`` | ``SECURITY_GROUPS_COMMON`` | ``SECURITY_GROUPS_CONTENT_AUDIT`` | ``SECURITY_GROUPS_USAGE_AUDIT`` | ``SHIELD_ADVANCED`` | ``WAFV2`` | ``WAF``

        - ManagedServiceData - Details about the service that are specific to the service type, in JSON format.
        - Example: ``DNS_FIREWALL``

        ``"ManagedServiceData": "{ \\"type\\": \\"DNS_FIREWALL\\", \\"preProcessRuleGroups\\": [{\\"ruleGroupId\\": \\"rslvr-frg-123456\\", \\"priority\\": 11}], \\"postProcessRuleGroups\\": [{\\"ruleGroupId\\": \\"rslvr-frg-123456\\", \\"priority\\": 9902}]}"``

        - Example: ``NETWORK_FIREWALL``

        ``"ManagedServiceData":"{\\"type\\":\\"NETWORK_FIREWALL\\",\\"networkFirewallStatelessRuleGroupReferences\\":[{\\"resourceARN\\":\\"arn:aws:network-firewall:us-east-1:000000000000:stateless-rulegroup\\/example\\",\\"priority\\":1}],\\"networkFirewallStatelessDefaultActions\\":[\\"aws:drop\\",\\"example\\"],\\"networkFirewallStatelessFragmentDefaultActions\\":[\\"aws:drop\\",\\"example\\"],\\"networkFirewallStatelessCustomActions\\":[{\\"actionName\\":\\"example\\",\\"actionDefinition\\":{\\"publishMetricAction\\":{\\"dimensions\\":[{\\"value\\":\\"example\\"}]}}}],\\"networkFirewallStatefulRuleGroupReferences\\":[{\\"resourceARN\\":\\"arn:aws:network-firewall:us-east-1:000000000000:stateful-rulegroup\\/example\\"}],\\"networkFirewallOrchestrationConfig\\":{\\"singleFirewallEndpointPerVPC\\":false,\\"allowedIPV4CidrList\\":[]}}"``

        - Example: ``SECURITY_GROUPS_COMMON``

        ``"SecurityServicePolicyData":{"Type":"SECURITY_GROUPS_COMMON","ManagedServiceData":"{\\"type\\":\\"SECURITY_GROUPS_COMMON\\",\\"revertManualSecurityGroupChanges\\":false,\\"exclusiveResourceSecurityGroupManagement\\":false,\\"securityGroups\\":[{\\"id\\":\\" sg-000e55995d61a06bd\\"}]}"},"RemediationEnabled":false,"ResourceType":"AWS::EC2::NetworkInterface"}``

        - Example: ``SECURITY_GROUPS_CONTENT_AUDIT``

        ``"SecurityServicePolicyData":{"Type":"SECURITY_GROUPS_CONTENT_AUDIT","ManagedServiceData":"{\\"type\\":\\"SECURITY_GROUPS_CONTENT_AUDIT\\",\\"securityGroups\\":[{\\"id\\":\\" sg-000e55995d61a06bd \\"}],\\"securityGroupAction\\":{\\"type\\":\\"ALLOW\\"}}"},"RemediationEnabled":false,"ResourceType":"AWS::EC2::NetworkInterface"}``

        The security group action for content audit can be ``ALLOW`` or ``DENY`` . For ``ALLOW`` , all in-scope security group rules must be within the allowed range of the policy's security group rules. For ``DENY`` , all in-scope security group rules must not contain a value or a range that matches a rule value or range in the policy security group.

        - Example: ``SECURITY_GROUPS_USAGE_AUDIT``

        ``"SecurityServicePolicyData":{"Type":"SECURITY_GROUPS_USAGE_AUDIT","ManagedServiceData":"{\\"type\\":\\"SECURITY_GROUPS_USAGE_AUDIT\\",\\"deleteUnusedSecurityGroups\\":true,\\"coalesceRedundantSecurityGroups\\":true}"},"RemediationEnabled":false,"Resou rceType":"AWS::EC2::SecurityGroup"}``

        - Specification for ``SHIELD_ADVANCED`` for Amazon CloudFront distributions

        ``"ManagedServiceData": "{\\"type\\": \\"SHIELD_ADVANCED\\", \\"automaticResponseConfiguration\\": {\\"automaticResponseStatus\\":\\"ENABLED|IGNORED|DISABLED\\", \\"automaticResponseAction\\":\\"BLOCK|COUNT\\"}, \\"overrideCustomerWebaclClassic\\":true|false}"``

        For example: ``"ManagedServiceData": "{\\"type\\":\\"SHIELD_ADVANCED\\",\\"automaticResponseConfiguration\\": {\\"automaticResponseStatus\\":\\"ENABLED\\", \\"automaticResponseAction\\":\\"COUNT\\"}}"``

        The default value for ``automaticResponseStatus`` is ``IGNORED`` . The value for ``automaticResponseAction`` is only required when ``automaticResponseStatus`` is set to ``ENABLED`` . The default value for ``overrideCustomerWebaclClassic`` is ``false`` .

        For other resource types that you can protect with a Shield Advanced policy, this ``ManagedServiceData`` configuration is an empty string.

        - Example: ``WAFV2``

        ``"ManagedServiceData": "{\\"type\\":\\"WAFV2\\",\\"preProcessRuleGroups\\":[{\\"ruleGroupArn\\":null,\\"overrideAction\\":{\\"type\\":\\"NONE\\"},\\"managedRuleGroupIdentifier\\":{\\"version\\":null,\\"vendorName\\":\\"AWS\\",\\"managedRuleGroupName\\":\\"AWSManagedRulesAmazonIpReputationList\\"},\\"ruleGroupType\\":\\"ManagedRuleGroup\\",\\"excludeRules\\":[]}],\\"postProcessRuleGroups\\":[],\\"defaultAction\\":{\\"type\\":\\"ALLOW\\"},\\"overrideCustomerWebACLAssociation\\":false,\\"loggingConfiguration\\":{\\"logDestinationConfigs\\":[\\"arn:aws:firehose:us-west-2:12345678912:deliverystream/aws-waf-logs-fms-admin-destination\\"],\\"redactedFields\\":[{\\"redactedFieldType\\":\\"SingleHeader\\",\\"redactedFieldValue\\":\\"Cookies\\"},{\\"redactedFieldType\\":\\"Method\\"}]}}"``

        In the ``loggingConfiguration`` , you can specify one ``logDestinationConfigs`` , you can optionally provide up to 20 ``redactedFields`` , and the ``RedactedFieldType`` must be one of ``URI`` , ``QUERY_STRING`` , ``HEADER`` , or ``METHOD`` .

        - Example: ``WAF Classic``

        ``"ManagedServiceData": "{\\"type\\": \\"WAF\\", \\"ruleGroups\\": [{\\"id\\":\\"12345678-1bcd-9012-efga-0987654321ab\\", \\"overrideAction\\" : {\\"type\\": \\"COUNT\\"}}],\\"defaultAction\\": {\\"type\\": \\"BLOCK\\"}}``

        AWS WAF Classic doesn't support rule groups in CloudFront . To create a WAF Classic policy through CloudFormation, create your rule groups outside of CloudFront , then provide the rule group IDs in the WAF managed service data specification.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-securityservicepolicydata
        '''
        result = self._values.get("security_service_policy_data")
        assert result is not None, "Required property 'security_service_policy_data' is missing"
        return typing.cast(typing.Union[CfnPolicy.SecurityServicePolicyDataProperty, _IResolvable_da3f097b], result)

    @builtins.property
    def delete_all_policy_resources(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Used when deleting a policy. If ``true`` , Firewall Manager performs cleanup according to the policy type.

        For AWS WAF and Shield Advanced policies, Firewall Manager does the following:

        - Deletes rule groups created by Firewall Manager
        - Removes web ACLs from in-scope resources
        - Deletes web ACLs that contain no rules or rule groups

        For security group policies, Firewall Manager does the following for each security group in the policy:

        - Disassociates the security group from in-scope resources
        - Deletes the security group if it was created through Firewall Manager and if it's no longer associated with any resources through another policy

        After the cleanup, in-scope resources are no longer protected by web ACLs in this policy. Protection of out-of-scope resources remains unchanged. Scope is determined by tags that you create and accounts that you associate with the policy. When creating the policy, if you specify that only resources in specific accounts or with specific tags are in scope of the policy, those accounts and resources are handled by the policy. All others are out of scope. If you don't specify tags or accounts, all resources are in scope.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-deleteallpolicyresources
        '''
        result = self._values.get("delete_all_policy_resources")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def exclude_map(
        self,
    ) -> typing.Optional[typing.Union[CfnPolicy.IEMapProperty, _IResolvable_da3f097b]]:
        '''Specifies the AWS account IDs and AWS Organizations organizational units (OUs) to exclude from the policy.

        Specifying an OU is the equivalent of specifying all accounts in the OU and in any of its child OUs, including any child OUs and accounts that are added at a later time.

        You can specify inclusions or exclusions, but not both. If you specify an ``IncludeMap`` , AWS Firewall Manager applies the policy to all accounts specified by the ``IncludeMap`` , and does not evaluate any ``ExcludeMap`` specifications. If you do not specify an ``IncludeMap`` , then Firewall Manager applies the policy to all accounts except for those specified by the ``ExcludeMap`` .

        You can specify account IDs, OUs, or a combination:

        - Specify account IDs by setting the key to ``ACCOUNT`` . For example, the following is a valid map: ``{“ACCOUNT” : [“accountID1”, “accountID2”]}`` .
        - Specify OUs by setting the key to ``ORGUNIT`` . For example, the following is a valid map: ``{“ORGUNIT” : [“ouid111”, “ouid112”]}`` .
        - Specify accounts and OUs together in a single map, separated with a comma. For example, the following is a valid map: ``{“ACCOUNT” : [“accountID1”, “accountID2”], “ORGUNIT” : [“ouid111”, “ouid112”]}`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-excludemap
        '''
        result = self._values.get("exclude_map")
        return typing.cast(typing.Optional[typing.Union[CfnPolicy.IEMapProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def include_map(
        self,
    ) -> typing.Optional[typing.Union[CfnPolicy.IEMapProperty, _IResolvable_da3f097b]]:
        '''Specifies the AWS account IDs and AWS Organizations organizational units (OUs) to include in the policy.

        Specifying an OU is the equivalent of specifying all accounts in the OU and in any of its child OUs, including any child OUs and accounts that are added at a later time.

        You can specify inclusions or exclusions, but not both. If you specify an ``IncludeMap`` , AWS Firewall Manager applies the policy to all accounts specified by the ``IncludeMap`` , and does not evaluate any ``ExcludeMap`` specifications. If you do not specify an ``IncludeMap`` , then Firewall Manager applies the policy to all accounts except for those specified by the ``ExcludeMap`` .

        You can specify account IDs, OUs, or a combination:

        - Specify account IDs by setting the key to ``ACCOUNT`` . For example, the following is a valid map: ``{“ACCOUNT” : [“accountID1”, “accountID2”]}`` .
        - Specify OUs by setting the key to ``ORGUNIT`` . For example, the following is a valid map: ``{“ORGUNIT” : [“ouid111”, “ouid112”]}`` .
        - Specify accounts and OUs together in a single map, separated with a comma. For example, the following is a valid map: ``{“ACCOUNT” : [“accountID1”, “accountID2”], “ORGUNIT” : [“ouid111”, “ouid112”]}`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-includemap
        '''
        result = self._values.get("include_map")
        return typing.cast(typing.Optional[typing.Union[CfnPolicy.IEMapProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def resources_clean_up(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Indicates whether AWS Firewall Manager should automatically remove protections from resources that leave the policy scope and clean up resources that Firewall Manager is managing for accounts when those accounts leave policy scope.

        For example, Firewall Manager will disassociate a Firewall Manager managed web ACL from a protected customer resource when the customer resource leaves policy scope.

        By default, Firewall Manager doesn't remove protections or delete Firewall Manager managed resources.

        This option is not available for Shield Advanced or AWS WAF Classic policies.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-resourcescleanup
        '''
        result = self._values.get("resources_clean_up")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def resource_tags(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnPolicy.ResourceTagProperty, _IResolvable_da3f097b]]]]:
        '''An array of ``ResourceTag`` objects, used to explicitly include resources in the policy scope or explicitly exclude them.

        If this isn't set, then tags aren't used to modify policy scope. See also ``ExcludeResourceTags`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-resourcetags
        '''
        result = self._values.get("resource_tags")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnPolicy.ResourceTagProperty, _IResolvable_da3f097b]]]], result)

    @builtins.property
    def resource_type_list(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An array of ``ResourceType`` objects.

        Use this only to specify multiple resource types. To specify a single resource type, use ``ResourceType`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-resourcetypelist
        '''
        result = self._values.get("resource_type_list")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[CfnPolicy.PolicyTagProperty]]:
        '''A collection of key:value pairs associated with an AWS resource.

        The key:value pair can be anything you define. Typically, the tag key represents a category (such as "environment") and the tag value represents a specific value within that category (such as "test," "development," or "production"). You can add up to 50 tags to each AWS resource.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[CfnPolicy.PolicyTagProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPolicyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnNotificationChannel",
    "CfnNotificationChannelProps",
    "CfnPolicy",
    "CfnPolicyProps",
]

publication.publish()

def _typecheckingstub__7a03e25c676e3f843e7365938075353612a65a3a2bd2538074f016448b29053c(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    sns_role_name: builtins.str,
    sns_topic_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eae25dcbfb8d4710a66ea0f6804d609f2c8fbb762e291caa42156e2d5e0a5ccd(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__27e0110b31984037127ddfc8639de3754907e90f7485cfd5b43a5fbe4ad39717(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00bd3c5f6e0b7d08ecc3e9d3f09ce0486f75f4e24649a6e59140bdaa48e6e9ed(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d5dd2548355a1129e0085759bb293de343519fe581ead5c659ceff8ec36b346(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5624e06a5ce62823c414e320e35e25799cfeb05a7db7fa7dc3f5353d1e0fe469(
    *,
    sns_role_name: builtins.str,
    sns_topic_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a29b3b13041b0ccbd18a0c29ff5cff0adbc0e2aedc87591f1c54ec7a1fc830b4(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    exclude_resource_tags: typing.Union[builtins.bool, _IResolvable_da3f097b],
    policy_name: builtins.str,
    remediation_enabled: typing.Union[builtins.bool, _IResolvable_da3f097b],
    resource_type: builtins.str,
    security_service_policy_data: typing.Union[typing.Union[CfnPolicy.SecurityServicePolicyDataProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b],
    delete_all_policy_resources: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    exclude_map: typing.Optional[typing.Union[typing.Union[CfnPolicy.IEMapProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
    include_map: typing.Optional[typing.Union[typing.Union[CfnPolicy.IEMapProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
    resources_clean_up: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    resource_tags: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union[CfnPolicy.ResourceTagProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]]]] = None,
    resource_type_list: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[CfnPolicy.PolicyTagProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4bd3d819ff879695091ea1782c6d44919a2d5d60ac904eb958a4baa5a9b7b105(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b5336d629941f59b9bc57ae2f0f9086302ff307956a981d17c0c74f56e281a98(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20a6c43cec956bc22ae07e19e1af4001c23e93faad6ca1043a917bf0f5dcfc1d(
    value: typing.Union[builtins.bool, _IResolvable_da3f097b],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__62ed5a312383f144ece33d5d7f925fd2a4d83062b6024f0b02b573273b2f360d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce24f414c17fee1c6464201d3595af0f5eddf30ec4dc5532e27f42a5a60bfba0(
    value: typing.Union[builtins.bool, _IResolvable_da3f097b],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45fbd20db788e5f26784bca772c0c150d7f583f3b21916156a9f85bdbbbd064d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c28ba46bb386f4176af9e17ecbe45582b554c7807d38f2929fb3fd7a81f3976(
    value: typing.Union[CfnPolicy.SecurityServicePolicyDataProperty, _IResolvable_da3f097b],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9fe798b33151903c0017cb9d94013617a6afcad058e7ae0fe54c9cfd6dd679c2(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8f8c8d7be71d632f5fd707992c674dd52c74761a09f147830413fcfba30c273(
    value: typing.Optional[typing.Union[CfnPolicy.IEMapProperty, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94290c92cb339b7d588eedc5f7e4693403e89224115f954743aa8b94e5920b0f(
    value: typing.Optional[typing.Union[CfnPolicy.IEMapProperty, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12534b322db922dabec65a01e84b63ba7b3a489d9d25d5870fef80727d31a5c3(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c77d40603d6f4c051dd3f9b5d662e1b2f8b3690fcfa612876de86b1cfb05ac0(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnPolicy.ResourceTagProperty, _IResolvable_da3f097b]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__defb2e92d0f62de49ea900ef5497c0bb92b81e991fe094bca77e0bc3225a174e(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e61b60deb504fb101d8b3c5d4d91824672d7a44fdd9537dec8f729c7d34256be(
    value: typing.Optional[typing.List[CfnPolicy.PolicyTagProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6bcb551e43b08ef4828de279b99e59a3954c4cdc19c8adfe6bf93e810ce36917(
    *,
    account: typing.Optional[typing.Sequence[builtins.str]] = None,
    orgunit: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1dee79c6872a0421399375d5fc2757431881011031a81ccd6674040de21bac13(
    *,
    firewall_deployment_model: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5979520d8e95acd573ee171b00e0dcba3be3872b80af53615d64bc000f703299(
    *,
    network_firewall_policy: typing.Optional[typing.Union[typing.Union[CfnPolicy.NetworkFirewallPolicyProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
    third_party_firewall_policy: typing.Optional[typing.Union[typing.Union[CfnPolicy.ThirdPartyFirewallPolicyProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d5ee16e00771d59c6939cbdec3cdf3c57cdb9a09a7e914e3faf7baaa7416d62(
    *,
    key: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1533af324aea7be8b3e806a7d4a851c48bea2139cd3bb0ce1cc81ff86e976487(
    *,
    key: builtins.str,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c049eeb7140522ded2ec5e8c352001a90a84400f6f8d601bcb6b17805b0a150e(
    *,
    type: builtins.str,
    managed_service_data: typing.Optional[builtins.str] = None,
    policy_option: typing.Optional[typing.Union[typing.Union[CfnPolicy.PolicyOptionProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f4a7c7a12ee187727472c21f2a6147ca000c43ae4d50b0ab60025dea29d98eb(
    *,
    firewall_deployment_model: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8455eef74a6daf8d86ebd4c14f18184bf9c938d95a07a9902bf05c79f9b2b322(
    *,
    exclude_resource_tags: typing.Union[builtins.bool, _IResolvable_da3f097b],
    policy_name: builtins.str,
    remediation_enabled: typing.Union[builtins.bool, _IResolvable_da3f097b],
    resource_type: builtins.str,
    security_service_policy_data: typing.Union[typing.Union[CfnPolicy.SecurityServicePolicyDataProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b],
    delete_all_policy_resources: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    exclude_map: typing.Optional[typing.Union[typing.Union[CfnPolicy.IEMapProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
    include_map: typing.Optional[typing.Union[typing.Union[CfnPolicy.IEMapProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
    resources_clean_up: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    resource_tags: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union[CfnPolicy.ResourceTagProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]]]] = None,
    resource_type_list: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[CfnPolicy.PolicyTagProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
