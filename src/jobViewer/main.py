from cProfile import run
import os
from utils import *
from datetime import datetime
from jobs import *
from time import sleep
pat = os.environ['PAT']
authorization_pat = authorization(pat, 'application/json')
url = "https://dev.azure.com/ITWINS/_apis/distributedtask/pools/12/jobrequests"
running_jobs = []


while True:
    # get current jobs
    jobs = devopsGetApiRequest(url, authorization_pat)['value']
    
    current_jobs = getCurrentJobs(jobs)

    # get running jobs
    for current_job in current_jobs:
        current_job_id = current_job['jobId']
        current_job_queue_time = current_job['queueTime'].split('.')[0]
        print(current_job['queueTime'])
        current_job_queue_time = datetime.strptime(
            current_job_queue_time,
            '%Y-%m-%dt%H:%M:%S')
        print(current_job_queue_time)

        # Add new jobs if not existing
        exists = False
        for running_job in running_jobs:
            if current_job_id == running_job.id:
                exists = True
                break
        if not exists:
            new_running_job = Job(
                id = current_job_id,
                queue_time = current_job_queue_time,
                pool_id = current_job['poolId'])
            running_jobs.append(new_running_job)


    for running_job in running_jobs:
        print(running_job)
        if not running_job.started:
            print('starting job')
            running_job.started = True

        if running_job.started:
            if running_job.done:
                print('job {id} has been completed'.format(id=running_job.id))
            else:
                print('job {id} is still running'.format(id=running_job.id))
        print(running_job)

    sleep(10)