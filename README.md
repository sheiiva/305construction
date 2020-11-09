305construction
===

Time:       2 weeks

Team:       1

Language:   Python


The project
----
In the construction industry, the foreman is the person who manages, among other things, the scheduling of a construction site, and plans when contractors are intervening (which can be frequently). In order to do this, he uses software to automate the scheduling.

You must create a project management software that helps organize construction, based on the MPM method. Starting from a file that describes all of the project tasks, you have to display the following:
* Total duration of construction
* The earliest and latest start dates for each task
* A Gantt chart that specifies intervals of fluctuation

> The tasks and the intervals of fluctuation are separated by a tab (not a space).Same for the intervals of fluctuation and the schedule.

> In the Gantt chart, tasks are ordered first by earliest start date, then by duration andfinally by id.

## USAGE:

```
>> ./305construction [-h | --help]
USAGE
    ./305construction file

DESCRIPTION
    file    file describing the tasks
```

***file*** describes the tasks. Each line represents a task, and contains 4 separate pieces of information separated by semicolons, in the following order:
* The task id
* The description of the task
* The duration of the task
* The list of the task prerequisites (also separated by semicolons).


Author [**Corentin COUTRET-ROZET**](https://github.com/sheiiva)