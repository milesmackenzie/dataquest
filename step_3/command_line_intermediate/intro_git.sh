# Creating direcotry random_numbers and initializing it as a git repository.

/home/dq$ mkdir random_numbers
/home/dq$ cd random_numbers/
/home/dq/random_numbers$ git init
Initialized empty Git repository in /home/dq/random_numbers/.git/

# Checking contents of the random_numbers folder.

/home/dq/random_numbers$ ls -al
total 12
drwxr-xr-x 3 dq dq 4096 Apr  4 19:19 .
drwxr-xr-x 1 dq dq 4096 Apr  4 19:19 ..
drwxr-xr-x 7 dq dq 4096 Apr  4 19:19 .git

# Creating file README.md containing: Random number generator
# Creating file script.py containing:
#if __name__ == "__main__":
        #print ("10")

/home/dq/random_numbers$ touch README.md
/home/dq/random_numbers$ nano README.md
/home/dq/random_numbers$ touch script.py
/home/dq/random_numbers$ nano script.py

# Checking git status and addint script.py and README.csv to
# the staging area.

/home/dq/random_numbers$ git status
On branch master

Initial commit

Untracked files:
  (use "git add <file>..." to include in what will be committed)

        README.md
        script.py

nothing added to commit but untracked files present (use "git add" to
 track)
/home/dq/random_numbers$ git add script.py
/home/dq/random_numbers$ git add README.md

# Configuring git with email and name.

/home/dq/random_numbers$ git config --global user.eamil "email@gmail.
.com"
/home/dq/random_numbers$ git config --global user.name "name"

# Commiting to repository.

/home/dq/random_numbers$ git commit -m "Initial commit. Added script.
py and README.md"
[master (root-commit) 809c14f] Initial commit. Added script.py and RE
ADME.md
 2 files changed, 3 insertions(+)
 create mode 100644 README.md
 create mode 100644 script.py

# Modifying script.py to print a random number from 0-10.
# Using git diff to track how Git is tracking modifications.
# Checking git status.

 /home/dq/random_numbers$ git diff
 diff --git a/script.py b/script.py
 index 1b5d34e..25a6bd6 100644
 --- a/script.py
 +++ b/script.py
 @@ -1,2 +1,3 @@
 +import random
  if __name__ == "__main__":
 -       print ("10")
 +       print (random.randint(0,10))

/home/dq/random_numbers$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working dire
ctory)

        modified:   script.py

no changes added to commit (use "git add" and/or "git commit -a")

# Adding and commitng modified script.py.

/home/dq/random_numbers$ git add script.py
/home/dq/random_numbers$ git commit -m "Modified script.py"
[master 5f80064] Modified script.py
 1 file changed, 2 insertions(+), 1 deletion(-)

 # Using git log to see the commit history.

/home/dq/random_numbers$ git log
commit 5f800647c0c2d4ef7a6a5df80ce21ffaf20cc572
Author: name <mileymac@gmail.com>
Date:   Wed Apr 4 19:43:39 2018 +0000

    Modified script.py

commit 809c14f7cbd67cbc3fe3cba9b3842d8195f6ba66
Author: name <mileymac@gmail.com>
Date:   Wed Apr 4 19:37:07 2018 +0000

    Initial commit. Added script.py and README.md

# Using git log --stat to see more details about the commits.

/home/dq/random_numbers$ git log --stat
commit 5f800647c0c2d4ef7a6a5df80ce21ffaf20cc572
Author: name <mileymac@gmail.com>
Date:   Wed Apr 4 19:43:39 2018 +0000

    Modified script.py

 script.py | 3 ++-
 1 file changed, 2 insertions(+), 1 deletion(-)

commit 809c14f7cbd67cbc3fe3cba9b3842d8195f6ba66
Author: name <mileymac@gmail.com>
Date:   Wed Apr 4 19:37:07 2018 +0000

    Initial commit. Added script.py and README.md

 README.md | 1 +
 script.py | 2 ++
