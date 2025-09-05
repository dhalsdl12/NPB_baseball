from github import Github


def get_github_repo(access_token, repository_name):
    g = Github(access_token)
    return g.get_user().get_repo(repository_name)


def upload_github_issue(repo, title, body):
    repo.create_issue(title=title, body=body)
