# Random Joke with Python and Docker 

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Docker](https://img.shields.io/badge/Docker-20.10%2B-blue)
![License: MIT](https://img.shields.io/badge/License-MIT-green)

This Python project uses JokeAPI to display a random joke. Thanks to Docker, it ensures optimal portability and reproducibility.

## Project Objective

### Motivation
Facilitate API exploration while learning how to use Docker containers for simple and efficient deployments.

### Problem Solved
This project demonstrates how to integrate a public API into a Python application and containerize it to ensure it runs smoothly on any machine.

## Table of Contents
1. Features
2. Installation and Usage
   - Local Execution
   - Docker Execution
3. Example Output
4. License
5. Useful links

## Features
- Fetches a random joke (either one-liner or two-part) using JokeAPI.
- Can be run locally or within a Docker container.
- Portable and easy to share via a Dockerized environment.

## Installation and Usage

### Local Execution
1. Clone the repository :
   ```bash
   git clone https://github.com/your-username/ue19-lab-05.git
   cd ue19-lab-05

2. Install the dependencies :
   ```bash
   pip install -r requirements.txt
3. Run the application :
   ```bash
   python app.py

### Docker Execution

1. Ensure Docker is installed on your machine.
2. Build the Docker image :
   ```bash
   docker build -t blague-app .
3. Run the container :
   ```bash
   docker run --rm blague-app

---

## Example Output

Question: Why do programmers prefer coffee?

Answer: Because it contains Java.

---

## License

This project is licensed under the MIT License.

---

## Useful Links

- JokeAPI Documentation : https://jokeapi.dev/
- Docker Official Documentation : https://docs.docker.com/
- Python Official Documentation : https://docs.python.org/3/

---

## Author

Alviamp