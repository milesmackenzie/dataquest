# Cloning repo chatbot from /dataquest/user/git/chatbot  to
# /home/dq/chatbot

/home/dq$ git clone /dataquest/user/git/chatbot
Cloning into 'chatbot'...
done.
/home/dq$ cd chatbot/

# Creating branch feature/king-bot and switching to branch.

/home/dq/chatbot$ git branch feature/king-bot
/home/dq/chatbot$ git checkout feature/king-bot
Switched to branch 'feature/king-bot'

# Editing bot.py to print a statement.
# Commiting changes.

/home/dq/chatbot$ nano bot.py
/home/dq/chatbot$ git add bot.py
/home/dq/chatbot$ git commit -m "update"
[feature/king-bot 0a94ddf] update
 1 file changed, 2 insertions(+), 1 deletion(-)

 # Switching to master branch, creating a branch feature/queen-bot.
 # Editing bot.py in the feature/queen-bot branch to pring a separate statement.
 # Commiting changes.
/home/dq/chatbot$ git checkout master
Switched to branch 'master'
Your branch is up-to-date with 'origin/master'.
/home/dq/chatbot$ git branch feature/queen-bot
/home/dq/chatbot$ git checkout feature/queen-bot
Switched to branch 'feature/queen-bot'
/home/dq/chatbot$ nano bot.py
/home/dq/chatbot$ git add bot.py
/home/dq/chatbot$ git commit -m "update2"
[feature/queen-bot 1be32a2] update2
 1 file changed, 2 insertions(+), 1 deletion(-)

# Attempting to merge feature/king-bot into master.
# Getting conflict and aborting merge.

/home/dq/chatbot$ git merge feature/king-bot
Auto-merging bot.py
CONFLICT (content): Merge conflict in bot.py
Automatic merge failed; fix conflicts and then commit the result.
/home/dq/chatbot$ git merge feature/queen-bot
error: 'merge' is not possible because you have unmerged files.
hint: Fix them up in the work tree,
hint: and then use 'git add/rm <file>' as
hint: appropriate to mark resolution and make a commit,
hint: or use 'git commit -a'.
fatal: Exiting because of an unresolved conflict.
/home/dq/chatbot$ git merge --abort

# Fixing merge conflicts, commiting changes and pushing to remote.

/home/dq/chatbot$ git checkout master
Switched to branch 'master'
Your branch is up-to-date with 'origin/master'.
/home/dq/chatbot$ git merge feature/queen-bot
Updating 7f60551..1be32a2
Fast-forward
 bot.py | 3 ++-
 1 file changed, 2 insertions(+), 1 deletion(-)
/home/dq/chatbot$ echo "print('I am the queen')" > bot.py
/home/dq/chatbot$ git add bot.py
/home/dq/chatbot$ git commit -m "Fixed conflicts"
[master 35145b0] Fixed conflicts
 1 file changed, 1 insertion(+), 3 deletions(-)
/home/dq/chatbot$ git push origin master
Counting objects: 8, done.
Delta compression using up to 36 threads.
Compressing objects: 100% (5/5), done.
Writing objects: 100% (6/6), 600 bytes | 0 bytes/s, done.
Total 6 (delta 0), reused 0 (delta 0)
To /dataquest/user/git/chatbot
   7f60551..35145b0  master -> master

# Creating branch feature/random-printing and editing bot.py
# to print several lines.
# Commiting changes.

/home/dq/chatbot$ git checkout master
Already on 'master'
Your branch is up-to-date with 'origin/master'.
/home/dq/chatbot$ git branch feature/random-printing
/home/dq/chatbot$ git checkout feature/random-printing
Switched to branch 'feature/random-printing'
/home/dq/chatbot$ nano bot.py
# Code added:
"""
for i in range(0,3):
    print ("statement")
for i in range(0,3):
    print ("statement2")
"""
/home/dq/chatbot$ git add bot.py
/home/dq/chatbot$ git commit -m "block"
[feature/random-printing 2d0d69e] block
 1 file changed, 4 insertions(+), 1 deletion(-)

 # Creating branch feature/dice-roller and editing bot.py
 # that prints two random numbers.
 # Commiting changes.

/home/dq/chatbot$ git checkout master
Switched to branch 'master'
Your branch is up-to-date with 'origin/master'.
/home/dq/chatbot$ git branch feature/dice-roller
/home/dq/chatbot$ git checkout feature/dice-roller
Switched to branch 'feature/dice-roller'
/home/dq/chatbot$ nano bot.py
# Code added:
"""
import random

for i in range(0,2):
    print (random.randint(0,10))
"""
/home/dq/chatbot$ git add bot.py
/home/dq/chatbot$ git commit -m "numbers"
[feature/dice-roller 3c783e9] numbers
1 file changed, 4 insertions(+), 1 deletion(-)

# Merging feature/random-printing and feature/dice-roller.
# Getting conflict and resolving conflict.
# Commiting resolved multi-line conflict.
# Pushing to remote.

/home/dq/chatbot$ git checkout master
Switched to branch 'master'
Your branch is up-to-date with 'origin/master'.
/home/dq/chatbot$ git merge feature/random-printing
Updating 35145b0..2d0d69e
Fast-forward
 bot.py | 5 ++++-
 1 file changed, 4 insertions(+), 1 deletion(-)
/home/dq/chatbot$ git merge feature/dice-roller
Auto-merging bot.py
CONFLICT (content): Merge conflict in bot.py
Automatic merge failed; fix conflicts and then commit the result.
/home/dq/chatbot$ nano bot.py
/home/dq/chatbot$ git add bot.py
/home/dq/chatbot$ git commit -m "Resolved multi-line conflict"
[master 57a1f8f] Resolved multi-line conflict
/home/dq/chatbot$ git push origin master
Counting objects: 11, done.
Delta compression using up to 36 threads.
Compressing objects: 100% (9/9), done.
Writing objects: 100% (9/9), 863 bytes | 0 bytes/s, done.
Total 9 (delta 2), reused 0 (delta 0)
To /dataquest/user/git/chatbot
   35145b0..57a1f8f  master -> master

# More practice with resolving multiple conflicts.


/home/dq/chatbot$ git branch feature/more-printing
/home/dq/chatbot$ git checkout feature/more-printing
Switched to branch 'feature/more-printing'
/home/dq/chatbot$ nano bot.py
# Code:
"""
def maskify(cc):
    if len(cc) < 4:
      return cc
    return '#' * (len(cc)-4) + cc[-4:]


n = "453678430293834764647564848rhdhfbfhrw7474768wyr"
print (maskify(n))
"""
/home/dq/chatbot$ python bot.py
statement
statement
statement
statement2
statement2
statement2
2
4
###########################################8wyr
/home/dq/chatbot$ git add bot.py
/home/dq/chatbot$ git commit -m "Added lines"
[feature/more-printing 20226a8] Added lines
 1 file changed, 9 insertions(+)


/home/dq/chatbot$ git checkout master
Switched to branch 'master'
Your branch is up-to-date with 'origin/master'.
/home/dq/chatbot$ git branch feature/more-printing-2
/home/dq/chatbot$ git checkout feature/more-printing-2
Switched to branch 'feature/more-printing-2'
/home/dq/chatbot$ nano bot.py
# Code added :
"""
def returns(holdings, percent, days):
    total = holdings
    percent = percent + 1
    count = 0
    while count < days:
        total = (total * percent)
        count += 1
    return total - holdings
print (returns(10000, 0.0033, 365))
"""
/home/dq/chatbot$ python bot.py
statement
statement
statement
statement2
statement2
statement2
0
10
23284.83971591483
/home/dq/chatbot$ git add bot.py
/home/dq/chatbot$ git commit -m "Added liness"
[feature/more-printing-2 fcbdf7e] Added liness
 1 file changed, 10 insertions(+)
/home/dq/chatbot$ git checkout master
Switched to branch 'master'
Your branch is up-to-date with 'origin/master'.
/home/dq/chatbot$ git merge feature/more-printing
Updating 57a1f8f..20226a8
Fast-forward
 bot.py | 9 +++++++++
 1 file changed, 9 insertions(+)
/home/dq/chatbot$ git merge feature/more-printing-2
Auto-merging bot.py
CONFLICT (content): Merge conflict in bot.py
Automatic merge failed; fix conflicts and then commit the result.
/home/dq/chatbot$ nano bot.py
/home/dq/chatbot$ git add bot.py
/home/dq/chatbot$ git commit -m "Resolved multiple conflicts"
[master 7f75c5b] Resolved multiple conflicts
/home/dq/chatbot$ git push origin master
Counting objects: 11, done.
Delta compression using up to 36 threads.
Compressing objects: 100% (9/9), done.
Writing objects: 100% (9/9), 1.01 KiB | 0 bytes/s, done.
Total 9 (delta 3), reused 0 (delta 0)
To /dataquest/user/git/chatbot
   57a1f8f..7f75c5b  master -> master

# Creating two branches, one removing bot.py and one editing bot.py.
# Resolving conflict but using git checkout --theirs . to keep bot.py.
# Pushing changes to remote.

/home/dq/chatbot/home/dq/chatbot$ git checkout master
Already on 'master'
Your branch is up-to-date with 'origin/master'.
/home/dq/chatbot$ git branch feature/remove-bot
/home/dq/chatbot$ git checkout feature/remove-bot
Switched to branch 'feature/remove-bot'
/home/dq/chatbot$ git rm bot.py
rm 'bot.py'
/home/dq/chatbot$ git add .
/home/dq/chatbot$ git commit -m "Remove bot"
[feature/remove-bot 7c7301e] Remove bot
 1 file changed, 5 deletions(-)
 delete mode 100755 bot.py
/home/dq/chatbot$ git checkout master
Switched to branch 'master'
Your branch is up-to-date with 'origin/master'.
/home/dq/chatbot$ git branch feature/keep-bot
/home/dq/chatbot$ git checkout feature/keep-bot
Switched to branch 'feature/keep-bot'
/home/dq/chatbot$ nano bot.py
/home/dq/chatbot$ git add bot.py
/home/dq/chatbot$ git commit -m "Keeping bot.py"
[feature/keep-bot a9ba5f9] Keeping bot.py
 1 file changed, 2 insertions(+), 1 deletion(-)
/home/dq/chatbot$ git checkout master
Switched to branch 'master'
Your branch is up-to-date with 'origin/master'.
/home/dq/chatbot$ git merge feature/remove-bot
Updating f4ce530..7c7301e
Fast-forward
 bot.py | 5 -----
 1 file changed, 5 deletions(-)
 delete mode 100755 bot.py
/home/dq/chatbot$ git merge feature/keep-bot
CONFLICT (modify/delete): bot.py deleted in HEAD and modified in feat
ure/keep-bot. Version feature/keep-bot of bot.py left in tree.
Automatic merge failed; fix conflicts and then commit the result.
/home/dq/chatbot$ git checkout --theirs .
/home/dq/chatbot$ git add .
/home/dq/chatbot$ git commit -m "Keeping bot.py"
[master 8ab31d7] Keeping bot.py
/home/dq/chatbot$ git push origin master
Counting objects: 8, done.
Delta compression using up to 36 threads.
Compressing objects: 100% (5/5), done.
Writing objects: 100% (6/6), 571 bytes | 0 bytes/s, done.
Total 6 (delta 3), reused 0 (delta 0)
To /dataquest/user/git/chatbot
   f4ce530..8ab31d7  master -> master

# Adding line DS_Store and *.pyc to gitignore.

/home/dq/chatbo/home/dq/chatbot$ git checkout master
Already on 'master'
Your branch is up-to-date with 'origin/master'.
/home/dq/chatbot$ printf ".DS_Store\n*.pyc" > gitignore
/home/dq/chatbot$ git add .
/home/dq/chatbot$ git commit -m "Added gitignore"
[master 1450d72] Added gitignore
 1 file changed, 2 insertions(+)
 create mode 100644 gitignore
/home/dq/chatbot$ git push origin master
Counting objects: 4, done.
Delta compression using up to 36 threads.
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 322 bytes | 0 bytes/s, done.
Total 3 (delta 0), reused 0 (delta 0)
To /dataquest/user/git/chatbot
   f5fe1c2..1450d72  master -> master ter

# Removing cached bot.py, commiting changes and pushing to remote.

/home/dq/chatb/home/dq/chatbot$ git checkout master
Already on 'master'
Your branch is up-to-date with 'origin/master'.
/home/dq/chatbot$ git rm --cached bot.py
rm 'bot.py'
/home/dq/chatbot$ git commit -m "Removed bot.py"
[master d76277a] Removed bot.py
 1 file changed, 6 deletions(-)
 delete mode 100755 bot.py
/home/dq/chatbot$ git push origin master
Counting objects: 3, done.
Delta compression using up to 36 threads.
Compressing objects: 100% (2/2), done.
Writing objects: 100% (2/2), 217 bytes | 0 bytes/s, done.
Total 2 (delta 1), reused 0 (delta 0)
To /dataquest/user/git/chatbot
   c845ffb..d76277a  master -> master      master -> master
