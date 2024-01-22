# Git

## Remotes

Remote repositories are versions of a project hosted somewhere on the Internet. You can several of
them, each of which can be either read-only or read-write for you.

Note that a "remote repository" could also be on your machine. The word "remote" only implies that 
it is stored somewhere else than your local version. In practice, remotes are not usually stored on
the same computer.

When cloning a Git project (from Github, Gitlab, etc.), Git uses "origin" as the default name for
the server you cloned from.

```aln
command to show the list of current remote servers : git remote
    git remote option to show the full URL of each remote : -v
command to add a remote with a {shortname} and {url} : git remote add shortname url
```