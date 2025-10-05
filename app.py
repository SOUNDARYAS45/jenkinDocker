import os

env = os.environ.get('ENV', 'dev')
print(f"Hello from {env} environment!")
