import os
import json
from flask import Request, url_for
from werkzeug.utils import secure_filename
from blueprints.mappers import allowed_file, DIRECTOR_FOLDER_PATH
from dtos import DirectorDto, CreateDirectorDto
from models import Director

class DirectorMappers():

  def requestToCreateDirectorDtoMapper(self, request: Request) -> CreateDirectorDto:
    jsonForm = json.loads(request.form.get('data'))
    createDirectorDto = CreateDirectorDto()
    createDirectorDto.first_name = jsonForm.get('first_name') if jsonForm.get('first_name') != None else ''
    createDirectorDto.last_name = jsonForm.get('last_name') if jsonForm.get('last_name') != None else ''
    createDirectorDto.nationality = jsonForm.get('nationality') if jsonForm.get('nationality') != None else ''
    createDirectorDto.description = jsonForm.get('description') if jsonForm.get('description') != None else ''
    if 'file' in request.files:
        file = request.files['file']
        if file and file.filename != '' and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(DIRECTOR_FOLDER_PATH, filename))
            createDirectorDto.file_path = filename
    return createDirectorDto

  def directorSqlAlchemyToDtoMapper(self, directorDb: Director) -> DirectorDto:
    directorDto = DirectorDto()
    directorDto.id = directorDb.id
    directorDto.first_name = directorDb.first_name
    directorDto.last_name = directorDb.last_name
    directorDto.nationality = directorDb.nationality
    directorDto.description = directorDb.description
    directorDto.file_path = url_for('static', filename = 'director/' + directorDb.file_path)
    return directorDto

  def createDirectorDtoToSqlAlchemyMapper(self, createDirectorDto: CreateDirectorDto) -> Director:
    return Director(createDirectorDto.first_name, createDirectorDto.last_name, createDirectorDto.nationality, createDirectorDto.file_path, createDirectorDto.description)