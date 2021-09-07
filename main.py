from fastapi import FastAPI
from graphene import ObjectType, List, String, Schema, Field
from graphql.execution.executors.asyncio import AsyncioExecutor
from starlette.graphql import GraphQLApp
from schemas import repoType
import json

class Query(ObjectType):
  repo_list = None
  get_repo = List(repoType)
  async def resolve_get_repo(self, info):
    with open("./repo.json") as repo:
      repo_list = json.load(repo)
    return repo_list

app = FastAPI()
app.add_route("/", GraphQLApp(
  schema=Schema(query=Query),
  executor_class=AsyncioExecutor)
)
#uvicorn main:app --reload