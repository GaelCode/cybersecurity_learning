# Explanation about the test I made

First of all, I installed Docker Desktop on Windows using the instructions on the Docker website.

Next, I created a Docker image:

docker pull sundowndev/phoneinfoga:latest

(:latest is used to get the latest stable version of the image)

After that, there are different command lines for starting PhoneInfoga:

```
docker run -it sundowndev/phoneinfoga scan -n <PHONE_NUMBER>
```

The results will be shown in the terminal.

And:

```
docker run -it -p 8080:8080 sundowndev/phoneinfoga serve -p 8080
```

This will create a server for PhoneInfoga on port 8080. After that, in Docker Desktop, there will be a container, and it's possible to click on it to be redirected to this port.
