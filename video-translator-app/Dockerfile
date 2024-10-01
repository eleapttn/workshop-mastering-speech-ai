# 🐳 Base image
FROM python:3.11

# 👱 Set the working directory inside the container
WORKDIR /workspace

# 🐍 Copy all folder files (requirements.txt, python code, ...) into the /workspace folder
ADD . /workspace

# 📚 Install missing system packages and dependencies mentioned in the requirements.txt file
RUN apt-get update && apt-get install -y ffmpeg libsndfile1-dev
RUN pip install -r requirements.txt

# 🔑 Give correct access rights to the OVHcloud user
RUN chown -R 42420:42420 /workspace
ENV HOME=/workspace

# 🚀 Define the command to run the app, when the container is launched
CMD [ "python3" , "/workspace/main.py" ]  