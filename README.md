# Profile-As-Code
> A single source of truth for personal-development related stuff. 

## Purpose
In this repository exists my personal information (experience, projects, skills, etc.)
organised in [`yaml`](http://yaml.org/) files along side code to transform the information into different formats.

## Why?
I have found information on myself in different places getting out of sync, e.g. 
my CV compared to my Linkedin compared to my website. It was a bit of a faff keeping things 
in check and working out the place with the latest edits and improvements, so
this is an effort to limit the information to one source of truth. 

## Project Organisation
Yaml files containing my personal information live in the `/profile` directory. This is all information I'm comfortable having public.
Any private information I add to `.private.yml` which isn't committed to source control.

Python scripts live in the `pyprofile/` directory. These exist to parse the `yaml` files and convert them into useful forms.

Invoke the different transformations using the `Makefile`.

## Available Output Formats
| Format           | Status      |
|------------------|-------------|
| Single YAML file | Done        |
| LaTeX CV         | In progress |
| Website          | Todo        |

# ToDo
- add long descriptions and other experience from linkedin
- add ability to select experience, add key field?
- add full data, inc skills and skills to be developed
- tweak spacing in cv pdf
- add code to compile pdf, perhaps using docker
- add code to generate website - maybe even move this repo to twindebank.io
- have 'build' checks for validation
