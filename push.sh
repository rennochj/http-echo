git add -A && git commit -m "adding x-ray"
git push https://github.com/connerjh/http-echo.git

docker build -t connerjh/http-echo .
docker push connerjh/http-echo
