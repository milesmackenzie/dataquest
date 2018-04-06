# Cloning /dataquest/user/git/chatbot.
# Creating a branch called more-speech and switching into that branch.

/home/dq$ git clone /dataquest/user/git/chatbot
Cloning into 'chatbot'...
done.
/home/dq$ cd chatbot/
/home/dq/chatbot$ git branch more-speech
/home/dq/chatbot$ git checkout more-speech
Switched to branch 'more-speech'
/home/dq/chatbot$ python bot.py
Hello, lets chat!

# Editing bot.py to print more output.
# Commiting changes.

/home/dq/chatbot$ nano bot.py
/home/dq/chatbot$ git add bot.py
/home/dq/chatbot$ git commit -m "Added more output"
[more-speech fdba754] Added more output
 1 file changed, 2 insertions(+), 1 deletion(-)

 # Pushing the more-speech branch to the remote origin.

/home/dq/chatbot$ git push origin more-speech
Counting objects: 5, done.
Delta compression using up to 36 threads.
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 341 bytes | 0 bytes/s, done.
Total 3 (delta 0), reused 0 (delta 0)
To /dataquest/user/git/chatbot
 * [new branch]      more-speech -> more-speech

 # Switching into master branch, merging more-speech into master and
 # pushing to remote repo.

 /home/dq/chatbot$ git checkout master
 Switched to branch 'master'
 Your branch is up-to-date with 'origin/master'.
 /home/dq/chatbot$ git merge more-speech
 Updating 634eeac..1ed0970
 Fast-forward
  bot.py | 3 ++-
  1 file changed, 2 insertions(+), 1 deletion(-)
 /home/dq/chatbot$ git push origin master
 Total 0 (delta 0), reused 0 (delta 0)
 To /dataquest/user/git/chatbot
    634eeac..1ed0970  master -> master

# Deleting more-speech branch.

/home/dq/chatbot$ git branch -d more-speech
Deleted branch more-speech (was 1ed0970).

# Creating branch happy-bot.
# Adding an output to bot.py.
# Commiting and pushong branch to remote.


/home/dq$ cd chatbot
/home/dq/chatbot$ git branch happy-bot
/home/dq/chatbot$ nano bot.py
/home/dq/chatbot$ git add bot.py
/home/dq/chatbot$ git commit -m "Made the bot 20% happier!"
[master b7b8aef] Made the bot 20% happier!
 1 file changed, 2 insertions(+), 1 deletion(-)
/home/dq/chatbot$ git push origin happy-bot
Total 0 (delta 0), reused 0 (delta 0)
To /dataquest/user/git/chatbot
 * [new branch]      happy-bot -> happy-bot

 # Creating branch feature/random-messages, editing bot.py and
 # commiting and pushing branch to remote.

/home/dq/chatbot$ git branch feature/random-messages
/home/dq/chatbot$ nano bot.py
/home/dq/chatbot$ git add bot.py
/home/dq/chatbot$ git commit -m "Updated"
[master 32c855e] Updated
 1 file changed, 7 insertions(+), 1 deletion(-)
/home/dq/chatbot$ git push origin feature/random-messages
Counting objects: 5, done.
Delta compression using up to 36 threads.
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 338 bytes | 0 bytes/s, done.
Total 3 (delta 1), reused 0 (delta 0)
To /dataquest/user/git/chatbot
 * [new branch]      feature/random-messages -> feature/random-messag
es

# Checking out feature/random-messages branch and creating
# branch feature spam-messages branch.

/home/dq/chatbot$ git checkout feature/random-messages
Switched to branch 'feature/random-messages'
/home/dq/chatbot$ git checkout -b feature/spam-messages
Switched to a new branch 'feature/spam-messages'
