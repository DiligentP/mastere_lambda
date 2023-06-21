
## s3:PutBucketPolicy Access Denied Error
```
root@aws-ramda-dev:~/mastere_ramda# serverless deploy

Deploying mastere-ramda to stage dev (ap-northeast-2)

✖ Stack mastere-ramda-dev failed to deploy (36s)
Environment: linux, node 18.16.1, framework 3.32.2, plugin 6.2.3, SDK 4.3.2
Credentials: Local, "serverless-admin" profile
Docs:        docs.serverless.com
Support:     forum.serverless.com
Bugs:        github.com/serverless/serverless/issues

Error:
CREATE_FAILED: ServerlessDeploymentBucketPolicy (AWS::S3::BucketPolicy)
API: s3:PutBucketPolicy Access Denied

View the full error: https://ap-northeast-2.console.aws.amazon.com/cloudformation/home?region=ap-northeast-2#/stack/detail?stackId=arn%3Aaws%3Acloudformation%3Aap-northeast-2%3A993880387813%3Astack%2Fmastere-ramda-dev%2F71be7db0-1033-11ee-8047-0a9ebafd7240
```

### 다음 방법을 사용 하여 해결
```
AWS Identity and Access Management (IAM)을 사용하여 s3:PutBucketPolicy 액세스 권한을 부여하는 방법은 다음과 같습니다:

AWS Management Console에 로그인하고 IAM 콘솔을 엽니다.

좌측 탐색 메뉴에서 "Roles"을 선택합니다.

스택을 배포하거나 업데이트하는 데 사용되는 IAM 역할을 선택합니다. 해당 역할이 없는 경우 새 역할을 생성해야 합니다.

"Permissions" 탭에서 "Attach policies"를 선택합니다.

"Filter policies" 검색 상자에서 "AmazonS3FullAccess"를 입력하고 나타나는 결과에서 "AmazonS3FullAccess"를 선택합니다. 이 정책은 s3:PutBucketPolicy 액션과 다른 S3 액션을 포함합니다.

"Attach policy"를 클릭하여 역할에 정책을 첨부합니다.

이제 역할에 s3:PutBucketPolicy 액세스 권한이 부여되었으므로 해당 역할을 사용하여 CloudFormation 스택을 배포하거나 업데이트할 때 ServerlessDeploymentBucketPolicy (AWS::S3::BucketPolicy)를 생성하는 작업이 성공할 것입니다.
```

## module을 찾지 못하는 문제
https://jsikim1.tistory.com/180

