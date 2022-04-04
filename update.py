import json
import os
from pathlib import Path

import requests


def transform(resume: dict) -> dict:
    resume['theme'] = 'actual'
    resume['basics']['email'] = os.environ['EMAIL']
    resume['basics']['phone'] = os.environ['PHONE']
    resume['skills'] = []
    resume['basics']['profiles'] = resume['basics']['profiles'][1:]
    resume['work'] = resume['work'][:6]
    resume['languages'] = None
    resume['basics']['picture'] = ''
    resume['volunteer'] = []
    return resume


def main():
    raw = requests.get("https://gitconnected.com/v1/portfolio/twindebank")
    data = raw.json()
    build_dir = Path('build')
    build_dir.mkdir(exist_ok=True)
    (build_dir / 'resume.json').write_text(json.dumps(transform(data), indent=2))


if __name__ == "__main__":
    main()
