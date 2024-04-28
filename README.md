# FastApi-project

# To start
```bash
docker build . --tag fastapi
docker run -p 80:80 fastapi

docker build . --tag fastapi && docker run -p 80:80 fastapi_app
```
```bash
git init
git remote add origin git@github.com:falcolnic/fastapi-project.git
.... add gitignore
git add .
git commit -m "..."
git branch -M main
git push -u origin main
```

# docker
https://docs.docker.com/engine/install/ubuntu/

Add Docker's official GPG key:
```bash
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc
```
Add the repository to Apt sources:
```bash
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
```

After action above
```bash
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```
