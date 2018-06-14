var objStorage = "/static/drafter/mesh/"

function geometryHandler(objFile, material, scene, WORLD_ROOT, envmap=false, castshadow=true) {
    var objMesh = new THREE.OBJLoader();
    objMesh.load(objStorage + objFile, function (mesh) {
        for (i=0; i < mesh.children.length; i++) {
            var childMesh = mesh.children[i];
            childMesh.receiveShadow = true;
            childMesh.rotation.y = WORLD_ROOT;

            if (childMesh.name.endsWith("_glass")) {
                childMesh.material = defaultGlass;
            } else if (childMesh.name.endsWith("_metal")) {
                childMesh.material = defaultSteel;
            } else if (childMesh.name.endsWith("_louvers")) {
                childMesh.material = defaultSteelBlack;
            } else {
                childMesh.material = material;
            }
            
            if (envmap !== false) {
                childMesh.material.envMap = envmap;
            };

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

function buildDefaultRenderer(document, container, params) {
    renderer = new THREE.WebGLRenderer( { antialias: params.antialias } );
    renderer.setPixelRatio( window.devicePixelRatio );
    renderer.setSize(window.innerWidth, container.offsetHeight);
    renderer.shadowMap.enabled = params.enableShadowMap;
    renderer.shadowMap.type = THREE.PCFSoftShadowMap;

    //document.body.appendChild( renderer.domElement );
    container.appendChild( renderer.domElement );
    // document.body.replaceChild(renderer.domElement, container);

    return renderer;
};

function keyBindings(document) {
    var onKeyDown = function ( event ) {
        switch ( event.keyCode ) {
            case 82: // R
                moveUp = true;
                break;
            case 70: // F
                moveDown = true;
                break;
            case 38: // up
            case 87: // w
                moveForward = true;
                break;
            case 37: // left
            case 65: // a
                moveLeft = true; 
                break;
            case 40: // down
            case 83: // s
                moveBackward = true;
                break;
            case 39: // right
            case 68: // d
                moveRight = true;
                break;
            case 32: // space
                if ( canJump === true ) velocity.y += 350;
                canJump = false;
                break;
        }
    };
    var onKeyUp = function ( event ) {
        switch( event.keyCode ) {
            case 82: // R
                moveUp = false;
                break;
            case 70: // F
                moveDown = false;
                break;
            case 38: // up
            case 87: // w
                moveForward = false;
                break;
            case 37: // left
            case 65: // a
                moveLeft = false;
                break;
            case 40: // down
            case 83: // s
                moveBackward = false;
                break;
            case 39: // right
            case 68: // d
                moveRight = false;
                break;
        }
    };

    document.addEventListener( 'keydown', onKeyDown, false );
    document.addEventListener( 'keyup', onKeyUp, false );
};


function parseGeometryParams(params, material, scene, WORLD_ROOT, envmap) {
    for (var k in params) {
        if (params.hasOwnProperty(k)) {
            // fetch objects and apply materials
            geometryHandler(params[k], material, scene, WORLD_ROOT, envmap);
        }
    }

};