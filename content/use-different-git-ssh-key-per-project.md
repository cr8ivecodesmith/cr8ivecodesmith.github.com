Title: use different git ssh key per project
Date: 2016-09-14 16:47
Category: code
Status: published


If you happen to be using different git accounts with they're own SSH keys;
i.e. you use different keys for deployment, personal, company A, company B, etc.

Then you probably have wondered how to tell git which key to use to manage the
repo.

You could use the [git-remote-ext][1] utility.


#### cloning new projects

```bash
$ git clone "ext::ssh -i /path/ssh/key git@github.com %S /gituser/repo.git"
```


#### existing projects

Edit the `.git/config` file directly or via the terminal:

```bash
$ git remote remove origin
$ git remote add origin "ext::ssh -i /path/ssh/key git@github.com %S /gituser/repo.git"
```


#### verifying new remote origin

```bash
$ git remote -v

origin ext::ssh -i /path/ssh/key git@github.com %S /gituser/repo.git (fetch)
origin ext::ssh -i /path/ssh/key git@github.com %S /gituser/repo.git (push)

$ git fetch
```


[1]: https://www.git-scm.com/docs/git-remote-ext
