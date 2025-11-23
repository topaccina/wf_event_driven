"""
Flow A: Generates a random number and publishes a Prefect event.

This flow is designed to be manually triggered from Prefect Cloud UI.
It generates a random number and emits an event that will trigger Flow B.
"""

import random
from prefect import flow, task
from prefect.events import emit_event


@task
def generate_random_number() -> int:
    """Generate a random number between 1 and 100."""
    number = random.randint(1, 100)
    return number


@flow(name="flow-a", log_prints=True)
def flow_a():
    """
    Flow A: Generates a random number and publishes a Prefect event.
    
    This flow:
    1. Generates a random number
    2. Logs the generated number
    3. Emits a Prefect event that will trigger Flow B
    """
    print("Flow A started: Generating random number...")
    
    # Generate random number
    random_number = generate_random_number()
    
    print(f"Generated random number: {random_number}")
    
    # Emit Prefect event that will trigger Flow B
    emit_event(
        event="italy.random.number.generated",
        resource={"prefect.resource.id": "flow-a"},
        payload={"random_number": random_number},
    )
    
    print(f"Event 'italy.random.number.generated' emitted with number: {random_number}")
    print("Flow A completed successfully!")
    
    return random_number


if __name__ == "__main__":
    # Allow running locally for testing
    flow_a()

