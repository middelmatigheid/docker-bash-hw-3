#!/bin/bash

case "$1" in
    build_generator)
        docker build -t generator -f Dockerfile.generator .
        ;;
    run_generator)
        docker run -v /${PWD}/data:/app/data generator
        ;;
    create_local_data)
        python generate.py ./local_data
        ;;
    
    build_reporter)
        docker build -t reporter -f Dockerfile.reporter .
        ;;
    run_reporter)
        docker run -v /${PWD}/data:/data reporter
        ;;

    structure)
        ls -laR
        ;;
    clear_data)
        rm -f data/*.csv 
        rm -f data/*.html 
        ;;
    inside_generator)
        docker run -v /${PWD}/data:/app/data generator
        docker run -v /${PWD}/data:/app/data generator ls -lah /app/data/
        ;;
    inside_reporter)
        docker run -v /${PWD}/data:/data reporter
        docker run -v /${PWD}/data:/data reporter ls -lah /data/
        ;;
esac