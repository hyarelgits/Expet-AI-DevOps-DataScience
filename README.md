┌──────────────────────────────────────────────────────────────────────────────┐
│                         AI STUDENT MANAGEMENT SYSTEM                         │
└──────────────────────────────────────────────────────────────────────────────┘

                                   STUDENT
                                       │
                                       ▼
                         ┌────────────────────────┐
                         │  Web UI / Browser      │
                         │  (HTML,CSS,JS)         │
                         └──────────┬─────────────┘
                                    │ HTTP Request
                                    ▼
                         ┌────────────────────────┐
                         │      FastAPI App       │
                         │       app/main.py      │
                         └───────┬───────┬────────┘
                                 │       │
                    Prediction   │       │ AI Chat
                                 │       │
                                 ▼       ▼

                 ┌──────────────────┐   ┌─────────────────┐
                 │ ML Model         │   │ Ollama LLM      │
                 │ placement_model  │   │ llama3/mistral  │
                 │ joblib.load()    │   │ chatbot.py      │
                 └────────┬─────────┘   └────────┬────────┘
                          │                      │
                          └──────────┬───────────┘
                                     │
                                     ▼
                      ┌──────────────────────────┐
                      │ Prediction / AI Response │
                      └─────────────┬────────────┘
                                    │
                                    ▼
                      ┌──────────────────────────┐
                      │      REST API JSON       │
                      └─────────────┬────────────┘
                                    │
                                    ▼
                             USER OUTPUT


═══════════════════════════════════════════════════════════════════════════════
                            CONTAINERIZATION LAYER
═══════════════════════════════════════════════════════════════════════════════

                      ┌──────────────────────────┐
                      │      Dockerfile          │
                      └─────────────┬────────────┘
                                    │
                                    ▼
                      ┌──────────────────────────┐
                      │    Docker Image          │
                      │  hyareldocker1/app:v1   │
                      └─────────────┬────────────┘
                                    │
                                    ▼
                      ┌──────────────────────────┐
                      │     Docker Hub           │
                      └─────────────┬────────────┘
                                    │
                                    ▼

═══════════════════════════════════════════════════════════════════════════════
                           KUBERNETES PLATFORM
═══════════════════════════════════════════════════════════════════════════════

              ┌──────────────────────────────────────────┐
              │          Kubernetes Cluster             │
              └────────────────┬────────────────────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │     Deployment      │
                    │  student-app.yaml   │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │       Pod(s)        │
                    │  student-app-pod    │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │      Service        │
                    │    ClusterIP /      │
                    │    NodePort         │
                    └──────────┬──────────┘
                               │
                               ▼
                          End Users


═══════════════════════════════════════════════════════════════════════════════
                               DEVOPS PIPELINE
═══════════════════════════════════════════════════════════════════════════════

 Developer
     │
     ▼
┌──────────┐
│   Git    │
└────┬─────┘
     │ Push
     ▼
┌──────────┐
│ GitHub   │
└────┬─────┘
     │ Webhook
     ▼
┌──────────┐
│ Jenkins  │
│ Pipeline │
└────┬─────┘
     │
     ├── Build
     ├── Test
     ├── Docker Build
     ├── Docker Push
     ▼
┌──────────┐
│ ArgoCD   │
└────┬─────┘
     │ GitOps Sync
     ▼
┌──────────┐
│Kubernetes│
└──────────┘


═══════════════════════════════════════════════════════════════════════════════
                             MONITORING STACK
═══════════════════════════════════════════════════════════════════════════════

          Kubernetes
               │
      ┌────────┴────────┐
      ▼                 ▼
┌──────────┐      ┌──────────┐
│Prometheus│─────▶│Grafana   │
└──────────┘      └──────────┘


How to explain to learners in 30 seconds
Frontend sends request.
FastAPI receives request.
ML Model predicts placement probability.
Ollama LLM answers AI-related queries.
Application is packaged into a Docker Image.
Image is stored in Docker Hub.
Kubernetes runs and scales containers.
Jenkins automates build and deployment.
ArgoCD performs GitOps synchronization.
Prometheus + Grafana monitor the application.

This single diagram covers Python, ML, AI, Ollama, Docker, Kubernetes, Jenkins, GitOps, ArgoCD, Monitoring, and DevOps in one architecture view.
