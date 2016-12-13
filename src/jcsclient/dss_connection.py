# Copyright (c) 2016 Jiocloud.com, Inc. or its affiliates.  All Rights Reserved
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish, dis-
# tribute, sublicense, and/or sell copies of the Software, and to permit
# persons to whom the Software is furnished to do so, subject to the fol-
# lowing conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABIL-
# ITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT
# SHALL THE AUTHOR BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
#

from jcsclient.dss_api.dss_bucket_ops import *
from jcsclient.dss_api.dss_object_ops import *
from jcsclient.config import *


class DSSConnection(object):
    """DSS main class, each cli command is processed here
    Object is created from inside the dss Controller
    """

    def __init__(self, url, access_key, secret_key, secure, debug):
        setup_config_handler(url, access_key, secret_key, secure, debug)

    def operate(self, op):
        op.parse_args()
        op.validate_args()
        result = op.execute()
        processed_result = op.process_result(result)
        return processed_result

    def main(self):
        pass

    def create_bucket(self, bucketName):
        op = CreateBucketOp(bucketName)
        result = self.operate(self,op)
        return result

    def delete_bucket(self, bucketName):
        op = CreateBucketOp()
        result = self.operate(self,op)
    def head_bucket(self, bucketName):
        op = CreateBucketOp()
        result = self.operate(self,op)

    def list_buckets(self):
        op = CreateBucketOp()
        result = self.operate(self,op)

    def copy_object(self):
        op = CreateBucketOp()
        result = self.operate(self,op)

    def delete_object(self, buckName, objName):
        op = CreateBucketOp()
        result = self.operate(self,op)

    def get_object(self, buckName, objName):
        op = CreateBucketOp()
        result = self.operate(self,op)

    def list_objects(self, buckName):
        op = CreateBucketOp()
        result = self.operate(self,op)

    def head_object(self, buckName, objName):
        op = CreateBucketOp()
        result = self.operate(self,op)

    def put_object(self, buckName, objName, path):
        op = CreateBucketOp()
        result = self.operate(self,op)

    def get_presigned_url(self, buckName, objName, period):
        op = CreateBucketOp()
        result = self.operate(self,op)



class DSSOpFactory(object):
    """Factory to create objects of types DSSOp based on the
    cli arguments
    """

    def __init__(self):
        pass

    def get_op(self, cli_action):
        if(cli_action == 'create-bucket'):
			return CreateBucketOp()
        if(cli_action == 'delete-bucket'):
			return DeleteBucketOp()
        if(cli_action == 'head-bucket'):
			return HeadBucketOp()
        if(cli_action == 'list-buckets'):
			return ListBucketsOp()
        if(cli_action == 'copy-object'):
			return CopyObjectOp()
        if(cli_action == 'delete-object'):
			return DeleteObjectOp()
        if(cli_action == 'get-object'):
			return GetObjectOp()
        if(cli_action == 'head-object'):
			return HeadObjectOp()
        if(cli_action == 'list-objects'):
			return ListObjectsOp()
        if(cli_action == 'put-object'):
			return PutObjectOp()
        if(cli_action == 'get-presigned-url'):
			return GetPresignedURLOp()
        if(cli_action == 'create-multipart-upload'):
			return InitMPUploadOp()
        if(cli_action == 'abort-multipart-upload'):
			return CancelMPUploadOp()
        if(cli_action == 'complete-multipart-upload'):
			return CompleteMPUploadOp()
        if(cli_action == 'list-multipart-uploads'):
			return ListMPUploadsOp()
        if(cli_action == 'list-parts'):
			return ListPartsOp()
        if(cli_action == 'upload-part'):
			return UploadPartOp()

        return None
