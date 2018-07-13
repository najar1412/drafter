function buildSun(scene, params) {
    light = new THREE.DirectionalLight( 0x404040, 4 );
    light.castShadow = params.enableShadows;

    //Set up shadow properties for the light
    light.shadow.mapSize.width = 2048;  // default
    light.shadow.mapSize.height = 2048; // default
    light.shadow.camera.near = 0;    // default
    light.shadow.camera.far = 60000;     // default

    light.shadow.camera.left = -1000;
    light.shadow.camera.right = 1000;
    light.shadow.camera.top = 1000;
    light.shadow.camera.bottom = -1000;

    light_shadowbox_helper = new THREE.CameraHelper( light.shadow.camera );
    // scene.add( light_shadowbox_helper );
    scene.add( light );

    return light;
};


function buildDefaultSky(scene, params) {
    // Skybox
    var sky = new THREE.Sky();
    sky.scale.setScalar( 10000 );
    scene.add( sky );

    var uniforms = sky.material.uniforms;
    uniforms.turbidity.value = params.turbidity;
    uniforms.rayleigh.value = params.rayleigh;
    uniforms.luminance.value = params.luminance;
    uniforms.mieCoefficient.value = 0.005;
    uniforms.mieDirectionalG.value = params.mieDirectionG;

    return sky;
};


function buildDefaultScene(params) {
    scene = new THREE.Scene();
    if (params.fog) {
        scene.fog = new THREE.FogExp2( params.sceneFogColor, params.sceneFogDensity );
    };

    var skyLight = new THREE.AmbientLight( params.sceneSkyLightColor, params.sceneSkyLightIntensity ); // soft white light
    scene.add( skyLight );

    return scene;

};


function updateSun(scene, renderer, cubeCamera, lightSource, sky, water, params) {
    sky.material.uniforms.rayleigh.value = params.rayleigh;
    sky.material.uniforms.turbidity.value = params.turbidity;
    sky.material.uniforms.luminance.value = params.luminance;
    sky.material.uniforms.mieDirectionalG.value = params.mieDirectionG;
    
    var theta = Math.PI * ( params.inclination - 0.5 );
    var phi = 2 * Math.PI * ( params.azimuth - 0.5 );

    lightSource.position.x = params.distance * Math.cos( phi );
    lightSource.position.y = params.distance * Math.sin( phi ) * Math.sin( theta );
    lightSource.position.z = params.distance * Math.sin( phi ) * Math.cos( theta );
    
    sky.material.uniforms.sunPosition.value = lightSource.position.copy( lightSource.position );
    water.material.uniforms.sunDirection.value.copy( lightSource.position ).normalize();
    
    cubeCamera.update( renderer, scene );
};

function buildDefaultWater(scene, lightSource, params) {
    var waterGeometry = new THREE.PlaneBufferGeometry( 100000, 100000 );
    water = new THREE.Water(waterGeometry,
        {
            textureWidth: 512,
            textureHeight: 512,
            waterNormals: new THREE.TextureLoader().load( engineTextureStore + 'waternormals.jpg', function ( texture ) {
                texture.wrapS = texture.wrapT = THREE.RepeatWrapping;
            }),
            alpha: params.alpha,
            sunDirection: lightSource.position.clone().normalize(),
            sunColor: 0xffffff,
            waterColor: 0x001e0f,
            distortionScale:  params.distortionScale,
            // fog: scene.fog
        }
    );

    water.rotation.x = - Math.PI / 2;

    scene.add( water );

    return water;
    
};