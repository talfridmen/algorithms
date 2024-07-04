# Algorithms
Each directory in this repo contains only a readme file describing the algorithm that you need to implement

## How to work
Create your own branch: <your name>/main
This will, from now on, be your main branch.
For each algorithm, create a seperate branch <your name>/<algorithm name> and implement it on that branch.
once the algorithm is fully implemented, and you are happy with the results, open a PR pushing your algorithm branch to your main branch.

#### Example:
I will create a branch called tf/main.
when I develop the algorithm called fibonacci, I will create a branch called tf/fibonacci.
When ready, I will create a PR from tf/fibonacci to tf/main.

## How to test yourselves
In each exercise, there is already a list of tests under the *_test.py file which you can run by running the file with python. 
Also, in some Expert level exercises, there is some useful command examples already implemented in the main block. you may modify those as you please. These are intended to help you understand the objects required to implement these algorithms.

## Branches PATBAS/*
For each algorithm there is a branch names PATBAS/<algorithm name>.
This branch contains a suggested implementation for the algorithms.
For some of these algorithms there might be more than one solution.

The purpose of this branch is to help you in case you get stuck. Please do not look at the solution before trying yourself first as it will simply ruin the fun :)

*** There might be other solutions not implemented here. This is merely a suggestion.

## Git commands to get you started
git clone git@github.com:talfridmen/algorithms.git     -> clone the repo locally\
git checkout -b \<yourname>/main                        -> create your main branch\
git checkout -b \<yourname>/\<exercise> \<yourname>/main  -> create a new branch for the new exercise, starting from your main branch\
\<write code>\
git add \<files to add or -A for all>                   -> will add all the files you listed to the tracked files list\
git commit -m "\<describe your commit>"                 -> will commit (save) your changes to your local git\
git push --set-upstream origin/\<branchname>            -> will push the changes to the remote branch\
\<log in to github and open a PR>
