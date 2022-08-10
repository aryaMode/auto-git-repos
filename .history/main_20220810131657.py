import os
from github import Github
import subprocess


def get_dics():
    dics = [(name) for name in os.listdir(".") if (
        os.path.isdir(name) and name[0] != '.')]
    return dics


def create_remote_repo(repo_name):

    g = Github(input("Enter Github Token: "))
    user = g.get_user()
    repo = user.create_repo(repo_name, private=False)
    repo_url = repo.git_url.replace("git://", "https://")
    repo_dir = os.path.join(os.getcwd(), repo_name)

    os.chdir(repo_dir)
    subprocess.call(['git', 'init'])
    subprocess.call(['git', 'add', '.'])
    subprocess.call(['git', 'commit', '-m', '{}'.format("my_first_commit")])
    subprocess.call(['git', 'branch', '-M', 'main'])
    subprocess.call(['git', 'remote', 'add', 'origin', '{}'.format(repo_url)])
    subprocess.call(['git', 'push', '-u', 'origin', 'main'])


dics = get_dics()

operation = input(
    "1. Single Repository\n2. All Repositories\nEnter your choice: ")
print()

if operation == "1":

    for dicIn in range(len(dics)):
        print(str(dicIn+1) + ".", dics[dicIn])
        print()

    dic = dics[(int(input("Choose a repository: ")))-1]

    print("\nSelected Repository: " + dic, "\n")

    create_remote_repo(dic)

if operation == "2":
    for dic in dics:
        create_remote_repo