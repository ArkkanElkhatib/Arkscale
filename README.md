# Arkscale
A lightweight web application that upscales low-resolution images using AI-based super-resolution models in Python.

This project was built to solve a common problem I encountered while working on side projects: very small images (e.g., 20x20 px icons) becoming unusable when scaled manually. Most free online tools were limited, unreliable, or restricted, so I built a simple, reproducible solution that performs high-quality image upscaling locally.

## Tech Stack
Python
Docker

### Python Libraries
Streamlit (UI layer)
Super-Image (super-resolution models)

## How It Works
1. User uploads a low-resolution image.
2. The image is processed using a super-resolution model from the super-image package.
3. The AI model reconstructs a higher-resolution version of the image.
4. The upscaled image is displayed and available for download.

The project focuses on making AI upscaling accessible through a simple and clean interface while keeping deployment straightforward.

## Local Deployment
1. Clone Repository
  - `git@github.com:ArkkanElkhatib/Arkscale.git && cd Arkscale`
2. Build Docker Container
  - `docker build -t arkscale .`
3. Deploy Container
  - `docker run -it -p 80:80 arkscale`
4. Visit application at `http://localhost:80/`
