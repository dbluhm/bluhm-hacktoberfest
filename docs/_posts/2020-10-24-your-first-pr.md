---
layout: post
title: Your First Pull Request
date: 2020-10-24 16:26 -0400
---

This post will walk you through your first Pull Request for Hacktoberfest!

You can do this with me (Daniel -- I have slides that might help you through
this process if this is your first time) or on your own.

## Outline

1. What is Git?
2. Set up a GitHub account.
3. Sign up for Hacktoberfest.
4. Fork the project repository.
5. Set up Git Kraken.
6. Create new participant entry.
7. Open pull request.

## 1. What is Git?

Git is a version control system. It helps you collaborate on projects with
others or even just manage your own work. Git achieves this by keeping track of
changes made to files inside of a Git repository.

So, instead of creating a named versions of files ("My sociology paper", "My
sociology paper final version", "My sociology paper actually final version", "My
sociology paper final final FINAL version", etc.), git takes care of it all for
you (with some hints from you, the user).

Because git keeps track of your file versions, it makes it easy for you and your
collaborators to work on the same project, or even the same file, in parallel
and merge these changes back together automatically.

### Key terms

These definitions will probably come in handy throughout this walk-through.

- **Git:** A version control system.
- **Git repository:** A folder containing files managed by git + the `.git`
  folder that git uses to store its own files.
- **Commit:** A snapshot of the state of your git project.
- **Git history:** A stream of commits (snapshots of state) of your project. Your
  git history forms a timeline of changes for all of your files.
- **Branch:** A branch is a parallel version of a git repository. It is used to
  keep track of changes separate from the main copy of your work. If you think
  of your git history as a timeline, a branch would be a branch off of that
  timeline at a specific point in history that runs parallel to the original
  timeline. Think _Back to the Future_!
- **Merge:** A merge is taking changes from one branch and merging them into
  another to combine the changes of both branches.
- **Fork:** A fork is a copy of a git repository. On GitHub, forks are used to
  give individuals their own timeline to work from on a project while also
  giving them a way to get new code from the main repository and to contribute
  code back into the main repository.
- **Pull request:** A pull request is the way GitHub enables contributing back
  to the main repository from a fork.

## 2. Set up a GitHub Account

In order to participate in Hacktoberfest, you first need to create a GitHub
account if you haven't already.

You can do this by going to [Github](https://github.com) and registering in the
form:

![Github website]({{site.baseurl}}/assets/images/github_signup.png)

## 3. Sign up for Hacktoberfest

Go to [Hacktoberfest](https://hacktoberfest.digitalocean.com/) and click "Start
Hacking:"

![Hacktoberfest website]({{site.baseurl}}/assets/images/hacktoberfest_start_hacking.png)

And authorize Hacktoberfest to access your GitHub account.

## 4. Fork the project repository.

Navigate to the [project repository](https://github.com/dbluhm/bluhm-hacktoberfest)
and press the **fork** button.

![The fork button is located in the top right of the
page]({{site.baseurl}}/assets/images/fork_button.jpeg)

## 5. Set up Git Kraken

### Getting the Git Kraken Client

Follow [this link](https://www.gitkraken.com/invite/96o3BqpL) and press **Sign
up free**.

![]({{site.baseurl}}/assets/images/gk_signup.png)

On the next page, press **Sign in with GitHub**.

![]({{site.baseurl}}/assets/images/gk_signin.png)

Then click **Download for Free**.

![]({{site.baseurl}}/assets/images/gk_download.png)

And select the appropriate client for your operating system.

![]({{site.baseurl}}/assets/images/gk_client_download.png)

### Setting up Git Kraken Client

After downloading and installing Git Kraken, you will again be prompted to
**Sign in with GitHub**.

After sign in, you will be prompted to start a free trial of Git Kraken Pro.
Ignore this and just press **Not now, thanks** below the big green button.

### Clone Project Repository

Cloning the repository will make it available on your computer for editing and
viewing.

Press **Clone a repo**.

![]({{site.baseurl}}/assets/images/gk_clone.png)

Select a directory on your computer where the project will be cloned. I am
personally fond of creating a `dev` sub-folder in my `home` directory where I
keep all of my Git projects.

For the **URL**, use the URL of your fork of the Hacktoberfest repository.

![]({{site.baseurl}}/assets/images/gk_clone_dialog.png)

After cloning, you should see the following banner (the text will differ). Press
**Open Now**.

![]({{site.baseurl}}/assets/images/gk_clone_successful.png)

### Add Upstream Remote Repository

Next we will add a remote. This gives us a reference to the original project
repository.

Press the green plus sign that appears when hovering over **REMOTE** in the
left-side menu.

![]({{site.baseurl}}/assets/images/gk_remote_add.png)

Select `dbluhm/bluhm-hacktoberfest` from the **GitHub Repo** drop down menu and
put `upstream` in the **Name** input field. Then, click **Add Remote**.

## 6. Create New Participant Entry

We're now going to create a new branch and make some changes that we'll later
turn into our first Pull Request.

Press the **Branch** button at the top of the Git Kraken window.

Enter something like "add-participant" for in the box with placeholder text
**enter branch name**.

![]({{site.baseurl}}/assets/images/gk_branch.png)

In an editor of your choice ([Atom][atom], [Sublime][sublime], and [VS
Code][vscode] are some good, popular code editors), open up the
`bluhm-hacktoberfest/docs/_participants` folder. Copy `daniel.md` to
`YOUR_NAME_HERE.md`.

Open up `YOUR_NAME_HERE.md` and using the text already
present as a template, fill it out with your name, interests, favorite color,
etc. and write some content to answer the question "Why are you excited about
Hacktoberfest?" in the section after the second `---`.

### Commit your changes

Return to Git Kraken. At the top of right-side menu, you should now see a status
message saying something to the effect of "1 file changed in working directory".

Click **View changes**.

![]({{site.baseurl}}/assets/images/gk_view_changes.png)

Press **Stage all changes** to prepare all of your changes for committing.

![]({{site.baseurl}}/assets/images/gk_stage.png)

Write something descriptive in the **Summary** input like "Add YOUR_NAME_HERE to
participants."

![]({{site.baseurl}}/assets/images/gk_commit.png)

And finally, press **Commit changes to 1 file**.

![]({{site.baseurl}}/assets/images/gk_commit_ready.png)

[atom]: https://atom.io
[sublime]: https://www.sublimetext.com
[vscode]: https://code.visualstudio.com

## 7. Open Pull Request

At the top of Git Kraken, press the **Push** button.

Leave the default and press **Submit**.

![]({{site.baseurl}}/assets/images/gk_push.png)

Next, navigate to the [project repository](https://github.com/dbluhm/bluhm-hacktoberfest)
and click the **Pull requests** tab.

You should see a banner in yellow across the top prompting you to open a pull
request for the branch you just pushed to your fork. Follow the prompt.

Type a good summary and description and then hit **Submit**. And you're done!

I (Daniel) will review the PR and help you make any further modifications that
need to be made and then merge your changes into the main repository.
