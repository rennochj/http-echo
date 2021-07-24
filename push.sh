git add -A && git commit -m "adding x-ray"
git push https://github.com/connerjh/http-echo.git

docker build -t connerjh/http-echo .
docker push connerjh/http-ec

docker build -t http-echo .
docker tag http-echo:latest 882103041271.dkr.ecr.us-west-2.amazonaws.com/http-echo:latest
docker push 882103041271.dkr.ecr.us-west-2.amazonaws.com/http-echo:latest
