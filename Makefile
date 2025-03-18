
ROBOT ?= air_humanoid

.PHONY: clean urdf mjcf usd

all: clean urdf mjcf usd

urdf:
	mv ./data/scad/* ./
	mkdir -p ./data/meshes/
	mkdir -p ./data/parts/
	mkdir -p ./data/scad/
	mkdir -p ./data/urdf/
	onshape-to-robot .
	mv *.stl ./data/meshes/
	mv *.part ./data/parts/
	mv *.scad ./data/scad/
	mv *.urdf ./data/urdf/
	python postprocess.py
	mv ./data/urdf/robot.urdf ./data/urdf/${ROBOT}.urdf

mjcf:
	${MUJOCO_HOME}/compile ./data/urdf/${ROBOT}.urdf ./data/mjcf/${ROBOT}.xml

usd:
	python ${ISAACLAB_HOME}/source/standalone/tools/convert_urdf.py ./data/urdf/${ROBOT}.urdf ./data/usd/${ROBOT}.usd --merge-joints --make-instanceable

clean:
	rm -rf ./data/meshes/*
	rm -rf ./data/parts/*
	rm -rf ./data/scad/*
	rm -rf ./data/urdf/*
	cp ./scad_override/* ./data/scad/
