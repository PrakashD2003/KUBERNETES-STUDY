
# Kubernetes Study

This repository explores Kubernetes fundamentals through a set of practical examples.  
It contains multiple branches that demonstrate how to containerise a Python application, deploy it to a local cluster, and run a simple Nginx pod.  
The default `main` branch is an empty skeleton with only a `.gitignore`, while the feature branches (`kubernetes-test-app` and `nginx-pod-deployment`) contain the hands-on code and YAML manifests.

---

## 🚀 Quick Overview

**Goal:** Learn how to build, containerise and deploy applications on Kubernetes.  
Examples use a **Flask app** and an **Nginx pod** to illustrate core resources (Pods, Deployments, Services) and workflows with **Minikube**.

**Branches & Topics:**
- **`kubernetes-test-app`** – a Flask web app  
  - `Dockerfile` to build the image  
  - `deployment.yml` to run two replicas  
  - `service.yml` to expose via NodePort  
  - `app.py` renders a form and returns a personalised message  

- **`nginx-pod-deployment`** – standalone Nginx pod with Service  
  - Step-by-step instructions for installing `kubectl` & Minikube  
  - YAML files for Pod & Service  

- **`main`** – empty branch with `.gitignore`

**Tech Stack:** Docker, Python/Flask, Kubernetes (Pods, Deployments, Services), YAML, Minikube  
**Highlights:** Containerisation, declarative resource definition, scaling with replicas, NodePort exposure, and both imperative & declarative `kubectl` commands.

---

## 📂 Repository Structure

| Branch | Path | Description |
|--------|------|-------------|
| **main** | `.gitignore` | Python ignore file |
| **kubernetes-test-app** | `Dockerfile` | Builds Flask app container |
| | `app.py` | Flask backend with greeting form |
| | `templates/index.html` | HTML frontend |
| | `static/style.css` | CSS styles |
| | `deployment.yml` | Deployment with 2 replicas, resources, port 5000 |
| | `service.yml` | NodePort Service to expose app |
| | `requirements.txt` | Dependencies (Flask) |
| **nginx-pod-deployment** | `NGINX-POD/nginx-pod.yml` | Pod manifest (Nginx, port 80) |
| | `NGINX-POD/nginx-service.yml` | Service exposing pod on port 80 |
| | `README.md` | Branch README with setup + usage |

---

## ⚙️ How It Works

### Kubernetes Test App (`kubernetes-test-app`)
- **Containerisation:** `Dockerfile` uses Python 3.9, copies files, installs Flask, sets `app.py` entrypoint.  
- **Web Application:** `app.py` defines GET/POST route. Submitting a name returns a personalised greeting.  
- **Deployment:** `deployment.yml` creates a Deployment with two replicas, labels, resource limits, port 5000.  
- **Service Exposure:** `service.yml` defines a NodePort Service mapping external port → container port.  
- **Usage:** Build & push image, start Minikube, deploy with `kubectl apply -f`, then `minikube service kubernetes-test-app --url`.

### Nginx Pod Deployment (`nginx-pod-deployment`)
- **Environment Setup:** Follow README for `kubectl` + Minikube installation.  
- **Create Pod:** `nginx-pod.yml` runs Nginx with limits. Apply via `kubectl apply -f`.  
- **Expose Pod:** `nginx-service.yml` creates a NodePort Service exposing port 80.  
- **Access & Cleanup:** Use `minikube service nginx-service --url` for external URL. Delete pod & service after use.

---

## ▶️ Running the Examples

1. Clone repo:
   ```bash
   git clone https://github.com/PrakashD2003/KUBERNETES-STUDY.git
   cd KUBERNETES-STUDY
   ```

2. Checkout a branch:

   ```bash
   git checkout kubernetes-test-app   # Flask example
   git checkout nginx-pod-deployment  # Nginx example
   ```

3. Install dependencies: Docker, `kubectl`, Minikube.

4. Start Minikube:

   ```bash
   minikube start
   ```

5. Deploy resources:

   * Flask app:

     ```bash
     kubectl apply -f Kubernetes-test-app/deployment.yml
     kubectl apply -f Kubernetes-test-app/service.yml
     minikube service kubernetes-test-app --url
     ```
   * Nginx pod:

     ```bash
     kubectl apply -f NGINX-POD/nginx-pod.yml
     kubectl apply -f NGINX-POD/nginx-service.yml
     minikube service nginx-service --url
     ```

---

## 📊 Key Learnings

* **Containerisation with Docker** – building Python/Flask image with Dockerfile
* **Kubernetes resources** – Pods, Deployments, Services; scaling via replicas; NodePort exposure
* **Imperative vs Declarative** – `kubectl run/apply` vs YAML manifests
* **Local clusters with Minikube** – quick Kubernetes testing


---

## 🙌 Closing Notes

This repo is an evolving collection of **Kubernetes experiments**.
Feel free to open issues or PRs with suggestions or improvements.
Contributions are welcome!

👉 [View Repository on GitHub](https://github.com/PrakashD2003/KUBERNETES-STUDY)

```


