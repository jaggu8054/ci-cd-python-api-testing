## 1. Build Docker image 
```commandline
docker build -t python-rest-api .
```

## 2. Run Docker image
```commandline
docker run -p 9001:9001 python-rest-api
```

for checking  the  endpoint use 
--->  :9091/test 
port used here  is   9091  for your application running 
