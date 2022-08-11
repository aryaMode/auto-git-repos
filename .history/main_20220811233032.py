from email.mime import base
import os
from github import Github
import subprocess
from configparser import ConfigParser

def readConfig():
    file = "config.ini"
    config = ConfigParser()
    config.read(file)

    return config["GitHub API"]["token"]


def get_dics():
    dics = [(name) for name in os.listdir(".") if (
        os.path.isdir(name) and name[0] != '.')]
    return dics


def create_remote_repo(token, repo_name, base_working_dir):

    g = Github(token)
    user = g.get_user()
    repo = user.create_repo(repo_name, private=False)
    repo_url = repo.git_url.replace("git://", "https://")
    repo_dir = os.path.join(base_working_dir, repo_name)

    os.chdir(repo_dir)
    subprocess.call(['git', 'init'])
    subprocess.call(['git', 'add', '.'])
    subprocess.call(['git', 'commit', '-m', '{}'.format("my_first_commit")])
    subprocess.call(['git', 'branch', '-M', 'main'])
    subprocess.call(['git', 'remote', 'add', 'origin', '{}'.format(repo_url)])
    subprocess.call(['git', 'push', '-u', 'origin', 'main'])


