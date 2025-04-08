# NGINX Kubernetes Deployment with Minikube

## ✅ Goal
- Install Minikube and kubectl
- Start a local Kubernetes cluster
- Deploy a simple Nginx Pod
- Expose it via a Service and access it in the browser

---

## 🔧 Prerequisites
- Virtualization enabled in BIOS
- Recommended: 4 CPU cores, 8GB+ RAM
- Docker or a hypervisor (VirtualBox / Hyper-V)
- Installed: `kubectl`, `minikube`

---

## 1️⃣ Install kubectl

### ✅ On Linux (Debian-based):
```bash
sudo apt-get update
sudo apt-get install -y apt-transport-https curl
curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
echo "deb https://apt.kubernetes.io/ kubernetes-xenial main" | sudo tee /etc/apt/sources.list.d/kubernetes.list
sudo apt-get update
sudo apt-get install -y kubectl
```

### ✅ On Windows/Mac:
- Download from: https://kubernetes.io/docs/tasks/tools/

---

## 2️⃣ Install Minikube

### ✅ On Linux:
```bash
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube
```

### ✅ On Windows/Mac:
- Download from: https://minikube.sigs.k8s.io/docs/start/

---

## 3️⃣ Start Minikube Cluster
```bash
minikube start --driver=docker
```
> Starts a local single-node Kubernetes cluster using Docker

---

## 4️⃣ Verify Installation
```bash
kubectl version --client
kubectl get nodes
kubectl cluster-info
```

---

## 5️⃣ Create NGINX Pod

### ✅ Imperative Way
```bash
kubectl run nginx-pod --image=nginx
```

### ✅ Declarative Way (Recommended)
Create a file named `nginx-pod.yaml`:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx-pod
  labels:
    app: nginx
spec:
  containers:
  - name: nginx
    image: nginx
    ports:
    - containerPort: 80
```

Apply it:
```bash
kubectl apply -f nginx-pod.yaml
```

---

## 6️⃣ Expose NGINX as a Service

### ✅ Imperative Way
```bash
kubectl expose pod nginx-pod --type=NodePort --port=80
```

### ✅ Declarative Way
Create a file named `nginx-service.yaml`:
```yaml
apiVersion: v1
kind: Service
metadata:
  name: nginx-service
spec:
  selector:
    app: nginx
  ports:
    - protocol: TCP
      port: 80
      targetPort: 80
  type: NodePort
```

Apply it:
```bash
kubectl apply -f nginx-service.yaml
```

---

## 7️⃣ Access the NGINX Page
```bash
minikube service nginx-service --url
```
This will return a local URL like `http://127.0.0.1:30007` — open it in your browser.

---

## 8️⃣ Useful Commands
```bash
kubectl get pods
kubectl describe pod nginx-pod
kubectl logs nginx-pod
kubectl delete pod nginx-pod
kubectl get svc
```

---

## 📦 Bonus: Clean Up
```bash
kubectl delete pod nginx-pod
kubectl delete svc nginx-service
minikube stop
minikube delete
```

---

## 📘 What You Learn
| Concept       | Purpose                              |
|---------------|--------------------------------------|
| Minikube      | Local Kubernetes cluster             |
| kubectl       | CLI to interact with the cluster     |
| Pod           | Basic deployable unit in Kubernetes  |
| Service       | Exposes Pods to internal/external traffic |
| YAML          | Declarative config for K8s resources |

---

## 💼 GitHub Project Setup
To track your progress and share your project:
```bash
git init
git add .
git commit -m "Initial commit for NGINX K8s setup"
git remote add origin https://github.com/<your-username>/<repo-name>.git
git push -u origin main
```



