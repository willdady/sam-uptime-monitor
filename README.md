Serverless application which will ping a URL every N minutes. Sends an email when transitioning between OK and ALARM states.

# Setup

Checkout repository and create a virtual environment for it targeting Python 3. Install aws-sam-cli (on Mac `brew install aws-sam-cli`) and Docker.

# Building

```
sam build
```

# Deploying

```
sam deploy --guided
```

# Invoking locally

```
sam local invoke --parameter-overrides "ParameterKey=UrlToMonitorParameter,ParameterValue=https://google.com"
```
