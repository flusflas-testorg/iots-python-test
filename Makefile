.PHONY: all

all: anythingdb

anythingdb:
	datamodel-codegen  --input openapi/anythingdb.yaml --input-file-type openapi --output swx/models/anythingdb.py --base-class swx.models.basemodel.IterBaseModel

clean_models:
	python tools/clean_models.py swx/models/anythingdb.py