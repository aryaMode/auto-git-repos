import os
from github import Github
import subprocess
from configparser import ConfigParser

# TODO: Make a working GUI with
# TODO: Make this a package and distribute

def readConfig():
    config = ConfigParser()
    path = '/'.join((os.path.abspath(__file__).replace('\\', '/')).split('/')[:-1])
    config.read(os.path.join(path, 'config.ini'))

    return config["accessToken"]["token"]


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


base_working_dir = os.path.join(os.getcwd())

dics = get_dics()

operation = input(
    "1. Single Repository\n2. All Repositories\nEnter your choice: ")
print()

token = readConfig()

if operation == "1":

    for dicIn in range(len(dics)):
        print(str(dicIn+1) + ".", dics[dicIn])
        print()

    dic = dics[(int(input("Choose a repository: ")))-1]

    print("\nSelected Repository: " + dic, "\n")

    create_remote_repo(token, dic, base_working_dir)

if operation == "2":
    for dic in dics:
        create_remote_repo(token, dic, base_working_dir)