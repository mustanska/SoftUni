jobs = [int(x) for x in input().split(", ")]
interested_job_index = int(input())

clock_cycles = 0

while True:
    shorted_job = min(x for x in jobs if x != 0)
    index = jobs.index(shorted_job)
    jobs[index] = 0

    clock_cycles += shorted_job

    if index == interested_job_index:
        break


print(clock_cycles)
