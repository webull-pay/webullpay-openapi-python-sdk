# Copyright 2025 Webullpay
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# 	http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

# coding=utf-8

"""
This file borrowed some of its methods from a  modified fork of the
https://github.com/aliyun/aliyun-openapi-python-sdk/blob/master/aliyun-python-sdk-core/aliyunsdkcore/retry/retry_policy.py
which was part of Alibaba Group.
"""

from webullpaysdkcore.retry.retry_condition import RetryCondition, NoRetryCondition, \
    DefaultConfigRetryCondition
from webullpaysdkcore.retry.backoff_strategy import BackoffStrategy, NoDelayStrategy, DefaultMixedBackoffStrategy


class RetryPolicy(RetryCondition, BackoffStrategy):
    def __init__(self, retry_condition, backoff_strategy):
        self.retry_condition = retry_condition
        self.backoff_strategy = backoff_strategy

    def should_retry(self, retry_policy_context):
        return self.retry_condition.should_retry(retry_policy_context)

    def compute_delay_before_next_retry(self, retry_policy_context):
        return self.backoff_strategy.compute_delay_before_next_retry(retry_policy_context)


NO_RETRY_POLICY = RetryPolicy(NoRetryCondition(), NoDelayStrategy())


def get_default_retry_policy(max_retry_times=None):
    return RetryPolicy(DefaultConfigRetryCondition(max_retry_times), DefaultMixedBackoffStrategy())
