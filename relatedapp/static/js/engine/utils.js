var objStorage = "static/mesh/"





function objsLoader(objFile, material, scene, WORLD_ROOT, castshadow=true) {

    var objMesh = new THREE.OBJLoader();
    objMesh.load(objStorage + objFile, function (mesh) {
        for (i=0; i < mesh.children.length; i++) {
            var childMesh = mesh.children[i];
            childMesh.receiveShadow = true;
            childMesh.rotation.y = WORLD_ROOT;
            childMesh.material = material;

            if (castshadow) {
                childMesh.castShadow = true;
            } else {
                childMesh.castShadow = false;
            };
            
    
        };
        scene.add( mesh );
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


};