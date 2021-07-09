django-cognito-auth
Django user authentication using cognito

Please export following env var

```
export COGNITO_USER_POOL_ID="" 
export COGNITO_APP_CLIENT_ID="" 
export COGNITO_APP_CLIENT_SECRET="" 
export AWS_ACCESS_KEY_ID="" 
export AWS_SECRET_ACCESS_KEY="" 
export AWS_REGION="" 
export S3_BUCKET="" 
export DB_NAME="" 
export DB_USERNAME="" 
export DB_PASSWORD="" 
```

## Note
all api response will have ```HTTP_ACCESSTOKEN``` and ```HTTP_REFRESHTOKEN``` headers, set these headers for further api access

## signup api
### Header
Authorization: Basic "base64 username:password"

### Request
```
{
    "user_attributes": [{
        "Name": "given_name",
        "Value": "ABC"
    },{
        "Name": "family_name",
        "Value": "XYZ"
    }]
}
```

## Login api
### Header
Authorization: Basic "base64 username:password"

### Request - None
### Response
```
{
    "msg": "Welcome <user email>"
}
```


## LogOut api
### Header
pass ```HTTP_ACCESSTOKEN``` and ```HTTP_REFRESHTOKEN``` headers


## Confirm Signup api
### Header
pass ```HTTP_ACCESSTOKEN``` and ```HTTP_REFRESHTOKEN``` headers

### Request
```
{
    "username": "<user email>",
    "password": "<verification code>",
    "force_alias_creation": false
}
```

### Response
```
{
    "ResponseMetadata": {
        "RequestId": "2c8c55e8-9434-4685-a200-16c1c623e844",
        "HTTPStatusCode": 200,
        "HTTPHeaders": {
            "date": "Thu, 08 Jul 2021 22:09:05 GMT",
            "content-type": "application/x-amz-json-1.1",
            "content-length": "2",
            "connection": "keep-alive",
            "x-amzn-requestid": "2c8c55e8-9434-4685-a200-16c1c623e844"
        },
        "RetryAttempts": 0
    }
}
```


## Forgot Password api
### Header
pass ```HTTP_ACCESSTOKEN``` and ```HTTP_REFRESHTOKEN``` headers

### Request
```
{
    "email": "<user email>"
}
```

## Confirm Forgot Password api
### Header
pass ```HTTP_ACCESSTOKEN``` and ```HTTP_REFRESHTOKEN``` headers

### Request
```
{
    "email": "<user email>",
    "new_password": "",
    "code": "<confirmation code"
}
```
