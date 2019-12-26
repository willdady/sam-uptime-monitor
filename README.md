# Setup

1. Install virtualenvwrapper
2. Install aws-sam-cli (`brew install aws-sam-cli`)
3. Install Docker for Mac
4. `sam build`
5. `sam deploy --guided` (See https://aws.amazon.com/blogs/compute/a-simpler-deployment-experience-with-aws-sam-cli/)

# Invoking locally

```
sam local invoke --parameter-overrides "ParameterKey=UrlToMonitorParameter,ParameterValue=https://google.com"
```

# Building

```
sam build
```

# Deploying

```
sam deploy --guided
```
