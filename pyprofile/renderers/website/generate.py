import logging
import os

from pyprofile.transformers.website import cv, index

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def set_up_html_dir(html_dir):
    if not os.path.exists(html_dir):
        os.makedirs(html_dir)
    os.system(f"cp -r pyprofile/transformers/website/_source/* {html_dir}")


def save_html(html, filename):
    fd = open(filename, "w")
    fd.write(html)
    fd.close()


def main(profile, website_save_dir):
    logger.info(f"Generating tex cv in '{website_save_dir}'")

    set_up_html_dir(website_save_dir)

    menu_items = {
        'cv': 'cv.html',
        'git': profile['basic_details']['git'],
        'linkedin': profile['basic_details']['linkedin'],
        'misc': '#'
    }
    index_html = index.generate_html(profile, menu_items)
    save_html(index_html, f"{website_save_dir}/index.html")

    cv_html = cv.generate_html(profile)
    save_html(cv_html, f"{website_save_dir}/src/cv-body.html")

    logger.info(f"Output saved to '{website_save_dir}'")
