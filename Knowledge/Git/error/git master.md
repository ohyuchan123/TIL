# git push 과정 중 오류 발생

git push -u origin master
To https://github.com/ohyuchan123/github-issue.git
 ! [rejected]        master -> master (non-fast-forward)
error: failed to push some refs to 'https://github.com/ohyuchan123/github-issue.git'  
hint: Updates were rejected because the tip of your current branch is behind
hint: its remote counterpart. Integrate the remote changes (e.g.
hint: 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.

**해결 방법**
`git push -u origin +master`