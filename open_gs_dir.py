import sys
import urllib.parse
import os
import subprocess

GOOGLE_CLOUD_URL='"https://console.cloud.google.com/storage/browser/{path};tab=objects?project={project}&prefix=&forceOnObjectsSortingFiltering==false"'

DEFAULT_PROJECT_NAME=''

CHROME_URL = '"<path_to_chrome>/chrome.exe" --profile-directory="<chrome_profile_number>" {}'

def strip_gs_url(url):
    url = url.replace('gs://', '')
    url = urllib.parse.quote(url, safe=':, /')
    return url

def get_project(env):
    match env:
        case 'dev':
            return '<dev_project_name>'
        case 'prod':
            return '<prod_project_name'
        case _:
            return env

if __name__ == '__main__':
    if(len(sys.argv) < 2):
        print('Please enter valid gs url')
        sys.exit()

    stripped_url = strip_gs_url(sys.argv[1])
    project = DEFAULT_PROJECT_NAME if len(sys.argv) <= 2 else get_project(sys.argv[2])

    gurl = GOOGLE_CLOUD_URL.format(path=stripped_url, project=project)

    subprocess.run(CHROME_URL.format(gurl), capture_output=True)

