"""
Release message body generator
"""

import os

import github


def create_release_body(repo, target_commitish="master"):
    """
    Takes in repo and target branch/commit for release, master is default.
    Gathers all commit messages created since the last release to be put into message body.
    Returns a string with these commit messages separated by bullet points.
    """

    latest_release_tag = repo.get_latest_release().tag_name

    commit_objects = repo.compare(latest_release_tag, target_commitish).commits
    commit_message_list = [
        "* " + commit_object.commit.message for commit_object in commit_objects
    ]

    release_body = "\n".join(commit_message_list)

    if not release_body:
        release_body = "No previous commit messages to display"

    return release_body


if __name__ == "__main__":
    github_token = os.getenv("GITHUB_TOKEN")
    g = github.Github(github_token)
    repo = os.getenv("REPO")
    github_repo = g.get_user().get_repo(repo)

    print(create_release_body(repo))
