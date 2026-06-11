---
title: Toxic Detector
emoji: 🧪
colorFrom: blue
colorTo: green
sdk: docker
app_file: app.py
pinned: false
---

# Toxic Detector

FastAPI service for toxicity prediction.

## Hugging Face Spaces deployment

This repo is set up to deploy as a Hugging Face Docker Space.

### 1. Create the Space

1. Go to Hugging Face Spaces.
2. Click New Space.
3. Enter a name.
4. Choose Docker as the SDK.
5. Create the Space.

### 2. Push this repo to the Space

Clone the Space repo and copy these files into it:

- app.py
- model.py
- requirements.txt
- Dockerfile
- .dockerignore

Then push with git:

```bash
git add .
git commit -m "Add Hugging Face deployment"
git push
```

### 3. What the Space runs

The Dockerfile installs dependencies and starts Uvicorn on port 7860, which is the expected port for Spaces.

### 4. If the build is still too heavy

If the Space takes too long to start or runs out of memory, the main cause is the model load in model.py. The next fixes are:

1. use a smaller model
2. lazy-load the model on first request
3. move inference to a Hugging Face Inference Endpoint

### 5. Test locally

Run this before pushing:

```bash
docker build -t toxic-detector .
docker run -p 7860:7860 toxic-detector
```