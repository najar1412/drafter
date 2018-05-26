function buildEnvSun(scene) {
    light = new THREE.DirectionalLight( 0x404040, 4 );
    light.castShadow = true;

    //Set up shadow properties for the light
    light.shadow.mapSize.width = 1024;  // default
    light.shadow.mapSize.height = 1024; // default
    light.shadow.camera.near = 0;    // default
    light.shadow.camera.far = 600000;     // default

    light.shadow.camera.left = -1000;
    light.shadow.camera.right = 1000;
    light.shadow.camera.top = 1000;
    light.shadow.camera.bottom = -1000;

    light_shadowbox_helper = new THREE.CameraHelper( light.shadow.camera );
    // scene.add( light_shadowbox_helper );
    scene.add( light );

    return light;
};

function buildEnvAmbient() {
    var am_light = new THREE.AmbientLight( 0x404040, 1 ); // soft white light
    scene.add( am_light );

    return am_light;
};