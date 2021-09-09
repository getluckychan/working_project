from fastapi import FastAPI
from graphene import ObjectType, List, String, Schema, Field
from graphql.execution.executors.asyncio import AsyncioExecutor
from starlette.graphql import GraphQLApp
from schemas import repoType
import json
import socket
import sys

class Query(ObjectType):
  repo_list = None
  get_repo = List(repoType)
  async def resolve_get_repo(self, info):
    with open("./repo.json") as repo:
      repo_list = json.load(repo)
    return repo_list

app1 = FastAPI()
hostname = socket.gethostname()
version = f"{sys.version_info.major}.{sys.version_info.minor}"
app1.add_route("/", GraphQLApp(
  schema=Schema(query=Query),
  executor_class=AsyncioExecutor)
)
@app1.get("/")
async def read_root():
    return {
        "name": "my-app",
        "host": hostname,
        "version": f"Hello world! From FastAPI running on Uvicorn. Using Python {version}"
    }
#uvicorn main:app --reload