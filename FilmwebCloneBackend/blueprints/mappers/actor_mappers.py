import os
import json
from flask import Request, url_for
from werkzeug.utils import secure_filename
from blueprints.mappers import allowed_file, ACTOR_FOLDER_PATH
from dtos import ActorDto, CreateActorDto
from models import Actor

class ActorMappers():

  def requestToCreateActorDtoMapper(self, request: Request) -> CreateActorDto:
    jsonForm = json.loads(request.form.get('data'))
    createActorDto = CreateActorDto()
    createActorDto.first_name = jsonForm.get('first_name') if jsonForm.get('first_name') != None else ''
    createActorDto.last_name = jsonForm.get('last_name') if jsonForm.get('last_name') != None else ''
    createActorDto.nationality = jsonForm.get('nationality') if jsonForm.get('nationality') != None else ''
    createActorDto.description = jsonForm.get('description') if jsonForm.get('description') != None else ''
    if 'file' in request.files:
        file = request.files['file']
        if file and file.filename != '' and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(ACTOR_FOLDER_PATH, filename))
            createActorDto.file_path = filename
    return createActorDto

  def actorSqlAlchemyToDtoMapper(self, actorDb: Actor) -> ActorDto:
    actorDto = ActorDto()
    actorDto.id = actorDb.id
    actorDto.first_name = actorDb.first_name
    actorDto.last_name = actorDb.last_name
    actorDto.nationality = actorDb.nationality
    actorDto.description = actorDb.description
    actorDto.file_path = url_for('static', filename = 'actor/' + actorDb.file_path)
    return actorDto

  def createActorDtoToSqlAlchemyMapper(self, createActorDto: CreateActorDto) -> Actor:
    return Actor(createActorDto.first_name, createActorDto.last_name, createActorDto.nationality, createActorDto.file_path, createActorDto.description)