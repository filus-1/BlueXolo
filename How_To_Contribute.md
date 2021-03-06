# How To Contribute

## Terminology Table

| Instance | Branch | Description, Instructions, Notes |
| :---:         |     :---:      |          :---: |
| Stable   | Master     | Accepts merges from Working and Hotfixes    |
| Working     | Stage       | Accepts merges from Features/Issues and Hotfixes      |
| Features/Issues   | topic-*     | Always branch off HEAD of Working    |
| Hotfix     | hotfix-*       | Always branch off Stable      |

## Main Branches
The main repository holds 2 branches: 
- Production
- Master.

<p align="justify">
The main branch should be considered <b>Origin/Master</b> and will be the main branch where the source code of HEAD always reflects a state with the latest delivered development changes for the next release. As a developer, you will be branching and merging from <b>Master</b>.
</p>

<p align="justify">
Consider Production to always represent the latest code deployed to <b>Production</b>. During day to day development, the <b>Production</b> branch will not be interacted with.
</p>

<p align="justify">
When the source code in the <b>Master</b> branch is stable and has been deployed, all of the changes will be merged into <b>Production</b> and tagged with a release number. How this is done in detail will be discussed later.
</p>

## Deployment Schedule:

<table>
  <tbody>
    <tr>
      <th align="center">Day</th>
      <th align="center">Action</th>
    </tr>
    <tr>
      <td align="center">Thursday</td>
      <td>
        <ul>
          <li>If Master is stable all the changes will be merge into Production.</li>
          <li>Otherwise the development team must investigate and open/close any issue addressing issues to the Master Branch.</li>
          <li>After all the changes from Master were merged its time to deploy all the pull requests that were accepted into the Master branch.</li
        </ul>
      </td>
    </tr>
    <tr>
      <td align="center">Monday to Wednesday</td>
      <td>
        <ul>
          <li>During this time frame the senior developer is going to decide if a pull request is accepted or not.</li>
          <li>This process can take longer than 3 days.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td align="center">At any time</td>
      <td>
        <ul>
          <li>Commits can be made at any time.</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

## Supporting Branches

<p align="justify">
Supporting branches are used to aid parallel development between team members, ease tracking of features, and to assist in quickly fixing live production problems. Unlike the main branches, these branches always have a limited life time, since they will be removed eventually.
</p>

The different types of branches we may use are:
- Feature branches
- Bug branches
- Hotfix branches

<p align="justify">
Each of these branches have a specific purpose and are bound to strict rules as to which branches may be their originating branch and which branches must be their merge targets. Each branch and its usage is explained below.
</p>

### Feature Branches

<p align="justify">
Feature branches are used when developing a new feature or enhancement which has the potential of a development lifespan longer than a single deployment. When starting development, the deployment in which this feature will be released may not be known. No matter when the feature branch will be finished, it will always be merged back into the master branch.
</p>

<p align="justify">
During the lifespan of the feature development, the lead should watch the master branch (network tool or branch tool in GitHub) to see if there have been commits since the feature was branched. Any and all changes to master should be merged into the feature before merging back to master; this can be done at various times during the project or at the end, but time to handle merge conflicts should be accounted for.
</p>

Represents the Basecamp project to which Project Management will be tracked.

- Must branch from: master
- Must merge back into: master
- Branch naming convention: feature\-\<tbd number\>

### Working with a feature branch

<p align="justify">
If the branch does not exist yet (check with the Lead), create the branch locally and then push to GitHub. A feature branch should always be 'publicly' available. That is, development should never exist in just one developer's local branch.
</p>

```
$ git checkout -b feature-id master                   // creates a local branch for the new feature
$ git push origin feature-id                          // makes the new feature remotely available
```

<p align="justify">
Periodically, changes made to master (if any) should be merged back into your feature branch.
</p>

```
$ git merge master                                   // merges changes from master into feature branch
```

<p align="justify">
When development on the feature is complete, the lead (or engineer in charge) should merge changes into master and then make sure the remote branch is deleted.
</p>

```
$ git checkout master                               // change to the master branch
$ git merge --no-ff feature-id                      // makes sure to create a commit object during merge
$ git push origin master                            // push merge changes
$ git push origin :feature-id                       // deletes the remote branch
```

### Bug Branches

<p align="justify">
Bug branches differ from feature branches only semantically. Bug branches will be created when there is a bug on the live site that should be fixed and merged into the next deployment. For that reason, a bug branch typically will not last longer than one deployment cycle. Additionally, bug branches are used to explicitly track the difference between bug development and feature development. No matter when the bug branch will be finished, it will always be merged back into master.
</P>

<p align="justify">
Although likelihood will be less, during the lifespan of the bug development, the lead should watch the master branch (network tool or branch tool in GitHub) to see if there have been commits since the bug was branched. Any and all changes to master should be merged into the bug before merging back to master; this can be done at various times during the project or at the end, but time to handle merge conflicts should be accounted for.
</P>

Represents the Basecamp project to which Project Management will be tracked.

- Must branch from: master
- Must merge back into: master
- Branch naming convention: bug-<tbd number>

### Working with a bug branch

<p align="justify">
If the branch does not exist yet (check with the Lead), create the branch locally and then push to GitHub. A bug branch should always be 'publicly' available. That is, development should never exist in just one developer's local branch.
</P>

```
$ git checkout -b bug-id master                     // creates a local branch for the new bug
$ git push origin bug-id                            // makes the new bug remotely available
```

Periodically, changes made to master (if any) should be merged back into your bug branch.

```
$ git merge master                                  // merges changes from master into bug branch
```

<p align="justify">
When development on the bug is complete, [the Lead] should merge changes into master and then make sure the remote branch is deleted.
</P>

```
$ git checkout master                              // change to the master branch
$ git merge --no-ff bug-id                         // makes sure to create a commit object during merge
$ git push origin master                           // push merge changes
$ git push origin :bug-id                          // deletes the remote branch
```

### Hotfix Branches

<p align="justify">
A hotfix branch comes from the need to act immediately upon an undesired state of a live production version. Additionally, because of the urgency, a hotfix is not required to be be pushed during a scheduled deployment. Due to these requirements, a hotfix branch is always branched from a tagged stable branch. This is done for two reasons:
</P>

- Development on the master branch can continue while the hotfix is being addressed.
- A tagged stable branch still represents what is in production. At the point in time where a hotfix is needed, there could have been multiple commits to master which would then no longer represent production. 


Represents the Basecamp project to which Project Management will be tracked.

- Must branch from: tagged stable
- Must merge back into: master and stable
- Branch naming convention: hotfix-<tbd number>

### Working with a hotfix branch

<p align="justify">
If the branch does not exist yet (check with the Lead), create the branch locally and then push to GitHub. A hotfix branch should always be 'publicly' available. That is, development should never exist in just one developer's local branch.
</P>

```
$ git checkout -b hotfix-id stable                 // creates a local branch for the new hotfix
$ git push origin hotfix-id                        // makes the new hotfix remotely available
```

When development on the hotfix is complete, [the Lead] should merge changes into stable and then update the tag.

```
$ git checkout stable                             // change to the stable branch
$ git merge --no-ff hotfix-id                     // forces creation of commit object during merge
$ git tag -a <tag>                                // tags the fix
$ git push origin stable --tags                   // push tag changes
```

Merge changes into master so not to lose the hotfix and then delete the remote hotfix branch.

```
$ git checkout master                             // change to the master branch
$ git merge --no-ff hotfix-id                     // forces creation of commit object during merge
$ git push origin master                          // push merge changes
$ git push origin :hotfix-id                      // deletes the remote branch
```


##### Models Taken from:

By Jeremy Helms, 2012, digitaljhelms, https://gist.github.com/digitaljhelms/4287848
By Vincent Driessen, on Tuesday, January 05, 2010, A successful Git branching model http://nvie.com/posts/a-successful-git-branching-model/
