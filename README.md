# About the project

It's an uni homework for exercising with Docker and Bash

# Downloading the project

To download the project open terminal and use commands

```bash
git clone https://github.com/middelmatigheid/docker-bash-hw-3.git
cd docker-bash-hw-3
```

# Commands

### Generator

Building generator's image

```bash
./run.sh build_generator
```

Running the generator

```bash
./run.sh run_generator
```

Running the generator and checking that container can see the data

```bash
./run.sh inside_generator
```

Creating local data for local debugging

```bash
./run.sh create_local_data
```

### Reporter

Building reporter's image

```bash
./run.sh build_reporter
```

Running the reporter

```bash
./run.sh run_reporter
```

Running the reporter and checking that container can see the data

```bash
./run.sh inside_reporter
```

### Additional

Getting project's structure

```bash
./run.sh structure
```

Clearing the data folder

```bash
./run.sh clear_data
```

# Project structure

```bash
docker-bash-hw-3/
├── generator.py                
├── Dockerfile.generator        
├── package.json                
├── report.js
├── Dockerfile.reporter
└── run.sh
```
