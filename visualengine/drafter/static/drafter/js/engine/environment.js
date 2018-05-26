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

function buildDefaultSky(scene) {
    // Skybox
    var sky = new THREE.Sky();
    sky.scale.setScalar( 10000 );
    scene.add( sky );

    var uniforms = sky.material.uniforms;
    uniforms.turbidity.value = 10;
    uniforms.rayleigh.value = 2;
    uniforms.luminance.value = 1;
    uniforms.mieCoefficient.value = 0.005;
    uniforms.mieDirectionalG.value = 0.8;

    return sky;
};


function buildDefaultScene() {
    scene = new THREE.Scene();

    // buildDefaultSky(scene);

    scene.fog = new THREE.FogExp2( 0xF2F5F8, 0.0005 );
    scene.fog.density = 0.0001;

    var skyLight = new THREE.AmbientLight( 0x404040, 1 ); // soft white light
    scene.add( skyLight );

    return scene;

};

function updateSun(scene, renderer, cubeCamera, envSun, sky, water, params) {
    var theta = Math.PI * ( params.inclination - 0.5 );
    var phi = 2 * Math.PI * ( params.azimuth - 0.5 );
    envSun.position.x = params.distance * Math.cos( phi );
    envSun.position.y = params.distance * Math.sin( phi ) * Math.sin( theta );
    envSun.position.z = params.distance * Math.sin( phi ) * Math.cos( theta );
    
    sky.material.uniforms.sunPosition.value = envSun.position.copy( envSun.position );
    water.material.uniforms.sunDirection.value.copy( envSun.position ).normalize();
    
    cubeCamera.update( renderer, scene );
}