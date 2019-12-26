Serverless application which will ping a URL every N minutes. Will send an email when transitioning between OK and ALARM states.

# Setup

* Checkout repository and create a virtual environment for it targeting Python 3.7+
* Install aws-sam-cli (on Mac `brew install aws-sam-cli`) and Docker

# Building

```
sam build
```

# Deploying

```
sam deploy --guided
```

# Invoking function locally (requires Docker)

```
sam local invoke --parameter-overrides "ParameterKey=UrlToMonitorParameter,ParameterValue=https://google.com"
```

# Delete stack

```
aws cloudformation delete-stack --stack-name uptime-monitor
```

```
aws cloudformation list-stacks --stack-status-filter DELETE_IN_PROGRESS
```
