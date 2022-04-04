# syntax=docker/dockerfile:1
FROM debian:buster
RUN apt update -y
RUN apt upgrade -y
RUN apt install chromium -y
RUN apt install npm -y
RUN npm update -g

ENV PUPPETEER_SKIP_CHROMIUM_DOWNLOAD=1
ENV PUPPETEER_EXECUTABLE_PATH=/usr/bin/chromium-browser
ENV RESUME_PUPPETEER_NO_SANDBOX=1
RUN npm install -g resume-cli --unsafe-perm=true --allow-root
RUN ln /usr/bin/chromium /usr/bin/chromium-browser

ARG THEME
ENV THEME=$THEME
WORKDIR /resume
COPY Makefile Makefile
RUN npm install jsonresume-theme-${THEME}
RUN npm install -g jsonresume-theme-${THEME}
RUN mkdir build


