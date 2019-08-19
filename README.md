## Overview - Creating Packages

Packages allow us organize and group modules (or python files).

```bash
├── package
│   ├── __init__.py
│   ├── module.py
│   ├── module.py
```

### __init__.py

> The __init__.py files are required to make Python treat directories
> containing the file as packages. This prevents directories with a common
> name, such as string, unintentionally hiding valid modules that occur later
> on the module search path. In the simplest case, __init__.py can just be an
> empty file, but it can also execute initialization code for the package or
> set the __all__ variable, described later.
>
> -- <cite>python docs</cite>


## PR (Pull Request) Workflow for this Assignment
1. *Fork* this repository into your own personal github account.
2. Then *Clone* your own repo to your local development machine.
3. Create a separate branch named `dev`, and checkout the branch.
5. Commit your changes, then `git push` the branch back to your own github account.
5. From your own Github repo, create a pull request (PR) from your `dev` branch back to your own master.
6. Copy/Paste the URL **link to your PR** as your assignment submission.
7. Your grader will post code review comments inline with your code, in your github account. Be sure to respond to any comments and make requested changes. **RESUBMIT** a new link to your PR after making changes.  This is the code review iteration cycle.
