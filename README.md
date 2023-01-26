# There are 2 docker images one for windows and second is linux based but the EveryDream2trainer
repo is compitable for windows

# Build a Docker file
docker build . -t windows:v1

#After the successfull build run the container and make sure that it has a open port 5000
docker run -it -d --name {container_name} -p 5000:5000 -v {add_directory_path}:/app windows:v1 bin/bash

# toggle to /app directory and run
python Flask_code/test.py





# EveryDream Trainer 2.0

Welcome to v2.0 of EveryDream trainer! Now with more diffusers and even more features!

[Companion tools](https://github.com/victorchall/EveryDream)

Please join us on Discord! https://discord.gg/uheqxU6sXN

If you find this tool useful, please consider subscribing to the project on [Patreon](https://www.patreon.com/everydream) or a one-time donation at [Ko-fi](https://ko-fi.com/everydream).

## Video tutorials

### [Basic setup and getting started](https://www.youtube.com/watch?v=OgpJK8SUW3c) 

Covers install, setup of base models, startning training, basic tweaking, and looking at your logs
### [Multiaspect and crop jitter](https://www.youtube.com/watch?v=0xswM8QYFD0)

Behind the scenes look at how the trainer handles multiaspect and crop jitter

### Tools repo

Make sure to check out the [tools repo](https://github.com/victorchall/EveryDream), it has a grab bag of scripts to help with your data curation prior to training.  It has automatic bulk BLIP captioning for BLIP, script to web scrape based on Laion data files, script to rename generic pronouns to proper names or append artist tags to your captions, etc. 

## Docs

[Setup and installation](doc/SETUP.md)

[Download and setup base models](doc/BASEMODELS.md) 

[Data Preparation](doc/DATA.md)

[Training](doc/TRAINING.md) - How to start training

[Basic Tweaking](doc/TWEAKING.md) - Important args to understand to get started

[Logging](doc/LOGGING.md) 

[Advanced Tweaking](doc/ATWEAKING.md) - More stuff to tweak once you are comfortable

[Chaining training sessions](doc/CHAINING.md) - Modify training parameters by chaining training sessions together end to end

[Shuffling Tags](doc/SHUFFLING_TAGS.md)

[Data Balancing](doc/BALANCING.md) - Includes my small treatise on model preservation with ground truth data
