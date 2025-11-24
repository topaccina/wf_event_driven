from math import e
from prefect import flow

if __name__ == "__main__":
    flow.from_source("https://github.com/topaccina/wf_event_driven.git",
    entrypoint="src/flows/flow_a.py:flow_a").deploy(
        name="flow-a-deployment",
        work_pool_name="laural-workpool",
    )
    flow.from_source("https://github.com/topaccina/wf_event_driven.git",
    entrypoint="src/flows/flow_b.py:flow_b").deploy(
        name="flow-b-deployment",
        work_pool_name="laural-workpool",
    )