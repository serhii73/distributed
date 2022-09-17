Build an image

```
$ docker build --tag image .
```

Run your image as a container   
```
 $ docker run image
```

Go to the three directories and run the container. You can now send a request to the master.

# post a message (master only)
`curl -H "Content-Type: application/json" -X POST -d '{"message":"test"}' localhost:8000/`
