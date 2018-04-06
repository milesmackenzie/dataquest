/home/dq$ git clone /dataquest/user/git/chatbot
Cloning into 'chatbot'...
done.

# Updating README.md to say: This project needs no installation
# Adding README.md to staging area and commiting to repo.

/home/dq$ cd chatbot
/home/dq/chatbot$ nano README.md
/home/dq/chatbot$ git add README.md
/home/dq/chatbot$ git commit -m "Updated README.md"
[master 68ef0a6] Updated README.md
 1 file changed, 2 insertions(+), 1 deletion(-)
/home/dq/chatbot$ git status
On branch master
Your branch is ahead of 'origin/master' by 1 commit.
  (use "git push" to publish your local commits)

nothing to commit, working directory clean

# Using git branch to see all of the branches that exist in the chatbot repo.

/home/dq/chatbot$ git branch
* master

# Pushing the master branch of the local chatbot repo to the remote origin.

/home/dq/chatbot$ git push origin master
Counting objects: 5, done.
Delta compression using up to 36 threads.
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 307 bytes | 0 bytes/s, done.
Total 3 (delta 1), reused 0 (delta 0)
To /dataquest/user/git/chatbot
   73c2d12..68ef0a6  master -> master

# Using git log to find most recent commit hash.

/home/dq/chatbot$ git log
commit ed292ff4cdac9e84e9cb8af157230148a4fb601a
Author: Dataquest <me@dataquest.io>
Date:   Thu Apr 5 18:22:08 2018 +0000

    Updated README.md

commit ba7832b369edb4659c7e8b5b229ef1d1de3bac90
Author: Dataquest <me@dataquest.io>
Date:   Thu Apr 5 18:22:07 2018 +0000

    Add the initial version of README.md

# Using git show to to see what the commit did.

/home/dq/chatbot$ git show
commit ed292ff4cdac9e84e9cb8af157230148a4fb601a
Author: Dataquest <me@dataquest.io>
Date:   Thu Apr 5 18:22:08 2018 +0000

Updated README.md

diff --git a/README.md b/README.md
index f4871de..c2efe6e 100755
--- a/README.md
+++ b/README.md
@@ -1,3 +1,3 @@
 README

-This is a README file.  Its typical for Github projects to have a R
EADME.  A README gives information about what the project is about, a
nd usually how to install and use it.
\ No newline at end of file

# Using git reset to reset the chatbot repo to the oldest commit.

/home/dq/chatbot$ git reset --hard $HASH
HEAD is now at ba7832b Add the initial version of README.md

# Pulling the latest commits from the chatbot repo.

/home/dq/chatbot$ git pull
Updating dc6f5ca..70bfaa6
Fast-forward
 README.md | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)

 # Using git reset with the HEAD variable to reset the chatbot
 # repo to the second most recent commit.

 /home/dq/chatbot$ git reset --hard HEAD~1
HEAD is now at dc6f5ca Add the initial version of README.md
/home/dq/chatbot$ git rev-parse HEAD
dc6f5caa7d0bc08bce3cfe580f4f5c2ff03a108c
