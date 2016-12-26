# import jcsclient
# from jcsclient.dss_connection import DSSConnection
# import os
# import math
# from jcsclient.filechunkio import *
#
# ACCESS_KEY="<access-key>"
# SECRET_KEY="<secret-key>"
# URL = "https://dss.ind-west-1.jiocloudservices.com"
#
# # create a DSSConnection object to use DSS APIs
#
# conn = DSSConnection(url=URL, access_key=ACCESS_KEY, secret_key=SECRET_KEY, secure=True, debug=False)
#
# print "\n print create_bucket now \n"  # To Delete a bucket, delete_bucket(<bucket name>)
# res1 = conn.create_bucket("bucket-test-2614")
# for key in res1:
#     print key + ": " + str(res1[key])
#
#
# print "\n printing delete_bucket now \n"  # To Delete a bucket, delete_bucket(<bucket name>)
# res2 = conn.delete_bucket("bucket-test-2614")
# for key in res2:
#     print key + ": " + str(res2[key])
#
#
# print "\n printing head_bucket now \n"  # To HEAD a bucket, head_bucket(<bucket name>)
# res3 = conn.head_bucket("bucket-test-2613")
# for key in res3:
#     print key + ": " + str(res3[key])
#
#
# print "\n printing list buckets now \n"  # To list all user buckets, list_bucket()
# res4 = conn.list_buckets()
# for key in res4:
#     print key + ": " + str(res4[key])
#
#
# # To list all objects in a bucket, list_objects(<bucket name>, <params dictionary>)
# # The params dictionary contains query params (if any) and should contain them in such manner
# # (only which are being sent should be included in dictionary.)
# # {"prefix": <prefix>, "marker": <marker>, "max-keys": <max-keys>, "delimiter": <delimiter>}
#
# print "\n printing list objects now \n"
# res5 = conn.list_objects("bucket-test-2613")
# for key in res5:
#     print key + ": " + str(res5[key])
#
#
# #To create a new object provide bucket name, key name and path to the file being uploaded
# #In case the object size is bigger than 5GB, it is uploaded as a multipart. User need not to change anything for this.
# #and call put_object(<bucket name>, <key name>, <file path>)
#
# print "\n printing put objects now \n"
# res6 = conn.put_object("bucket-test-2613", "key3", "/Users/harshalgupta/Movies/videos/songs/ek-glassy.mp4")
# for key in res6:
#     print key + ": " + str(res6[key])
#
#
#
# print "\n printing head objects now \n"  # To head an object, head_object(<bucket name>, <key name>)
# res7 = conn.head_object("bucket-test-2613", "key1")
# for key in res7:
#     print key + ": " + str(res7[key])
#
#
# #To download an object, get_object(<bucket name>, <key name> <file path in which the object should be to download>)
# #If file path is not given, the object is downloaded in file with same name as key
#
# print "\n printing get objects now \n"
# res8 = conn.get_object("bucket-test-2614", "key10", "/Users/harshalgupta/code/python-sdk/ari-ari-new.mp4")
# for key in res8:
#     print key + ": " + str(res8[key])
#
#
# print "\nprinting delete object now\n" # # To delete an object, delete_object(<bucket name>, <key name>)
# res9 = conn.delete_object("bucket-test-2613", "key8")
# for key in res9:
#     print key + ": " + str(res9[key])
#
#
# # returns a upload id which is used to upload parts and complete/cancel mp upload. It remains unique for each multipart operation and remains same for all the APIs for that multipart.
# print "\n init multipart upload \n"
# res10 = conn.init_multipart_upload("bucket-test-2614", "key10")
# for key in res10:
#     print key + ": " + str(res10[key])
#
#
# # To upload individual parts of a file in a multipart upload, user need to use filechunkio class of jcsclient to break the file and upload the data in parts.
# # Use the following code snipet as an example.
#
# print "\n upload  multipart upload individual parts \n"
# file_path = "<path to the data file>"
# uploadId = "<which was returned in ini_multipart_upload method"
# part_size = 5 * 1024 * 1024  #  (can be anything between 1MB and 5GB)
# statinfo = os.stat(file_path)
# total_size = statinfo.st_size
# print("\nPerforming multipart upload as the size of file " + file_path + " is greater that 5GB : " + str(
#     total_size))
# part_count = int(math.ceil(total_size / float(part_size)))
# for i in range(part_count):
#     offset = part_size * i
#     bytes = min(part_size, total_size - offset)
#     with FileChunkIO(file_path, 'r', offset=offset, bytes=bytes) as fp:
#         args_dict = {"upload_id": uploadId, "part_number": str(i+1), "file_path": file_path}
#         res11 = conn.upload_multipart_parts("bucket-test-2614", "key10", args_dict, fp, bytes)
#         for key in res11:
#             print key + ": " + str(res11[key])
#
#
# # returns parts in an xml format, If user provides a file path, the info will be written in the file else will be returned in "content" part of response
# print "\n list multipart parts \n".
# res12 = conn.list_multipart_parts("bucket-test-2614", "key10", "<upload id>", "<path to file for storing parts info in xml format>")
# for key in res12:
#     print key + ": " + str(res12[key])
#
#
# print "\n list multipart uploads \n" # returns all multiparts for given bucket in xml format in content part of response
# res13 = conn.list_multipart_uploads("bucket-test-2614")
# for key in res13:
#     print key + ": " + str(res13[key])
#
#
# print "\n cancel multipart upload \n"
# res14 = conn.cancel_multipart_upload("bucket-test-2614", "key5", "<upload id>")
# for key in res14:
#     print key + ": " + str(res14[key])
#
#
#
# # To complete a multipart operation, user need to provide parts info in a xml format. The method takes a file as an input which contains the parts info as xml.
# # File can be same as returned in list parts API
#
# print "\n complete multipart upload \n"
# args_dict = {"upload_id": "<upload id>", "mp_parts_file": "<path to file storing parts info in xml format>"}
# res15 = conn.complete_multipart_upload("bucket-test-2614", "key10", args_dict)
# for key in res15:
#     print key + ": " + str(res15[key])
#
#
# print "\n rename object in a bucket \n" # Renames a object in a bucket
#
# res16 = conn.rename_object("<bucket name>", "<current keyname>", "<new keyname>")
# for key in res16:
#     print key + ": " + str(res16[key])
#
#
# # To cppy an object in same or other bucket. Give <source-bucket/source-keyname> as third param
#
# print "\n copy a object in same/another bucket \n"
# res17 = conn.copy_object("<new-bucket>", "<new-keyame>", "<original-bucket/original-keyname>")
# for key in res17:
#     print key + ": " + str(res17[key])
#
#
# # Returns a url string. Pass the validity of the url in time (in seconds) as third param
#
# print "\n pre-signed url of an object \n"
# res18 = conn.get_presigned_url("bucket-test-2614", "keyname", 1800)
# print res18


# # NOTES:
# # 1. The APIs where no content is expected in response(like create bucket, head bucket and delete bucket and same operation on objects),
# #    the response is a dictionary containing following:
# #    headers : <a dictionary of headers>
# #    status_code: HTTP status code
# #    status_message: HTTP status message
# #    error_message: An xml containing details about reason of failure (only in case of a failed API call)
# #
# # 2. The APIs where content is expected in response(like list buckets or list objects)
# #    the response contains an extra field called "content" which is an xml containing the desired list of results. (Only when successfull API call)
# #
# # 3. In case of HEAD APIs, the info is contained in "headers" dictionary.
