var objStorage = "static/mesh/"

function objsLoader(objFile, scene, WORLD_ROOT) {
    var objGroup = new THREE.Group();
    var objMesh = new THREE.OBJLoader();
    objMesh.load(objStorage + objFile, function (mesh) {
        for (i=0; i < mesh.children.length; i++) {
            var childMesh = mesh.children[i];
            childMesh.receiveShadow = true;
            childMesh.castShadow = true;
            childMesh.rotation.y = WORLD_ROOT;
            
            objGroup.add(childMesh);
        };
        scene.add( objGroup );
        },
        // called when loading is in progresses
        function ( xhr ) {
            console.log( ( xhr.loaded / xhr.total * 100 ) + '% loaded' );
        },
        // called when loading has errors
        function ( error ) {
            console.log( 'An error happened' );
        }
    );

    return objGroup;

};