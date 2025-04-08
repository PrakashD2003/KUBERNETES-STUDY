Here’s the updated `README.md` for your **Kubernetes Test App**, taking into account that:

- `index.html` is inside a `templates/` directory
- `style.css` is inside a `static/` directory

---

# 🚀 Kubernetes Test App

A simple Flask-based web application deployed on Kubernetes using Minikube.

---

## 🧾 Project Structure

```
.
├── app.py                   # Flask backend
├── templates/
│   └── index.html           # Frontend HTML
├── static/
│   └── style.css            # Frontend CSS
├── Dockerfile               # Docker image instructions
├── deployment.yml           # Kubernetes Deployment configuration
├── service.yml              # Kubernetes Service configuration
```

---

## 🛠️ Prerequisites

- Docker installed and running (e.g., Docker Desktop)
- Minikube installed
- kubectl installed
- Docker Hub account (to push the image)

---

## 🐳 Step 1: Create Docker Image

### 1. Create a Dockerfile

Create a `Dockerfile` in the project root:

```Dockerfile
# Use official Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy application files
COPY app.py .
COPY templates/ ./templates/
COPY static/ ./static/

# Install dependencies
RUN pip install flask

# Expose Flask default port
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]
```

### 2. Build the Docker Image

```bash
docker build -t prakash3112/kubernetes-test-app:v3 .
```

### 3. Push the Image to Docker Hub

> Be sure to login first: `docker login`

```bash
docker push prakash3112/kubernetes-test-app:v3
```

---

## ☸️ Step 2: Start Minikube

```bash
minikube start
```

(Optional: Add `--driver=docker` if needed)

---

## 📦 Step 3: Deploy on Kubernetes

### 1. Apply the Deployment

```bash
kubectl apply -f deployment.yml
```

### 2. Apply the Service

```bash
kubectl apply -f service.yml
```

---

## 🌐 Step 4: Access the App

### 1. Get Service URL

```bash
minikube service kubernetes-test-app --url
```

Open the URL shown in your browser to access the web app.

---

## 🧹 Cleanup

```bash
kubectl delete -f deployment.yml
kubectl delete -f service.yml
```

---

## 📄 File Summary

- `app.py`: Flask server that renders `index.html`
- `templates/index.html`: Frontend page rendered by Flask
- `static/style.css`: Styling for the webpage
- `Dockerfile`: Builds the container image
- `deployment.yml`: Runs 2 replicas of the app in a deployment
- `service.yml`: Exposes the app via NodePort for external access

---

Let me know if you'd like me to generate the `Dockerfile` as a file or anything else for deployment automation (e.g., a Makefile or shell script).