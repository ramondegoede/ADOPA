

from datetime import datetime


class Job():
    def __init__(self, id, pool_id, queue_time):
        self.id = id
        self.pool_id = pool_id
        self.queue_time = queue_time
        self.assign_time = ""
        self.finish_time = ""
        self.done = False
        self.started = False

    def __repr__(self):
        return 'job_id:{id}, started:{started}, done:{done}'.format(
            id=self.id,
            started=self.started,
            done=self.done)

def getCurrentJobs(jobs):
    """
    Gets all current running jobs
    """
    current_jobs = []
    for job in jobs:
        if 'result' not in job:
            current_jobs.append(job)
    return current_jobs

def getCompletedJobs(jobs):
    """
    Gets all completed jobs
    """
    completed_jobs = []
    for job in jobs:
        if 'result' in job:
            completed_jobs.append(job)
    return completed_jobs