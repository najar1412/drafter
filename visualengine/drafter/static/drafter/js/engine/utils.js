var objStorage = "/static/drafter/mesh/"

function objsLoader(objFile, material, scene, WORLD_ROOT, envmap=false, castshadow=true) {
    var objMesh = new THREE.OBJLoader();
    objMesh.load(objStorage + objFile, function (mesh) {
        for (i=0; i < mesh.children.length; i++) {
            var childMesh = mesh.children[i];
            childMesh.receiveShadow = true;
            childMesh.rotation.y = WORLD_ROOT;
            childMesh.material = material;
            
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

function makeWater(scene, envSun) {

				
    // Water
    var waterGeometry = new THREE.PlaneBufferGeometry( 100000, 100000 );
    water = new THREE.Water(
        waterGeometry,
        {
            textureWidth: 512,
            textureHeight: 512,
            waterNormals: new THREE.TextureLoader().load( '/static/drafter/textures/waternormals.jpg', function ( texture ) {
                texture.wrapS = texture.wrapT = THREE.RepeatWrapping;
            }),
            alpha: 1.0,
            sunDirection: envSun.position.clone().normalize(),
            sunColor: 0xffffff,
            waterColor: 0x001e0f,
            distortionScale:  3.7,
            fog: scene.fog
        }
    );
    water.rotation.x = - Math.PI / 2;
    scene.add( water );

    return water;
    
};

function buildDefaultRenderer(document) {
    renderer = new THREE.WebGLRenderer( { antialias: true } );
    renderer.setPixelRatio( window.devicePixelRatio );
    renderer.setSize( window.innerWidth, window.innerHeight );
    renderer.shadowMap.enabled = true;
    renderer.shadowMap.type = THREE.PCFSoftShadowMap;

    document.body.appendChild( renderer.domElement );

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

function onWindowResize(camera) {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize( window.innerWidth, window.innerHeight );
}