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
| LaTeX CV         | Done        |
| Website          | Done        |
| LinkenIn         | Not Started |

# ToDo
- reduce older exp
- fill out current exp
- update readme post-refactor
- move personal info to own repo, generalise this one
- add website background argument
- update readme
- integrate linkedin target
