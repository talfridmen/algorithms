# Algorithms
Each directory in this repo contains only a readme file describing the algorithm that you need to implement

## Some Highlights:
- You never need to use the `input` command in these exercises. When I say "receive the value from the user" or similar, my meaning is that it is received *as a parameter to the function*
- If you are not clear on one of the tasks, first read it in full (except for the `Other Methods` section). All the info should be there. If you still are not clear on the algorithm itself that you need to implement, ask me before diving in.
- Each exercise is ordered so that each one uses new logic/operators that are increasingly harder. If you start from the first task, there shouldn't be any advanced programming skills involved. 
- Each exercise has a part that *you* need to figure out how to implement. I will not give you the answer to everything. I strongly suggest if it does not come too easy for you, to take a piece of paper, write a few examples of what you expect to happen, and start jotting down general idea guidelines of how to do it. 
- In most exercises, there could arise some edge cases. This means, that with some inputs, the function might be just a little bit off. I want you to find how to handle these. This means thinking of what might happen in different flows of the algorithms, so jot down some edge case ideas and think yourself what might happen and try following your algorithm manually on a piece of paper. Examples of edge cases, if I ask for an integer input, the simple case would be numbers like 1,2,5,10... what would happen if it is 0? or -1? or some insanely big number such as 1,000,000? I tried to cover these edge cases in the tests, so if one of them fails, try to think of the edge cases yourself, or go into the test file just to have a quick look at the specific case you failed on, and learn from it!
- Good luck!


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
