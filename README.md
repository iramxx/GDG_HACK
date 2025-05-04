# Hocus Focus

Hocus Focus is an AI-powered educational game that helps users learn vocabulary and object recognition through interactive, image-based challenges.

## Project Overview

The game uses a Vision-Language Large Model (VLLM) to automatically detect and localize objects in any image. Players are shown the name of a hidden object and must click on it within the image. If they miss, the system provides visual hints by drawing circles that shrink with each attempt until the correct location is revealed.

This approach makes vocabulary learning more engaging by combining visual discovery with interactive feedback.

## Features

- AI-powered object detection and localization
- Interactive gameplay with progressive visual hints
- Dynamic image analysis powered by Google Vertex AI
- Backend integration with Django
- Frontend built with HTML, CSS, and JavaScript

## How It Works

1. An image is processed by the AI model to extract object names and coordinates.
2. One object is selected as the target for the player to find.
3. The user clicks on the image to guess the object’s location.
4. Each incorrect guess triggers a hint circle around the target.
5. After three misses, the correct object is revealed.

## Tech Stack

- Backend: Django
- Frontend: HTML, CSS, JavaScript (Canvas API)
- AI Model: Vision-Language Large Model (VLLM) on Google Vertex AI
- Deployment: Google Cloud Run
