#central repository - typically located on remote server
#local repository - typically located on local machine

# 1. git init
# 2. git remote add origin "link" (by copying and pasting from github)
# 3. git pull origin master #pulls all friles from central repositry to local repository
# git status
# add any untracked files (git add <file> / git add -A)
# git commit -m "message" / git commit -a "message" (can only be used if it has already been commited in the past)
# git log

###

# git branch "branch name"
# git checkout "branch name" - used to switch to specified branch
# add
# commit
# ls - check all files in branch

###

# Merging: combining work of different branches all together
# Merge INTO master branch
# git merge "name of branch you want to merge into current branch that is in checkout"
# must add file into index again after changes have been made (git commit -a -m "message")
# make sure you merge in copies as well otherwise modifications will not be shown in modification

###

# Rebasing: done to reduce the number of branches and keep clearer project history
# helps navigate better because of linear workflow
# takes branch and adds it to master branch
# git rebase "branch name"

###

# ssh-keygen
# copy where it has been saved
# cat "where it has been saved"
# copy key and paste into github key place
# ssh -T git@github.com

###

# git remote add origin "link"
# git push origin "name of branch" - sends contents of branch to central repository